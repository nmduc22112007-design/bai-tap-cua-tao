class SinhVien:
    def __init__(self, ma_sv, ho_ten, tuoi, que_quan):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.que_quan = que_quan

    def __str__(self):
        return f"Mã: {self.ma_sv}, Họ tên: {self.ho_ten}, Tuổi: {self.tuoi}, Quê quán: {self.que_quan}"


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def nhap_danh_sach(self):
        n = int(input("Nhập số lượng sinh viên: "))
        for i in range(n):
            print(f"\nNhập thông tin sinh viên {i + 1}:")
            ma_sv = input("Mã sinh viên: ")
            ho_ten = input("Họ tên: ")
            tuoi = int(input("Tuổi: "))
            que_quan = input("Quê quán: ")
            sv = SinhVien(ma_sv, ho_ten, tuoi, que_quan)
            self.danh_sach.append(sv)

    def hien_thi_tuoi_tren_19(self):
        print("\nDanh sách sinh viên có tuổi trên 19:")
        found = False
        for sv in self.danh_sach:
            if sv.tuoi > 19:
                print(sv)
                found = True
        if not found:
            print("Không có sinh viên nào có tuổi trên 19")


if __name__ == "__main__":
    ql = QuanLySinhVien()  # tạo một lần, bên ngoài vòng lặp
    while True:
        try:
            n = int(input("Nhập 1 (thêm SV), 2 (xem SV tuổi > 19) hay 0 (thoát): "))
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
            continue

        if n == 1:
            ql.nhap_danh_sach()
        elif n == 2:
            ql.hien_thi_tuoi_tren_19()
        elif n == 0:
            break
        else:
            print("Lựa chọn không hợp lệ")