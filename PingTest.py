import subprocess


def ping_test():
    host = input("Enter the host to ping (e.g., google.com): ")
    try:
        subprocess.run(["ping", "-c", "4", host], check=True)
    except subprocess.CalledProcessError:
        print(f"Ping to {host} failed.")
