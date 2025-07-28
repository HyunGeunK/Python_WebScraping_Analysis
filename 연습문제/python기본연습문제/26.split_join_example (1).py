# split_join_example.py
# 기존 방식 (비추천)
text = "Python is awesome programming language"
words = []
word = ""
for char in text:
    if char == " ":
        words.append(word)
        word = ""
    else:
        word += char
words.append(word)

# Pythonic 방식 (추천)
text = "Python is awesome programming language"
words = text.split()
hyphen_joined = "-".join(words)
upper_joined = " ".join(word.upper() for word in words)

print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")
print(f"하이픈으로 연결: {hyphen_joined}")
print(f"대문자로 변환 후 공백으로 연결: {upper_joined}")