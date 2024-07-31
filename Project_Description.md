# NIST Cybersecurity Framework Project - Version 1

This project demonstrates the implementation of the NIST Cybersecurity Framework using open-source tools on Ubuntu.

## Features

### 1. Asset Management (Identify)
- **Purpose**: Inventory and manage organizational assets.
- **Key Functionality**:
  - Automatic discovery of network devices.
  - Logging of identified devices with their IP addresses, MAC addresses, and open ports.

### 2. Access Control (Protect)
- **Purpose**: Manages user accounts and permissions.
- **Key Functionality**:
  - Add new users to the system.
  - Setting directory permission to a user.

### 3. Data Encryption (Protect)
- **Purpose**: Ensure data confidentiality and integrity.
- **Key Functionality**:
  - Encryption of specified files.
  - Use of public key cryptography to secure data.

### 4. Log Monitoring (Detect)
- **Purpose**: Detect potential security incidents.
- **Key Functionality**:
  - Real-time monitoring of Snort logs.
  - Detection of various types of attacks, such as network scans and information leaks.
  - Notification of detected incidents.

### 5. Incident Response (Respond)
- **Purpose**: Respond to detected cybersecurity events.
- **Key Functionality**:
  - Automatic response to specific incidents (e.g., blocking an IP address).
  - Logging and notification of response actions.
  - Integration with other tools for comprehensive incident management.

### 6. Data Backup and Restoration (Recover)
- **Purpose**: Ensure data availability and integrity post-incident.
- **Key Functionality**:
  - Scheduled and on-demand backups of specified directories.
  - Restoration of data from backups.
  - Logging of backup and restoration operations.

## Coding

### Identify: Asset Management (`asset_management.py`)
This script uses the `nmap` library to scan the local network and list all devices.
- **Importing nmap**: The `nmap` library is used to perform network scanning. Ensure it is installed via `pip install python-nmap`.
- **Defining `scan_network` Function**:
  - Initializes a `PortScanner` object.
  - Scans the local network (substitute `192.168.1.0/24` with your network range).
  - Iterates through all detected hosts and prints their IP addresses and hostnames.
- **Running the Script**: When executed, the script runs the `scan_network` function.

### Protect: Access Control(`access_control.py`)
- **Importing Libraries**: The `subprocess` module is imported to run system commands from within the Python script. It allows for the execution of shell commands, capturing their output, and handling errors.
- **Defining `add_user` Function**:
  - Adds a new user to the system.
  - `sudo` is used to execute the command with superuser privileges.
- **Defining `set_permissions` Function**:
  - Sets the ownership of a directory and its contents to a specified user.
  - Runs the `chown` command with `sudo` to change the ownership of the directory and its contents to the specified user.
- **Running the Script**: When executed, the script runs the `add_user` and `set_permissions` function.

### Protect: Data Encryption (`data_encryption.py`)
- **Importing gnupg**: The `gnupg` library is used for encryption. Install it via `pip install python-gnupg`.
- **Defining `encrypt_file` Function**:
  - Initializes a `GPG` object.
  - Opens the specified file in binary read mode.
  - Encrypts the file for the specified recipient and writes the encrypted file with a `.gpg` extension.
  - Returns the encryption status.
- **Running the Script**: Defines the file to encrypt and the recipient, then calls `encrypt_file` and prints the result.

### Detect: Log Monitoring (`monitor_logs.py`)
- **Importing Libraries**: `time` for delay management and `os` for file operations.
- **Defining `monitor_logs` Function**:
  - Continuously checks if the specified log file exists.
  - Once the file exists, opens it and seeks to the end.
  - Continuously reads new lines from the log file, printing each new log entry.
- **Running the Script**: Calls the `monitor_logs` function with the Snort log file path.

### Respond: Incident Response (`incident_response.py`)
- **Importing Libraries**: `smtplib` for sending emails and `email.mime.text` for creating email messages.
- **Defining `send_alert` Function**:
  - Creates an email message with the specified subject and body.
  - Sends the email via an SMTP server.
- **Defining `analyze_logs` Function**:
  - Opens the log file and reads it line by line.
  - Sends an email alert if a line contains "ALERT".
- **Running the Script**: Specifies the log file and calls `analyze_logs`.

### Recover: Backup and Restore (`backup_restore.py`)
- **Importing Libraries**: `shutil` for file operations and `os` for path operations.
- **Defining `backup_data` Function**:
  - Checks if the destination directory exists and removes it if it does.
  - Copies the source directory to the destination.
- **Defining `restore_data` Function**:
  - Similar to backup_data, but copies from the backup directory to the target directory.
- **Running the Script**: Specifies the source, backup, and target directories, then calls `backup_data` and `restore_data`.

