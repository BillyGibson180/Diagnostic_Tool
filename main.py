from DNSLookup import dns_lookup
from NetworkInfo import network_info
from PingTest import ping_test
from PortScanner import port_scanner
from SpeedTest import speed_test
from Traceroute import traceroute

def main_menu():
    print("\nNetwork Diagnostic Tool")
    print("1. Ping Test")
    print("2. Port Scanner")
    print("3. DNS Lookup")
    print("4. Speed Test")
    print("5. Traceroute")
    print("6. Network Info")
    print("7. Exit")
    choice = input("Select an option: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            ping_test()
        elif choice == "2":
            port_scanner()
        elif choice == "3":
            dns_lookup()
        elif choice == "4":
            speed_test()
        elif choice == "5":
            traceroute()
        elif choice == "6":
            network_info()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")