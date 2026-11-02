
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from markupsafe import escape
import os
import hashlib
from datetime import datetime

from hashing import generate_hash
from blockchain import Blockchain
from database import (
    create_table,
    add_evidence,
    get_all_evidence,
    total_evidence,
    search_case,
    get_hash
)

app = Flask(__name__)

# Initialize database and blockchain
create_table()

blockchain = Blockchain()

# Storage configuration
DATA_DIR = os.environ.get("APP_DATA_DIR", ".")

UPLOAD_FOLDER = os.path.join(DATA_DIR, "evidence")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Maximum upload size: 10 MB
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


# Generate SHA-256 hash directly from uploaded file
def generate_hash_from_upload(file):

    sha256 = hashlib.sha256()

    while True:

        data = file.stream.read(4096)

        if not data:
            break

        sha256.update(data)

    return sha256.hexdigest()


# Home page and evidence upload
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        case_id = request.form["case_id"]
        investigator = request.form["investigator"]
        description = request.form["description"]

        file = request.files.get("evidence")

        if file and file.filename:

            filename = secure_filename(file.filename)

            if not filename:
                return "Invalid filename", 400

            file_path = os.path.join(UPLOAD_FOLDER, filename)

            # Prevent overwriting existing evidence
            if os.path.exists(file_path):

                return (
                    "A file with this name already exists. "
                    "Please rename your file.",
                    409
                )

            # Save uploaded evidence
            file.save(file_path)

            # Generate SHA-256 hash
            hash_value = generate_hash(file_path)

            # Add evidence to blockchain
            blockchain.add_block(filename, hash_value)

            upload_time = datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            # Save evidence details in database
            add_evidence(
                case_id,
                investigator,
                description,
                filename,
                hash_value,
                upload_time
            )

            return f"""
            <h2>Evidence Uploaded Successfully!</h2>

            <hr>

            <p><b>Case ID:</b> {escape(case_id)}</p>

            <p><b>Investigator:</b> {escape(investigator)}</p>

            <p><b>Description:</b> {escape(description)}</p>

            <p><b>Filename:</b> {escape(filename)}</p>

            <p><b>SHA-256 Hash:</b></p>

            <p>{hash_value}</p>

            <hr>

            <h3>Blockchain Status</h3>

            <p><b>Total Blocks:</b> {len(blockchain.chain)}</p>

            <p>
                <b>Current Block:</b>
                {blockchain.chain[-1]['index']}
            </p>

            <br>

            <a href="/blockchain">View Blockchain</a>

            <br><br>

            <a href="/verify">Verify Evidence</a>

            <br><br>

            <a href="/">Upload Another Evidence</a>
            """

    return render_template(
        "index.html",
        total=total_evidence(),
        blocks=len(blockchain.chain)
    )


# View blockchain
@app.route("/blockchain")
def view_blockchain():

    return render_template(
        "blockchain.html",
        blockchain=blockchain.display_chain()
    )


# Verify evidence integrity
@app.route("/verify", methods=["GET", "POST"])
def verify():

    result = ""

    if request.method == "POST":

        case_id = request.form["case_id"]

        file = request.files.get("evidence")

        if file and file.filename:

            filename = secure_filename(file.filename)

            if not filename:

                result = "Invalid filename"

            else:

                # Calculate hash of uploaded verification file
                new_hash = generate_hash_from_upload(file)

                # Retrieve previously stored hash
                stored_hash = get_hash(case_id, filename)

                if stored_hash is None:

                    result = "Case ID or filename not found"

                elif stored_hash == new_hash:

                    result = "Evidence Verified (Not Tampered)"

                else:

                    result = "Evidence Tampered"

    return render_template(
        "verify.html",
        result=result
    )


# View uploaded evidence records
@app.route("/evidence")
def evidence():

    records = get_all_evidence()

    return render_template(
        "evidence.html",
        records=records
    )


# Search evidence by Case ID
@app.route("/search", methods=["GET", "POST"])
def search():

    records = []

    if request.method == "POST":

        case_id = request.form["case_id"]

        records = search_case(case_id)

    return render_template(
        "search.html",
        records=records
    )


# Download blockchain JSON file
@app.route("/download")
def download():

    blockchain_path = os.path.join(
        DATA_DIR,
        "blockchain.json"
    )

    return send_file(
        blockchain_path,
        as_attachment=True
    )


# Run application locally
if __name__ == "__main__":

    app.run(debug=False)
