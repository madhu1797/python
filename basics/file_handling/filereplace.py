"""name     = filemanupulation.py
Description = This is a program to get number of lines and
number of charcters in the file
"""
import fileinput
FLAG = 0
FILE1 = input("Enter the filename:")
search = input("Enter the search word")
replace = input ("Enter replacing word")
F = open(FILE1, "r")
F1 = F.readlines()
for line in F1:
    print(line)
#    list1 = line.split(" ")
#    l1 = len(list1)
#    for i in range (0,l1):
    if search in line:
        print("Matched")
        FLAG = 1
        break
    else:
        print("Not matched")
if FLAG == 1:
    F = open(FILE1, "r+")
    F.write( line.replace(search,replace) )
    
F.close()
