import sys

def ex_sys_argv():
	print("Hello {0}, How is your {1}".format(sys.argv[1],sys.argv[2]))

'''
Execution:  python sys_library_basics.py madhu journey
output:     Hello madhu, How is your journey

'''

ex_sys_argv()

## Redirect terminal logs to specific file

def redirect_logs():
	temp = sys.stdout                 # store original stdout object for later
	sys.stdout = open('log.txt', 'w') # redirect all prints to this log file
	print("testing123")               # nothing appears at interactive prompt
	print("another line")             # again nothing appears. it's written to log file instead
	sys.stdout.close()                # ordinary file object
	sys.stdout = temp                 # restore print commands to interactive prompt
	print("back to normal")           # this shows up in the interactive prompt

'''
Execution:  python3 sys_library_basics.py 
output:     back to normal
			vvdn@VVDN:~/Documents/PYTHON/sys$ cat log.txt 
			testing123
			another line


'''


redirect_logs()
