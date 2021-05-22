def isNumber(str):
     return any(char.isdigit() for char in str)
name = input("Nhập tên: ")
while isNumber(name):
    name = input("nhập lại tên: ")
age = (input("Nhập tuổi: "))
while not age.isdigit:
        age= (input("nhập lại tuổi: "))
arr = name.split()
name = " ".join(arr)
name = (name.lower()).title()
print(name)
print(age)
