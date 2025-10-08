class op:
    def __init__(self,num):
        self.num=num
        
    def __add__(self,obj):
        return self.num+obj.num 
    
    def __sub__(self,obj):
        return self.num-obj.num
o=op(100)
o1=op(200)
print(o+o1)
print(o1-o)
