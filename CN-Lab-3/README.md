# HTTP Caching and Cookie Management in Python

This project contains two Python server implementations to demonstrate fundamental concepts of the HTTP protocol: server-driven caching and cookie-based session management.

## Overview

This repository is divided into two parts:

1.  **Part 1: HTTP Caching Server**: An HTTP server that uses `ETag` and `Last-Modified` headers to reduce redundant data transfers by leveraging browser caching.
2.  **Part 2: Cookie Management Server**: An HTTP server built with raw sockets that manages client sessions using cookies to overcome the stateless nature of HTTP.

---

## Part 1: HTTP Caching Server

This server demonstrates how to implement conditional requests to optimize network bandwidth. It serves a single `index.html` file.

### How it Works

* **`Last-Modified` Header**: The server includes the file's last modification time in the response. A client can use this in a subsequent request with the `If-Modified-Since` header.
* **`ETag` Header**: The server generates an MD5 hash of the file's content and sends it as an `ETag` (entity tag). This is a strong validator. The client can send this value back in an `If-None-Match` header to check if the content has changed.
* **`304 Not Modified`**: If the client's cached version is still valid (based on the headers), the server responds with a `304 Not Modified` status and an empty body, saving bandwidth.
* **`200 OK`**: If the file has been modified or the client has no cache, the server sends the full content along with the new `ETag` and `Last-Modified` headers.

### How to Run

1.  Make sure `caching_server.py` and `index.html` are in the same directory.
2.  Run the server from your terminal:
    ```bash
    python caching_server.py
    ```
3.  Open your web browser and navigate to `http://localhost:8000`.

### How to Test

1.  Open your browser's **Developer Tools** and go to the **Network** tab.
2.  Load the page. You will see a `200 OK` status. Note the `ETag` and `Last-Modified` headers in the response.
3.  Refresh the page. You should now see a `304 Not Modified` status, indicating the browser used its cached version.
4.  Modify the content inside `index.html` and save the file.
5.  Refresh the page again. You will see a `200 OK` status with the new content and updated `ETag` and `Last-Modified` headers.

---

## Part 2: Cookie Management Server

This server is built using Python's low-level `socket` module to demonstrate how cookies are used for client identification and session management.

### How it Works

* The server listens for TCP connections on a raw socket.
* It manually parses HTTP request headers to check for a `Cookie` header.
* **First-Time Visit**: If no `session_id` cookie is found, the server sends a response that includes a `Set-Cookie` header, assigning a value like "User123". It displays a generic welcome message.
* **Returning Visit**: If a `session_id` cookie is found in the request, the server extracts its value and displays a personalized "Welcome back" message, demonstrating a persistent session.

### How to Run

1.  Run the server from your terminal:
    ```bash
    python cookie_server.py
    ```
2.  Open your web browser and navigate to `http://localhost:8080`.

### How to Test

1.  **First Visit**: Load the page. You will see the "Welcome, new visitor!" message. In your browser's Developer Tools (Application -> Cookies), you will see a `session_id` cookie has been set.
2.  **Second Visit**: Refresh the page. The browser now sends the cookie back to the server in the request header. The server will respond with the "Welcome back, User123!" message.
3.  Clear your browser's cookies for `localhost` and refresh the page. You will once again be treated as a new visitor.

---

## Files in this Repository

* `caching_server.py`: The Python code for the caching server (Part 1).
* `index.html`: The HTML file served by the caching server.
* `cookie_server.py`: The Python code for the cookie management server (Part 2).
* `README.md`: This file.
