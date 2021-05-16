#Câu1
def is_palindrome(str):
    return (str==str[::-1])
str = input("Nhap chuoi kiem tra:  ")
print("Kết quả: " ,is_palindrome(str))