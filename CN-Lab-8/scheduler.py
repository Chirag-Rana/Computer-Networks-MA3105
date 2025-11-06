# File: scheduler.py
# Implements Part 3: Output Port Scheduling Simulation [cite: 60]

from dataclasses import dataclass

@dataclass
class Packet: # [cite: 65]
    """
    A simple class to represent a network packet.
    """
    source_ip: str # [cite: 67]
    dest_ip: str # [cite: 68]
    payload: str # [cite: 69]
    priority: int  # 0=High, 1=Medium, 2=Low [cite: 70]

def fifo_scheduler(packet_list: list) -> list:
    """
    Simulates a First-Come, First-Served (FCFS/FIFO) scheduler.
    [cite: 71, 72]
    """
    # For FIFO, the order of transmission is the same as the order of arrival.
    # We return a copy to avoid modifying the original list.
    # [cite: 73, 74]
    return packet_list.copy()

def priority_scheduler(packet_list: list) -> list:
    """
    Simulates a Priority Scheduler.
    [cite: 76, 77]
    """
    # Sorts the list based on the 'priority' attribute.
    # Lower numbers (higher priority) will come first. [cite: 80]
    # This uses the hint to sort the list. [cite: 81]
    return sorted(packet_list, key=lambda packet: packet.priority)

# --- Test Case for Part 3 ---
if __name__ == "__main__":
    print("\n--- Testing Part 3: scheduler.py ---")

    # Create the list of packets in arrival order [cite: 85]
    p1 = Packet(source_ip="1.1.1.1", dest_ip="2.2.2.2", payload="Data Packet 1", priority=2) # [cite: 87]
    p2 = Packet(source_ip="1.1.1.2", dest_ip="2.2.2.3", payload="Data Packet 2", priority=2) # [cite: 89]
    p3 = Packet(source_ip="1.1.1.3", dest_ip="2.2.2.4", payload="VOIP Packet 1", priority=0) # [cite: 91]
    p4 = Packet(source_ip="1.1.1.4", dest_ip="2.2.2.5", payload="Video Packet 1", priority=1) # [cite: 93]
    p5 = Packet(source_ip="1.1.1.5", dest_ip="2.2.2.6", payload="VOIP Packet 2", priority=0) # [cite: 94]
    
    arrival_list = [p1, p2, p3, p4, p5]
    
    print("Arrival Order (Payloads):")
    print([p.payload for p in arrival_list])
    
    # --- Verify FIFO Scheduler ---
    # [cite: 96]
    fifo_output = fifo_scheduler(arrival_list)
    fifo_payloads = [p.payload for p in fifo_output]
    print("\nFIFO Scheduler Output:")
    print(fifo_payloads)
    
    expected_fifo = ["Data Packet 1", "Data Packet 2", "VOIP Packet 1", "Video Packet 1", "VOIP Packet 2"] # [cite: 98]
    assert fifo_payloads == expected_fifo
    
    # --- Verify Priority Scheduler ---
    # [cite: 97]
    priority_output = priority_scheduler(arrival_list)
    priority_payloads = [p.payload for p in priority_output]
    print("\nPriority Scheduler Output:")
    print(priority_payloads)
    
    expected_priority = ["VOIP Packet 1", "VOIP Packet 2", "Video Packet 1", "Data Packet 1", "Data Packet 2"] # [cite: 100, 101]
    assert priority_payloads == expected_priority
    
    print("Part 3 Tests Passed.")
