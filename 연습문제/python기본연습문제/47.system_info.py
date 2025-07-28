# system_info.py
import os
import sys

# 현재 작업 디렉토리
current_dir = os.getcwd()
print(f"현재 작업 디렉토리: {current_dir}")

# Python 버전 정보
print(f"Python 버전: {sys.version}")

# 운영체제 정보
print(f"운영체제: {os.name}")

# 환경 변수
path_env = os.environ.get('PATH', '')
print(f"환경 변수 PATH 일부: {path_env[:50]}...")

# 파일 경로 다루기
file_path = "/Users/username/documents/report.txt"
print(f"파일 경로 정보:")
print(f"- 디렉토리: {os.path.dirname(file_path)}")
print(f"- 파일명: {os.path.basename(file_path)}")
print(f"- 확장자: {os.path.splitext(file_path)[1]}")

# 파일 존재 확인
print(f"파일 존재 여부: {os.path.exists(file_path)}")

# 현재 디렉토리의 파일 목록 (처음 5개만)
files = os.listdir(current_dir)[:5]
print(f"현재 디렉토리의 파일들: {files}")