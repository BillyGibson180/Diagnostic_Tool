import socket
import subprocess

def network_info():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"Local IP Address: {local_ip}")
    public_ip = subprocess.getoutput("curl ifconfig.me")
    print(f"Public IP Address: {public_ip}")
