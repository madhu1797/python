import pyshark

## sniff packet over the air
def packet_capture(interface_name, time):
    capture = pyshark.LiveCapture(interface=interface_name)
    capture.sniff(timeout=time)
    print(capture)
    #for i in range (0, 10):
    #    print(capture[i])

## sniff and save the packet capture

def capture_save_packets(interface_name, time, file_name):
    capture = pyshark.LiveCapture(interface=interface_name, output_file=file_name)
    capture.sniff(timeout=time)
    print(capture)


## Apply filter over the captured pcap file
def get_packet_cout(object):
    result = (object[0].__dict__)
    print(result)
    return result["captured_length"]

def read_pcap_files(File_name):
    cap1 = pyshark.FileCapture('sniff_save.pcap')
    print(cap1)
    packet = get_packet_cout(cap1)
    print(packet)
    

def read_pcap_files_with_filter(File_name, filters):
    cap1 = pyshark.FileCapture(File_name, display_filter=filters)
    print(cap1)
    
    packet = get_packet_cout(cap1)
    print(packet)
    
    print(cap1[0])
    
    """
    records = []
    for i in cap1:
        print(i)
    
    #print(records)
     """  
def read_pcap_files_with_multiple_filter(File_name):
    cap1 = pyshark.FileCapture(File_name)
    print(cap1)
    
    try:
        for i in cap1:
    	    if "arp" in i or "dns" in i:
                print(i)
    except Exception as e:        
        pass


#packet_capture("wlp2s0", 10)
#capture_save_packets("wlp2s0", 10, 'sniff_save.pcap')
#read_pcap_files("/home/vvdn/AP305c_client_roaming_issue.pcapng")
read_pcap_files_with_filter("/home/vvdn/AP305c_client_roaming_issue.pcapng", "wlan.fc.type_subtype == 8")
#read_pcap_files_with_multiple_filter('sniff_save.pcap')
