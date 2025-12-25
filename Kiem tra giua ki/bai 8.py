n = int(input("Nhập n:"))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i +1}:"))
    arr.append(x)
def insertion_sort(arr):
    for i in range(0,len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        print(f"Step {i+1}: {arr}")
        arr[j+1] = key
insertion_sort(arr)
print(f"Insertion Sort result: {arr}")