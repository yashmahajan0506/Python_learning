# Create a dictionary of employees with (name, role, salary). Print only salaries > 30k.
# Create a tuple of 5 elements, try modifying it, and note the error.

# Write a program to swap two numbers without a third variable.
# Reverse a string without using slicing.
# Print current date in format YYYY-MM-DD.
# Function with **kwargs to print employee details.
# Write a lambda function to filter even numbers from a list.
# Create a class Product with fields: name, price. Add method to apply discount.Inherit Electronics from Product, add warranty period.Create 3 different product objects and print final price after discount.
# Create Shape base class with method area(). Inherit Circle and Rectangle with their own area() implementation.
# Create a class method (@classmethod) to count number of objects created.

# Store student data in JSON
# Export student data to CSV.
# Build Student CRUD app in Python
# Write a generator that yields even numbers up to 100.
# Create a decorator to log function execution time.
# Create a custom iterator that returns numbers 1–5.
# Write a dictionary comprehension to map numbers 1–5 to their squares.
# Use regex to extract all email addresses from a string.
# Convert Python dict into JSON and save to file.
# Read a CSV of employees (id, name, salary) and print those with salary > 50k.


# def kwarg_fucntionn (**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)

# kwarg_fucntionn(name="yash",age=21)

# import datetime

# today_date=datetime.datetime.today()
# new_date=today_date.strftime("%y-%m-%d")
# print(new_date)


# Create a class method (@classmethod) to count number of objects created.

class count_object:
    count=0
    
    def __init__(self):
          count_object.count+=1
          
    @classmethod 
    def class_method(cls):  
            return cls.count

cm=count_object()
cm2=count_object()
cm3=count_object()


print(cm.class_method())


# dict1={'name':"yash","mobile_no":13333333}

# print(dict1["age"])






