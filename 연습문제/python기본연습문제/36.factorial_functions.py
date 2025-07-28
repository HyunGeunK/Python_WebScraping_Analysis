# factorial_functions.py
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 함수 테스트
numbers = [5, 7]
for num in numbers:
    rec_result = factorial_recursive(num)
    iter_result = factorial_iterative(num)
    print(f"{num}! (재귀) = {rec_result}")
    print(f"{num}! (반복) = {iter_result}")