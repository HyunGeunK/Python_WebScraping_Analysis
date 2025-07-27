# 문제 3-10 (중/하)
# 설명: 학생 정보를 딕셔너리의 리스트로 저장하고 나이 순으로 정렬하는 프로그램을 작성하세요.
#  파일명: student_sort.py
#  출력결과:
# 나이 순으로 정렬된 학생 목록:
# 김철수 (20세) - 컴퓨터공학과
# 박민수 (21세) - 경영학과
# 이영희 (22세) - 영어영문학과
# 최수진 (23세) - 수학과

students = [
    {"name": "김철수", "age": 20, "major": "컴퓨터공학과"},
    {"name": "박민수", "age": 21, "major": "경영학과"},
    {"name": "이영희", "age": 22, "major": "영어영문학과"},
    {"name": "최수진", "age": 23, "major": "수학과"},
]

sorted_students = sorted(students, key=lambda s: s["age"])

print("나이 순으로 정렬된 학생 목록:")
for s in sorted_students:
    print(f"{s['name']} ({s['age']}세) - {s['major']}")