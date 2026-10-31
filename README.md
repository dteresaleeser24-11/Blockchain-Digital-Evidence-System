

\# Blockchain-Based Digital Evidence Integrity System



A Python Flask-based application designed to maintain the integrity and traceability of digital evidence using SHA-256 cryptographic hashing and a hash-linked blockchain structure.



\## Project Overview



Digital evidence such as documents, images, videos, and other electronic files must maintain their integrity during investigation and examination.



This project provides a system to upload digital evidence, generate unique SHA-256 hashes, record evidence metadata, and verify whether evidence has been modified.



The application uses a blockchain-inspired structure in which each block is linked to the previous block using cryptographic hashes.



\## Key Features



\- Digital evidence upload

\- SHA-256 hash generation

\- Blockchain-based evidence records

\- Previous hash and current hash linking

\- Evidence integrity verification

\- Case ID-based evidence search

\- Investigator and case information management

\- SQLite database integration

\- Flask-based web interface



\## Technologies Used



| Technology | Purpose |

|---|---|

| Python | Application development |

| Flask | Web application framework |

| SHA-256 | Digital evidence hashing |

| SQLite | Database management |

| HTML | Web page structure |

| CSS | User interface styling |

| Git \& GitHub | Version control and source code hosting |



\## How It Works



1\. The investigator enters case details.

2\. Digital evidence is uploaded through the web interface.

3\. The system calculates the SHA-256 hash of the uploaded file.

4\. Evidence metadata and hash information are recorded.

5\. A new block is created with its index, timestamp, filename, file hash, previous hash, and current hash.

6\. The blockchain structure links the new block to the previous block.

7\. Evidence integrity can be checked by comparing its current hash with the recorded hash.



\## Blockchain Structure



Each block contains:



\- Index

\- Timestamp

\- Filename

\- File Hash

\- Previous Hash

\- Current Hash



The previous hash connects each block to its predecessor, helping detect changes to the recorded chain.



\## Project Structure



```text

Blockchain-Digital-Evidence-System/

│

├── app.py

├── blockchain.py

├── database.py

├── hashing.py

├── requirements.txt

├── .gitignore

├── README.md

│

├── templates/

│   ├── base.html

│   ├── index.html

│   ├── evidence.html

│   ├── blockchain.html

│   ├── search.html

│   └── verify.html

│

├── static/

│

└── evidence/

```



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone https://github.com/dteresaleeser24-11/Blockchain-Digital-Evidence-System.git

```



\### 2. Navigate to the project folder



```bash

cd Blockchain-Digital-Evidence-System

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the virtual environment



Windows PowerShell:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### 5. Install dependencies



```bash

pip install -r requirements.txt

```



\### 6. Run the application



```bash

python app.py

```



\### 7. Open in your browser



http://127.0.0.1:5000



\## Security and Evidence Integrity



SHA-256 is used to generate a cryptographic hash for each digital evidence file.



The hash-linked block structure helps identify modifications to recorded evidence or blockchain records.



\*\*Note:\*\* This is an educational blockchain-based integrity prototype. It is not a distributed blockchain network or a replacement for a production digital evidence management system. Proper access controls, secure storage, backups, and independent verification are necessary for real forensic investigations.



\## Future Enhancements



\- User authentication and role-based access control

\- Authorized investigator management

\- Evidence access audit logs

\- Improved evidence verification

\- Digital signature integration

\- Secure evidence storage

\- Dashboard and reporting features

\- Deployment to a secure hosting environment



\## Author



\*\*Teresa Leeser Dake\*\*



M.Sc. Cyber Security \& Law



GitHub: https://github.com/dteresaleeser24-11



\---



Developed as a cybersecurity and digital forensics academic project.



