class HocSinh:
    def __init__(self, ma, ten, toan, van, anh):
        self.ma = ma
        self.ten = ten
        self.toan = toan
        self.van = van
        self.anh = anh
    def tong_diem(self):
        return self.toan * 2 + self.van * 2 + self.anh
    def __str__(self):
        return f"{self.ma},{self.ten},{self.toan},{self.van},{self.anh}"
def nhap_hoc_sinh():
    n = int(input("Nhập số lượng học sinh: "))
    danh_sach = []
    for i in range(n):
        print(f"\nNhập thông tin học sinh {i + 1}:")
        ma = input("Mã học sinh: ")
        ten = input("Họ tên: ")
        toan = float(input("Điểm Toán (0-10): "))
        van = float(input("Điểm Văn (0-10): "))
        anh = float(input("Điểm Tiếng Anh (0-10): "))
        danh_sach.append(HocSinh(ma, ten, toan, van, anh))
    return danh_sach

def ghi_file(danh_sach, filename="danhsachhocsinh.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for hs in danh_sach:
            f.write(f"{hs.ma},{hs.ten},{hs.toan},{hs.van},{hs.anh}\n")

def doc_file(filename="danhsachhocsinh.txt"):
    danh_sach = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            ma, ten, toan, van, anh = parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4])
            danh_sach.append(HocSinh(ma, ten, toan, van, anh))
    return danh_sach

def tong_diem_thap_nhat(danh_sach):
    print("\n" + "=" * 50)
    print("Hoc sinh co tong diem thap nhat:")
    print("\n" + "=" * 50)
    for HocSinh in danh_sach:
        if  HocSinh.tong_diem in danh_sach == min(danh_sach):
            print(HocSinh)
if __name__ == '__main__':
    danh_sach = nhap_hoc_sinh()
    ghi_file(danh_sach)


