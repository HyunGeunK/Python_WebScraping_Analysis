# any_all_example.py
numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

# 기존 방식 (비추천)
def all_even_traditional(nums):
    for num in nums:
        if num % 2 != 0:
            return False
    return True

# Pythonic 방식 (추천)
def check_conditions(nums):
    all_even = all(num % 2 == 0 for num in nums)
    any_greater_than_10 = any(num > 10 for num in nums)
    return all_even, any_greater_than_10

print(f"숫자 리스트: {numbers1}")
all_even1, any_gt_10_1 = check_conditions(numbers1)
print(f"모든 수가 짝수인가? {all_even1}")
print(f"하나라도 10보다 큰 수가 있는가? {any_gt_10_1}")

print(f"\n숫자 리스트2: {numbers2}")
all_even2, any_gt_10_2 = check_conditions(numbers2)
print(f"모든 수가 짝수인가? {all_even2}")
print(f"하나라도 10보다 큰 수가 있는가? {any_gt_10_2}")