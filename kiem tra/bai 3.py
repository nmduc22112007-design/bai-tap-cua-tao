n = int(input("Nhập n:"))
if n % 6 == 0:
    print(f"Số {n} là số chia hết cho 6")
else:
    print(f"Số {n} là số không chia hết cho 6")
if n < 0:
    print(f"Số {n} là số âm")