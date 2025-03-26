import nmap
import os

# Ensure Nmap is in PATH
os.environ["PATH"] += os.pathsep + "C:\\Program Files (x86)\\Nmap"

def nmap_scan(target, ports):
    scanner = nmap.PortScanner()
    scanner.scan(target, ports)

    # Check if target is in scan results
    if target not in scanner.all_hosts():
        print(f"[-] No scan results for {target}. The host may be down or blocked.")
        return []

    # Check if 'tcp' key exists
    if 'tcp' not in scanner[target]:
        print(f"[-] No open TCP ports found on {target}.")
        return []

    open_ports = [int(port) for port in scanner[target]['tcp'] if scanner[target]['tcp'][port]['state'] == 'open']
    return open_ports

# Manual IP Entry
target_ip = input("Enter Target IP: ")
port_range = input("Enter Port Range (e.g., 1-1000): ")

open_ports = nmap_scan(target_ip, port_range)
print("Open Ports:", open_ports if open_ports else "No open ports found.")

