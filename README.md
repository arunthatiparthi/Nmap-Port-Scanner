# Nmap Port Scanner

## Overview
This Python script utilizes the `nmap` module to perform a port scan on a given target IP address and port range. It checks for open TCP ports and provides the scan results.

## Prerequisites
Ensure you have the following installed:

1. **Python** (Ensure Python 3 is installed)
2. **Nmap** (Download and install from [Nmap Official Website](https://nmap.org/download.html))
3. **Python-nmap** (Install using `pip`)
   ```sh
   pip install python-nmap
   ```

## Installation & Setup
1. Clone or download this repository.
2. Ensure Nmap is installed and available in your system's PATH.
3. Run the script with Python:
   ```sh
   python nmap_scanner.py
   ```

## Usage
1. Enter the **target IP address** when prompted.
2. Enter the **port range** (e.g., `1-1000`).
3. The script will scan the provided IP and display open TCP ports.

## Example Output
```sh
Enter Target IP: 192.168.1.1
Enter Port Range (e.g., 1-1000): 1-50
Open Ports: [22, 80, 443]
```

## Troubleshooting
### "nmap program was not found in path"
- Ensure Nmap is installed and added to your system's environment PATH.
- Run the following command to verify:
  ```sh
  nmap --version
  ```

### "No scan results for target"
- Ensure the target IP is reachable (try `ping <target-ip>`).
- Run the script as **Administrator** on Windows or use `sudo` on Linux.

### "No open TCP ports found"
- The target might not have any open TCP ports in the specified range.
- Try scanning a known target like:
  ```sh
  Enter Target IP: scanme.nmap.org
  Enter Port Range (e.g., 1-1000): 22-80
  ```


