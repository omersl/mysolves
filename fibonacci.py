a,b = (0,1)
while b <= 4000000:
    a,b = b, a+b
    print(b)
