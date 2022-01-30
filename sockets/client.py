import socket

"""
socket.socket-------> To create object for socket
AF_INET ------------> responsible for IPV4 Address 
SOCK.STREAM---------> responsible for To estbalish TCP connection between to nod
es
"""



"""
general format for socket connection estbalishment --------> Object.connect(IP_address, Port_Name)    <--------->  client side

"""
def send_request_to_server(command):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    test_connection=client.connect((socket.gethostname(), 9998))
    msg = client.recv(1024)
    print(msg.decode("utf-8"))
    #send_data= client.send(bytes(" echo I got ur response","utf-8"))
    send_data= client.send(bytes(command,"utf-8"))
    msg = client.recv(1024)
    print(msg.decode("utf-8"))
    
    
send_request_to_server("ping google.com -c 4")
send_request_to_server("traceroute google.com")


