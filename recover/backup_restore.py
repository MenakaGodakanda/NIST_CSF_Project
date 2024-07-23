import shutil
import os

def backup_data(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)  # Remove destination directory if it exists
    shutil.copytree(source, destination)  # Copy source directory to destination

def restore_data(backup, target):
    if os.path.exists(target):
        shutil.rmtree(target)  # Remove target directory if it exists
    shutil.copytree(backup, target)  # Copy backup directory to target

if __name__ == "__main__":
    source = '/home/data'  # Source directory to backup
    backup = '/home/backup'  # Backup directory
    target = '/home/restore'  # Target directory for restoration

    # Perform backup
    print("Starting backup...")
    backup_data(source, backup)
    print("Backup completed.")

    # Perform restore
    print("Starting restoration...")
    restore_data(backup, target)
    print("Restoration completed.")
