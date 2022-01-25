from scapy.all import *

def read_capture(filename):
    packet = rdpcap(filename)
    print(packet)
    """
    for i in packet:
        print("==============================================================================================================")
        print(i.show())
        print("==============================================================================================================")
    """


def sniff_with_count(count1):
   capture = sniff(count = count1)
   print(capture.summary())
   
def sniff_and_save_Capture(interface, count1, filename):
    packet = sniff(iface=interface, count=count1)
    wrpcap(filename, packet)

   
#read_capture("packet_09:24:41.pcapng")
#sniff_with_count(5)

sniff_and_save_Capture("wlp2s0", 10, "scapy_sniff.pcap")
