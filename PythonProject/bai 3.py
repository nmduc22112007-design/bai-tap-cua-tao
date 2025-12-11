n = int(input("Nhập vào số phần tử trong mảng:"))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i +1}:"))
    arr.append(x)
for x in range(n-1, -1, -1):
    print(f"arr[{x}] = {arr[x]}")
