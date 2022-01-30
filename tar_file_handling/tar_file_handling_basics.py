from tarfile import *
import os

##To check file is tar archieve or not

file_obj= "test_file.txt"

Status = is_tarfile(file_obj)         
if Status:
    print(file_obj,"is tar file")
else:
    print(file_obj,"it is not a tar file")

##To create tar file 
file_obj_1= "test_file.txt"
file_obj_2= "test_file_2.txt"
file_1 = open('test_file_tar.tar.gz', mode='w')
file_2 = file_1.add(file_obj_1)
file_1.close()

## To get the member files inside the tar file - METHOD:: 1
file_1 = open('test_file_tar.tar.gz', mode='r')
print("member files list Before append the new file")
for files in file_1.getmembers():
    print(files.name)

## to append new file to existing tar file

file_1 = open('test_file_tar.tar.gz', mode='a')
file_2 = file_1.add(file_obj_2)
file_1.close()

## To get the member files inside the tar file - METHOD::2
print("member files list after append the new file")
file_1 = open('test_file_tar.tar.gz', mode='r')
for files in file_1.getnames():
    print(files)
file_1.close()

## To extract files from archieve
cr_dir = os.system("mkdir test")
mv_file = os.system('mv test_file_tar.tar.gz test/.')
ch_dir = os.chdir("test")
print(os. getcwd())
file_1 = open('test_file_tar.tar.gz')

##To extract all files in tar
f_obj = file_1.extractall()
print(f_obj)

##To extract particular file in tar - method_1
#f_obj = file_1.extract(file_obj_1)
#print(f_obj)

"""
##To extract particular file in tar - method_2 --->Not working
file_1 = open('test_file_tar.tar.gz', mode='r')
for files in file_1.getmembers():
    print(files)
    f_obj = file_1.extractfile(files)
"""
file_1.close()

