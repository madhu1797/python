from netaddr import *
starting_address=input("Enter the starting ip address=")

## To check IP ADDRESS IS UNICAST OR NOT
if IPAddress(starting_address).is_unicast():
	print(starting_address,"is unicast address")
elif IPAddress(starting_address).is_multicast():
	print(starting_address,"is multicastaddress")
elif IPAddress(starting_address).is_broadcast():
	print(starting_address,"is broadcast address") 
else:
	print("INVALID IP")

## To check private or public ip

if IPAddress(starting_address).is_private():
	print(starting_address,"is private address")
elif IPAddress(starting_address).is_reserved():
	print(starting_address,"is reserved address")
else:
	print(starting_address,"is public address")

## To check the mask type

if IPAddress(starting_address).is_netmask():
	print(starting_address,"is netmask address")
elif IPAddress(starting_address).is_hostmask():
	print(starting_address,"is hostmask address")
elif IPAddress(starting_address).is_loopback():
	print(starting_address,"is loopback address")
else:
	print("Not a mask address")






