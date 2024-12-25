import socket

# Function to scan a given host for open ports
def scan_ports(host):
    open_ports = []
    for port in range(1, 1025):  # Scanning ports 1-1024
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target IP or hostname: ")
    open_ports = scan_ports(target_host)
    if open_ports:
        print(f"Open ports on {target_host}: {open_ports}")
    else:
        print("No open ports found.")
