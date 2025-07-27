# 8. 모듈과 패키지 (3문제)
# 문제 8-1 (중/하)
# 설명: 수학 연산을 위한 모듈을 만들고 이를 사용하는 메인 프로그램을 작성하세요.
#  파일명: main_program.py, math_operations.py
#  출력결과:
# 원의 넓이: 78.54
# 직사각형 넓이: 50
# 팩토리얼 5! = 120
# 최대공약수(48, 18) = 6

# main_program.py

import 연습문제.문제8.math_operations as m

print(f"원의 넓이: {m.area_circle(5):.2f}")
print(f"직사각형 넓이: {m.area_rectangle(10, 5)}")
print(f"팩토리얼 5! = {m.factorial(5)}")
print(f"최대공약수(48, 18) = {m.gcd(48, 18)}")
