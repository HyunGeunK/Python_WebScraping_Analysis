# email_parser.py
email = input("이메일 주소를 입력하세요: ")
username, domain = email.split('@')
print(f"사용자명: {username}")
print(f"도메인: {domain}")