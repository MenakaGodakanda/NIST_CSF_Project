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
![Screenshot 2024-07-23 153059](https://github.com/user-attachments/assets/4d10cc29-f664-454c-a413-bef543b208f4)

- This script will create an `assets.json` file with the identified hosts.<br>
![Screenshot 2024-07-24 040649](https://github.com/user-attachments/assets/8fccb66f-5f41-4643-ab9c-a1d39dd6f3eb)

## Protect

### Access Control

- Script: `protect/access_control.py`
- This script manages user permissions and access to directories. Run the script:
```
python3 protect/access_control.py
```
![Screenshot 2024-07-23 153307](https://github.com/user-attachments/assets/86774ba2-0351-4aa6-81bf-34df8ab590e6)

### Data Protection

#### 1. Create a Sensitive File
  - Create the `sensitive_data.txt` file:
  ```
  echo "This is some sensitive data that needs to be encrypted." > sensitive_data.txt
  ```
  - Verify the file exists:
  ```
  ls -l sensitive_data.txt
  ```
  ![Screenshot 2024-07-24 152724](https://github.com/user-attachments/assets/6ecef176-7e37-49fb-b62b-3e712d117952)

#### 2. GPG Key Creation
  - Generate a GPG Key:
  ```
  gpg --full-generate-key
  ```
  ![Screenshot 2024-07-24 153040](https://github.com/user-attachments/assets/0c8315d3-5185-4a02-915b-6b8ac2dcbed3)

  - Follow the prompts to generate your key. Use the same email address you will use in the script as the recipient.
  - Export the GPG Key:
  ```
  gpg --export -a "your_email@example.com" > public.key
  ```
  - Replace "your_email@example.com" with your actual email address.

  - Use the Correct Recipient:
  - Ensure the recipient in your `data_encryption.py` script matches the email or key ID of the generated GPG key:
  ```
  recipient = 'your_email@example.com'
  ```
  - Check GnuPG Configuration:
  ```
  gpg --list-keys
  ```

#### 3. Running Data Protection Script
  - Script: `protect/data_encryption.py`
  - This script encrypts sensitive data using `gnupg`.
  - Run the script:
  ```
  python3 protect/data_encryption.py
  ```
![Screenshot 2024-07-23 154259 - Copy](https://github.com/user-attachments/assets/a84135b7-e9cd-44e3-bef4-00f67699d447)

## Detect

### Intrusion Detection

#### 1. Verify Snort Installation:
- Ensure Snort is installed and running correctly. If not installed, use the following command:
```
sudo apt update
sudo apt install snort
```

#### 2. Configure Snort Logging:
- Ensure Snort is configured to log alerts to /var/log/snort/alert. Edit the Snort configuration file (usually located at /etc/snort/snort.conf):
```
sudo nano /etc/snort/snort.conf
```
- Ensure the following line is uncommented or added to log alerts to the specified file:
```
output alert_fast: /var/log/snort/alert
```
![Screenshot 2024-07-24 155237](https://github.com/user-attachments/assets/2dae2862-8a99-4e7e-bc66-73b9523a20e9)

#### 3. Create and Set Permissions for Log Directory:
- Ensure the directory /var/log/snort exists and has the correct permissions:
```
sudo mkdir -p /var/log/snort
sudo chown snort:snort /var/log/snort
```
- Change permissions of the log directory and files so that the user can read the log file.:
```
sudo chmod -R 755 /var/log/snort
sudo chown -R $USER:$USER /var/log/snort
```
- Verify the permissions of the alert file to ensure they are correctly set:
```
ls -l /var/log/snort/alert
```
![Screenshot 2024-07-24 155505](https://github.com/user-attachments/assets/1b22aaf4-05d3-4cb0-9361-60281ec0e801)

#### 4. Start Snort:
- Start Snort with the appropriate configuration. Make sure it uses the configuration file you modified:
```
sudo snort -A fast -c /etc/snort/snort.conf -i enp0s3
```
![Screenshot 2024-07-24 153432](https://github.com/user-attachments/assets/274d9fca-83d2-4713-bef8-83407e6a02c4)

- Replace `enp0s3` with the appropriate network interface on your system.

#### 5. Generate Test Alerts:
- Generate some test traffic to ensure Snort logs alerts. Use tools like `Nmap` to scan your network, which should trigger Snort alerts:
```
sudo apt install nmap
sudo nmap -v -sS 192.168.1.0/24  # Replace with your network range
```
![Screenshot 2024-07-24 153602](https://github.com/user-attachments/assets/f086c558-ef67-49cf-bb49-d1e9d34d3720)

#### 6. Verify Snort Logs:
- Check if the alert file is created and populated with data:
```
ls -l /var/log/snort/alert
cat /var/log/snort/alert
```
![Screenshot 2024-07-24 153835](https://github.com/user-attachments/assets/a3bffa68-03d2-43c0-be54-8a067cced088)

- If the file exists and contains data, your Snort configuration is working correctly.

#### 7. Running Data Protection Script
- Script: `detect/monitor_logs.py`
- This script monitors Snort logs for intrusion detection alerts. Run the script:
```
python3 detect/monitor_logs.py
```
![Screenshot 2024-07-23 160445 - Copy](https://github.com/user-attachments/assets/826d5e1b-ccb6-4ef2-816d-55d361a86153)

- This script will keep checking for the log file until it exists and then proceed to monitor it. If Snort is correctly configured and running, the script will eventually detect the log file and start printing new alerts.

## Respond

### Incident Response

- Script: `respond/incident_response.py`
- This script isolates affected machines by modifying `iptables` rules.
- Identify the IP address of affected machines and insert the below lines in the `incident_response.py` script.
```
ip_address = '192.168.1.7'    # IP address of affected machine
isolate_machine(ip_address)
print(f'Machine {ip_address} isolated')
```
- Run the script:
```
python3 respond/incident_response.py
```
![Screenshot 2024-07-24 032656](https://github.com/user-attachments/assets/7210cfa2-dc0c-46c1-ba10-140c23c556a2)

## Recover

### Backup and Restore

#### 1. Create the Directory:
- Create the directory `/home/data` if it doesn't exist with proper permissions:
```
mkdir -p /home/data
sudo chown $USER:$USER /home/data
sudo chmod 755 /home/data
```
- You can also add some test files to this directory to simulate data:
```
echo "This is a test file" > /home/data/testfile1.txt
echo "This is another test file" > /home/data/testfile2.txt
```
- Verify Directory and Files:
```
ls -ld /home/data
ls -l /home/data
```
![Screenshot 2024-07-24 154152](https://github.com/user-attachments/assets/2241d664-7509-46f0-815b-e6dd9581c25f)

#### 2. Running the Backup and Restore Script:
- Script: `recover/backup_restore.py`
- This script backs up and restores data using `shutil`. Run the script:
```
python3 recover/backup_restore.py
```
![Screenshot 2024-07-23 160942](https://github.com/user-attachments/assets/f529f1c5-44b4-4565-aab4-4c179d610ab2)

#### 3. Verifying the Backup and Restore
1. Check the Backup Directory:
- Verify that the backup was created correctly:
```
ls -l /home/backup
```
![Screenshot 2024-07-24 154333](https://github.com/user-attachments/assets/2bb99e63-d2ab-45d5-a129-db6dbec80409)

2. Check the Restore Directory:
- Verify that the restoration was completed successfully:
```
ls -l /home/restore
```
![Screenshot 2024-07-24 154338](https://github.com/user-attachments/assets/a455253b-b5eb-4342-935c-70b495b7849e)

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
