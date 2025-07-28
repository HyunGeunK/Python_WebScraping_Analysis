# student_sort.py
students = [
    {'name': '김철수', 'age': 20, 'major': '컴퓨터공학과'},
    {'name': '이영희', 'age': 22, 'major': '영어영문학과'},
    {'name': '박민수', 'age': 21, 'major': '경영학과'},
    {'name': '최수진', 'age': 23, 'major': '수학과'}
]

sorted_students = sorted(students, key=lambda x: x['age'])

print("나이 순으로 정렬된 학생 목록:")
for student in sorted_students:
    print(f"{student['name']} ({student['age']}세) - {student['major']}")