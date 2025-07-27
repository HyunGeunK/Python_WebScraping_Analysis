# 3. 자료구조 (List, Dict, Tuple) 처리하기 (10문제)
# 문제 3-1 (하)
# 설명: 5개의 숫자를 리스트에 저장하고 합계와 평균을 구하는 프로그램을 작성하세요.
#  파일명: list_statistics.py
#  출력결과:
# 숫자들: [10, 20, 30, 40, 50]
# 합계: 150
# 평균: 30.0

number = []

for i in range(5):
    num = int(input(f"{i+1}번째 숫자를 입력하세요: "))
    number.append(num)

total = sum(number)
avg = total / len(number)

print(f"숫자들: {number}")
print(f"합계: {total}")
print(f"평균: {avg}")