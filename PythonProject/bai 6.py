n = int(input("Nhập vào số phần tử trong mảng:"))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i +1}:"))
    arr.append(x)
print("Tổng các phần tử trong mảng là:")
total = sum(arr(x) for x in arr)
print(total)