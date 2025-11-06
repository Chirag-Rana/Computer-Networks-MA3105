# File: router.py
# Implements Part 2: Router Forwarding Table (Longest Prefix Match) [cite: 24]

# Import the utility functions from Part 1
import ip_utils 

class Router: # [cite: 29]
    def __init__(self, routes):
        """
        Initializes the Router with a list of routes.
        [cite: 30, 31, 32]
        """
        # Call the helper method to process and store the routes [cite: 34]
        self.forwarding_table = self._build_forwarding_table(routes) # [cite: 35]

    def _build_forwarding_table(self, routes):
        """
        Processes the human-readable routes into an optimized internal table.
        [cite: 36, 37]
        """
        internal_table = []
        for cidr, link in routes:
            # Convert the CIDR prefix to its binary representation [cite: 38]
            # We can't use get_network_prefix directly as we need the *full*
            # binary IP to extract the prefix correctly.
            ip, prefix_len_str = cidr.split('/')
            prefix_length = int(prefix_len_str)
            
            binary_ip = ip_utils.ip_to_binary(ip)
            binary_prefix = binary_ip[:prefix_length]
            
            internal_table.append((binary_prefix, link))
        
        # Sort the table by prefix length, from longest to shortest [cite: 39]
        internal_table.sort(key=lambda item: len(item[0]), reverse=True)
        
        return internal_table

    def route_packet(self, dest_ip: str) -> str:
        """
        Performs Longest Prefix Match for a destination IP.
        [cite: 40, 42, 43]
        """
        # (a) Convert the destination IP to 32-bit binary [cite: 44]
        binary_dest_ip = ip_utils.ip_to_binary(dest_ip)
        
        # (b) Iterate through the sorted internal forwarding table [cite: 45]
        for prefix, link in self.forwarding_table:
            # (c) Check if the binary destination IP starts with the prefix [cite: 46]
            if binary_dest_ip.startswith(prefix):
                # (d) First match is the longest match, return the link [cite: 47, 48]
                return link
        
        # (e) If no match is found, return the default route [cite: 49]
        return "Default Gateway"

# --- Test Case for Part 2 ---
if __name__ == "__main__":
    print("\n--- Testing Part 2: router.py ---")
    
    # Initialize the router with the test routes [cite: 50]
    test_routes = [
        ("223.1.1.0/24", "Link 0"), 
        ("223.1.2.0/24", "Link 1"), 
        ("223.1.3.0/24", "Link 2"), 
        ("223.1.0.0/16", "Link 4 (ISP)")
    ] # [cite: 51, 52]
    
    my_router = Router(test_routes)
    
    print("Internal Forwarding Table (Sorted by prefix length):")
    for prefix, link in my_router.forwarding_table:
        print(f"  Prefix: {prefix.ljust(24)} ({len(prefix)} bits) -> {link}")

    # --- Verification ---
    print("\nVerifying route_packet():")
    
    # Test 1: Should match "223.1.1.0/24" [cite: 54]
    ip1 = "223.1.1.100"
    print(f"Routing '{ip1}' -> {my_router.route_packet(ip1)}")
    assert my_router.route_packet(ip1) == "Link 0"
    
    # Test 2: Should match "223.1.2.0/24" [cite: 57]
    ip2 = "223.1.2.5"
    print(f"Routing '{ip2}' -> {my_router.route_packet(ip2)}")
    assert my_router.route_packet(ip2) == "Link 1"
    
    # Test 3: Should fail /24, match "223.1.0.0/16" [cite: 58]
    ip3 = "223.1.250.1"
    print(f"Routing '{ip3}' -> {my_router.route_packet(ip3)}")
    assert my_router.route_packet(ip3) == "Link 4 (ISP)"
    
    # Test 4: Should match nothing, return default [cite: 59]
    ip4 = "198.51.100.1"
    print(f"Routing '{ip4}' -> {my_router.route_packet(ip4)}")
    assert my_router.route_packet(ip4) == "Default Gateway"
    
    print("Part 2 Tests Passed.")
