n = int(input("Nhap vao 1 so nguyen: "))
#cau a:
if n& 7 == 0:
    print("n la so chia het cho 7")
else:
    print("n khong phai la so chia het cho 7")
#cau b:
m = 0
for i in range(0, n+1):
    if i % 2 == 0:
        m += i
print(m)
#CAU B THU 2
def sum(n):
    if n < 1:
        return 0
    if n % 2 == 0:
        return sum(n-1)
    else:
        return n + sum(n-2)
print(sum(n))
#cau c:
def giai_thua(n):
    if n ==0:return 1
    return n * giai_thua(n-1)
print(giai_thua(n))