n = int(input("Nhap n:"))
if n % 5 == 0:
    print(f"{n} la so chia het cho 5")
else:
    print(f"{n} khong phai so chia het cho 5")
if n > 0:
    for i in range(1,n+1):
        if i % 5 == 0:
            print(i)