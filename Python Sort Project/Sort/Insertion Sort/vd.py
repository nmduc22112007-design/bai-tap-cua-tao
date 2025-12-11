def insertion_sort(arr):
    for i in range(0,len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        print(f"Step {i+1}: {arr}")
        arr[j+1] = key
arr2 = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr2)
print(f"Insertion Sort: {arr2}")
