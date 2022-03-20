"""name     = fileorting.py
Description = This is a program used sort filecontent based on
alphabhetical order

"""
from os import listdir 
file1 = input("Enter the file name:")
f = open(file1, "r+")
d = []
for line in sorted(f):
    print(line)
    d.append(line)
f = open(file1,"w")
for line in d:
    f.write(line) 
