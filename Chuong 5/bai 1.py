#viet 1 chuong trinh co chuc nang sau:
#1. Cho nguoi dung nhap vao 1 so nguyen
# neu chon so 1 thi thuc hien thong bao cho ndung nhap vao sl sinh vien moi
#sau do lan luot nhap cac thong tin cho sv do gom ma sv, ho ten, tuoi, que quan
# neu chon so 2 thi in ra toan bo danh sach sinh vien co tuoi > 19
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
    def thongtinsinhvien():
        file = open("sinh_vien.txt","a",encoding="utf-8")
        file.writelines(QuanLySinhVien().danh_sach)
        file.close()
    ql = QuanLySinhVien()
    while True:
        try:
            n = int(input("Nhập 1 (thêm sinh viên), 2 (xem danh sách sinh viên có tuổi > 19) hoặc 0 để thoát chương trình và lưu file: "))
        except ValueError:
            print("Vui lòng nhập 1 hoặc 2")
            continue
        if n == 1:
            ql.nhap_danh_sach()
            thongtinsinhvien()
        elif n == 2:
            ql.hien_thi_tuoi_tren_19()
            thongtinsinhvien()
        elif n == 0:
            break
        thongtinsinhvien()