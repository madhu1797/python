import ipaddress
from netaddr import *
starting_address=input("Enter the starting ip address=")
subnet_mask=input("Enter the subnet mask as number (e.g) 24=")
ip=starting_address+"/"+str(subnet_mask)
#net4 = ipaddress.ip_network(ip)
#for x in net4.hosts():
#	print(x) 
net4 = IPNetwork(ip)
print("NETWORK_ADDRESS:",net4.network,"BORADCAST_ADDRESS:",net4.broadcast)
for ip in net4:
	print(ip)

