import random
n = int(input("Nhập vào số phần tử trong list:"))
lst = [random.randint(0,20) for i in range(n)]
x = int(input(f"Thêm 1 phần tử vào list:"))
lst.append(x)
print(lst)
k = int((input("Nhập số k:")))
lst = [x for x in lst if x != k]
print(lst)
def so_doi_xung(lst):
    return lst == lst[::-1]
if so_doi_xung(lst) == True:
    print(f"List {lst} là 1 list đối xứng")
else:
    print(f"List {lst} không phải là 1 list đối xứng")