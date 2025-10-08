class granfather:
    def __init__(self,height_size):
        self.height_size=height_size
        
    def height_gradfather(self):
        print("My height is:",self.height_size)
        
class father(granfather):
    eyes_color="Grey"
    def eyes_father(self):
        print("My eyes of is:",self.eyes_color) 
        
class son(father):
    pass

s1=son("6ft")
s1.height_gradfather()
s1.eyes_father()

