def myfucntion(n):
    return lambda a :a*n

mydoubler=myfucntion(2)

# print(mydoubler(3))

# square=lambda a:a*a

# print(square(11))


# Use filter() with a lambda to find all even numbers from [1, 2, 3, 4, 5, 6, 7, 8].
# list1=[1,2,3,4,5,6]


# var=filter(lambda x:x % 2==0,list1 )

# print(list(var))

# Use a lambda to get the square of each element in [1, 2, 3, 4, 5] using map().
list1=[1,2,3,4,5,6]

f = map(lambda x: x**2,list1)
 
print(list(f))


# Write a lambda function that checks if a string starts with the letter 'A'.
#so it should return true if the name is starting from A


# check_A = lambda s: s.startswith('A')
# print(check_A("Ashish"))

# Use filter() and a lambda to extract only numbers greater than 10 from [3, 12, 9, 15, 7, 20].

numebers=[3, 12, 9, 15, 7, 20]

filterd_items=filter(lambda x: x >10 ,numebers)

print(list(filterd_items))


# Given names = ['John', 'alice', 'Bob', 'carol'], use a lambda with map() to capitalize all names properly (first letter uppercase).

ls1=['John', 'alice', 'Bob', 'carol']
filterd_elements=map(lambda s : s.isupper(),ls1)

print(list(filterd_elements))

#Use reduce() and a lambda to find the product of all numbers in [1, 2, 3, 4, 5].

from functools import reduce
ls2=[1, 2, 3, 4, 5]
reduce_item=reduce(lambda x,y:x+y,ls2)
print(reduce_item)