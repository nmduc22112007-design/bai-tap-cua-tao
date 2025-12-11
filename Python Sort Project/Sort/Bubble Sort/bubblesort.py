#vd1:
n = int(input("Nhập vào số phần tử trong mảng:"))
arr1 = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i +1}:"))
    arr1.append(x)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            print(f"Bước {i + 1}: {arr}")
        if not swapped:
            break

bubble_sort(arr1)
print("Bubble Sort (tăng dần):", arr1)
#vd2:
n = int(input("Nhập vào số phần tử trong mảng:"))
arr1 = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}:"))
    arr1.append(x)

def bubble_sort(arr):
    n = len(arr)
    print(f"Mảng ban đầu: {arr}")
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Bước {i + 1}: {arr}")
        if not swapped:
            break

bubble_sort(arr1)
print("Bubble Sort (giảm dần):", arr1)
#vd3:
n = int(input("Nhập vào số phần tử trong mảng:"))
arr1 = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}:"))
    arr1.append(x)
def bubble_sort_alternating(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            print(f"Bước {i + 1}: {arr}")
        if not swapped:
            break
bubble_sort_alternating(arr1)
for i in range(1,n-1,2):
    arr1[i], arr1[i + 1] = arr1[i + 1], arr1[i]
print("Sắp xếp tăng giảm đan xen:", arr1)
#vd4:
def la_so_chinh_phuong(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    arr = n // 2
    while arr * arr > n:
        arr = ((arr + n // arr) // 2)
    return arr * arr == n
n = int(input("Nhập vào số phần tử trong mảng:"))
arr1 = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}:"))
    arr1.append(x)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Bước {i + 1}: {arr}")
        if not swapped:
            break

arr1 = [x for x in arr1 if not la_so_chinh_phuong(x)]
bubble_sort(arr1)
print("Bubble Sort (tăng dần):", arr1)
#vd5:
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
    x = int(input(f"Nhập phần tử thứ {i + 1}:"))
    arr1.append(x)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Bước {i + 1}: {arr}")
        if not swapped:
            break
arr1 = [x for x in arr1 if not la_so_nguyen_to(x)]
bubble_sort(arr1)
print("Bubble Sort (tăng dần):", arr1)
#vd6:
n = int(input("Nhập vào số phần tử trong mảng:"))
arr1 = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}:"))
    arr1.append(x)


