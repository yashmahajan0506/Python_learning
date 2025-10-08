class string:
    
    def __init__(self,id,name):
            self.id=id
            self.name=name
    def __str__(self):
          return f"Id is :{self.id},Name is :{self.name}"


s1=string(1,"yash")
print(s1)