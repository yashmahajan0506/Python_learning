#diamon-shaped 
class a():
    def show(self):
        print("this is A parent class")
class b(a):
    def show(self):
        print("this is b Class ")
class c(a):
     def show(self):
         print("this is class")
class d(b,c):
    pass

d1=d()
d1.show()