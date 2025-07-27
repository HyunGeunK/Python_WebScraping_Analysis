# 6. 함수 (5문제)
# 문제 6-1 (하)
# 설명: 두 수를 받아서 사칙연산을 수행하는 함수들을 작성하는 프로그램을 만드세요.
#  파일명: calculator_functions.py
#  출력결과:
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2.0

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b


x = 10
y = 5
print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {multiply(x, y)}")
print(f"{x} / {y} = {divide(x, y)}")