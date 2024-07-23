import subprocess

def add_user(user):
    subprocess.run(['sudo', 'adduser', user])

def set_permissions(user, directory):
    subprocess.run(['sudo', 'chown', '-R', f'{user}:{user}', directory])

if __name__ == "__main__":
    user = 'testuser'
    directory = '/home/testuser'
    add_user(user)
    set_permissions(user, directory)
