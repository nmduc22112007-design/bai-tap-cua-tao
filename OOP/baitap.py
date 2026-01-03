#khai báo 1 đối tượng sinh viên gồm các thuộc tính: Mã sinh viên, họ tên, điểm tích lũy.
# Nhập số n t bàn phím l số lượng sinh viên, sau đó lần lượt nhập thông tin cho mã sinh viên.
#Sử dụng thuật toán sắp xếp chèn để sắp xếp laại danh sách sinh viên thep thứ tự giam dần theo điểm tích lũy
class SinhVien:
    def __init__(self, ma_sv, ho_ten, diem_tich_luy):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_tich_luy = diem_tich_luy

    def __str__(self):
        return f"Mã: {self.ma_sv}, Họ tên: {self.ho_ten}, Điểm: {self.diem_tich_luy}"
class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def nhap_danh_sach(self):
        n = int(input("Nhập số lượng sinh viên: "))
        for i in range(n):
            print(f"\nNhập thông tin sinh viên {i + 1}:")
            ma_sv = input("Mã sinh viên: ")
            ho_ten = input("Họ tên: ")
            diem_tich_luy = float(input("Điểm tích lũy: "))
            sv = SinhVien(ma_sv, ho_ten, diem_tich_luy)
            self.danh_sach.append(sv)

    def sap_xep_chen(self):
        # Sắp xếp chèn giảm dần theo điểm tích lũy
        for i in range(1, len(self.danh_sach)):
            key = self.danh_sach[i]
            j = i - 1
            while j >= 0 and self.danh_sach[j].diem_tich_luy < key.diem_tich_luy:
                self.danh_sach[j + 1] = self.danh_sach[j]
                j -= 1
            self.danh_sach[j + 1] = key

    def hien_thi(self):
        print("\nDanh sách sinh viên sau khi sắp xếp:")
        for sv in self.danh_sach:
            print(sv)


# Main
if __name__ == "__main__":
    ql = QuanLySinhVien()
    ql.nhap_danh_sach()
    ql.sap_xep_chen()
    ql.hien_thi()