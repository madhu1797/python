import string
def solve(s):
    words=s.split(" ")
    print(words)
    string=''
    list_1=[]
    for s in words:
         if len(s) > 0:
             print(s)
             a=s[0].upper()  
             string= string+a
             string=string+s[1:]+" "
         else:
             string=string+" "
    return string 

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

