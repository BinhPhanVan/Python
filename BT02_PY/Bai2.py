register ={}
number_register = int(input())
for i in range(number_register):
    tmp = input()
    arr = tmp.split()
    name, subject = " ".join(arr[1::-1]), arr[-1]
    if name in register:
        register[name] = set()
    register[name].add(subject)
for i in register:
    print(i.name, subject)