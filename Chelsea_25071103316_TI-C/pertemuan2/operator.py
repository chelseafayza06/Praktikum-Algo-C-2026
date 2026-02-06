# Aritmetic operator
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Assigment operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Comparison Operator
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Membership Operator
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# Bitwise Operator
print(6 & 3)
print(6 | 3)

# Operator Precedence
print(5 + 4 - 7 + 3)












#logical operator
x = 5

print(x > 0 and x < 10)

x = 5

print(x < 5 or x > 10)

x = 5

#identity operator
print(not(x > 3 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x


print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)