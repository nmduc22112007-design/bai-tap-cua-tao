n = int(input("Nhap n:"))
arr = []
for i in range(1,n+1):
    x = int(input(f"Nhap phan tu thu {i}:"))
    arr.append(x)
print(f"giá trị lớn nhất trong mảng là {max(arr)}")
def insertion_sort(arr):
    for i in range(0,len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j-=1
        print(f"Step {i+1}: {arr}")
        arr[j+1] = key
insertion_sort(arr)
print(f"Insertion Sort (đảo ngược): {arr}")
if len(arr) >= 3:
    third_max = arr[2]
    vi_tri = [i for i, x in enumerate(arr) if x == third_max]
    print(f"Giá trị lớn thứ ba: {third_max}, vị trí: {vi_tri}")#cf
