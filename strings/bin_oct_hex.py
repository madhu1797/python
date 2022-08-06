def print_formatted(number):
    # your code goes here
    list_1=[]
    for n in range (1,number+1):
        print(n,"     ",

)
        o=oct(n)
        print(o[2:],"     ")
#        a= a+"o[2:]"+"     "
        h= hex(n)
#        a=a+"h[2:]"+"     "
        print(h[2:],"     ")
        b=bin(n)
#        a=a+"b[a:]"+"     "
        print(b[2:],"     ")
#        list_1.append(a)
#        return list_1
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
