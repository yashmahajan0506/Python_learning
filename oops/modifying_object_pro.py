class student:
      
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
     
    def student_information(self):
        print(f"the id of student is {self.id}")
        print(f"the name of student is {self.name}")
        print(f"the marks of student is {self.marks}")
        
s=student(1,'yash',50)

s.student_information()

s.name="sujal"
s.student_information()