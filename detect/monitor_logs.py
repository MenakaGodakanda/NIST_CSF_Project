import time
import os

def monitor_logs(log_file='/var/log/snort/alert'):
    while not os.path.isfile(log_file):
        print(f"Log file {log_file} does not exist. Waiting for Snort to create it...")
        time.sleep(5)  # Wait before checking again

    with open(log_file, 'r') as file:
        # Move the cursor to the end of the file
        file.seek(0, 2)

        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Sleep briefly
                continue
            print(line.strip())

if __name__ == "__main__":
    log_file = '/var/log/snort/alert'  # Default Snort alert log file path
    monitor_logs(log_file)
