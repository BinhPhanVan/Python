arr , arr1 = [], []
numbers = int(input("nhap so luong phan tu: "))
for index in range(numbers):
    arr.append(int(input('Nhap so thu %d: ' % (index+1))))
for index in range(numbers):
    arr1.append(sum(arr[:index+1]))
print(arr1)