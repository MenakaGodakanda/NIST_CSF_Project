import subprocess

def isolate_machine(ip_address):
    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'])
    subprocess.run(['sudo', 'iptables', '-A', 'OUTPUT', '-d', ip_address, '-j', 'DROP'])

if __name__ == "__main__":
    ip_address = '192.168.1.4'    # IP address of affected machine
    isolate_machine(ip_address)
    print(f'Machine {ip_address} isolated')

    ip_address = '192.168.1.7'    # IP address of affected machine
    isolate_machine(ip_address)
    print(f'Machine {ip_address} isolated')
    
    ip_address = '192.168.1.9'    # IP address of affected machine
    isolate_machine(ip_address)
    print(f'Machine {ip_address} isolated')
