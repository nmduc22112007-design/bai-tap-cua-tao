def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n: "))
so_nguyen_to = [n for n in range(2, n + 1) if la_so_nguyen_to(n)]
print(f"Các số nguyên tố bé hơn hoặc bằng {n} là:", so_nguyen_to)