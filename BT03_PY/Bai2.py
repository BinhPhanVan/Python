import json
students = {
    "001":{
        "fullname": "Phan Văn Bình",
        "class" :"19TCLC_DT4",

    },
    "002":{
        "fullname": "NTLLASLA",
        "class" :"19TCLC_DT2",
        
    }
}
print(students)
#đọc dữ liệu file json
with open("students.json", "w") as f: # w= db
    json.dump(students, f, indent=4)
with open("students.json", "r") as f: # w= db
    data= json.load(f)
print(data)
#json handle in python
