n = int(input("Nhập vào số phần tử trong mảng: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}:"))
    arr.append(x)
def so_doi_xung(num):
    s = str(num)
    return s == s[::-1]
so_doi_xung = [x for x in arr if so_doi_xung(x)]
print(f"Các số đối xứng trong mảng là {so_doi_xung}")