n = int(input("Nhập vào số phần tử trong mảng: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    arr.append(x)
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
so_nguyen_to = [x for x in arr if la_so_nguyen_to(x)]
so_nguyen_to.sort()
print(f"Các số nguyên tố trong mảng là arr{arr} = {so_nguyen_to}")