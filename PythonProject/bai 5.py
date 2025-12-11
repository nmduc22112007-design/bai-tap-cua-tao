n = int(input("Nhập vào số phần tử trong mảng:"))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i}:"))
    arr.append(x)
print("Các phần tử có giá trị là số chẵn là:")
for i in range(n):
    if arr[i] % 2 == 0:
        print(arr[i])