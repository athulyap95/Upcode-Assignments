# 1. Exponentiation

def exponentiation(base, power):
    #return base ** power
    result = 1
    count = 0
    while count < power:
        result = result * base
        count += 1
    return result

# 2. Square Root

def square_root(number):
    #return number** 0.5
    i = 1
    while i * i <= number:
        i += 1
    return i - 1


# 3. Factorial

def factorial(n):
    # if n == 0:
    #     return 1
    # return n * factorial(n - 1)
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result



print(exponentiation(2, 3))  
print(square_root(16))        
print(factorial(5))          

