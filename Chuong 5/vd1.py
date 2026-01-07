def thongtinsingvien():
    file = open("sv.txt","w",encoding="utf-8")
    file.writelines("BIT123; Nguyen Van B; Thanh Hoa\n")
    file.writelines("BIT124; Nguyen Thi C; Nam Dinh\n")
    file.writelines("BIT125; Nguyen Thanh Tung; 36\n")
    file.close()
thongtinsingvien()