a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
n = int(input("Nhập các số từ 1 đến 5 để chọn các phép tính:"))
def cong(x,y):
    return x+y
tong = cong(a,b)
def tru(x,y):
    return x - y
hieu = tru(a,b)
def nhan(x,y):
    return x * y
tich = a*b
def chia(x,y):
    return x / y
if b == 0:
    print("Không thể chia cho 0")
thuong = chia(a,b)
def max_value(a,b):
    return max(a,b)
if n == 1:
     print(f"{a} + {b} = ", cong(a,b))
elif n == 2:
    print(f"{a} - {b} = ", tru(a,b))
elif n == 3:
    print(f"{a} * {b} = ", nhan(a,b))
elif n == 4:
    print(f"{a} / {b} = ", chia(a,b))
elif n == 5:
    if a == b:
        print(f"2 số {a} và {b} bằng nhau")
    else:
        print(f"Số lớn hơn trong 2 số {a} và {b} là", max_value(a,b))