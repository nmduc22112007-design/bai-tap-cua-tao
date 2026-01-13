n = int(input("Nhap n(n > 0):"))
if n <= 0:
    n = int(input("Vui long nhap n > 0:"))
def tong(n):
    if n < 10:
        return n
    else:
        return tong(n//10) + n%10
print(tong(n))