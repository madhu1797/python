a= 100
b =10

##When you compare two values, the expression is evaluated and Python returns the Boolean answer True or False 

if a>b:
    print("A is greater than B")
else:
    print("B is greater than A")

##OUTPUT:
##A is greater than B

##Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))
print(bool(0))
print(bool([]))
print(bool({}))

##OUTPUT
True
True
False
False
False

##Boolean with in operator
print("b" in "aba")
print("c" in "aba")

##OUTPUT
True
False

##Boolean in functions
def add_num_and_len(num, things=None):
     return num + len(things or [])

result=add_num_and_len(5, [1, 2, 3]) ##output = 8
print(result)
result=add_num_and_len(6) ##output = 6
print(result)


