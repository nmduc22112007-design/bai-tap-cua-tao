import math
n = int(input("Nhập vào số phần tử trong mảng: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    arr.append(x)
def so_chinh_phuong(n):
    if n < 2:
        return False
    tong_uoc = 1
    for i in range(n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
so_hoan_hao = [x for x in arr if so_chinh_phuong(x)]
print(f"Các số chính phương trong chuỗi là {so_chinh_phuong}")