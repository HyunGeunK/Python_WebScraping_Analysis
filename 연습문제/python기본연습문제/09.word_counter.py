# word_counter.py
sentence = input("문장을 입력하세요: ")
cleaned = sentence.strip()
words = cleaned.split()
print(f"공백 제거: {cleaned}")
print(f"단어 개수: {len(words)}개")