import os
#ip='8.8.8.8'

def ping_test(ip='8.8.8.8', c=9999, i=1, interface='wlp2s0'):
	cmd='ping {0} -c {1} -i {2} -I {3}'.format(ip,c,i,interface)
#	res=os.system('ping {0} -c {1} -i {1} -I {2}'.format(ip,c,i,interface))
	print(cmd)
	res=os.system(cmd)
	print(res)
ping_test()
ping_test('192.168.106.1', 2, 2, 'wlp2s0')
dict1={}
dict1['ip']='192.168.106.1'
dict1['c']=3
ping_test(**dict1)

 
