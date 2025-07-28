# module_usage.py
import datetime
import random

# datetime 모듈 사용
now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"포맷된 날짜: {now.strftime('%Y년 %m월 %d일 %A')}")

# random 모듈 사용
random_int = random.randint(1, 10)
random_float = random.uniform(1.0, 5.0)
print(f"임의의 숫자: {random_int}")
print(f"임의의 실수: {random_float:.2f}")

# 리스트에서 임의 선택
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
random_fruit = random.choice(fruits)
print(f"임의의 리스트 요소: {random_fruit}")

# 리스트 섞기
random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")