# discount_calculator.py
price = int(input("상품 가격을 입력하세요: "))
discount_rate = float(input("할인율을 입력하세요(%): "))

discount_amount = price * (discount_rate / 100)
final_price = price - discount_amount

print(f"원래 가격: {price}원")
print(f"할인율: {discount_rate}%")
print(f"할인 금액: {int(discount_amount)}원")
print(f"최종 가격: {int(final_price)}원")