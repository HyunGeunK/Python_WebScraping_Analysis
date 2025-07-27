# 문제 7-3 (중/하)
# 설명: 텍스트 파일의 단어 빈도를 계산하는 프로그램을 작성하세요.
#  파일명: word_frequency.py
#  출력결과:
# 단어 빈도 분석 결과:
# 파이썬: 3번
# 프로그래밍: 2번  
# 언어: 2번
# 배우기: 1번
# 쉬운: 1번
# 강력한: 1번

text = "파이썬 프로그래밍은 쉬운 언어입니다 파이썬은 강력한 언어입니다 파이썬 프로그래밍 배우기"

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(text)

word_count = {}

with open("text.txt", "r", encoding="utf-8") as f:
    line = f.read()
    words = line.split() 

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# 출력
print("단어 빈도 분석 결과:")
for word, count in word_count.items():
    print(f"{word}: {count}번")
