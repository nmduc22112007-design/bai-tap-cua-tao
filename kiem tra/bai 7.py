n = int(input("Nhập vào tháng:"))
i = int(input("Nhập vào năm:"))
if n == 2:
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(f"Tháng {n} năm {i} có 29 ngày")
    else:
        print(f"Tháng {n} năm {i} có 28 ngày")
if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print(f"Tháng {n} năm {i} có 31 ngày")
elif n == 4 or n == 6 or n == 9 or n == 11:
    print(f"Tháng {n} năm {i} có 30 ngày")
