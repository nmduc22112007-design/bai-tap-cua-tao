n = int(input("Nhập vào số phần tử trong mảng: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    arr.append(x)
def so_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
so_hoan_hao = [x for x in arr if so_hoan_hao(x)]
print(f"Các số hoàn hảo có trong mảng là {so_hoan_hao}")