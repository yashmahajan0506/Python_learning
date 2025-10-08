# single Level inheritance:- 

class animal:
    def __init__(self,name,size):
        self.name=name
        self.size=size
    
    def func_animal(self):
        print(f"The name of the animal is :{self.name}")
        print(f"The name of the animal is :{self.size}")

class cow(animal):
    def func_animal(self):
        return super().func_animal()
    
c1=cow("Dev","12cm")
c1.func_animal()
# print(c1)