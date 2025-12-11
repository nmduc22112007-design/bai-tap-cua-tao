def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr1 = [25,7,9,1,3]
selection_sort(arr1)
print("Selection sort:",arr1)
#btvn: Nhập n là số phần tử trong mảng, sau đó nhập lần lượt nhập các phần tử
# yêu cầu: sắp xếp lại mảng theo thuật toán sắp xếp chọn(selection sort)
# in kết quả sau mỗi bước làm
# bài 2: tương tự bài 1 nhưng sắp xếp theo thứ tự giảm dần
# bài 3: tương tự bài 1 nhưng đã kiểm tra và bỏ hết các số nguyên tố xuất hiện
# lưu ý: bỏ trước rồi ms sắp xếp
# bài 4: tương tự bài 1 nhưng trước khi sắp xếp thì bỏ hết các số hoàn hảo ra rồi ms sắp xếp tăng dần
