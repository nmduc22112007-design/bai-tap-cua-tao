def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
numbers = [3,1,2,5,9,4,6,8,7]
index = linear_search(numbers,7)
result = next()
print("Found at index:", index)