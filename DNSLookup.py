import dns.resolver

def dns_lookup():
    domain = input("Enter the domain (e.g., google.com): ")
    try:
        result = dns.resolver.resolve(domain, 'A')
        for ipval in result:
            print(f"IP Address: {ipval}")
    except Exception as e:
        print(f"DNS lookup failed: {e}")
