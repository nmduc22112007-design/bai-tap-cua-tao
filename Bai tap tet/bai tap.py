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

def ghi_file(danh_sach, filename="danhsachs.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for hs in danh_sach:
            f.write(f"{hs.ma},{hs.ten},{hs.toan},{hs.van},{hs.anh}\n")

def doc_file(filename="danhsachs.txt"):
    danh_sach = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            ma, ten, toan, van, anh = parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4])
            danh_sach.append(HocSinh(ma, ten, toan, van, anh))
    return danh_sach

def sap_xep_chen(danh_sach):
    for i in range(1, len(danh_sach)):
        key = danh_sach[i]
        j = i - 1
        while j >= 0 and danh_sach[j].tong_diem < key.tong_diem:
            danh_sach[j + 1] = danh_sach[j]
            j -= 1
        danh_sach[j + 1] = key
    return danh_sach

def xet_giai(danh_sach):
    giai_quy_dinh = [("Giải Đặc Biệt", 1), ("Giải Nhất", 2), ("Giải Nhì", 4),
                     ("Giải Ba", 6), ("Giải Khuyến Khích", 10)]

    index = 0
    for giai_name, so_luong in giai_quy_dinh:
        for _ in range(so_luong):
            if index < len(danh_sach):
                danh_sach[index].giai = giai_name
                index += 1

def in_ket_qua(danh_sach):
    print("\n" + "=" * 70)
    print("DANH SÁCH HỌC SINH ĐẠT GIẢI")
    print("=" * 70)
    for hs in danh_sach:
        if hs.giai != "Không có giải":
            print(f"{hs.ma:<10} | {hs.ten:<20} | {hs.tong_diem:<10.2f} | {hs.giai}")

def tim_max_diem(danh_sach):
    max_diem = max(hs.tong_diem for hs in danh_sach)
    print("\n" + "=" * 70)
    print("HỌC SINH CÓ TỔNG ĐIỂM CAO NHẤT")
    print("=" * 70)
    for hs in danh_sach:
        if hs.tong_diem == max_diem:
            print(f"{hs.ma:<10} | {hs.ten:<20} | {hs.tong_diem:<10.2f}")
if __name__ == "__main__":
    danh_sach = nhap_hoc_sinh()
    ghi_file(danh_sach)
    danh_sach = doc_file()
    tim_max_diem(danh_sach)
    danh_sach = sap_xep_chen(danh_sach)
    xet_giai(danh_sach)
    in_ket_qua(danh_sach)