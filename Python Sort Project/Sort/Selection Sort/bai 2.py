n = int(input("Nhập vào số phần tử trong mảng:"))
arr1 = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i +1}:"))
    arr1.append(x)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
selection_sort(arr1)
print("Selection sort result:", arr1[::-1])