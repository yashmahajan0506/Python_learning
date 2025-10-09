   
# def add(a,b):
#     if b==0:
#         raise ValueError("Can't be divided by zero")
#     return a / b

# try :
#     add(5,0)
# except ValueError as e:
#     print("caught Exception ",e)

# Custom Exception – Negative Age:
# Raise a custom exception if the user enters an age less than 0
class Negativeagerror (Exception):
    pass 
try:
    age= int(input("Enter your Age:"))
    if age <= 0:
        raise Negativeagerror ("The age shouldn't be Zero or less then Zero")
except Negativeagerror as e :
    print(e)
except ValueError:
    print("Enter Proper Type of Value")

else:
    print("Your age is :",age)
finally:
    print("Program excuted:")

    