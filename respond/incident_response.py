import subprocess

def isolate_machine(ip_address):
    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'])
    subprocess.run(['sudo', 'iptables', '-A', 'OUTPUT', '-d', ip_address, '-j', 'DROP'])

if __name__ == "__main__":
    ip_address = '192.168.1.100'
    isolate_machine(ip_address)
    print(f'Machine {ip_address} isolated')
