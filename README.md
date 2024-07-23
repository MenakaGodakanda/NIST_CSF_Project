# NIST Cybersecurity Framework Project

This project demonstrates the implementation of the NIST Cybersecurity Framework using open-source tools on Ubuntu.

## Overview
<img width="1266" alt="Screenshot 2024-07-23 at 5 38 47 PM" src="https://github.com/user-attachments/assets/3a955ff3-a7cf-4c44-b387-97c73c16fd91">

### Explanation
#### 1. Identify (Asset Management):
- The `identify/asset_management.py` script uses `nmap` to scan the network and identify connected devices.
- The discovered assets are documented in a JSON file (`assets.json`).

#### 2. Protect:
- Access Control:
  - The `protect/access_control.py` script manages user accounts and permissions using `adduser` and `chown`.
- Data Protection:
  - The `protect/data_encryption.py` script encrypts sensitive data files using `gnupg`.

#### 3. Detect (Intrusion Detection):
- The `detect/monitor_logs.py` script monitors Snort logs for suspicious activity.
- Snort configuration is set up in `detect/snort.conf`.

#### 4. Respond (Incident Response):
- The `respond/incident_response.py` script isolates affected machines by modifying `iptables` rules.

#### 5. Recover (Backup and Restore):
- The `recover/backup_restore.py` script backs up data from a source directory to a backup directory and restores data when needed using `shutil`.

## Setting Up the Project

### 1. Clone the repository:
```bash
git clone https://github.com/MenakaGodakanda/NIST_CSF_Project.git
cd NIST_CSF_Project
```

### 2. Install Tools:
1. **Python**: The primary scripting language for the project.
```
sudo apt install python3 python3-pip
```
2. **iptables**: A user-space utility program that allows a system administrator to configure the IP packet filter rules of the Linux kernel firewall.
```
sudo apt-get install iptable
```
3. **Nmap**: Nmap is used to discover hosts and services on a computer network by sending packets and analyzing the responses. This project uses `nmap` to scan the network and identify assets.
- Install `nmap` on the system:
```
sudo apt install nmap
```
- Install the `python-nmap` package for scripting:
```
pip3 install python-nmap
```
4. **GnuPG**: GnuPG allows the encryption and signing of data and communications. This project uses `gnupg` to implement encryption for sensitive data.
- Install `gnupg` on the system:
```
sudo apt install gnupg
```
- Install the `python-gnupg` package for scripting:
```
pip3 install python-gnupg
```
5. **Snort**: Snort is lightweight network intrusion detection system (NIDS) software for Linux and Windows that detects emerging threats. This project uses `snort` to set up an intrusion detection system.
```
sudo apt install snort
```
## Identify

### Asset Management

- Script: `identify/asset_management.py`
- This script uses `nmap` to scan the network and identify connected devices. Run the script:
```
python3 identify/asset_management.py
```

- This script will create an `assets.json` file with the identified hosts.

## Protect

### Access Control

- Script: `protect/access_control.py`
- This script manages user permissions and access to directories. Run the script:
```
python3 protect/access_control.py
```

### Data Protection

- Script: `protect/data_encryption.py`
- This script encrypts sensitive data using `gnupg`. Run the script:
```
python3 protect/data_encryption.py
```

## Detect

### Intrusion Detection

- Snort configuration: `detect/snort.conf`
- Script: `detect/monitor_logs.py`
- This script monitors Snort logs for intrusion detection alerts. Run the script:
```
python3 detect/monitor_logs.py
```

## Respond

### Incident Response

- Script: `respond/incident_response.py`
- This script isolates affected machines by modifying `iptables` rules. Run the script:
```
python3 respond/incident_response.py
```

## Recover

### Backup and Restore

- Script: `recover/backup_restore.py`
- This script backs up and restores data using `shutil`. Run the script:
```
python3 recover/backup_restore.py
```

## Project Structure
```
NIST_CSF_Project/
├── identify/
│ └── asset_management.py
├── protect/
│ ├── access_control.py
│ └── data_encryption.py
├── detect/
│ └── monitor_logs.py
├── respond/
│ └── incident_response.py
├── recover/
│ └── backup_restore.py
└── README.md
```

## License
This project is licensed under the MIT License.
