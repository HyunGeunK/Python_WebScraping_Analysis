# 문제 5-5 (중/하)
# 설명: 딕셔너리 컴프리헨션을 사용하여 숫자와 그 제곱값의 딕셔너리를 만드는 프로그램을 작성하세요.
#  파일명: dict_comprehension.py
#  출력결과:
# 1부터 5까지의 제곱 딕셔너리: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# 짝수만의 제곱 딕셔너리: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# # dict_comprehension.py
# # 기존 방식 (비추천)
# squares_dict = {}
# for i in range(1, 6):
#     squares_dict[i] = i ** 2


squares_dict = {i: i**2 for i in range(1, 6)}

even_squares = {i: i**2 for i in range(1, 11) if i % 2 == 0}

print("1부터 5까지의 제곱 딕셔너리:", squares_dict)
print("짝수만의 제곱 딕셔너리:", even_squares)
