# 문제 5-6 (중/하)
# 설명: any와 all 함수를 사용하여 조건을 검사하는 프로그램을 작성하세요.
#  파일명: any_all_example.py
#  출력결과:
# 숫자 리스트: [2, 4, 6, 8, 10]
# 모든 수가 짝수인가? True
# 하나라도 10보다 큰 수가 있는가? False

# 숫자 리스트2: [1, 3, 5, 7, 12]
# 모든 수가 짝수인가? False
# 하나라도 10보다 큰 수가 있는가? True
# # any_all_example.py
# numbers1 = [2, 4, 6, 8, 10]
# numbers2 = [1, 3, 5, 7, 12]

# # 기존 방식 (비추천)
# def all_even_traditional(nums):
#     for num in nums:
#         if num % 2 != 0:
#             return False
#     return True


numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

def check_conditions(numbers):
    print(f"숫자 리스트: {numbers}")
    print("모든 수가 짝수인가?", all(num % 2 == 0 for num in numbers))
    print("하나라도 10보다 큰 수가 있는가?", any(num > 10 for num in numbers))
    print()  

check_conditions(numbers1)
check_conditions(numbers2)
