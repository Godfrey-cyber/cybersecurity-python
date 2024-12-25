from scapy.all import *

# Function to capture and print network packets
def packet_sniffer(packet):
    print(packet.show())

# Sniff the network for 10 seconds
if __name__ == "__main__":
    print("Starting packet sniffer...")
    sniff(prn=packet_sniffer, timeout=10)  # Capture for 10 seconds
