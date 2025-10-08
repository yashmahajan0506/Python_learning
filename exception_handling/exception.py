# try:
#     res=10/0
#     "yash mahajn "    
# except ZeroDivisionError:
#     print("Can't Divide By zero")
# except ValueError:
#     print("Not Proper Value")
# except IndentationError:
#     print("Not properrly indented")
# except ValueError:
#     print("Value Erro:")
# except TypeError:
#     print("")

# finally:
#     print("Excuted ")
    
def add(a,b):
    if b==0:
        raise ValueError("Can't be divided by zero")
    return a / b

try :
    add(5,0)
except ValueError as e:
    print("caught Exception ",e)