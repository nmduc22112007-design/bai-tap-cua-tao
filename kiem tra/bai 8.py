n = int(input("Nhập n:"))
print("Hình 1:")
for i in range(1,n+1):
    print("*"*i)
print("Hình 2:")
for i in range(1,n+1):
    if i == 1 or i == 2 or i == n:
        print(" " * (n - i) + "* " * i)
    elif i == 3:
        print(" "*(n-i)+ "*"+ " "*i +"*")
    elif i == 4:
        print(" " * (n - i) + "*" + " " * (i+1) + "*")
    else:
        print(" "*(n-i)+ "*" + " "*(i+i-3) + "*")