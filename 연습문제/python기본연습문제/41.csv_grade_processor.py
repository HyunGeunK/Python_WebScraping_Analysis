# csv_grade_processor.py
import csv

# 학생 데이터
students_data = [
    ['이름', '점수'],
    ['김철수', '85'],
    ['이영희', '92'], 
    ['박민수', '78'],
    ['최수진', '95']
]

# CSV 파일 쓰기
with open('grades.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(students_data)

print("학생 성적이 grades.csv에 저장되었습니다.")

# CSV 파일 읽기 및 분석
print("\n성적 분석 결과:")
total_score = 0
student_count = 0

with open('grades.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 스킵
    
    for row in reader:
        name, score = row
        score = int(score)
        print(f"{name}: {score}점")
        total_score += score
        student_count += 1

average = total_score / student_count
print(f"전체 평균: {average}점")