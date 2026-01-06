class Sach:
    def __init__(self, ma_sach, ten_sach, don_gia, so_luong, nxb):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.nxb = nxb
        self.tong_tien = don_gia * so_luong
def nhap_sach():
    n = int(input("Nhập số lượng sách:"))
    danh_sach = []
    for i in range(n):
        print(f"Nhập thông tin cho cuốn sách thứ {i+1}:\n")
        ma_sach = input("Nhập mã sách:")
        ten_sach = input("Nhập tên sách:")
        don_gia = float(input("Nhập đơn giá:"))
        so_luong = float(input("Nhập số lượng sách:"))
        nxb = input("Nhập tên nhà xuất bản:")
        danh_sach.append(Sach(ma_sach, ten_sach, don_gia, so_luong, nxb))
    return danh_sach
def ghi_file(danh_sach, filename="danhsachsach.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for Sach in danh_sach:
            f.write(f"{Sach.ma_sach}, {Sach.ten_sach}, {Sach.don_gia}, {Sach.nxb}\n")
def doc_file(filename="danhsachsach.txt"):
    danh_sach = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            ma_sach, ten_sach, don_gia, so_luong, nxb = parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4])
            danh_sach.append(Sach(ma_sach, ten_sach, don_gia, so_luong, nxb))
    return danh_sach
def in_sach(danh_sach):
    print("\n" + "=" * 50)
    print("Danh sach sach co tong tien > 3000000:")
    print("=" * 50)
    for Sach in danh_sach:
        if Sach.tong_tien > 3000000:
            print("Ma sach:", Sach.ma_sach)
            print("Ten sach:", Sach.ten_sach)
            print("Don gia sach:", Sach.don_gia)
            print("So luong sach:", Sach.so_luong)
            print("Tong tien sach:", Sach.tong_tien)
        else:
            print("Khong co cuon sach nao co tong tien lon hon 3000000")
if __name__ == '__main__':
    danh_sach = nhap_sach()
    ghi_file(danh_sach)
    in_sach(danh_sach)
