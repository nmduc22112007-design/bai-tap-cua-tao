n = int(input("Nhập n:"))
x = int(input("Nhập x: "))
def tam_giac(n,x):
    num = x
    for i in range(1,n+1):
        for j in range(i):
            print(num, end = " " if j < i -1 else "")
            num += x
        print()
if n <= 0 or x == 0:
    print("n phải > 0 và x khác 0")
else:
    print(tam_giac(n,x))