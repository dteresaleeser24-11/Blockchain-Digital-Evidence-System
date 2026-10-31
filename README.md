\# Blockchain Evidence System



A Flask application for recording digital evidence, generating SHA-256 file hashes, and storing evidence metadata in a simple hash-linked blockchain.



\## Features



\- Upload evidence with a case ID, investigator, and description

\- Generate a SHA-256 hash for each uploaded file

\- Append evidence hashes to `blockchain.json`

\- Store searchable evidence metadata in a local SQLite database

\- Verify whether a file matches its stored hash

\- View the blockchain and download its JSON representation



\## Requirements



\- Python 3.10 or newer

\- Flask



\## Setup



Create and activate a virtual environment, then install Flask:



```bash

python -m venv venv

```



Activate the virtual environment:



\*\*Windows:\*\*

```bash

venv\\Scripts\\activate

```



\*\*Linux / macOS:\*\*

```bash

source venv/bin/activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\## Run the Application



```bash

python app.py

```



Open your browser and visit:



```text

http://127.0.0.1:5000

```



\## Technology Used



\- Python

\- Flask

\- SHA-256 Hashing

\- SQLite

\- Blockchain Technology



\## Project Purpose



This project demonstrates how blockchain technology and cryptographic hashing can be used to maintain the integrity and authenticity of digital evidence.

