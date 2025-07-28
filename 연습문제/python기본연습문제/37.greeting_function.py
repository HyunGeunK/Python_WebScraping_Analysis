# greeting_function.py
def create_greeting(name, language="한국어", extra_message=""):
    if language == "한국어":
        greeting = f"안녕하세요, {name}님!"
    elif language == "영어":
        greeting = f"Hello, {name}!"
    else:
        greeting = f"안녕하세요, {name}님!"
    
    if extra_message:
        greeting += f" {extra_message}"
    
    return greeting

# 함수 사용
print(create_greeting("김철수"))
print(create_greeting("John", "영어"))
print(create_greeting("이영희", extra_message="좋은 하루 되세요!"))