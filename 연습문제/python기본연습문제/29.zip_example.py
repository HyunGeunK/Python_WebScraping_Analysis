# zip_example.py
students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

# 기존 방식 (비추천)
print("기존 방식:")
for i in range(len(students)):
    print(f"{students[i]}: {scores[i]}점")

# Pythonic 방식 (추천)
print("\n학생과 점수 매칭:")
for student, score in zip(students, scores):
    print(f"{student}: {score}점")

# 딕셔너리로 변환
student_scores = dict(zip(students, scores))
print(f"점수별 학생 딕셔너리: {student_scores}")