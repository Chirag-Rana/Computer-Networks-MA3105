# client.py

import socket

# 1. Define client and server configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
CLIENT_NAME = "Testing Client" # A string with your name [cite: 9]

# 2. Get integer from the user
# Accept an integer between 1 and 100 from the keyboard. [cite: 6]
while True:
    try:
        client_number_str = input("Enter an integer between 1 and 100: ")
        client_number = int(client_number_str)
        # Note: The server handles the final 1-100 validation as per requirements.
        # This loop just ensures an integer is entered.
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# 3. Create and connect the client socket
# Open a TCP socket connection to the server. [cite: 7]
# The 'with' statement ensures the socket is automatically closed [cite: 18]
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        # 4. Send the client's name and number to the server [cite: 8]
        message = f"{CLIENT_NAME};{client_number}"
        s.sendall(message.encode('utf-8'))
        print("\n⏳ Message sent. Waiting for server reply...")

        # 5. Wait for a reply from the server [cite: 10]
        data = s.recv(1024).decode('utf-8')
        
        # 6. On receiving the reply, process and display it [cite: 11]
        server_name, server_number_str = data.split(';')
        server_number = int(server_number_str)
        
        print("\n--- Results ---")
        print(f"Client's Name: {CLIENT_NAME}") # [cite: 13]
        print(f"Server's Name: {server_name}") # [cite: 14]
        print(f"Client's Integer: {client_number}") # [cite: 15]
        print(f"Server's Integer: {server_number}") # [cite: 16]
        
        # Calculate and display the sum
        total_sum = client_number + server_number
        print(f"Sum of Integers: {total_sum}") # [cite: 17]

except ConnectionRefusedError:
    print("❌ Connection failed. Is the server running?")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n🔌 Client has terminated.")
