n = int(input("Nhập vào số phần tử trong mảng: "))
def so_doi_xung(num):
    s = str(num)
    return s == s[::-1]
while so_doi_xung(n) == True:
    print(f"{n} là số đối xứng")
    x = input("Bạn có muốn tiếp tục không?(vui lòng chọn có hoặc không):")
    if not "có":
        print("Cảm ơn!")
        break
else:
    print(f"{n} không phải là số đối xứng")
