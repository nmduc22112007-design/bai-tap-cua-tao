n = int(input("Nhập vào số phần tử trong list:"))
lst = []
for i in range(n):
    lst.append(int(input(f"Nhập vào phần tử thứ {i+1} trong list:")))
def so_le(n):
    if i % 2 != 0:
        return True
    else:
        return False
def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(so_le(n))
