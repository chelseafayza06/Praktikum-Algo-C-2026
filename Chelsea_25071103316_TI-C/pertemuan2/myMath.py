a = 10
b = 5

#Penambahan
def penambahan (a,b):
  return a + b
print(a+b)

#pengurangan
def pengurangan (a,b):
  return a-b
print (a-b)

#perkalian
def perkalian (a,b):
  return a*b
print(a*b)

#Pembagian
def pembagian (a,b):
  return a/b
print(a/b)
#"Pembagian tidak dapat dilakukan karena pembagi bernilai 0".

#Modulus
def modulus (a,b):
  return a%b
print(a%b)

#fibonacci(n)
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))

def fibonacci(n):
    deret = []
    a, b = 0, 1

# Fibonacci (yang benar,setelah dipelajari dan melihat referensi)
n = 7
fbnc = []
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range (n) :
  fbnc.append(fibonacci(n-i))
print (fbnc)


   
