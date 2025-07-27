# 문제 3-5 (중/하)
# 설명: 쇼핑 카트를 딕셔너리로 구현하여 상품을 추가하고 총 가격을 계산하는 프로그램을 작성하세요.
#  파일명: shopping_cart.py
#  출력결과:
# 쇼핑 카트:
# 사과: 2개 (개당 1000원) = 2000원
# 바나나: 3개 (개당 800원) = 2400원
# 오렌지: 1개 (개당 1500원) = 1500원
# 총 가격: 5900원

cart = {
    "사과": {"수량": 2, "단가": 1000},
    "바나나": {"수량": 3, "단가": 800},
    "오렌지": {"수량": 1, "단가": 1500}
}

print("쇼핑 카트:")
total_price = 0

for item, i in cart.items():
    count = i["수량"]
    price = i["단가"]
    item_total = count*price
    total_price += item_total
    print(f"{item}: {count}개 (개당 {price}원) = {item_total}원")

print(f"총 가격: {total_price}원")