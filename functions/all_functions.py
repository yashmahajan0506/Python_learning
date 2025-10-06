import math,os

module=math.sqrt(49)

# module_2=math.pow(2,4)
# print(round(module))
# path=os.system()
# print(path)
# Function to check prime number, Lambda functions
# Python modules (math, datetime, os)

# num=2
# lambda_function= lambda a,b : a+b
# print("the sum is ",lambda_function(1,2))

# prime_number:- 
def prim_number(num):
    if num<=1:
        print("the number is not prime number:")
    else:
        for i in range(2,num):
            if num % i==0:
                return "The number is not Prime Number"
                # break
        else:
           return "The number is prime number"

func=prim_number(11)
print(func)
            


