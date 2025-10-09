try:
    x=int(input("Enter the Number: "))
except ValueError:
    print("Invalid Value")
else:
    print("No error here and the number is :",x)
finally:
    print("Executed")
