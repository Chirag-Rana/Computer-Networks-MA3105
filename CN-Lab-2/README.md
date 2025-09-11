# Computer Networks Lab Assignment 2: Application Layer Protocols

This repository contains the Python script solutions for the Computer Networks Lab Assignment 2. Each script implements the functionality of a key Application Layer protocol.

## 🎯 Objective

The objective of this assignment is to understand and implement the functionality of the following Application Layer protocols using Python:
* HTTP (Hypertext Transfer Protocol) 
* SMTP (Simple Mail Transfer Protocol) 
* FTP (File Transfer Protocol) 
* DNS (Domain Name System) 

---

## 🚀 How to Run

Follow the instructions below for each protocol script.

### A. HTTP Client (`http_client.py`)

This script sends **GET** and **POST** requests to a public test API. It then displays the server's response (status code, headers, and body) and logs any connection errors to a file. 

**1. Prerequisites**

You need to install the `requests` library.
```bash
pip install requests
```

**2. Execution**

Run the script directly from your terminal.
```bash
python http_client.py
```

The script will send one successful **GET** and **POST** request, followed by a failing GET request to demonstrate the error logging feature. Check the http_errors.log file for logged errors.

### B. SMTP Client (smtp_client.py)

This script connects to an SMTP server to send a test email to a specified recipient. The full communication log with the server is printed to the console for reference. 


**1. Prerequisites**

This script uses Python's built-in libraries, so no installation is needed.

**2. Configuration**

Before running, you must edit the smtp_client.py file:

Set your sender_email address.

Set the receiver_email address.

⚠️ Important: If you are using a Gmail account with 2-Factor Authentication (2FA) enabled, you must generate and use an App Password. Your regular account password will not work and will result in an authentication error.

**3. Execution**

Run the script and enter your App Password when prompted.

```bash
python smtp_client.py
```

### C. FTP Client (ftp_client.py)

This script performs a complete FTP session: connecting to a server, listing directory contents, uploading a file, downloading it, and verifying its integrity. 

**1. Prerequisites**

No external libraries are required.

**2. Execution**

The script is pre-configured to use a public test FTP server, so no changes are needed. Simply run it from your terminal.

```bash
python ftp_client.py
```

It will automatically create a local test file, perform all FTP operations, print the progress, and clean up the created files afterward.

### D. DNS Query Tool (dns_tool.py)
This script resolves a given domain name to its IP address and retrieves different types of DNS records (A, MX, CNAME). All query results are saved to a log file. 


**1. Prerequisites**

You need to install the dnspython library.

```bash
pip install dnspython
```

**2. Configuration (Optional)**

You can easily query a different domain by modifying the DOMAIN_TO_QUERY variable inside the dns_tool.py script.

**3. Execution**

Run the script from your terminal.

```bash
python dns_tool.py
```

A log file named dns_log.txt will be created in the same directory containing the detailed results of the queries.
