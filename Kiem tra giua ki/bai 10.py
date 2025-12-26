n = int(input("Nhập n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(" ".join(str(j) for j in range(n)))