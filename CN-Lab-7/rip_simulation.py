import networkx as nx
import time

# Use a graph to represent the network topology [cite: 13, 26]
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('C', 'G'),
    ('D', 'H'), ('E', 'H'), ('F', 'H'), ('G', 'H')
])
routers = list(G.nodes)

# Each router maintains its own distance vector (routing table) 
# Format: routing_tables[router] = {destination: (next_hop, hop_count)}
routing_tables = {router: {dest: ('-', float('inf')) for dest in routers} for router in routers}

# Initialize tables: distance to self is 0
for router in routers:
    routing_tables[router][router] = (router, 0)

def simulate_rip_updates(G, routing_tables):
    """
    Simulates one round of periodic routing updates between neighbors. [cite: 28]
    """
    converged = True
    # Each router sends its table to its neighbors
    for u in G.nodes:
        for v in G.neighbors(u):
            # v receives u's table
            for dest, (next_hop_u, cost_u) in routing_tables[u].items():
                
                # Bellman-Ford algorithm logic [cite: 27]
                # The cost to get to 'dest' via 'u' is cost(v, u) + cost(u, dest)
                # In RIP, all link costs are 1 (hop count)
                new_cost = 1 + cost_u
                
                # If the new path is better, or if no path exists
                if new_cost < routing_tables[v][dest][1]:
                    routing_tables[v][dest] = (u, new_cost)
                    converged = False # A change occurred, so not converged
                
                # Handle the case where the current best path goes through the sender
                # This is a simplified check. Real RIP uses split horizon.
                elif routing_tables[v][dest][0] == u and new_cost > routing_tables[v][dest][1]:
                    routing_tables[v][dest] = (u, new_cost)
                    converged = False

    return converged

# --- Main Simulation ---
print("--- Simulating RIP Convergence ---")
iteration = 0
while True:
    iteration += 1
    print(f"\nIteration {iteration}:")
    converged = simulate_rip_updates(G, routing_tables)
    
    if converged:
        print("Convergence reached! No further updates.")
        break
    
    # Optional: Print tables at each step to see convergence
    # for router in routers:
    #     print(f"  Table for {router}: {routing_tables[router]}")
    
    time.sleep(0.5) # Simulate periodic delay

# Display final routing tables after convergence [cite: 29]
print("\n--- Final Routing Tables (RIP) ---")
for router in sorted(routers):
    print(f"\n[Router {router}]")
    print("Dest | Next Hop | Hop Count")
    print("----------------------------")
    for dest, (next_hop, cost) in sorted(routing_tables[router].items()):
        print(f" {dest}   |    {next_hop}     |     {cost} ")
