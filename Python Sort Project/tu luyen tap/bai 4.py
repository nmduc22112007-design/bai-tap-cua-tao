n = int(input("Nhập n:"))
for i in range(n,0,-1):
    trai = " ".join(str(j) for j in range(i,0,-1))
    phai = " ".join(str(j) for j in range(2,i+1))
    print("  " * (n - i) + trai + " " + phai)