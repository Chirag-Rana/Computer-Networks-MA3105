import networkx as nx
import time
import pprint

# Define an AS-level topology [cite: 44]
# We use a DiGraph (Directed Graph) because BGP relationships are directional
G = nx.DiGraph()
G.add_edges_from([
    ('AS1', 'AS2'), ('AS2', 'AS1'), # Peering
    ('AS1', 'AS3'), ('AS3', 'AS1'),
    ('AS2', 'AS4'), ('AS4', 'AS2'),
    ('AS3', 'AS4'), ('AS4', 'AS3'),
    ('AS4', 'AS5'), ('AS5', 'AS4') # AS5 is only connected to AS4
])

# Add a target prefix (e.g., a specific IP block) advertised by AS5
TARGET_PREFIX = "198.51.100.0/24"

# Routing tables (BGP tables)
# Format: bgp_tables[router] = {prefix: (best_as_path)}
bgp_tables = {router: {} for router in G.nodes}

# Initialize: AS5 originates the prefix
bgp_tables['AS5'][TARGET_PREFIX] = ['AS5']

def simulate_bgp_updates(G, bgp_tables):
    """
    Simulate BGP UPDATE message exchanges between neighboring ASes. [cite: 46]
    """
    converged = True
    
    # Iterate in a specific order for stable propagation (or multiple rounds)
    for u in G.nodes:
        # Get u's best path for the prefix
        path_info = bgp_tables[u].get(TARGET_PREFIX)
        if not path_info:
            continue # This router doesn't have a path to advertise yet

        # Send this path to all neighbors
        for v in G.neighbors(u):
            # BGP Loop Prevention: 
            # "discarding routes containing the local AS number"
            if v in path_info:
                continue # Neighbor v sees itself in the path, so it discards it.
            
            # Neighbor v receives the path and prepends its own AS
            new_path = [v] + path_info
            
            # Path selection based on AS path length 
            current_best_path = bgp_tables[v].get(TARGET_PREFIX)
            
            if not current_best_path or len(new_path) < len(current_best_path):
                # This new path is shorter, so update the table
                bgp_tables[v][TARGET_PREFIX] = new_path
                converged = False # A change occurred

    return converged

# --- Main Simulation ---
print(f"--- Simulating BGP Convergence for prefix {TARGET_PREFIX} ---")
print(f"Prefix originated by AS5.\n")
iteration = 0
while True:
    iteration += 1
    print(f"Iteration {iteration}...")
    converged = simulate_bgp_updates(G, bgp_tables)
    
    if converged:
        print("Convergence reached!")
        break
    
    time.sleep(0.5)

# Show final routing tables for all routers after convergence [cite: 48]
print("\n--- Final BGP Routing Tables ---")
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(bgp_tables)
