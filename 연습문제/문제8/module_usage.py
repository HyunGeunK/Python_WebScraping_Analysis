# 문제 8-2 (중/하)
# 설명: datetime과 random 모듈을 사용하여 임의의 날짜와 숫자를 생성하는 프로그램을 작성하세요.
#  파일명: module_usage.py
#  출력결과:
# 현재 날짜와 시간: 2025-07-20 14:30:25
# 포맷된 날짜: 2025년 07월 20일 일요일
# 임의의 숫자: 7
# 임의의 실수: 3.14
# 임의의 리스트 요소: 바나나
# 섞인 리스트: ['포도', '사과', '오렌지', '바나나', '딸기']

# module_usage.py

import datetime
import random

# 현재 날짜와 시간
now = datetime.datetime.now()
print("현재 날짜와 시간:", now.strftime("%Y-%m-%d %H:%M:%S"))

# 포맷된 날짜 (예: 2025년 07월 20일 일요일)
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
day_name = days[now.weekday()]  # weekday(): 월=0 ~ 일=6

print(f"포맷된 날짜: {now.year}년 {now.month:02d}월 {now.day:02d}일 {day_name}")

# 임의의 정수 (1~10)
print("임의의 숫자:", random.randint(1, 10))

# 임의의 실수 (0.0 ~ 10.0)
print("임의의 실수:", round(random.uniform(0, 10), 2))

# 리스트에서 임의 요소 선택
fruits = ["사과", "바나나", "딸기", "포도", "오렌지"]
print("임의의 리스트 요소:", random.choice(fruits))

# 리스트 섞기
random.shuffle(fruits)
print("섞인 리스트:", fruits)
