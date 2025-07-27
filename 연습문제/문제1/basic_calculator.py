# 문제 1-1 (하)
# 설명: 사용자로부터 두 개의 정수를 입력받아 사칙연산(+, -, *, /)의 결과를 출력하는 프로그램을 작성하세요.
#  파일명: basic_calculator.py
#  출력결과:
# 첫 번째 숫자를 입력하세요: 10
# 두 번째 숫자를 입력하세요: 3
# 10 + 3 = 13
# 10 - 3 = 7
# 10 * 3 = 30
# 10 / 3 = 3.33

first = int(input("첫 번째 숫자를 입력하세요:"))
second = int(input("두번째 숫자를 입력하세요:"))

print(f"{first} + {second} = {first+second}")
print(f"{first} - {second} = {first-second}")
print(f"{first} * {second} = {first*second}")
print(f"{first} / {second} = {first/second:.2f}")
