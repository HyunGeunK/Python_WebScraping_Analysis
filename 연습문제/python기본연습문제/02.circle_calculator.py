# circle_calculator.py
PI = 3.14159
radius = float(input("원의 반지름을 입력하세요: "))

area = PI * radius ** 2
circumference = 2 * PI * radius

print(f"반지름이 {radius}인 원의 넓이: {area:.2f}")
print(f"반지름이 {radius}인 원의 둘레: {circumference:.2f}")