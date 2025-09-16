# Video Streaming over UDP using Python Sockets

This project is a simple implementation of a video streaming application using UDP sockets in Python, based on a computer networks lab assignment. The server reads a video file and streams it frame-by-frame to a client, which then displays the video in real-time. 


## 📝 Overview

The core of this project is the use of the **User Datagram Protocol (UDP)** for transmission. UDP is a connectionless protocol that offers low latency at the cost of reliability, making it suitable for real-time applications like video streaming where speed is more critical than ensuring every single packet arrives.

-   **Server (`server.py`)**: Reads a video file using OpenCV, encodes each frame into JPEG format, splits the compressed frame data into smaller chunks, and sends these chunks over a UDP socket to the client. 
-   **Client (`client.py`)**: Listens on a UDP port, receives the chunks, reassembles them into a complete frame, decodes the JPEG data, and displays the resulting video stream using OpenCV. 

## ✅ Requirements

To run this project, you will need:
* Python 3.x 
* OpenCV for Python (`opencv-python`) 
* NumPy 

## 🛠️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Chirag-Rana/Computer-Networks-MA3105
    cd CN-Lab-4
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install opencv-python numpy
    ```

3.  **Add a video file:**
    Place a video file in the root directory of the project. You can change the video file path by editing the `VIDEO_PATH` variable in `server.py`. Currently a        sample video URL has been placed in the variable.

## 🚀 How to Run

You need to run the server and the client scripts in two separate terminal windows.

1.  **Start the server:**
    Open a terminal and run the server script. It will wait to stream the video.
    ```bash
    python server.py
    ```
    You should see an output like:
    `Streaming video to 127.0.0.1:9999`

2.  **Start the client:**
    Open a second terminal and run the client script.
    ```bash
    python client.py
    ```
    A window titled "Video Stream" will pop up and begin displaying the video sent from the server.

3.  **Stop the client:**
    To stop the stream, make sure the client's video window is active and press the **'q'** key. 

## ⚙️ How It Works

The key challenge with sending video frames over UDP is that a single compressed frame is often larger than the maximum UDP packet size (~64KB).

-   **Chunking**: To solve this, the server splits each frame into smaller, fixed-size chunks that can fit into a single UDP packet.
-   **Frame Reassembly**: The server adds a 1-byte header to each chunk. This header acts as a marker: a value of `1` indicates the **last chunk of a frame**, while `0` indicates an intermediate chunk. The client collects incoming chunks until it receives one with the "last chunk" marker, at which point it knows the frame is complete and proceeds to decode and display it.
