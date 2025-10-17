# 📡 Computer Networks Lab: Wireshark Protocol Analysis Assignment

This repository contains the deliverables for the Computer Networks Lab assignment focusing on network traffic capture and protocol analysis using **Wireshark**.

The objective of this lab was to capture live network traffic, identify various network protocols (ICMP, DNS, TCP/TLS), and analyze packet-level details to understand communication patterns.

---

## 📁 Repository Contents

| File Name | Description |
| :--- | :--- |
| `capture.pcap` | **Raw Packet Capture** file containing all traffic captured while visiting websites and running the ping command.
| `filtered_packets.pcap` | Captured packets filtered to show only traffic originating from the system's IP (web traffic).
| `report.pdf` | **Final Assignment Report** summarizing key findings, most active protocols, insights, and unusual traffic observed.
| `http.png`, `icmp.png`, `dns.png`, `filtered.png` |Screenshots for protocol identification, detailed packet analysis, and custom filter creation.

---

## 🔬 Analysis Summary

The analysis highlighted the following key points:

1.  **Protocol Identification:** Demonstrated the use of Wireshark display filters (`icmp`, `dns`, `tcp.port == 443`) to isolate specific protocol traffic.
2.  **Encrypted Traffic:** The capture primarily contained **TLS/HTTPS traffic (TCP port 443)**, confirming that all website visits were secured, and thus, plain HTTP packets were absent.
3.  **Communication Flow:** Confirmed the basic network flow: DNS for name resolution, followed by TCP/TLS for application data transfer, and ICMP for basic network connectivity (`ping 8.8.8.8`).

---

## 🛠️ Tools Used

* **Wireshark:** Used for capturing traffic, applying display filters, analyzing packet details, and generating statistics.
