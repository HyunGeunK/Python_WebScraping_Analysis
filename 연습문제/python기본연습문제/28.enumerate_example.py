# enumerate_example.py
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

# 기존 방식 (비추천)
print("기존 방식:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Pythonic 방식 (추천)
print("\n과일 목록:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")