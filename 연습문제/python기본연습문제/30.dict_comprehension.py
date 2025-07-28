# dict_comprehension.py
# 기존 방식 (비추천)
squares_dict = {}
for i in range(1, 6):
    squares_dict[i] = i ** 2

# Pythonic 방식 (추천)
squares_dict = {i: i**2 for i in range(1, 6)}
even_squares = {i: i**2 for i in range(1, 11) if i % 2 == 0}

print(f"1부터 5까지의 제곱 딕셔너리: {squares_dict}")
print(f"짝수만의 제곱 딕셔너리: {even_squares}")