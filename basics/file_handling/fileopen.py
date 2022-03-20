"""name     = filemanupulation.py
Description = This is a program to get number of lines and
number of charcters in the file
"""
FILE1 = input("Enter the filename:")
try:
    f1 = open(FILE1, "r")
    print("Enter as lines or words")
    VAR = input(" You want number of lines or number of words from the file")
    def fileline(F):
        COUNT = 0
        FF = F.readlines()
        for i in FF:
            COUNT += 1
            print(COUNT)
    def fileword(f):
        COUNT = f.readlines()
        Len = 0
        for i in count:
            word = i.split()
            Len += len(word)
        print(Len)    
    def filechar(f):
        count = f.readlines()
        char = 0
        for i in count:
            char += len(i)
        print(char)
    if VAR == "line":
        fileline(f1)
    elif VAR == "words":
        fileword(f1)   
    elif VAR == "char":
        filechar(f1)
    else:
        print("Enter valid operation as lines or words or char")
except FileNotFoundError:
        print("Enter the valid filename")


