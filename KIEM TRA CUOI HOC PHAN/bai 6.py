print("=============MENU=============")
print("1. Cau 1:")
print("2. Cau 2:")
print("3. Cau 3:")
print("4. Cau 4:")
print("5. Cau 5:")
print("0. Thoat")
def cau1():
    n = int(input("Nhap n:"))
    if n % 5 == 0:
        print(f"{n} la so chia het cho 5")
    else:
        print(f"{n} khong phai so chia het cho 5")
    if n > 0:
        for i in range(1, n + 1):
            if i % 5 == 0:
                print(i)
def cau2():
    n = int(input("Nhap n(n > 0):"))
    if n <= 0:
        n = int(input("Vui long nhap n > 0:"))

    def tong(n):
        if n < 10:
            return n
        else:
            return tong(n // 10) + n % 10

    print(tong(n))
def cau3():
    n = input("Vui long nhap 1 chuoi ky tu:")
    print(f"So ky tu trong chuoi la: {sum(1 for n in n if n.isdigit())}")
    str(n).upper().split()
    print(f"Chuoi sau khi xoa bo toan bo khoang trang va chuyen thanh chuoi viet hoa la: {n}")
def cau4():
    n = int(input("Nhap n:"))
    arr = []
    for i in range(n):
        x = int(input(f"Nhap phan tu thu {i + 1}:"))
        arr.append(x)

    # def tong_so_nguyen_am(n):
    # x = 0
    # for x in arr:
    # if i < 0:
    # x += x
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
def cau5():
    class nhanvien:
        def __init__(self, ma_nhan_vien, ho_ten, luong_co_ban, phu_cap, thuong):
            self.ma_nhan_vien = ma_nhan_vien
            self.ho_ten = ho_ten
            self.luong_co_ban = luong_co_ban
            self.phu_cap = phu_cap
            self.thuong = thuong

        def tong_thu_nhap(self):
            return self.luong_co_ban + self.phu_cap + self.thuong
        def __str__(self):
            return f"{self.ma_nhan_vien},{self.ho_ten},{self.luong_co_ban},{self.phu_cap},{self.thuong}"
def nhap_nhan_vien():
        n = int(input("Nhập số lượng nhân viên: "))
        danh_sach = []
        for i in range(n):
            print(f"\nNhập thông tin nhân viên thứ {i + 1}:")
            ma_nhan_vien = input("Mã nhân viên: ")
            ten = input("Họ tên: ")
            luong_co_ban = float(input("Lương cơ bản:"))
            phu_cap = float(input("Phụ cấp:"))
            thuong = float(input("Thưởng: "))
            danh_sach.append(nhanvien(ma_nhan_vien, ten, luong_co_ban, phu_cap, thuong))
        return danh_sach

def ghi_file(danh_sach, filename="danhsachnv.txt"):
        with open(filename, 'w', encoding='utf-8') as f:
            for nv in danh_sach:
                f.write(f"{nv.ma_nhan_vien},{nv.ten},{nv.luong_co_ban},{nv.phu_cap},{nv.thuong}\n")

def doc_file(filename="danhsachnv.txt"):
        danh_sach = []
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(',')
                ma_nhan_vien, ten, luong_co_ban, phu_cap, thuong = parts[0], parts[1], float(parts[2]), float(
                    parts[3]), float(parts[4])
                danh_sach.append(nhanvien(ma_nhan_vien, ten, luong_co_ban, phu_cap, thuong))
        return danh_sach

def tong_thu_nhap_cao_nhat(danh_sach):
        print("\n" + "=" * 50)
        print("Nhân viên có tổng thu nhập cao nhất:")
        print("\n" + "=" * 50)
        for nhanvien in danh_sach:
            if nhanvien.tong_thu_nhap in danh_sach == max(danh_sach):
                print(nhanvien)
if __name__ == '__ma_nhan_vien__':
    danh_sach = nhap_nhan_vien()
    ghi_file(danh_sach)
    nhap_nhan_vien()
while True:
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
        cau5()
    elif n == 0:
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại\n")