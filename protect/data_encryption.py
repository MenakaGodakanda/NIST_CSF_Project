import gnupg

def encrypt_file(file_path, recipient):
    gpg = gnupg.GPG()
    with open(file_path, 'rb') as f:
        status = gpg.encrypt_file(f, recipients=[recipient], output=f'{file_path}.gpg')
    return status.ok

if __name__ == "__main__":
    file_path = 'sensitive_data.txt'
    recipient = 'recipient@example.com'  # Replace with your recipient's email or key ID
    if encrypt_file(file_path, recipient):
        print('File encrypted successfully')
    else:
        print('File encryption failed')
