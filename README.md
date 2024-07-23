# NIST Cybersecurity Framework Project

This project demonstrates the implementation of the NIST Cybersecurity Framework using open-source tools on Ubuntu.

## Overview
<img width="1266" alt="Screenshot 2024-07-23 at 5 24 22 PM" src="https://github.com/user-attachments/assets/048d12fe-2da1-416d-b7bc-5c2facd05df0">

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

## Identify

### Asset Management

Script: `identify/asset_management.py`

This script uses `nmap` to scan the network and identify connected devices.

## Protect

### Access Control

Script: `protect/access_control.py`

This script manages user permissions and access to directories.

### Data Protection

Script: `protect/data_encryption.py`

This script encrypts sensitive data using `gnupg`.

## Detect

### Intrusion Detection

Snort configuration: `detect/snort.conf`

Script: `detect/monitor_logs.py`

This script monitors Snort logs for intrusion detection alerts.

## Respond

### Incident Response

Script: `respond/incident_response.py`

This script isolates affected machines by modifying `iptables` rules.

## Recover

### Backup and Restore

Script: `recover/backup_restore.py`

This script backs up and restores data using `shutil`.

