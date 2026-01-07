
def cau1():
    n = input("Nhap 1 chuoi ky tu:")
    print(f"Viết thường:{n.lower()}")
    print(f"Viết hoa: {n.upper()}")
    print(f"Số lần xuất hiện của ký tự a và t lần lượt là {n.lower().count("a")} và {n.lower().count("t")}")
    print(f"Số ký tự số trong chuỗi là: {sum(1 for c in n if c.isdigit())}")
    print(f"Số ký tự chữ trong chuỗi là: {sum(1 for c in n if c.isalpha())}")
    print(f"Số từ có trong chuỗi là: {len(n.split())}")
def cau2():
    n = int(input("Nhập n:"))
    def tong_chu_so(n):
        n = abs(n)
        if n < 10:
            return n
        return n % 10 + tong_chu_so(n // 10)
    print(tong_chu_so(n))
def cau3():
    n = int(input("Nhap n:"))
    def tong_so_le(n):
        if n < 1:
            return 0
        if n % 2 == 1:
            return n + tong_so_le(n - 2)
        return tong_so_le(n - 1)
    print(tong_so_le(n))
def cau4():
    n = int(input("Nhap n:"))
    arr = []
    for i in range(1, n + 1):
        x = int(input(f"Nhap phan tu thu {i}:"))
        arr.append(x)
    print(f"giá trị lớn nhất trong mảng là {max(arr)}")
    def insertion_sort(arr):
        for i in range(0, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            print(f"Step {i + 1}: {arr}")
            arr[j + 1] = key
    insertion_sort(arr)
    print(f"Insertion Sort (đảo ngược): {arr}")
    if len(arr) >= 3:
        third_max = arr[2]
        vi_tri = [i for i, x in enumerate(arr) if x == third_max]
        print(f"Giá trị lớn thứ ba: {third_max}, vị trí: {vi_tri}")
while True:
    print("\n=============MENU=============")
    print("1. Câu 1: String operations")
    print("2. Câu 2: Sum of digits using recursion")
    print("3. Câu 3: Sum of odd numbers using recursion")
    print("4. Câu 4: Array operations with insertion sort")
    print("5. Câu 5: Student class and file operations")
    print("0. Thoát")
    print(f"{"="*30}")
    n = int(input("Vui lòng chọn 1 số (0-5): "))
    if n == 1:
        cau1()
    elif n == 2:
        cau2()
    elif n == 3:
        cau3()
    elif n == 4:
        cau4()
    elif n == 5:
        print("Chưa làm")
    elif n == 0:
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại\n")#nah