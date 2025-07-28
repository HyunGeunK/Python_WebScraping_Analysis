# shopping_cart.py
cart = {
    '사과': {'quantity': 2, 'price': 1000},
    '바나나': {'quantity': 3, 'price': 800},
    '오렌지': {'quantity': 1, 'price': 1500}
}

print("쇼핑 카트:")
total_price = 0
for item, info in cart.items():
    item_total = info['quantity'] * info['price']
    total_price += item_total
    print(f"{item}: {info['quantity']}개 (개당 {info['price']}원) = {item_total}원")

print(f"총 가격: {total_price}원")