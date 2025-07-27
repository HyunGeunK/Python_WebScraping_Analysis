# 문제 6-3 (중/하)
# 설명: 기본값 매개변수를 사용하여 인사말을 생성하는 함수를 작성하세요.
#  파일명: greeting_function.py
#  출력결과:
# 안녕하세요, 김철수님!
# Hello, John!
# 안녕하세요, 이영희님! 좋은 하루 되세요!


def greet(name, message="안녕하세요", ending="님!"):
    """기본 인사말을 생성하는 함수"""
    print(f"{message}, {name}{ending}")

greet("김철수")                         # 기본값 사용
greet("John", message="Hello", ending="!")  # 영어 인사
greet("이영희", ending="님! 좋은 하루 되세요!")  # 한국어 인사 + ending만 수정
