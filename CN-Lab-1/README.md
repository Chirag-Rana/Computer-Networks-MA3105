# CN Lab 1: TCP Client-Server Application

## 🎯 Objective

This project is a TCP-based client-server application. The client sends its name and a number to the server. The server then responds with its own name and another number. Finally, both the client and the server display all the exchanged values and compute the sum of the two numbers.

-   **Client Requirements:** The client must accept an integer between 1 and 100 from the user, send a message containing its name and the number, wait for the server's reply, and then display both names, both numbers, and their sum.
-   **Server Requirements:** The server listens for client connections. For each message, it extracts the client's data, picks its own number, displays both names and numbers with their sum, and sends its own name and number back to the client. The server must terminate if it receives a number outside the 1-100 range.

---

## 🚀 How to Run

### Prerequisites

-   Python 3.x

### Instructions

Follow these steps to run the application. You will need two separate terminal windows.

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/Chirag-Rana/Computer-Networks-MA3105
    cd CN-Lab-1
    ```

2.  **Start the Server**

    Open your first terminal and run the `server.py` script. The server will start and wait for a client to connect.

    ```bash
    python server.py
    ```

    You should see the following output, indicating the server is ready:
    ```
    ✅ Server is listening on 127.0.0.1:65432
    ```

3.  **Run the Client**

    Open a second terminal and run the `client.py` script.

    ```bash
    python client.py
    ```

    The client will prompt you to enter a number. After you enter a number and press Enter, the client will communicate with the server, and both terminals will display the results.

---

## 📊 Sample Output

### Server Terminal

```bash
✅ Server is listening on 127.0.0.1:65432
🤝 Connected by ('127.0.0.1', 51834)

--- Received Data ---
Client's Name: Testing Client
Server's Name: Testing Server
Client's Number: 42
Server's Number: 77
Sum of Integers: 119

✅ Response sent to client.
🔌 Server has shut down.
