#  BLOCKCHAIN-BASED DIGITAL EVIDENCE MANAGEMENT SYSTEM

**A Blockchain-Inspired and Tamper-Evident Digital Evidence Management Application**

A Python-based web application designed to manage digital forensic evidence through cryptographic hashing and blockchain-inspired data integrity mechanisms.

The system records evidence details, generates unique SHA-256 fingerprints, and maintains a hash-linked record of evidence transactions to support integrity verification and forensic accountability.

---

##  PROJECT OVERVIEW

Digital evidence must be preserved carefully to prevent unauthorized modification or loss of integrity.

This project provides a centralized platform for uploading, documenting, tracking, and verifying digital evidence. It combines a Flask-based web interface, SHA-256 cryptographic hashing, SQLite storage, and a JSON-based hash-linked blockchain.

##  CORE CAPABILITIES

| Feature | Description |
|---|---|
| Evidence Registration | Upload digital files with case-related information. |
| Cryptographic Hashing | Generate SHA-256 hashes for uploaded evidence. |
| Integrity Verification | Compare file hashes to detect modifications. |
| Blockchain Records | Maintain hash-linked evidence entries. |
| Case Management | Record case IDs, investigator details, and descriptions. |
| Evidence Tracking | Store searchable metadata using SQLite. |
| Blockchain Inspection | View and download blockchain records in JSON format. |

---

##  SYSTEM WORKFLOW

1. **Evidence Submission** – The investigator uploads a digital evidence file.
2. **Metadata Collection** – Case ID, investigator name, and description are recorded.
3. **Hash Generation** – The application calculates the SHA-256 hash.
4. **Blockchain Recording** – Evidence hash information is appended to the blockchain JSON file.
5. **Database Storage** – Evidence metadata is saved in SQLite.
6. **Integrity Validation** – The uploaded file can be checked against its previously stored hash.

---

##  TECHNOLOGY STACK

- **Programming Language:** Python
- **Web Framework:** Flask
- **Cryptographic Algorithm:** SHA-256
- **Database:** SQLite
- **Data Storage:** JSON
- **Concept:** Blockchain-based integrity verification

---

##  INSTALLATION & CONFIGURATION

### Prerequisites

- Python 3.10 or later
- Git
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/dteresaleeser24-11/Blockchain-Digital-Evidence-System.git
cd Blockchain-Digital-Evidence-System
```


### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / Kali Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Live Demo

Explore the deployed application:

🔗 **Live Website:** https://blockchain-digital-evidence-system.onrender.com

📂 **GitHub Repository:** https://github.com/dteresaleeser24-11/Blockchain-Digital-Evidence-System

> Note: The live demo uses temporary storage. Uploaded test evidence and records may not persist after service restarts or redeployments. Please use dummy files only.

---

##  EXECUTION

Start the Flask application:

```bash
python app.py
```

Once the application starts, access it through your browser:

`http://127.0.0.1:5000`

---

##  PROJECT OBJECTIVES

- Maintain the integrity of digital forensic evidence.
- Apply cryptographic hashing for file verification.
- Improve evidence documentation and traceability.
- Demonstrate blockchain-inspired evidence record management.
- Provide a simple platform for forensic evidence handling.

---

##  SECURITY & INTEGRITY

The application uses SHA-256 hashing to generate a digital fingerprint for each evidence file.

These hashes are stored in hash-linked records, allowing the application to identify changes to evidence files during verification.

**Note:** This is a local blockchain-inspired implementation, not a decentralized blockchain network.

---

##  DEVELOPMENT

Developed as a Digital Forensics and Cybersecurity project to demonstrate the practical application of cryptographic hashing, evidence management, and blockchain concepts.

**Project Domain:** Cybersecurity , Digital Forensics , Blockchain Technology
