n = int(input("Nhập n:"))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}:"))
    arr.append(x)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
selection_sort(arr)
def binary_search(arr,target):
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
result = binary_search(arr,9)
print("Found at index:" if result != -1 else "Not found", result)