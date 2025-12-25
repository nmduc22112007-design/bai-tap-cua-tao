n = int(input("Nhập n:"))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i +1}:"))
    arr.append(x)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
        print(f"Step {i+1}: {arr}")
selection_sort(arr)
print("Selection sort result:", arr)