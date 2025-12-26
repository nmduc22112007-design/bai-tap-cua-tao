n = int(input("Nhập n:"))
def fibbonanci(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    return fibbonanci(n-1)+fibbonanci(n-2)
for i in range(n+1):
    print(fibbonanci(i) for j in range(1, i+1))