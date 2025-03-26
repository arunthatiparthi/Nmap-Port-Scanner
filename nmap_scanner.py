import nmap

def nmap_scan(target, ports):
    scanner = nmap.PortScanner()
    scanner.scan(target, ports)
    open_ports = [int(port) for port in scanner[target]['tcp'] if scanner[target]['tcp'][port]['state'] == 'open']
    return open_ports

# Manual IP Entry
target_ip = input("Enter Target IP: ")
port_range = input("Enter Port Range (e.g., 1-1000): ")
open_ports = nmap_scan(target_ip, port_range)

print("Open Ports:", open_ports)
