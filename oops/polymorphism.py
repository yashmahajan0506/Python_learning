# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     print(type(self.name))

# p1 = Person("John", 36)


 # print(p1)


# method overiding :- 

# class animal:
#     def speak(self):
#         print("Animal speaks")

# class dog(animal):
#     def speak(self):
#         super().speak()
#         print("Dog barks")

# class cat(dog):
#     def speak(self):
#         super().speak()
#         print("Cat meows")


# c1=cat()
# c1.speak()
 
 
 # Duck Typing:- 
 
 # if it walk like duck ,quack like duck then it's definity a duck :-   ,


class animal :
    def quack(self):
        print("Making quack to duck ")
class person:
    def quack(self):
       print("Making quack to person ")
    
def making_quack(obj):  
    obj.quack()

a1=animal()
making_quack(a1)
    
p1=person()
making_quack(p1)

