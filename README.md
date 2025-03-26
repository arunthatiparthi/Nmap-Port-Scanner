# Nmap Port Scanner (Python)

## Overview
This is a simple Python script that scans a given IP address for open ports using the `nmap` library. It allows users to manually input the target IP and port range.

## Prerequisites
Ensure you have the following installed before running the script:
- **Python 3**
- **nmap** (installed on your system)
- **python-nmap** library

## Installation
1. Install `nmap` on your system:
   - **Linux/macOS:**
     ```bash
     sudo apt install nmap  # Debian-based (Ubuntu, Kali, etc.)
     sudo yum install nmap  # CentOS/RHEL
     brew install nmap      # macOS
     ```
   - **Windows:** Download and install it from [nmap.org](https://nmap.org/download.html).

2. Install the `python-nmap` library:
   ```bash
   pip install python-nmap
   ```

## Usage
1. Run the script:
   ```bash
   python nmap_scanner.py
   ```
2. Enter the target IP address when prompted.
3. Enter the port range (e.g., `1-1000`).
4. The script will display the open ports.

## Code Example
```python
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
```

## Features
- Scans a target IP for open ports.
- Uses Nmap for accurate scanning.
- Allows user-defined port range input.

## Troubleshooting
- If you get a `nmap.PortScannerError`, ensure that `nmap` is installed and accessible in your system's PATH.
- Run the script with **administrator/root privileges** if required.

