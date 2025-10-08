# iterator :-  

# number=[1,2,4,5,6]

# iterator=iter(number)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


#genarator:- 

def count_up_to(n):
    # num = 1
    # while num <= n:
    #     yield num
    #     num += 1
    for i in range(n):
        yield i

for i in count_up_to(6):
    print(i)