# rectangle_calculator.py
width = float(input("가로 길이를 입력하세요: "))
height = float(input("세로 길이를 입력하세요: "))

area = width * height
perimeter = 2 * (width + height)

print(f"직사각형의 넓이: {area}")
print(f"직사각형의 둘레: {perimeter}")