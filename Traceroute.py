import subprocess


def traceroute():
    host = input("Enter the host for traceroute (e.g., google.com): ")
    try:
        subprocess.run(["traceroute", host])
    except Exception as e:
        print(f"Traceroute failed: {e}")
