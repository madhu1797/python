##Two strings,  and , are called anagrams if they contain all the same characters in the same frequencies. For example, the anagrams of CAT are CAT, ACT, TAC, TCA, ATC, and CTA.

##anagram
##margana
##Sample Output 0

##Anagrams
##Explanation 0

##Character	Frequency: anagram	Frequency: margana
## A or a		3						3
## G or g		1						1
## N or n		1						1
## M or m		1						1
## R or r		1						1
##===========================================================================================================================================

a=input(str("Get first string="))
b=input("get 2nd string=")
##count = 0
def collect_count(var):
	count = 0
	d= dict()
	for i in var:
		for j in var:
			if i == i:
				count += 1
		d=d.update(i=count)		
	return d
d=collect_count(a)
d1=collect_count(b)
print(d)
print(d1)

