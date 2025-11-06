# Lab 7: Routing Protocols Simulation in Python

This project contains Python simulations for four fundamental network routing protocols as part of the Lab Assignment 7 requirements. Each simulation demonstrates the core algorithm and convergence behavior of the respective protocol.

## 🎯 Objective

The objective is to simulate the working of various routing protocols in Python. This includes understanding and implementing the key algorithms (Bellman-Ford, Dijkstra) and behaviors (Distance-Vector, Link-State, Path-Vector) for each protocol.

## 📂 Project Contents

This repository includes the following simulation files:

1.  `rip_simulation.py`: Simulates the **Routing Information Protocol (RIP)**, a distance-vector protocol using the Bellman-Ford algorithm to find the shortest path based on hop count.
2.  `ospf_simulation.py`: Simulates the **Open Shortest Path First (OSPF)** protocol, a link-state protocol using Dijkstra's algorithm to compute the shortest path tree based on link costs.
3.  `bgp_simulation.py`: Simulates the **Border Gateway Protocol (BGP)**, a path-vector protocol. This simplified simulation demonstrates AS path selection and loop prevention.
4.  `isis_simulation.py`: Simulates the **Intermediate System to Intermediate System (IS-IS)** protocol. As a link-state protocol, its core logic is similar to OSPF and also uses Dijkstra's algorithm.

## 🛠️ Requirements

The simulations use the `networkx` library for graph representation and algorithms.

* Python 3.x
* `networkx`

## 🚀 How to Run

1.  **Clone the repository (or download the files):**
    ```bash
    git clone https://github.com/Chirag-Rana/Computer-Networks-MA3105
    cd CN-Lab-7
    ```

2.  **Install the required library:**
    ```bash
    pip install networkx
    ```

3.  **Run any of the simulations:**
    Execute each Python file from your terminal to see the protocol simulation and its final converged routing tables.

    **Example (RIP):**
    ```bash
    python rip_simulation.py
    ```
    *Expected Output:*
    ```
    --- Simulating RIP Convergence ---
    
    Iteration 1:
    Iteration 2:
    ...
    Convergence reached! No further updates.
    
    --- Final Routing Tables (RIP) ---
    [Router A]
    Dest | Next Hop | Hop Count
    ----------------------------
     A   |    A     |     0
     B   |    B     |     1
     ...
    ```

    **Example (OSPF):**
    ```bash
    python ospf_simulation.py
    ```
    *Expected Output:*
    ```
    --- Simulating OSPF (Dijkstra's Algorithm) ---
    
    --- Final Routing Tables (OSPF) ---
    [Router A]
    Dest | Next Hop | Total Cost
    ------------------------------
     A   |    -     |     0
     B   |    B     |     5
     ...
    ```


