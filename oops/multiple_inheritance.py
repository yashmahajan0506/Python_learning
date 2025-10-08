
class animal:
    def __init__(self,name,size):
        self.name=name
        self.size=size
    
    def func_animal(self):
        print(f"The name of the animal is :{self.name}")
        print(f"The name of the animal is :{self.size}")

class cow():
    # def func_animal(self):
    #     return super().func_animal()
    
    def fun_cow(self):
        print("This is class from cow")

class shark(animal,cow):
    def func_animal(self):
        return super().func_animal()
    def fun_cow(self):
        return super().fun_cow()
    
# c1=cow("Dev","12cm")
s1=shark("Yash","40cm")
s1.func_animal()
s1.fun_cow()