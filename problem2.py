total = 0
a = 0
b = 1
while b <= 4000000:
    if b % 2 == 0:
        total += b
    a,b = b, a+b
print(total)
