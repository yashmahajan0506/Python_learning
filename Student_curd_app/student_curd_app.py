student=[]

def create_student():
    id=int(input("Enter Student id:"))
    name=input("Enter student name: ")
    age=int(input("Enter student age: "))
    student.append({"id":id,"name":name,"age":age})
    print("Student created successfully")

def update_student():
    id =int(input("Enter the id to update student:"))
    for i in student:
        if i["id"] == id:
            i['name'] = input("Enter new name: ")
            i['age'] = int(input("Enter new age: "))
            print("student updated")
            
def delete_student():
    for i in student:
                 student.remove(i)
                 print("Studnet Deleted Sucessfully!")
    
def read_student():
    
    if not student:
        print("Student not found:")
    else:
        for i in student:
            print(i)
def menu():
    while True:
        print("1. Create Student")  
        print("2. Update Student")
        print("3. Read Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1: 
            create_student()
        elif choice == 2:
            update_student()
        elif choice == 3:
            read_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            break
        else:
             print("Invalid choice")
menu()

    