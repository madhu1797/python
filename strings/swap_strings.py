import string

def swap_by_function(a):
	final = ''
	for i in a:
		if i.islower():
			string= i.upper()
		else:
			string= i.lower()
		final = final + string
	return final

def swap_by_buildin(a):
	string= a.swapcase()
	return string

print 'ASDFtyuiPOI'
#a= swap_by_function('ASDFtyuiPOI')
a= swap_by_buildin('ASDFtyuiPOI')
print a
 
