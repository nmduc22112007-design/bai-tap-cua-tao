n = int((input("Nhập n:")))
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(n*i+j+1, end = " ")
        else:
            print(n*i+n-j, end = " ")
    print()