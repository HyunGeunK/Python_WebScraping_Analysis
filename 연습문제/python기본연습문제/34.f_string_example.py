# f_string_example.py
import datetime

name = "김철수"
age = 25
pi = 3.14159
price = 1234
percentage = 0.855
today = datetime.date(2025, 7, 20)

# 기존 방식 (비추천)
old_format = "이름: %s, 나이: %d" % (name, age)

# Pythonic 방식 (추천)
print(f"이름: {name}, 나이: {age}")
print(f"원주율: {pi:.2f}")
print(f"가격: {price:,}원")
print(f"퍼센트: {percentage:.2%}")
print(f"날짜: {today:%Y년 %m월 %d일}")