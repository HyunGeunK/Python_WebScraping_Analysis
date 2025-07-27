# 문제 5-9 (중/하)
# 설명: f-string을 사용한 문자열 포매팅 예제를 작성하세요.
#  파일명: f_string_example.py
#  출력결과:
# 이름: 김철수, 나이: 25
# 원주율: 3.14
# 가격: 1,234원
# 퍼센트: 85.50%
# 날짜: 2025년 07월 20일

# # f_string_example.py
# import datetime

# name = "김철수"
# age = 25
# pi = 3.14159
# price = 1234
# percentage = 0.855
# today = datetime.date(2025, 7, 20)

# # 기존 방식 (비추천)
# old_format = "이름: %s, 나이: %d" % (name, age)

import datetime

name = "김철수"
age = 25
pi = 3.14159
price = 1234
percentage = 0.855
today = datetime.date(2025, 7, 20)

print(f"이름: {name}, 나이: {age}")
print(f"원주율: {pi:.2f}")  # 소수점 둘째 자리까지
print(f"가격: {price:,}원")  # 천 단위 쉼표
print(f"퍼센트: {percentage:.2%}")  # 백분율 변환
print(f"날짜: {today.year}년 {today.month:02d}월 {today.day:02d}일")  # 2자리 수로 표현
