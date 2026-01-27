# 1. Exponentiation

def exponentiation(base, power):
    return base ** power

# 2. Square Root

def square_root(number):
    return number** 0.5

# 3. Factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(exponentiation(2, 3))  
print(square_root(16))        
print(factorial(5))          
