import json

# student = {
#     "name": "Alice",
#     "age": 22,
#     "is_student": True,
#     "courses": ["Math", "Science"]
# }

# y=json.dumps(student)

# print(y)


student = {"name": "Alice", "age": 22, "is_student": True}

with open('student.json','w') as file:
    json.dump(student,file)

print("Successfully saved")
# with open("student.json","r") as file:
#     data=json.load(file)
    
# print(data)
# print("Json data with the List or array:")
# print("student Marks: ",data["marks"])
# print("Student Address:",data["addresses"]["city"])
