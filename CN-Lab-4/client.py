import cv2
import socket
import numpy as np
import struct

# --- Configuration ---
# Client will listen on this IP and port
LISTEN_IP = '0.0.0.0' # Listen on all available interfaces
LISTEN_PORT = 9999
# Buffer size for receiving data, should be larger than chunk size
BUFFER_SIZE = 65536 

def main():
    """
    Main function to run the video streaming client.
    """
    # 1. Create a UDP socket and bind it to the listening port [cite: 31]
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((LISTEN_IP, LISTEN_PORT))
    print(f"Listening for video stream on {LISTEN_IP}:{LISTEN_PORT}")

    frame_buffer = b''

    try:
        # 2. Receive packets continuously in a loop [cite: 32]
        while True:
            # Receive a packet from the server
            packet, _ = client_socket.recvfrom(BUFFER_SIZE)
            if not packet:
                continue

            # Unpack the header (first byte) to get the marker
            # The header indicates if this is the last packet of a frame
            header = struct.unpack('!B', packet[:1])[0]
            chunk = packet[1:]

            # 3. Append the data chunk to our frame buffer [cite: 33]
            frame_buffer += chunk

            # If the marker is 1, it's the last packet of the frame [cite: 33]
            if header == 1:
                try:
                    # 4. Decode the complete frame data and display it [cite: 34]
                    # Convert byte buffer to a NumPy array
                    np_arr = np.frombuffer(frame_buffer, dtype=np.uint8)
                    # Decode the NumPy array as a color image
                    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

                    # Display the frame if it was successfully decoded
                    if frame is not None:
                        cv2.imshow("Video Stream", frame)
                    
                    # Reset the buffer for the next frame
                    frame_buffer = b''

                except Exception as e:
                    print(f"Error decoding frame: {e}")
                    # Reset buffer even if decoding fails
                    frame_buffer = b'' 
            
            # 5. Stop when the user presses the 'q' key [cite: 35]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Clean up resources
        print("Closing socket and windows.")
        client_socket.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
