# unpacking_example.py
# 튜플/리스트 언패킹
point = (10, 20)
x, y = point
print(f"좌표: x={x}, y={y}")

numbers = [1, 2, 3]
a, b, c = numbers
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# *args 예제
def sum_all(*args):
    return sum(args)

result = sum_all(10, 20, 30)
print(f"가변 인수의 합: {result}")

# **kwargs 예제
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}={value}", end=" ")

print("키워드 인수들: ", end="")
print_info(name="김철수", age=25, city="서울")
print()