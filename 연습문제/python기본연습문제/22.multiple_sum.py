# multiple_sum.py
multiples_of_3 = []
total = 0

for i in range(1, 101):
    if i % 3 == 0:
        multiples_of_3.append(i)
        total += i

print(f"1부터 100까지 3의 배수: {multiples_of_3}")
print(f"3의 배수의 합: {total}")
print(f"3의 배수의 개수: {len(multiples_of_3)}개")