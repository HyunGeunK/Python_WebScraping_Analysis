# 문제 8-3 (중/하)
# 설명: os와 sys 모듈을 사용하여 시스템 정보를 출력하고 파일 경로를 다루는 프로그램을 작성하세요.
#  파일명: system_info.py
#  출력결과:
# 현재 작업 디렉토리: /Users/username/python_practice
# Python 버전: 3.9.7 (default, Oct 13 2021, 06:44:56)
# 운영체제: posix
# 환경 변수 PATH 일부: /usr/local/bin:/usr/bin:/bin
# 파일 경로 정보:
# - 디렉토리: /Users/username/documents
# - 파일명: report.txt
# - 확장자: .txt
# 파일 존재 여부: False

# system_info.py

import os
import sys

# 현재 작업 디렉토리
print("현재 작업 디렉토리:", os.getcwd())

# Python 버전 정보
print("Python 버전:", sys.version)

# 운영체제 종류
print("운영체제:", os.name)

# 환경 변수 PATH 일부
path_env = os.environ.get("PATH", "")
print("환경 변수 PATH 일부:", path_env.split(":")[0:4])  # 앞 몇 개만 보기 좋게 출력

# 파일 경로 처리 예시
file_path = "/Users/username/documents/report.txt"
dir_name = os.path.dirname(file_path)
file_name = os.path.basename(file_path)
file_root, file_ext = os.path.splitext(file_name)

print("파일 경로 정보:")
print(f"- 디렉토리: {dir_name}")
print(f"- 파일명: {file_name}")
print(f"- 확장자: {file_ext}")

# 해당 파일 존재 여부 확인
print("파일 존재 여부:", os.path.exists(file_path))
