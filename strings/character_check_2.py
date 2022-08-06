import string
if __name__ == '__main__':
    a = input()
    count_1=count_2=count_3=count_4=count_5=0
    for s in a:
        if s.isalnum():
            print("True")
            count_1 += 1
            break
#    print(count_1) 
    if count_1 == 0:
         print("False")
    for s in a:
        if s.isalpha():
            print("True")
            count_2 += 1	
            break
#        print(count_2)
    if count_2 == 0:
        print("False")
    for s in a:
        if s.isdigit():
            print("True")
            count_3 += 1
            break
#        print(count_3)      
    if count_3 == 0:
        print("False") 
    for s in a:
        if s.islower():
            print("True")
            count_4 += 1 
            break
#        print(count_4) 
    if count_4 == 0:
        print("False")
    for s in a:
        if s.islower():
             print("True")
             count_5 += 1 
             break
#        print(count_5)
    if count_5 == 0:
        print("5.False")
      
