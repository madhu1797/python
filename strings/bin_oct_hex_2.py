def print_formatted(number):
    for n in range (1,number+1):
        o=oct(n)
        h= hex(n)
        b=bin(n)
        print(n,"     ",o[2:],"     ",h[2:],"     ",b[2:],"     ")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)    
