from scapy.all import *


def capture_Beacon_frames(packet):
	a=[]
	if packet.haslayer(Dot11):
		if packet.type == 0 and packet.subtype == 8:
			b=(packet.show())
			a.append(b)

def capture_probe_request_packets(packet):
	if packet.haslayer(Dot11):
		if packet.type == 0 and packet.subtype == 4:
			b=packet.show()
			print(type(b))

def capture_control_frames(packet):
	if packet.haslayer(Dot11):
		if packet.type == 1 and packet.subtype == 13: 
			packet.show()

def capture_data_frames(packet):
	if packet.haslayer(Dot11):

	
#sniff(iface="mon0", prn = capture_Beacon_frames, count=20)

#sniff(iface="mon0", prn=capture_probe_request_packets, count=100)

sniff(iface="mon0", prn=capture_control_frames, count=1000)




			
	
