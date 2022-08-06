from netaddr import *
starting_address=input("Enter the DNS ip address=")
dns_name=IPAddress(starting_address).reverse_dns
print("DNS_RESOLVED FOR", starting_address, dns_name)

