class SinhVien:
    def __init__(self, ma_sv, ho_ten, tuoi, que_quan):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.que_quan = que_quan

    def ghi_file(self):
        return f"{self.ma_sv},{self.ho_ten},{self.tuoi},{self.que_quan}"

    @staticmethod
    def tu_file(dong):
        du_lieu = dong.strip().split(",")
        return SinhVien(
            du_lieu[0],
            du_lieu[1],
            int(du_lieu[2]),
            du_lieu[3]
        )

def chuc_nang_1():
    n = int(input("Nhap so luong sinh vien moi: "))
    with open("thongtinSV.txt", "a", encoding="utf-8") as f:
        for i in range(n):
            print(f"\nNhap sinh vien thu {i + 1}:")
            ma_sv = input("Ma sinh vien: ")
            ho_ten = input("Ho va ten: ")
            tuoi = int(input("Tuoi: "))
            que_quan = input("Que quan: ")

            sv = SinhVien(ma_sv, ho_ten, tuoi, que_quan)
            f.write(sv.ghi_file() + "\n")

    print("\nDa ghi thong tin sinh vien vao file thongtinSV.txt")

def chuc_nang_2():
    print("\nDanh sach sinh vien co tuoi > 19:")

    try:
        with open("thongtinSV.txt", "r", encoding="utf-8") as f:
            for dong in f:
                sv = SinhVien.tu_file(dong)
                if sv.tuoi > 19:
                    print("------------------")
                    print("Ma SV:", sv.ma_sv)
                    print("Ho ten:", sv.ho_ten)
                    print("Tuoi:", sv.tuoi)
                    print("Que quan:", sv.que_quan)
    except FileNotFoundError:
        print("Chua co file thongtinSV.txt")

def menu():
    while True:
        print("\n========== MENU ==========")
        print("1. Nhap va luu thong tin sinh vien")
        print("2. Hien thi sinh vien co tuoi > 19")
        print("0. Thoat")

        chon = input("Nhap lua chon: ")

        if chon == "1":
            chuc_nang_1()
        elif chon == "2":
            chuc_nang_2()
        elif chon == "0":
            print("Thoat chuong trinh!")
            break
        else:
            print("Lua chon khong hop le!")
menu()






#day la cau test lenh