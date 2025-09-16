import cv2
import socket
import time
import struct

# --- Configuration ---
# Server will send to this IP and port
CLIENT_IP = '127.0.0.1'
CLIENT_PORT = 9999
# Max size of each UDP packet chunk
CHUNK_SIZE = 65500 
# Video file to stream
VIDEO_PATH = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4' 

def main():
    """
    Main function to run the video streaming server.
    """
    # 1. Create a UDP socket [cite: 21]
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_addr = (CLIENT_IP, CLIENT_PORT)
    print(f"Streaming video to {CLIENT_IP}:{CLIENT_PORT}")

    # 2. Open the video file [cite: 22]
    try:
        vid = cv2.VideoCapture(VIDEO_PATH)
        if not vid.isOpened():
            print(f"Error: Could not open video file at {VIDEO_PATH}")
            return
    except Exception as e:
        print(f"Error opening video capture: {e}")
        return

    # Get video FPS to control streaming speed
    fps = vid.get(cv2.CAP_PROP_FPS)
    frame_interval = 1 / fps if fps > 0 else 0.033 # Default to ~30 FPS if fps is 0
    print(f"Video FPS: {fps:.2f}, Frame Interval: {frame_interval:.4f}s")

    try:
        # 3. Loop through each frame of the video [cite: 24]
        while vid.isOpened():
            ret, frame = vid.read()
            if not ret:
                print("End of video stream.")
                break

            # (a) Resize and encode the frame into JPEG format [cite: 25]
            # Resizing reduces data size
            frame = cv2.resize(frame, (640, 480)) 
            # Encoding compresses the image data
            result, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            if not result:
                continue
            
            data = buffer.tobytes()
            data_size = len(data)

            # (b) Split the frame data into chunks [cite: 26]
            num_chunks = (data_size // CHUNK_SIZE) + 1

            for i in range(num_chunks):
                start = i * CHUNK_SIZE
                end = start + CHUNK_SIZE
                chunk = data[start:end]

                # (c) Send each chunk with a header [cite: 27]
                # The header is a single byte: 1 if it's the last packet of a frame, 0 otherwise.
                marker = 1 if i == num_chunks - 1 else 0
                header = struct.pack('!B', marker) # 'B' for unsigned char (1 byte)
                
                # Prepend header to the chunk and send
                message = header + chunk
                server_socket.sendto(message, client_addr)
            
            # 4. Sleep for the calculated frame interval to maintain FPS [cite: 28]
            time.sleep(frame_interval)

    finally:
        # 5. Clean up resources
        print("Closing resources.")
        vid.release()
        server_socket.close()

if __name__ == "__main__":
    main()
