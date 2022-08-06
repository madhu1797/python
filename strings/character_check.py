import string
if __name__ == '__main__':
    s = input()
    count_1=count_2=count_3=count_4=count_5=0
    list_1= []
    for a in s:
        if a.isalnum() and count_1 != 1: 
            print("True")
            count_1 += 1
        else:
            print("False")
    for a in s:
        if a.isalpha() and count_2 != 1:
            print("True")
            count_2 += 1
        :
            print("False")
    for a in s:     
         if a.isdigit() and count_3 != 1:
            print("True")
            count_3 += 1
         else:
            print("False")  
#           count_3 += 1
    for a in s:
         if a.islower() and count_4 != 1:
            print("True")
            count_4 += 1  
         else:
            print("False") 
#            count_4 += 1
    for a in s:  
         if a.isupper() and count_5 != 1:
            print("True")
            count_5 += 1
         else:
            print("False") 

