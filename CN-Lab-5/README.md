# Computer Networks Protocol Simulations

This repository contains Python scripts that simulate fundamental data transmission and congestion control protocols as part of a computer networks assignment. The simulations cover Stop-and-Wait ARQ, Go-Back-N ARQ, and TCP Congestion Control mechanisms.

## 📋 Table of Contents

* [Tasks Overview](#-tasks-overview)
* [Technologies Used](#-technologies-used)
* [Getting Started](#-getting-started)
* [Usage and Outputs](#-usage-and-outputs)
    * [Task 1: Stop-and-Wait ARQ](#task-1-stop-and-wait-arq)
    * [Task 2: Go-Back-N ARQ](#task-2-go-back-n-arq)
    * [Task 3: TCP Congestion Control](#task-3-tcp-congestion-control)

---

## ✨ Tasks Overview

This project implements three core networking concepts:

1.  **Stop-and-Wait ARQ**: A simulation of the simplest ARQ protocol where the sender transmits one frame and waits for an acknowledgment before sending the next. The simulation includes random frame/ACK loss and retransmission after a timeout.
2.  **Go-Back-N ARQ**: A simulation of the sliding window protocol using Go-Back-N logic. The sender can transmit multiple frames (up to a window size $N$) and the receiver sends cumulative ACKs. On frame loss, the sender retransmits all frames starting from the lost one.
3.  **TCP Congestion Control**: A simulation that models the behavior of TCP's congestion window (`cwnd`). It visualizes the **Slow Start** (exponential growth), **Congestion Avoidance** (linear growth), and **Multiplicative Decrease** phases that occur upon packet loss (timeout).

---

## 🛠️ Technologies Used

* **Language**: Python 3
* **Libraries**:
    * `random`, `time` (Standard libraries)
    * `matplotlib` (for plotting in the TCP Congestion Control simulation)

---

## 🚀 Getting Started

To run these simulations, you'll need Python 3 and Matplotlib installed.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Chirag-Rana/Computer-Networks-MA3105
    cd CN-Lab-5
    ```

2.  **Install Matplotlib:**
    ```bash
    pip install matplotlib
    ```

---

## 💻 Usage and Outputs

Each simulation can be run directly from the command line. You can modify parameters like `total_frames`, `window_size`, and `loss_prob` within each script to observe different behaviors.

### Task 1: Stop-and-Wait ARQ

* **File**: `stop_and_wait.py`
* **To Run**:
    ```bash
    python stop_and_wait.py
    ```
* **Expected Output**: The terminal will display the sequence of frames being sent, acknowledged, lost, and retransmitted after timeouts.

    ```text
    --- Stop-and-Wait ARQ Simulation ---
    Sending Frame 0
    ACK 0 received
    Sending Frame 1
    Timeout for Frame 1, retransmitting...
    Sending Frame 1
    ACK 1 received
    Sending Frame 2
    ACK for Frame 2 was lost.
    Timeout for Frame 2, retransmitting...
    Sending Frame 2
    ACK 2 received
    ...
    --- Simulation Complete ---
    ```

### Task 2: Go-Back-N ARQ

* **File**: `go_back_n.py`
* **To Run**:
    ```bash
    python go_back_n.py
    ```
* **Expected Output**: The terminal shows frames being sent in a window, the reception of cumulative ACKs, and the "go-back" retransmission process when a frame is lost.

    ```text
    --- Go-Back-N ARQ Simulation (Window Size: 4) ---
    Sending Frame 0
    Sending Frame 1
    Sending Frame 2
    Sending Frame 3
    -> Cumulative ACK 4 received. Window slides.
    --------------------
    Sending Frame 4
    Sending Frame 5
    Sending Frame 6
    Sending Frame 7
    !! Frame 6 was lost.
    Timeout! Retransmitting from Frame 6.
    --------------------
    ...
    --- Simulation Complete ---
    ```

### Task 3: TCP Congestion Control

* **File**: `congestion_control.py`
* **To Run**:
    ```bash
    python congestion_control.py
    ```
* **Expected Output**: The script will print the state of `cwnd` and `ssthresh` for each round to the terminal. More importantly, it will generate and display a plot, saving it as `cwnd_plot.png`. This plot visualizes the exponential and linear growth phases of `cwnd` and its reduction upon packet loss.

    ![TCP Congestion Window Plot](cwnd_plot.png)

---
