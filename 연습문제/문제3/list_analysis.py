# 문제 3-6 (중/하)
# 설명: 리스트에서 최댓값, 최솟값, 두 번째로 큰 값을 찾는 프로그램을 작성하세요.
#  파일명: list_analysis.py
#  출력결과:
# 숫자 목록: [15, 3, 27, 8, 19, 12, 31]
# 최댓값: 31
# 최솟값: 3
# 두 번째로 큰 값: 27

num_list = [15, 3, 27, 8, 19, 12, 31]
max_num = max(num_list)
min_num = min(num_list)
print(f"최댓값:{max_num }")
print(f"최솟값:{min_num }")

#정렬써서 구하기  첫번째랑 작은값도 이렇게하면 되는데 일부로 둘다함
sort = sorted(num_list, reverse=True)
second = sort[1]
print(f"두 번째로 큰 값:{second}")