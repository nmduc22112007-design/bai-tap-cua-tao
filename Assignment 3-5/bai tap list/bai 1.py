n = int(input("Nhập vào số phần tử trong list:"))
lst = []
for i in range(n):
    lst.append(int(input(f"Nhập vào phần tử thứ {i+1} trong list:")))
x = int(input(f"Thêm 1 phần tử vào list:"))
lst.append(x)
print(lst)
k = int(input("Nhập giá trị k:"))
count = lst.count(k)
print(f"giá trị {k} xuất hiện {count} lần")
lst.sort()
print(lst)
lst.clear()
print(lst)