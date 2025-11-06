import networkx as nx
import pprint

# Create a network graph with link costs (e.g., latency) [cite: 35]
G = nx.Graph()
G.add_edge('A', 'B', cost=5)
G.add_edge('A', 'C', cost=2)
G.add_edge('B', 'D', cost=4)
G.add_edge('B', 'E', cost=3)
G.add_edge('C', 'F', cost=6)
G.add_edge('C', 'G', cost=8)
G.add_edge('D', 'H', cost=1)
G.add_edge('E', 'H', cost=3)
G.add_edge('F', 'H', cost=7)
G.add_edge('G', 'H', cost=2)

routers = list(G.nodes)

# Simulate LSA exchange: In this simulation, we assume all routers
# have the complete topology G (the synchronized link-state database) [cite: 33, 37]

print("--- Simulating OSPF (Dijkstra's Algorithm) ---")

# Each router calculates its own shortest path tree 
all_routing_tables = {}
all_shortest_path_trees = {}

for router in sorted(routers):
    # Use Dijkstra's to find shortest paths from the current router
    # This returns a tuple: (lengths, paths)
    paths_and_lengths = nx.single_source_dijkstra(G, router, weight='cost')
    
    lengths = paths_and_lengths[0]
    paths = paths_and_lengths[1]
    
    # Store the full path tree [cite: 38]
    all_shortest_path_trees[router] = paths
    
    # Build the routing table
    routing_table = {}
    for dest, path_list in paths.items():
        if len(path_list) == 1:
            # It's the router itself
            next_hop = '-'
        else:
            # The next hop is the second item in the path list
            next_hop = path_list[1]
        
        cost = lengths[dest]
        routing_table[dest] = (next_hop, cost)
        
    all_routing_tables[router] = routing_table

# Display the shortest path tree and routing table for each router [cite: 38]
print("\n--- Final Routing Tables (OSPF) ---")
for router in sorted(routers):
    print(f"\n[Router {router}]")
    print("Dest | Next Hop | Total Cost")
    print("------------------------------")
    for dest, (next_hop, cost) in sorted(all_routing_tables[router].items()):
        print(f" {dest}   |    {next_hop}     |     {cost} ")

print("\n--- Shortest Path Trees (OSPF) ---")
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(all_shortest_path_trees)
