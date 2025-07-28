# multiplication_table.py
dan = int(input("몇 단을 출력할까요? "))
print(f"{dan}단 구구단:")

for i in range(1, 10):
    result = dan * i
    print(f"{dan} x {i} = {result}")