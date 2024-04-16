'''
Task 1: Email Extractor:

Problem Statement:
Write a Python script to extract all email addresses from a given text file (contacts.txt). 
The file contains a mix of text and email addresses.

File Example:
```
Contact List:
John Doe - john.doe@example.com
Jane Smith - jane.smith@gmail.com

For inquiries, please contact info@example.com
```
'''

import re

def extract_emails(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)

            print("Extracted email addresses:")
            for email in emails:
                print(email)
    except FileNotFoundError:
        print("File not found:", file_path)
    except PermissionError:
        print("Permission denied for file:", file_path)


file_path = "contacts.txt"
extract_emails(file_path)