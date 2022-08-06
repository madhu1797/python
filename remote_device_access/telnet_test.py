import telnetlib
import time

def open_telnet_Connection(telnet_ip, port, username, password):
     try:
          username = username.encode('utf-8')
          password = password.encode('utf-8')
          tn = telnetlib.Telnet(telnet_ip, port)
          tn.write(b"\n")
          status = tn.read_until(b"login:", timeout=10).decode('ascii')
          print(status)
          if "login" in status:
              tn.write(username + b"\n")
              tn.read_until(b"Password: ")
              tn.write(password, + b"\n")
              tn.read_until(b"#", timeout=10)
              tn.write("enable", + b"\n")
              tn.read_until(b"#", timeout=10)
          time.sleep(5)
          cmd = 'show version'.encode('utf-8')
          print(cmd)
          result = tn.write(cmd +  b"\n")
          result = tn.read_until(b"#", timeout=10).decode('ascii')
          print(result)
          #decode('ascii')
          #print(result)
          tn.close()
          return result
     except Exception as error:
        tn.close()
        print(error)
        return 1


result= open_telnet_Connection("49.207.180.204", 7011, "admin", "admin")
print(result)
