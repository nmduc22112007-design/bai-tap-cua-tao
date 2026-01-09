class Oto:
    def __init__(self, ma_xe, ten_xe, gia_ban, so_luong, hsx):
        self.ma_xe = ma_xe
        self.ten_xe = ten_xe
        self.gia_ban = gia_ban
        self.so_luong = so_luong
        self.hsx = hsx
        self.tong_tien = gia_ban * so_luong
def nhap_sach():
    n = int(input("Nhập số lượng xe ô tô:"))
    danh_sach = []
    for i in range(n):
        print(f"Nhập thông tin cho chiếc oto thứ {i+1}:\n")
        ma_xe = input("Nhập mã xe:")
        ten_xe = input("Nhập tên xe:")
        gia_ban = round(0),float(input("Nhập giá bán:"))
        so_luong = round(0),float(input("Nhập số lượng oto:"))
        hsx = input("Nhập tên nhà xuất bản:")
        danh_sach.append(Oto(ma_xe, ten_xe, gia_ban, so_luong, hsx))
    return danh_sach
def ghi_file(danh_sach, filename="danhsachxe.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for Oto in danh_sach:
            f.write(f"{Oto.ma_xe}, {Oto.ten_xe}, {Oto.gia_ban}, {Oto.hsx}\n")
def doc_file(filename="danhsachxe.txt"):
    danh_sach = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            ma_xe, ten_xe, gia_ban, so_luong, hsx = parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4])
            danh_sach.append(Oto(ma_xe, ten_xe, gia_ban, so_luong, hsx))
    return danh_sach
def in_ket_qua(danh_sach):
    print("\n" + "=" * 50)
    print("Xe oto co tong tien lon nhat")
    print("=" * 50)
    for Oto in danh_sach:
        if max(danh_sach):
            print("Ma xe:", Oto.ma_xe)
            print("Ten xe:", Oto.ten_xe)
            print("Gia ban xe:", Oto.gia_ban)
            print("So luong xe:", Oto.so_luong)
            print("Tong tien gia tri:", Oto.tong_tien.round(0))
if __name__ == '__main__':
    danh_sach = nhap_sach()
    ghi_file(danh_sach)
    in_ket_qua(danh_sach)
