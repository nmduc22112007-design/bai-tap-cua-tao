import random
m = int(input("Nhập m:"))
n = int(input("Nhập n:"))
for i in range(m):
    for j in range(n):
        x = [random.randint(0,20) for x in range(m*n)]
print(x)