class HocSinh:
    def __init__(self, ma, ten, toan, van, anh):
        self.ma = ma
        self.ten = ten
        self.toan = toan
        self.van = van
        self.anh = anh
        self.tong_diem = (toan + van) * 2 + anh
        self.giai = "Không có giải"

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
def tim_min_diem(danh_sach):
    min_diem = min(hs.tong_diem for hs in danh_sach)
    print("\n" + "=" * 70)
    print("HỌC SINH CÓ TỔNG ĐIỂM THẤP NHẤT")
    print("=" * 70)
    for hs in danh_sach:
        if hs.tong_diem == min_diem:
            print(f"{hs.ma:<10} | {hs.ten:<20} | {hs.tong_diem:<10.2f}")

danh_sach = nhap_hoc_sinh()
ghi_file(danh_sach)
danh_sach = doc_file()
tim_min_diem(danh_sach)
