# 문제 4-5 (중/하)
# 설명: 사용자가 입력한 숫자가 소수인지 판별하는 프로그램을 작성하세요.
#  파일명: prime_checker.py
#  출력결과:
# 숫자를 입력하세요: 17
# 17은 소수입니다.

num = int(input("숫자를 입력하세요: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num}은 소수입니다.")
else:
    print(f"{num}은 소수가 아닙니다.")