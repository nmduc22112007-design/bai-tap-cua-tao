n = int(input("Nhập n: "))
tong = 0
i = 2
while i <= n:
    tong += i
    i += 2
print(f"Tổng các số chẵn từ 2 đến {n} là {tong}")