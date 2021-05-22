import math
def palindrome(number):
    temp = str(number)[::-1]
    if temp == str(number):
        return True
    else:
        return False
left, right = int(input("Start: ")), int(input("End: "))
arr = []
for index in range(left, right+1):
    if(palindrome(index) and palindrome(int(math.sqrt(index))) and int(math.sqrt(index))==math.sqrt(index) ):
        arr.append(index)
print("Kết quả: ",arr)