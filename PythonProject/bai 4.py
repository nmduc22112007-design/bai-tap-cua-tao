n = int(input("Nhập vào số phần tử trong mảng:"))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i }:"))
    arr.append(x)
print("Các phần tử có vị trí chẵn là:")
for i in range(0, len(arr), 2):
    print(arr[i])