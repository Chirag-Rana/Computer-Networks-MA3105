# File: ip_utils.py
# Implements Part 1: IP Address and Subnet Utilities 

def ip_to_binary(ip_address: str) -> str:
    """
    Converts a standard dotted-decimal IP address to a 32-bit binary string.
    [cite: 13, 14]
    """
    # Split the IP into its four octets
    octets = ip_address.split('.')
    
    # Convert each octet to an 8-bit binary string, padding with leading zeros
    # [cite: 16]
    binary_octets = [bin(int(octet))[2:].zfill(8) for octet in octets]
    
    # Join the four binary strings to create the 32-bit representation
    return "".join(binary_octets) # [cite: 15]

def get_network_prefix(ip_cidr: str) -> str:
    """
    Takes a CIDR notation string and returns the network prefix as a binary string.
    [cite: 17, 18, 19]
    """
    # Split the CIDR string into the IP address and the prefix length
    try:
        ip_address, prefix_len_str = ip_cidr.split('/')
        prefix_length = int(prefix_len_str)
    except ValueError:
        return "Invalid CIDR format"

    # Use the function from the previous step to get the full binary IP
    # [cite: 21]
    full_binary_ip = ip_to_binary(ip_address)
    
    # Slice the binary string to get only the network prefix portion
    return full_binary_ip[:prefix_length] # [cite: 20]

# --- Test Cases for Part 1 ---
if __name__ == "__main__":
    print("--- Testing Part 1: ip_utils.py ---")
    
    # Test ip_to_binary [cite: 14, 15]
    test_ip = "192.168.1.1"
    expected_binary = "11000000101010000000000100000001"
    print(f"ip_to_binary('{test_ip}')")
    print(f"  Result:   {ip_to_binary(test_ip)}")
    print(f"  Expected: {expected_binary}")
    assert ip_to_binary(test_ip) == expected_binary

    # Test get_network_prefix [cite: 19, 20]
    test_cidr = "200.23.16.0/23"
    expected_prefix = "11001000000101110001000"
    print(f"\nget_network_prefix('{test_cidr}')")
    print(f"  Result:   {get_network_prefix(test_cidr)}")
    print(f"  Expected: {expected_prefix}")
    assert get_network_prefix(test_cidr) == expected_prefix
    print("Part 1 Tests Passed.")
