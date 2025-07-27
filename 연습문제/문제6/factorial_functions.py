# 문제 6-2 (중/하)
# 설명: 팩토리얼을 계산하는 재귀함수와 반복문을 사용한 함수를 각각 작성하세요.
#  파일명: factorial_functions.py
#  출력결과:
# 5! (재귀) = 120
# 5! (반복) = 120
# 7! (재귀) = 5040
# 7! (반복) = 5040


# factorial_functions.py

def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("음수의 팩토리얼은 정의되지 않습니다.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("음수의 팩토리얼은 정의되지 않습니다.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

for v in (5, 7):
    print(f"{v}! (재귀) = {factorial_recursive(v)}")
    print(f"{v}! (반복) = {factorial_iterative(v)}")
