n = int(input("Nhap n:"))
def tong_so_le(n):
    if n < 1:
        return 0
    if n % 2 != 0:
        return n + tong_so_le(n - 2)
    return tong_so_le(n - 1)
print(tong_so_le(n))#v