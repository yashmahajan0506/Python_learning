st="yash mahajan "
age=20
marks=30

print("Name is :"+st+ "Age is:",age,"marks is :",marks)

print("My name is {} My age is {} my marks is ".format(st,age,marks))

# print(st.upper())
# print(st.lower())
# print(st.count('a'))
# print(st.isprintable())

# print()


def func(list):
    return len(list)

ls1=map(func,('yash','sujal','dhsruv'))
print(ls1)