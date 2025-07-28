# word_frequency.py
# 샘플 텍스트 파일 생성
sample_text = """파이썬은 배우기 쉬운 프로그래밍 언어입니다
파이썬은 강력한 프로그래밍 언어입니다  
파이썬 언어를 배워봅시다"""

with open('sample_text.txt', 'w', encoding='utf-8') as file:
    file.write(sample_text)

# 파일 읽기 및 단어 빈도 계산
word_count = {}

with open('sample_text.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    words = content.replace('\n', ' ').split()
    
    for word in words:
        # 불필요한 문자 제거
        word = word.strip('.,!?')
        if word:
            word_count[word] = word_count.get(word, 0) + 1

# 빈도순으로 정렬하여 출력
print("단어 빈도 분석 결과:")
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"{word}: {count}번")