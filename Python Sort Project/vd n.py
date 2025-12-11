#cau 1:
def tam_giac(n,x):
    num = x
    for i in range(1,n+1):
        for j in range(i):
            print(num, end = " " if j < i -1 else "")
            num += x
        print()
if __name__ == "__main__":
    n = int(input("Nhập n:"))
    x = int(input("Nhập x: "))
    if n <= 0 or x == 0:
        print("n phải > 0 và x khác 0")
    else:
        print(tam_giac(n,x))
#bai 3:
n = int(input("Nhập n:"))
for i in range(1, n + 1):
    trai = " ".join(str(j) for j in range(i,0,-1))
    phai = " ".join(str(j) for j in range(2,i+1))
    print("  " * (n - i) + trai + " " + phai)
#bai 4:
n = int(input("Nhập n:"))
for i in range(n,0,-1):
    trai = " ".join(str(j) for j in range(i,0,-1))
    phai = " ".join(str(j) for j in range(2,i+1))
    print("  " * (n - i) + trai + " " + phai)