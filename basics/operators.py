Variable_1 = 10
Variable_2 = 20

##Arithmetic Operators
print("Arithmatic Evalulation")
print(Variable_1 + Variable_2)
print(Variable_1 - Variable_2)
print(Variable_1 * Variable_2)
print(Variable_2 / Variable_1)
print(Variable_2 // Variable_1)
print(Variable_2 % Variable_1)
print(Variable_2 ** 2)


##Assignment Operators
print("Assignment operation Evalulation")
x = 5	##x = 5
print(x)
x += 3	##x = x + 3
print(x)
x -= 3	##x = x - 3
print(x)
x *= 3	##x = x * 3
print(x)
x /= 3	##x = x / 3
print(x)
x %= 3	##x = x % 3
print(x)
x //= 3	##x = x // 3
print(x)
x **= 3	##x = x ** 3
print(x)
x=5
x &= 3	##x = x & 3
print(x)
x |= 3	##x = x | 3
print(x)
x ^= 3	##x = x ^ 3
print(x)
x >>= 3	##x = x >> 3
print(x)
x <<= 3	##x = x << 3
print(x)

##Comparison operators
x = 5
y = 3

print("Comparison operation Evalulation")

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

##Logical operators(and, or not)
x = 5
print("Logical Evalulation")
print(x > 3 and x < 10)
print(x > 3 or x < 10)
print(not(x > 3 and x < 10))

##Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("identity operation Evalulation")
print(x is z)
print(x is y)
print(x == y)

##Membership Operators
x = ["apple", "banana"]
print("membership operation Evalulation")
print("banana" in x)
print("papaya" in x)
