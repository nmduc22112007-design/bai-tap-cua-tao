#bai 1
#bai 2
#bai 3
#bai 4
#bai 5
#bai 6
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
print("Selection sort result:", arr1)
#bai 7
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
#bai 8
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
        print(f"Step {i + 1}: {arr}")
        if not swapped:
            break
bubble_sort(arr1)
print("Bubble Sort (tăng dần):", arr1)
#bai 9
#bai 10
#bai 11
#bai 12