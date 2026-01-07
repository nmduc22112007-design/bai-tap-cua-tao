n = input("Nhập 1 chuỗi ký tự:")
print(f"Viết thường:{n.lower()}")
print(f"Viết hoa: {n.upper()}")
print(f"Số ký tự số trong chuỗi là: {sum(1 for c in n if c.isdigit())}")
print(f"Số ký tự chữ trong chuỗi là: {sum(1 for c in n if c.isalpha())}")
print(f"Số lần xuất hiện của ký tự 'a' và 't' lần lượt là {n.lower().count("a")} và {n.lower().count("t")}")
words = [w for w in n.split('_') if w]
print(f"Số từ có trong chuỗi là: {len(words)}")
