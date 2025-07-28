# 3-1. 네이버 책 검색 API 호출하기 (필수)
# https://developers.naver.com/docs/serviceapi/search/book/book.md#%EC%B1%85

# 검색어(query)는  함수의 인자로 받아서 동적으로 처리 되어야 합니다. 
# 최대한 코드가 중복되지 않도록 공통으로 처리해야 하는 부분은 함수로 작성해서 재사용 하는 방식으로 코드를 작성해 주세요.

# def search_books(query):   
#     # query string 문자열을 dict 선언
#     payload = {
#     'query':  query, #'파이썬',
#     'display': 50,
#     'sort': 'sim'
#     }

#    url = 'https://openapi.naver.com/v1/search/book.json'
   
#    # requests get(url, params, headers) 요청 
#    res = requests.get(url, params=payload, headers=headers)
#    # json() 함수로 응답 결과 가져오기
#    items_data = res.json()['items'] 

# 1. 질문 :  검색어로  찾은  책 목록을 json 파일로 저장하기
#    data/books.json 파일로 저장해 주세요.

# 2. books.json 파일을 Pandas DataFrame로 저장하기

# 3. 질문 :  검색어로  찾은  책 목록 출력하기
# 출력결과 : 



# 4. 질문 :  검색어로  찾은  책 목록 중에서 가격이 2만원 이상인 책만 출력하기

# title,author,discount,publisher,pubdate 컬럼만 출력
# 가격은 descending (내림차순), index 초기화


# 6. 질문 :  검색어로  찾은  책 목록 중에서 출판사가 인피니티북스인 책만 출력하기

# image , description 컬럼은 제외한 모든 컬럼 출력하기
# index 는 초기화


# file: naver_book_search.py
# pip install requests pandas

# file: naver_book_search.py

import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv

# ─────────────────────────────────────────────
# 0) 환경변수 불러오기 (.env 사용)
# ─────────────────────────────────────────────
load_dotenv()

CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

HEADERS = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET
}

JSON_PATH = "data/books.json"

# ─────────────────────────────────────────────
# 유틸 함수
# ─────────────────────────────────────────────
def ensure_data_dir():
    os.makedirs("data", exist_ok=True)

def to_int_safe(x):
    try:
        return int(x)
    except:
        return 0

# ─────────────────────────────────────────────
# 1. 검색어로 책 검색 → JSON 저장 + DataFrame 반환
# ─────────────────────────────────────────────
def search_books(query):
    payload = {
        "query": query,
        "display": 50,
        "sort": "sim"
    }
    url = "https://openapi.naver.com/v1/search/book.json"

    res = requests.get(url, params=payload, headers=HEADERS)
    res.raise_for_status()  # 200 아니면 예외 발생

    items = res.json().get("items", [])

    # 1. JSON 저장
    ensure_data_dir()
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

    # 2. DataFrame 생성해서 반환
    df = pd.DataFrame(items)
    return df

# ─────────────────────────────────────────────
# 2. 저장된 books.json을 DataFrame으로 불러오기
# ─────────────────────────────────────────────
def load_books_df_from_json():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        items = json.load(f)
    return pd.DataFrame(items)

# ─────────────────────────────────────────────
# 3. 전체 목록 출력
# ─────────────────────────────────────────────
def print_all_books(df):
    cols = ["title", "author", "discount", "publisher", "pubdate", "isbn"]
    exist_cols = [c for c in cols if c in df.columns]
    print("\n📚 전체 책 목록:")
    print(df[exist_cols].reset_index(drop=True).to_string(index=False))

# ─────────────────────────────────────────────
# 4. 가격 2만원 이상 책 필터링 출력
# ─────────────────────────────────────────────
def print_books_over_20000(df):
    if "discount" not in df.columns:
        print("⚠️ discount 컬럼 없음")
        return

    df["discount_int"] = df["discount"].apply(to_int_safe)
    result = df[df["discount_int"] >= 20000] \
        .sort_values(by="discount_int", ascending=False) \
        .reset_index(drop=True)

    result = result.rename(columns={"discount_int": "discount"})

    print("\n💸 2만원 이상 책 목록:")
    print(result[["title", "author", "discount", "publisher", "pubdate"]].to_string(index=False))

# ─────────────────────────────────────────────
# 6. 출판사 인피니티북스 필터링 출력
# ─────────────────────────────────────────────
def print_books_infinitybooks(df):
    result = df[df["publisher"] == "인피니티북스"].reset_index(drop=True)
    result = result.drop(columns=[c for c in ["image", "description"] if c in result.columns], errors="ignore")

    print("\n🏢 인피니티북스 출판 책 목록:")
    if result.empty:
        print("없음")
    else:
        print(result.to_string(index=False))

# ─────────────────────────────────────────────
# main
# ─────────────────────────────────────────────
if __name__ == "__main__":
    query = input("🔍 검색어를 입력하세요: ").strip()

    try:
        df_books = search_books(query)

        print_all_books(df_books)
        print_books_over_20000(df_books)
        print_books_infinitybooks(df_books)

    except requests.exceptions.HTTPError as e:
        print("❌ HTTP 에러:", e)
    except Exception as e:
        print("❌ 예외 발생:", e)
