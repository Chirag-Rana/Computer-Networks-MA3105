# server.py

import socket

# 1. Define server configuration
# Use a port number greater than 5000 [cite: 43]
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
SERVER_NAME = "Testing Server" # [cite: 20]
SERVER_NUMBER = 77 # Pick an integer between 1 and 100 [cite: 26]

# 2. Create and set up the server socket
# The 'with' statement ensures the socket is automatically closed
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen() # Listen for incoming TCP connections [cite: 21]
    print(f"✅ Server is listening on {HOST}:{PORT}")
    
    # Wait for a client to connect
    conn, addr = s.accept()
    
    # The 'with' statement ensures the connection socket is closed
    with conn:
        print(f"🤝 Connected by {addr}")
        
        # 3. Receive message from the client
        # For each received client message: [cite: 22]
        data = conn.recv(1024).decode('utf-8')
        if not data:
            print("❌ Client disconnected without sending data.")
        else:
            # Parse the received data (format: "ClientName;ClientNumber")
            client_name, client_number_str = data.split(';')
            client_number = int(client_number_str)

            # 4. Check if the client's number is valid
            # If the server receives a number outside 1-100, close all sockets and terminate. [cite: 35]
            if not 1 <= client_number <= 100:
                print(f"🚨 Invalid number received: {client_number}. Server is terminating.")
                # The 'with' statements will handle closing sockets.
            else:
                # 5. Display received and server values [cite: 23, 27]
                print("\n--- Received Data ---")
                print(f"Client's Name: {client_name}") # [cite: 24]
                print(f"Server's Name: {SERVER_NAME}") # [cite: 25]
                print(f"Client's Number: {client_number}") # [cite: 28]
                print(f"Server's Number: {SERVER_NUMBER}") # [cite: 29]
                
                # Calculate and display the sum
                total_sum = client_number + SERVER_NUMBER
                print(f"Sum of Integers: {total_sum}") # [cite: 30]

                # 6. Send server's name and number back to the client [cite: 31]
                response_message = f"{SERVER_NAME};{SERVER_NUMBER}" # [cite: 33, 34]
                conn.sendall(response_message.encode('utf-8'))
                print("\n✅ Response sent to client.")

print("🔌 Server has shut down.")
