import nmap
import json

def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')
    return nm.all_hosts()

def document_assets(hosts, filename='assets.json'):
    with open(filename, 'w') as f:
        json.dump(hosts, f, indent=4)

if __name__ == "__main__":
    network = '192.168.1.0/24'
    hosts = scan_network(network)
    document_assets(hosts)
    for host in hosts:
        print(f'Host found: {host}')
