# 문제 5-8 (중/하)
# 설명: 언패킹과 *args, **kwargs를 사용하는 예제를 작성하세요.
#  파일명: unpacking_example.py
#  출력결과:
# 좌표: x=10, y=20
# 리스트 언패킹: a=1, b=2, c=3
# 가변 인수의 합: 60
# 키워드 인수들: name=김철수, age=25, city=서울

# 1. 튜플 언패킹
point = (10, 20)
x, y = point
print(f"좌표: x={x}, y={y}")

# 2. 리스트 언패킹
values = [1, 2, 3]
a, b, c = values
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# 3. *args 사용 예제 (가변 인수)
def sum_all(*args):
    return sum(args)

result = sum_all(10, 20, 30)
print(f"가변 인수의 합: {result}")

# 4. **kwargs 사용 예제 (키워드 인수)
def print_info(**kwargs):
    print("키워드 인수들:", end=" ")
    for key, value in kwargs.items():
        print(f"{key}={value}", end=", ")
    print()  # 줄바꿈

print_info(name="김철수", age=25, city="서울")
