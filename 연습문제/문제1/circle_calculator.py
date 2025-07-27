# 문제 1-2 (중/하)
# 설명: 원의 반지름을 입력받아 원의 넓이와 둘레를 계산하는 프로그램을 작성하세요. (π = 3.14159 사용)
#  파일명: circle_calculator.py
#  출력결과:
# 원의 반지름을 입력하세요: 5
# 반지름이 5인 원의 넓이: 78.54
# 반지름이 5인 원의 둘레: 31.42

radius = float(input("원의 반지름을 입력하세요: "))
pi = 3.14159

area = pi * radius ** 2
circumference = 2 * pi * radius

print(f"반지름이 {radius}인 원의 넓이: {area:.2f}")
print(f"반지름이 {radius}인 원의 둘레: {circumference:.2f}")