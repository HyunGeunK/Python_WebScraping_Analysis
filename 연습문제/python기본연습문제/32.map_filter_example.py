# map_filter_example.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 기존 방식 (비추천)
squared_old = []
for num in numbers:
    squared_old.append(num ** 2)

filtered_old = []
for num in numbers:
    if num > 5:
        filtered_old.append(num)

# Pythonic 방식 (추천)
squared_nums = list(map(lambda x: x**2, numbers))
filtered_nums = list(filter(lambda x: x > 5, numbers))
filtered_squared = list(map(lambda x: x**2, filter(lambda x: x > 5, numbers)))

print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squared_nums}")
print(f"5보다 큰 수들: {filtered_nums}")
print(f"5보다 큰 수들의 제곱: {filtered_squared}")