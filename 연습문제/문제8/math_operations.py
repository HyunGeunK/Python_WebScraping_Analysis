# math_operations.py

PI = 3.14159

def area_circle(r):
    return PI * r * r

def area_rectangle(w, h):
    return w * h

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
