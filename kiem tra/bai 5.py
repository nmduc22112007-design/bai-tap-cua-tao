n = float(input("Nhập cân nặng(kg):"))
i = float(input("Nhập chiều cao(mét):"))
BMI = n / i**2
print(BMI)
if BMI < 18.5:
    print("Bạn hơi gầy, cần ăn bồi bổ thêm")
elif 18.5 <= BMI < 25:
    print("Cơ thể cân đối")
else:
    print("Bạn đang hơi thừa cân, cần ăn uống lành mạnh hơn")