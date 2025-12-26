n = int(input("Nhập n:"))
for i in range(1,n+1):
    if i == 3:
        print(" "*(n-i)+"*" + " "*i +"*")
    elif i == 4:
        print(" " * (n - i) + "*" + " " * (i+1) + "*")
    else:
        print(" "*(n-i)+"* "*i)