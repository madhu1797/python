import time
import sys
import paramiko

def open_ssh_tunnel(credentials=None):
    '''
	Function name: open_ssh_tunnel
	Purpose: Establishes SSH Connection with the given Credentials
	Arguments:
		@dut: AP details dictionary present in configuration.yaml. Mandatory Argument
			 Type: Dict
		@credentials: Dictionary containing the SSH credentials of Device other than Execution DUT. Optional Argument
		     Type: Dict
		     Eg: {'username': 'user', password: 'test@123', 'host': '192.168.102.10'}
    '''
    global ssh
    ssh_status=list()
    if credentials != None:
        username = credentials["username"]
        password = credentials["password"]
        host = credentials["client_ip"]
        try:
            #ssh_status=list()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password, timeout=30, allow_agent=False,look_for_keys=False)
            ssh_status.append("true")
            ssh_status.append(ssh)
            return ssh_status
        except Exception as e:
            print("Unable to take SSH connection.Reason: {}".format(e))
            return ssh_status.append("false")
       
    else:
        print("!!!!!!!!!!!")
        print("Empty user credentials")
        return ssh_status.append("false")

def Execute_command_in_SSH_Client(ssh, command, timeout=60):

    '''
	Function Name: Execute_command_in_SSH_Client
	Purpose: Executes the given command by taking SSH to execution on Client and returns the output of the command
	Arguments:
	    @ssh: ssh tunnel object which is return from open_ssh_tunnel function
	    	 Type: object
		@command: Command that has to be executed. Mandatory Argument
			Type: String
		@timeout: Timeout(seconds) for command execution and output reading. Optional Argument. Default value is 60
			 Type: Int
			 Eg: 60
    '''
    stdin, stdout, stderr = ssh.exec_command(command, timeout=timeout, get_pty=True)
    out = stdout.read().decode().strip()
    #std_in = stdin.read().decode().strip()
    std_err = stderr.read().decode().strip()
    print("*************")
    print(std_err)
    return str(out)

def close_ssh_tunnel(ssh):
	'''
	Function Name: close_ssh_tunnel
	Purpose: To close the existing ssh tunnel.
	Arguments:
	    @ssh: ssh tunnel object which is return from open_ssh_tunnel function
	    	 Type: object
	'''
	ssh.close()


credentials = {"client_ip" : "192.168.1.193", "username" : "vvdn", "password" : "test@123"}
result = open_ssh_tunnel(credentials)
if result[0]:
    output = Execute_command_in_SSH_Client(result[1], "ifconfig")
    print(output)
close_ssh_tunnel(result[1])

