# 문제 1-5 (중/하)
# 설명: 상품의 가격과 할인율을 입력받아 할인된 가격을 계산하는 프로그램을 작성하세요.
#  파일명: discount_calculator.py
#  출력결과:
# 상품 가격을 입력하세요: 50000
# 할인율을 입력하세요(%): 20
# 원래 가격: 50000원
# 할인율: 20%
# 할인 금액: 10000원
# 최종 가격: 40000원

sangpum =  int(input("상품 가격을 입력하세요: "))
sale =  int(input("할인율을 입력하세요(%): "))
print(f"원래가격 : {sangpum}")
print(f"할인율: {sale}%")
sale_money = sangpum * (sale/100)
print(f"할인 금액 : {int(sale_money)}")
print(f"최종 가격: {int(sangpum - sale_money)}")