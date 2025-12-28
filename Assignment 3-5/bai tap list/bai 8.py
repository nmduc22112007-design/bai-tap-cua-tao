import random
n = int(input("Nhập vào số phần tử trong list:"))
lst = [random.randint(0,10) for i in range(n)]
lst.sort()
def reverse_list(i):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
reverse_list(lst)
print(lst)