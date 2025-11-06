# Computer Networks Lab: Data Plane Simulation

This project is a Python-based simulation of core components of a network router's data plane. It implements and simulates fundamental networking tasks as described in the "Computer Networks Lab" assignment, focusing on IP address manipulation, router forwarding logic, and output port scheduling.

## 🚀 Features

* **IP Address Utilities:** Convert dotted-decimal IP addresses to 32-bit binary strings and extract binary network prefixes from CIDR notation.
* **Router Forwarding Logic:** A `Router` class that uses the **Longest Prefix Match (LPM)** algorithm to determine the correct output link for a given destination IP.
* **Packet Scheduling Simulation:** Implementation of two common output port scheduling policies: **First-Come, First-Served (FIFO)** and **Priority Scheduling**.

---

## 📂 Modules

This project is divided into three main Python files:

### 1. IP Utilities (`ip_utils.py`)

This module provides essential helper functions for handling IP addresses.

* `ip_to_binary(ip_address: str) -> str`: Converts a standard dotted-decimal IP address (e.g., `"192.168.1.1"`) into its full 32-bit binary string representation (e.g., `"11000000101010000000000100000001"`).
* `get_network_prefix(ip_cidr: str) -> str`: Takes a CIDR notation string (e.g., `"200.23.16.0/23"`) and returns only the binary network prefix (e.g., `"11001000000101110001000"`).

### 2. Router (`router.py`)

This module simulates the core forwarding logic of a router's input port. It depends on `ip_utils.py`.

* **`Router` class**:
    * `__init__(self, routes)`: Initializes the router with a list of routes (e.g., `[("223.1.1.0/24", "Link 0")]`).
    * `_build_forwarding_table(self, routes)`: A private method that processes the routes into an internal, optimized format. It stores binary prefixes and **sorts the table by prefix length (longest to shortest)** to enable the LPM algorithm.
    * `route_packet(self, dest_ip: str) -> str`: The main function. It takes a destination IP string, converts it to binary, and iterates through the *sorted* forwarding table. It returns the output link of the first (and therefore longest) matching prefix. If no match is found, it returns `"Default Gateway"`.

### 3. Scheduler (`scheduler.py`)

This module simulates a router's output port, which must schedule packets for transmission.

* **`Packet` class**: A simple dataclass to store packet attributes, including `source_ip`, `dest_ip`, `payload`, and `priority` (where 0=High, 1=Medium, 2=Low).
* `fifo_scheduler(packet_list: list) -> list`: Simulates a First-Come, First-Served queue. It returns the packets in the same order they arrived.
* `priority_scheduler(packet_list: list) -> list`: Simulates a Priority scheduler. It returns the packets sorted by their `priority` attribute, ensuring high-priority packets are sent first.

---

## 🛠️ How to Use

Each of the three Python files (`ip_utils.py`, `router.py`, and `scheduler.py`) contains its own test suite within an `if __name__ == "__main__":` block.

To run the tests and see the implementation in action, simply execute each file directly using Python:

```bash
# Test the IP utility functions
python ip_utils.py

# Test the Router class and Longest Prefix Match
python router.py

# Test the FIFO and Priority schedulers
python scheduler.py
