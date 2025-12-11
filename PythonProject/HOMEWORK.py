# Khai báo thông tin cá nhân
Name = "Nguyễn Minh Đức," # tên
Age = int(input("Vui lòng nhập số tuổi:")) # nhập số tuổi
while Age <= 17:
    input("Đủ tuổi chưa mà đòi học đại học? ")
    Age = int(input("Nhập sai thì nhập lại, còn chưa đủ tuổi thì phải chịu:  "))
    ''' Số tuổi chưa đủ --> nhập lại số tuổi'''
print(Name,Age,"tuổi") # print để in ra tên, tuổi
Hometown = "Hải Phòng" # quê quán
print("Quê quán:", Hometown) # print để in ra quê quán
thxt = "Tổ hợp xét tuyển vào CMC:A01" # tổ hợp xét tuyển
print(thxt) # print để in ra tổ hợp xét tuyển
print("Điểm số:", len(thxt)) # print để in ra điểm số