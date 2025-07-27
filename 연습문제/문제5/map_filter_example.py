# 문제 5-7 (중/하)
# 설명: map과 filter를 사용하여 리스트를 처리하는 프로그램을 작성하세요.
#  파일명: map_filter_example.py
#  출력결과:
# 원본 숫자: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 모든 수의 제곱: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 5보다 큰 수들: [6, 7, 8, 9, 10]
# 5보다 큰 수들의 제곱: [36, 49, 64, 81, 100]

# # map_filter_example.py
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 기존 방식 (비추천)
# squared_old = []
# for num in numbers:
#     squared_old.append(num ** 2)

# filtered_old = []
# for num in numbers:
#     if num > 5:
#         filtered_old.append(num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x ** 2, numbers))

greater_than_5 = list(filter(lambda x: x > 5, numbers))

squared_gt5 = list(map(lambda x: x ** 2, greater_than_5))

print("원본 숫자:", numbers)
print("모든 수의 제곱:", squared)
print("5보다 큰 수들:", greater_than_5)
print("5보다 큰 수들의 제곱:", squared_gt5)
