# 문제 5-2 (중/하)
# 설명: 리스트에서 짝수만 추출하여 제곱하는 코드를 리스트 컴프리헨션으로 작성하세요.
#  파일명: list_comprehension_example.py
#  출력결과:
# 원본 리스트: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 짝수들: [2, 4, 6, 8, 10]
# 짝수의 제곱: [4, 16, 36, 64, 100]
# # list_comprehension_example.py
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 기존 방식 (비추천)
# even_numbers = []
# squared_evens = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
#         squared_evens.append(num ** 2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [n for n in numbers if n % 2 == 0]
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]

print("원본 리스트:", numbers)
print("짝수들:", even_numbers)
print("짝수의 제곱:", squared_evens)