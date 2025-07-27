# 5. Pythonic Coding 스타일 (10문제)
# 문제 5-1 (중/하)
# 설명: 문자열을 단어별로 분리했다가 다시 합치는 코드를 split과 join을 사용하여 작성하세요.
#  파일명: split_join_example.py
#  출력결과:
# 원본 문자열: Python is awesome programming language
# 분리된 단어들: ['Python', 'is', 'awesome', 'programming', 'language']
# 하이픈으로 연결: Python-is-awesome-programming-language
# 대문자로 변환 후 공백으로 연결: PYTHON IS AWESOME PROGRAMMING LANGUAGE
# split_join_example.py
# 기존 방식 (비추천)
text = "Python is awesome programming language"
words = text.split()
join_hyphen = "-".join(words)
join_up = " ".join(words).upper()

# 출력
print("원본 문자열:", text)
print("분리된 단어들:", words)
print("하이픈으로 연결:", join_hyphen)
print("대문자로 변환 후 공백으로 연결:", join_up)
