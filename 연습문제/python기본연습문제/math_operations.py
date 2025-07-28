# math_operations.py
import math

PI = 3.14159

def circle_area(radius):
    """원의 넓이를 계산하는 함수"""
    return PI * radius ** 2

def rectangle_area(width, height):
    """직사각형의 넓이를 계산하는 함수"""
    return width * height

def factorial(n):
    """팩토리얼을 계산하는 함수"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def gcd(a, b):
    """최대공약수를 계산하는 함수"""
    while b:
        a, b = b, a % b
    return a