n = int(input("Nhap vao n so phan tu(so nguyen): "))
arr = []
for i in range(0,n):
    x = int(input(f"nhap vao phan tu thu {i+1}: "))
    arr.append(x)
#cau a:
m = 0
for i in range(0, len(arr)):
    m += int(arr[i])
print("tong: ",m)
#cau b:
print("tbc: ",m/n)
#cau c:
print("gia tri lon nhat:",max(arr))
#cau d:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Bước {i+1}: {arr}")
        if not swapped:
            break
bubble_sort(arr)
print("Bubble Sort (giảm dần):", arr)
#cau e:
c = int(input("Nhập vào số cần tìm: "))
def binary_search(arr,target):
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
result = binary_search(arr,c)
print(f"Tìm thấy giá trị {c} ở vị trí thứ:" if result != -1 else "Không tìm thấy", result)
