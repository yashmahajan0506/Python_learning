class Emp:
    compamy="Wanbuffer"

    # def __init__(self,name):
    #     self.name=name
    
    @classmethod
    def change_company(cls,new_name):
        cls.compamy=new_name

    
e1=Emp()
print(Emp.compamy)
Emp.change_company("Google")
print("After Changing it ")
print(Emp.compamy)

        
        