n = int(input("Nhập n:"))
for i in range(1,n+1):
    trai = "".join(str(j) for j in range(1, i + 1))
    phai = "".join(str(j) for j in range(i-1, 0, -1))
    print(" " * (n - i) + trai + phai)