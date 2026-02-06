# Function 
def my_function():
  print("Hello from a function")

my_function() # Ini Cara manggilnya

def my_function(name="Chelsea"):
  print("Hello", name)

my_function()
my_function()
my_function()

#Using the return value directly

def get_greeting():
  return "Hello from a function"

print(get_greeting())

# Python Scope
def myfunc():
  x = 300
  print(x)

myfunc()

x = lambda a : a + 10
print(x(5))

def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))


# Fibonacci 
# Angka yang sekarang adalah hasil dari penjumlahan 2 angka sebelumnya 
# 0,1,1,2,3,5,8...
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2) 

print(fibonacci(7))

