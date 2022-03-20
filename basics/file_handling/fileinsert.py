"""name     = filemanupulation.py
Description = This is a program to insert or delete,
the line from the file
"""
file1 = input("Enter the filename:")
choice = input(" Do you want insert or delete line from file")
"""
def fileline(F):
        f = open(file1,"r+")
        COUNT = 0
        FF = f.readlines()
        for i in FF:
            COUNT += 1
            return COUNT
"""
N1 = 0

if choice == "insert":
    line = int(input("Enter the line do you want to insert"))
    str1 = str(input("Enter the content are you want to insert"))
    f = open(file1,"r+")
   # N = fileline(file1)
    #ff = f.readlines()
    for line1 in f:
        N1 += 1
        if N1 != line:
            f.write(line1)                     
        else:
            f.write(str1)
            f.write("\n")
            f.write(line1)

""" 
    string1 = ff[line]
    string1 = str(string1)
    print(string1)
    print(str1)
    f = open(file1, "r+")
    ff = str(ff)
    f.write(ff.replace(string1, str1) )      
"""  
    
if choice == "delete":
    f = open(file1,"r+")
    list1 = []
    list1 = f.readlines()
    print(list1)
    line = int(input("Enter the are you want to delete"))
    del list1[line]
    list1 = str(list1)
    f.write(list1)
   
f.close()
