# 문제 5-10 (중/하)
# 설명: 삼항 연산자와 조건부 표현식을 사용하는 예제를 작성하세요.
#  파일명: conditional_expression.py
#  출력결과:
# 점수: 85, 결과: 합격
# 나이: 17, 상태: 미성년자
# 숫자들의 최대값: 42
# 양수들: [5, 12, 8, 23]
# 답안 코드:
# python
# # conditional_expression.py
# # 기존 방식 (비추천)
# score = 85
# if score >= 80:
#     result = "합격"
# else:
#     result = "불합격"

# conditional_expression.py

# 1. 삼항 연산자 사용 예제
score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

# 2. 나이에 따른 미성년자/성인 판별
age = 17
status = "성인" if age >= 18 else "미성년자"
print(f"나이: {age}, 상태: {status}")

# 3. 최대값 찾기 (조건부 표현식 + max)
numbers = [5, -3, 12, 0, -7, 8, 23, 42, -1]
max_number = max(numbers) if numbers else "리스트가 비어있습니다"
print(f"숫자들의 최대값: {max_number}")

# 4. 양수만 필터링 (조건부 표현식 + 리스트 컴프리헨션)
positives = [num for num in numbers if num > 0]
print(f"양수들: {positives}")
