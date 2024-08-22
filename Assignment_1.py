

def product_up_to_n(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

n = int(input("Enter a number: "))
print("Product of numbers up to", n, ":", product_up_to_n(n))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
for i in range(2, n + 1):
    if is_prime(i):
        print(f"{i} is prime.")
    else:
        print(f"{i} is not prime.")

def factors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

for i in range(1, 101):
    print(f"Factors of {i}: {factors(i)}")

def multiply_primes_up_to_n(n):
    product = 1
    for i in range(2, n + 1):
        if is_prime(i):
            product *= i
    return product

n = int(input("Enter a number: "))
print("Product of prime numbers up to", n, ":", multiply_primes_up_to_n(n))

import math

x = float(input("Enter x coordinate: "))

def distance_from_origin(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)
y = float(input("Enter y coordinate: "))
z = float(input("Enter z coordinate: "))

distance = distance_from_origin(x, y, z)
print(f"Distance from (0,0,0) to ({x},{y},{z}) is {distance}")