## Snort Alert Analysis
### Log Entries Generated by Snort
The Snort alert log provides a chronological record of various network activities that have been flagged as potentially suspicious or malicious. 
```
07/23-15:58:35.761583  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.7:51226 -> 239.255.255.250:1900
07/23-15:58:36.318756  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.3:161
07/23-15:58:36.683690  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.7:51226 -> 239.255.255.250:1900
07/23-15:58:37.708027  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.7:51226 -> 239.255.255.250:1900
07/23-15:58:38.151467  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.2:161
07/23-15:58:38.734180  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.7:51226 -> 239.255.255.250:1900
07/23-15:58:39.743117  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.20:161
07/23-15:58:39.844201  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.20:161
07/23-15:58:50.741663  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.18:161
07/23-15:58:50.842137  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.18:161
07/23-15:58:51.172182  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.16:161
07/23-15:58:51.972138  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.16:161
07/23-15:58:52.638804  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.7:161
07/23-15:58:52.739821  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.7:161
07/23-15:58:53.118258  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.5:161
07/23-15:58:53.218715  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.5:161
07/23-15:58:53.310816  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.1:161
07/23-15:58:53.410911  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.1:161
07/23-15:59:08.735537  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.9:56663 -> 239.255.255.250:1900
07/23-15:59:26.278201  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.3:705
07/23-15:59:27.403906  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.16:705
07/23-15:59:27.849101  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.18:705
07/23-15:59:27.949114  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.18:705
07/23-15:59:28.137158  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.16:705
07/23-15:59:30.274151  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.20:705
07/23-15:59:33.165428  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.2:705
07/23-15:59:33.790601  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.7:705
07/23-15:59:33.891033  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.7:705
07/23-15:59:36.258532  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.5:705
07/23-15:59:36.361446  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.5:705
07/23-15:59:40.289391  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34715 -> 192.168.1.1:705
07/23-15:59:40.389807  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34716 -> 192.168.1.1:705
07/23-15:59:50.847634  [**] [1:1421:11] SNMP AgentX/tcp request [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34717 -> 192.168.1.16:705
07/23-15:59:58.423435  [**] [1:1418:11] SNMP request tcp [**] [Classification: Attempted Information Leak] [Priority: 2] {TCP} 192.168.1.4:34717 -> 192.168.1.16:161
07/23-16:00:35.785049  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.7:55878 -> 239.255.255.250:1900
07/23-16:00:36.706831  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.7:55878 -> 239.255.255.250:1900
07/23-16:00:37.730579  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.7:55878 -> 239.255.255.250:1900
07/23-16:00:38.752957  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.7:55878 -> 239.255.255.250:1900
07/23-16:01:08.655162  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.9:56663 -> 239.255.255.250:1900
```

### Log Entry Format
Each log entry follows a specific format:
```
07/23-15:58:35.761583  [**] [1:1917:6] SCAN UPnP service discover attempt [**] [Classification: Detection of a Network Scan] [Priority: 3] {UDP} 192.168.1.7:51226 -> 239.255.255.250:1900
```
- **07/23-15:58:35.761583**: Timestamp indicating when the event occurred (MM/DD-HH:MM
.microseconds).
- [**]: Delimiters for the alert message.
- **[1:1917:6]**: Snort rule ID (`1:1917:6`), where 1 is the generator ID, `1917` is the Snort rule ID, and `6` is the revision number.
- **SCAN UPnP service discover attempt**: Description of the detected activity.
- **[Classification: Detection of a Network Scan]**: Classification of the alert.
- **[Priority: 3]**: Priority level of the alert, with lower numbers indicating higher severity.
- **{UDP}**: Protocol used (UDP in this case).
- **192.168.1.7:51226 -> 239.255.255.250:1900**: Source IP and port, and destination IP and port.

### Detailed Analysis of Snort Alerts
#### SCAN UPnP Service Discover Attempt
- **Description**: These alerts indicate attempts to discover UPnP (Universal Plug and Play) services on the network. UPnP is a protocol that allows devices to discover each other on a network and establish functional network services for data sharing, communications, and entertainment.
- **Classification**: Detection of a Network Scan
- **Priority**: 3 (Medium)
- **Protocol**: UDP
- **Source IP**: 192.168.1.7 and 192.168.1.9
- **Behavior**: These IPs are scanning for UPnP services, indicating potential reconnaissance activity.
- **Destination IP**: 239.255.255.250 (Multicast address)

#### SNMP Request TCP
- **Description**: These alerts indicate SNMP (Simple Network Management Protocol) requests over TCP, which may be an attempt to gather information from network devices. SNMP is - commonly used for network management, but it can be exploited for information gathering if not properly secured.
- **Classification**: Attempted Information Leak
- **Priority**: 2 (High)
- **Protocol**: TCP
- **Source IP**: 192.168.1.4
- **Behavior**: This IP is making numerous SNMP requests to multiple destination IPs. These requests could be an attempt to gather information from devices on the network.
- **Destination IPs**:
  - 192.168.1.3
  - 192.168.1.2
  - 192.168.1.20
  - 192.168.1.18
  - 192.168.1.16
  - 192.168.1.7
  - 192.168.1.5
  - 192.168.1.1

#### SNMP AgentX/TCP Request
- **Description**: These alerts indicate SNMP AgentX requests over TCP. SNMP AgentX allows for the extension of SNMP agents with additional sub-agents, which might be used to extend functionality or potentially exploit vulnerabilities.
- **Classification**: Attempted Information Leak
- **Priority**: 2 (High)
- **Protocol**: TCP
- **Source IP**: 192.168.1.4
- **Behavior**: This IP is making numerous SNMP AgentX requests to multiple destination IPs. Similar to the SNMP requests, these could be attempts to exploit vulnerabilities or gather information.
- **Destination IPs**:
  - 192.168.1.3
  - 192.168.1.16
  - 192.168.1.18
  - 192.168.1.20
  - 192.168.1.2
  - 192.168.1.7
  - 192.168.1.5
  - 192.168.1.1

#### Isolation Recommendation
- `192.168.1.4` is the primary IP exhibiting malicious behavior through multiple attempted information leaks via SNMP and SNMP AgentX requests.
- `192.168.1.7` and `192.168.1.9` are involved in network scans via UPnP discovery, which could be a prelude to more malicious activities, and should be monitored closely.
- Therefore, `192.168.1.4` should be isolated immediately due to its high volume of suspicious activity and potential threat to the network.
- `192.168.1.7` and `192.168.1.9` should also be considered for isolation or at least close monitoring to prevent any further reconnaissance or potential exploitation activities.
