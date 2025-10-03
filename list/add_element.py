# #add elements in list:-  
# ls1=[1,2,4,5,5,6,7,1,5,6,88,92,2]


# ls1[0]=0

# print(ls1)
# # ls1[2]=3

# print("list Methods:- ")
# #append
# ap=ls1.append(8)
# print(ls1)

# #index:- 
# insert=ls1.insert(0,56)
# print(ls1)

# #pop item:-  
# pop=ls1.pop()
# print(ls1)

# cnt=ls1.count(5)
# print("The number of list :-  ",cnt)

# sort=ls1.sort()
# print("The sorted list:-",ls1)

# copy_elemet=ls1.copy()
# print(copy_elemet)


# remove=ls1.remove(92)
# print("remove from list:",ls1)

# ls2=[1,2,3,4,5,67]

# extented=ls1.extend(ls2)

# clr=ls1.clear()
# print(ls1)


# def list(ls1):
#     for i in ls1:
#         if i in ls1:
#             return True
    
# ls1=[1,2,4,5,6,7]

# for i in ls1:
#     print(i)
# last_ele=ls1[-1]
# print(last_ele)
# print(ls1)

# ls=ls1.pop(4)
# print(ls1)

#enumrate Function :- 
# print("//////")
# ls1=[1,2,7,4,5,6,3,8]

# for i ,j in enumerate(ls1):
#     print(i,j)



# How do you get a sorted copy of a list without modifying the original?
# shallow_copy=ls1.copy()
# sorted_element=sorted(shallow_copy)
# print(id(ls1))
# print(id(sorted_element))

# remove_elements from list:-  


# ls1=[1,2,7,4,5,6,3,8,1,2,4,5,7]

# empty_list=[]
# for i in ls1:
#     if i not in empty_list:
#         empty_list.append(i)

# print(empty_list)

# ls1=[1,2,3,4,5]

# k=2

# print(ls1[k:]+ls1[:k])


# def rotate_list(lst, k):
#     for i in range(k):
#         last = lst.pop()   
#         lst.insert(0, last) 
#     print(lst)

# print(rotate_list([1, 2, 3, 4, 5], 2))  

#how  to rotate list
# ls1=[1,2,3,4,5,6]

# k=2
# k=k%len(ls1)
# print(ls1[-2:]+ls1[:-2])



# k=2

# for i in range(k):
#     last=ls1.pop()
#     ls1.insert(0,last)
# print(ls1)

# k=2
# k=k%len(ls1)

# otate_list(lst, k):

#     k = k % len(lst)   # to handle cases when k > len(lst)
#     return lst[-k:] + lst[:-k]

# print(rotate_list([1, 2, 3, 4, 5], 2))



# ls1=[1,2,3,4,5,6]

# k=2
# k=k%len(ls1)

# print(ls1[-k:]+ls1[:-k])


# for i in range(k):
#     last=ls1.pop()
#     ls1.insert(0,last)

# print(ls1)