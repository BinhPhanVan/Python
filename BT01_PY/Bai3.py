import numpy as np
n = int(input("Ma tran vuong n= "))
arr= np.zeros((n,n),dtype=int)
tg=1
for i in range(0,n):
    for j in range(0,n):
        arr[i][j] = tg
        tg+=1
print("Origin:\n",arr)
def rotated(array):
    list_array = zip(*array[::1])
    return [list(elem) for elem in list_array]

print("Rotate 90 counterclockwise:\n",)
arr1=rotated(arr)[::-1]
for i in arr1:
    print(i)

print("Rotate 180 counterclockwise:\n",)
arr2=rotated(arr1)[::-1]
for i in arr2:
    print(i)