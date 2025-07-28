# json_handler.py
import json

# 저장할 데이터
person_data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자", 
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}

# JSON 파일 쓰기
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(person_data, file, ensure_ascii=False, indent=2)

print("데이터가 data.json에 저장되었습니다.")

# JSON 파일 읽기
print("\nJSON에서 읽어온 데이터:")
with open('data.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
    
    for key, value in loaded_data.items():
        print(f"{key}: {value}")