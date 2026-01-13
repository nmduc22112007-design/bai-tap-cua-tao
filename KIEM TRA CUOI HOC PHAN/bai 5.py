class nhanvien:
    def __init__(self,ma_nhan_vien, ho_ten, luong_co_ban, phu_cap, thuong):
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
            ma_nhan_vien, ten, luong_co_ban, phu_cap, thuong = parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4])
            danh_sach.append(nhanvien(ma_nhan_vien, ten, luong_co_ban, phu_cap, thuong))
    return danh_sach
def tong_thu_nhap_cao_nhat(danh_sach):
    print("\n" + "=" * 50)
    print("Nhân viên có tổng thu nhập cao nhất:")
    print("\n" + "=" * 50)
    for nhanvien in danh_sach:
        if  nhanvien.tong_thu_nhap in danh_sach == max(danh_sach):
            print(nhanvien)
if __name__ == '__ma_nhan_vien__':
    danh_sach = nhap_nhan_vien()
    ghi_file(danh_sach)
    nhap_nhan_vien()