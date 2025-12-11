n = int(input("Nhập n:"))
def so_nguyen_to(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
def so_nguyen_to_doi_xung(n):
    s = str(n)
    return s == s[::-1]
so_nguyen_to_doi_xung = [x for x in range(2, n + 1) if so_nguyen_to(x) and so_nguyen_to_doi_xung(x)]
print(f"Số nguyên tố đối xứng nhỏ hơn hoặc bằng {n} là: {so_nguyen_to_doi_xung}")