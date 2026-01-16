
def tong(n):
    if n < 10:
        return n
    else:
        return tong(n//10) + n%10
while True:
    try:
        n=int(input())
        if n<0:
            print("....")
        else:
            print(tong(n))
            break
    except ValueError:
        print("khong hop le")
