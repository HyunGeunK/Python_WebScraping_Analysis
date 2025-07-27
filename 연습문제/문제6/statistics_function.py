# 문제 6-4 (중/하)
# 설명: 리스트의 통계 정보(평균, 최댓값, 최솟값, 표준편차)를 반환하는 함수를 작성하세요.
#  파일명: statistics_function.py
#  출력결과:
# 숫자들: [10, 20, 30, 40, 50]
# 평균: 30.0
# 최댓값: 50
# 최솟값: 10
# 표준편차: 15.81

import math

def get_statistics(numbers):
    """리스트에서 평균, 최댓값, 최솟값, 표준편차를 반환"""
    if not numbers:
        return None

    avg = sum(numbers) / len(numbers)
    max_val = max(numbers)
    min_val = min(numbers)

    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    std_dev = round(math.sqrt(variance), 2)

    return avg, max_val, min_val, std_dev

nums = [10, 20, 30, 40, 50]
avg, max_val, min_val, std_dev = get_statistics(nums)

print(f"숫자들: {nums}")
print(f"평균: {avg}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"표준편차: {std_dev}")
