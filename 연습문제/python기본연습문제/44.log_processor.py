# log_processor.py
from datetime import datetime

# 로그 데이터 생성
log_entries = [
    "2025-07-20 09:00:00 - INFO - 서버 시작됨",
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다", 
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:00:00 - INFO - 사용자 로그인",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족"
]

# 로그 파일 생성
with open('application.log', 'w', encoding='utf-8') as file:
    for entry in log_entries:
        file.write(entry + '\n')

print("로그 파일이 생성되었습니다.")

# 특정 레벨의 로그 필터링 함수
def filter_logs_by_level(filename, level):
    filtered_logs = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if level in line:
                filtered_logs.append(line.strip())
    return filtered_logs

# ERROR 로그 필터링
error_logs = filter_logs_by_level('application.log', 'ERROR')
print(f"\nERROR 레벨 로그들:")
for log in error_logs:
    print(log)

# WARNING 로그 필터링  
warning_logs = filter_logs_by_level('application.log', 'WARNING')
print(f"\nWARNING 레벨 로그들:")
for log in warning_logs:
    print(log)