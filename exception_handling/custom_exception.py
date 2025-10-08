   
def add(a,b):
    if b==0:
        raise ValueError("Can't be divided by zero")
    return a / b

try :
    add(5,0)
except ValueError as e:
    print("caught Exception ",e)