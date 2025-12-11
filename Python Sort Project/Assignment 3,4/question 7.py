n = int(input("Nhập vào số phần tử trong mảng:"))
arr1 = []
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i +1}:"))
    arr1.append(x)
def insertion_sort(arr):
    for i in range(0,len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
insertion_sort(arr1)
print(f"Insertion Sort: {arr1[::-1]}")