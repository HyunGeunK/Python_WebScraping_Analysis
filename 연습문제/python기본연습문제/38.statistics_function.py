# statistics_function.py
import math

def calculate_statistics(numbers):
    if not numbers:
        return None, None, None, None
    
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    # 표준편차 계산
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    
    return mean, maximum, minimum, std_dev

# 함수 사용
data = [10, 20, 30, 40, 50]
mean, max_val, min_val, std_dev = calculate_statistics(data)

print(f"숫자들: {data}")
print(f"평균: {mean}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"표준편차: {std_dev:.2f}")