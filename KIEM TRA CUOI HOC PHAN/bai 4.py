n = int(input("Nhap n:"))
arr = []
for i in range(n):
    x = int(input(f"Nhap phan tu thu {i + 1}:"))
    arr.append(x)
def tong(arr):
    if i < 0:
        print(x for x in range(n))
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
bubble_sort(arr)
print("bubble sort (tang dan):", arr)
