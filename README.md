# NamasteKart - Automated Order File Validation System

## Project Overview

NamasteKart is an online mart operating in Bangalore and Mumbai. Each day, the system receives daily order transaction files that must be validated before being stored for analysis and business use. This project automates the validation, categorization (success/rejected), and notification process through Python.

---

## Objective

- Automate the process of receiving order files via SFTP.
- Validate each order file against a predefined set of business rules.
- Organize files into success or rejected folders.
- Generate detailed error files for all rejected records.


---

## Folder Structure

NamasteKart/
│
├── incoming_files/
│ └── YYYYMMDD/
│
├── success_files/
│ └── YYYYMMDD/
│
├── rejected_files/
│ └── YYYYMMDD/
│ ├── rejected_file.csv
│ └── error_rejected_file.csv
│
├── master_data/
│ └── product_master.csv
│
├── validationcheck.py
├── 
├── README.md


---

## Validation Rules

Each order is checked for the following conditions:

1. Product ID must be present in the product master file.
2. Total sales amount check.
3. Order date must not be in the future.
4. No fields should be empty.
5. City must be either 'Mumbai' or 'Bangalore.


---

Automation Process

1. Upload to SFTP  
   The script uploads all `.csv` files from the local incoming folder to the SFTP server.

2. Download from SFTP 
   Files are downloaded from the SFTP server's incoming folder to: NamasteKart/incoming_files/YYYYMMDD/


3. Validation Execution  
Each file is read using pandas. Validations are run via functions in validationcheck.py.

4. File Classification  
- If valid → moved to success_files/YYYYMMDD/
- If invalid → moved to rejected_files/YYYYMMDD/ and generates error_<filename>.csv


---

## Technologies Used

- Python 3
- pandas for file manipulation
- paramiko for SFTP transfers
- os, shutil, datetime for filesystem and date handling


---

## Conclusion

This project provides a complete end-to-end automation pipeline for NamasteKart's order validation:

1. Robust rule-based validation

2. Clean file organization and error reporting

3. Real-time SFTP integration

4. Scalable and maintainable design

5. It ensures business teams are informed daily while maintaining data integrity and compliance with operational rules.

