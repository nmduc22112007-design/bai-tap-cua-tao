def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập vào số phần tử trong mảng:"))
arr1 = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    arr1.append(x)
arr1 = [x for x in arr1 if not la_so_nguyen_to(x)]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
selection_sort(arr1)
print("Selection sort result:", arr1)
#bai 4:
def so_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
n = int(input("Nhập vào số phần tử trong mảng:"))
arr1 = [ ]
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i +1}:"))
    arr1.append(x)
arr1 = [x for x in arr1 if not so_hoan_hao(x)]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
selection_sort(arr1)
print("Selection sort result:", arr1)