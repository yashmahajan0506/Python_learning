
try :
    # if value != str:
    #     raise ValueError("The value is not valid")
    value=int(input("Enter the value:"))
except ValueError:
    print("The value should be integer")

else:
    print(f"The value is {value}")

finally:
    print("Perfectly executed")
    
    
    