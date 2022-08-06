from generate_mac import *

def generate_random_mac():
	return generate_mac.total_random()


def check_mac_address(mac):
	status=generate_mac.is_mac_address(mac)
##	print(status)
	if status:
		print("Given input is valid mac address")
	else:
		print("Invalid mac address")

def decimal(n):
	if n.upper() == "A":
		return 10
	elif n.upper() == "B":
		return 11
	elif n.upper() == "C":
		return 12
	elif n.upper() == "D":
		return 13
	elif n.upper() == "E":
		return 14
	else:
		return "Invalid"

	

def multicast_mac(n):
##	print(n)
	if int(n)<=9:
		n=n
	else:
		n=decimal(n)
##	b=2
	c=''
	if n != 'Invalid':
		n=int(n)
		while (n>1):
			a=n%2
			n=n//2
			c=c+str(a)
	return c	
	
	

def check_mac_type(mac):
	a=generate_mac.is_mac_address(mac)
	print(a)
	if a:
		print("***")
		msb=mac[1]
		print(msb)
		if mac == "ff:ff:ff:ff:ff:ff":
			return "Broadcast"
		else:
			stat = multicast_mac(msb)
			print(stat)
			print(stat[0])	
			if stat[0] == 1:
				return "Multicast Mac address"
			else:
				return "Unicast Mac Address"
	else:
		print("$$$")
		return "Invalid mac"


	
##mac=generate_random_mac()
##print(mac)
##check_mac_address("d8:9c:67:a6:71:a7")

status=check_mac_type("d8:9c:67:a6:71:a7")
print(status)

status=check_mac_type("01:00:CC:CC:DD:DD")
print(status)

status=check_mac_type("ff:ff:ff:ff:ff:ff")
print(status)

status=check_mac_type("asdfghjk")
print(status)
