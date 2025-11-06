import networkx as nx
import pprint

# 1. Create a graph representing routers and link metrics [cite: 55]
# We'll use the same graph as OSPF for comparison
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

# 2. Simulate link-state flooding and database synchronization [cite: 56]
# As with OSPF, we assume this step is complete and all routers
# have the full topology 'G'.

print("--- Simulating IS-IS (Dijkstra's Algorithm) ---")

all_routing_tables = {}

for router in sorted(routers):
    # 3. Use Dijkstra's algorithm to compute shortest paths 
    paths_and_lengths = nx.single_source_dijkstra(G, router, weight='cost')
    
    lengths = paths_and_lengths[0]
    paths = paths_and_lengths[1]
    
    # Build the routing table
    routing_table = {}
    for dest, path_list in paths.items():
        if len(path_list) == 1:
            next_hop = '-'
        else:
            next_hop = path_list[1]
        
        cost = lengths[dest]
        routing_table[dest] = (next_hop, cost)
        
    all_routing_tables[router] = routing_table

# 4. Display the final routing table for each router [cite: 58]
print("\n--- Final Routing Tables (IS-IS) ---")
for router in sorted(routers):
    print(f"\n[Router {router}]")
    print("Dest | Next Hop | Total Cost")
    print("------------------------------")
    for dest, (next_hop, cost) in sorted(all_routing_tables[router].items()):
        print(f" {dest}   |    {next_hop}     |     {cost} ")
