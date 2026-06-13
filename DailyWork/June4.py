# list:- 
# append:- add elements at the end 
# l=[1,2,3,4,5,6,7]
# l.append(12)
# print(l)
# # extend:- add multiple elements 
# l.extend([8,9,10,11])
# print(l)
# # insert:- add elements at specific index 
# l.insert(2,20)
# print(l)

# # remove:- 
# l.remove(2)
# print(l)
# # pop:- 
# l.pop(1)
# print(l)
# # clear:- 
# # l.clear()

# # searching and sorting 
# # index()
# print(l.index(10))
# # count()
# print(l.count(6))

# # sorting and reversing 
# b=[4,5,6,7,9,8,7,6,5,4,1,2,3,4]
# # b.sort()
# # print(b)

# # b.reverse()
# # print(b)

# b.sort(reverse=True)
# print(b)

# # len()
# print(len(b))

# print(max(b))
# print(min(b))

# b.clear()
# l.clear()
# print(b,l)


# tuple:-
# count()
# index()
# t=(1,2,3,4,5,6,7,8,9)
# print(t.count(3))
# print(t.index(5))


# set:- 
# s={1,2,3,4,5,6,7}
# add()
# s.add(8)
# print(s)
# update()
# s.update([9,10,11,12])
# print(s)
# remove()
# s.remove(4)
# print(s)
# discard()
# s.discard(12)
# print(s)

# s.remove(23)
# print(s)

# s.discard(23)
# print(s)

# union 
# a={1,2,3,4}
# b={3,4,5,6}
# print(a.union(b))
# intersection 
# print(a.intersection(b))
# difference 
# print(a.difference(b))

# clear()
# s.clear()
# print(s)


# dictionary 
# d={"name":"sakshi","age":25,"marks":100}
# keys 
# print(d.keys())
# print(d.values())
# print(d.items())

# print(d.get("age"))
# d.update({"age":29})
# print(d)
# pop()
# d.pop("age")
# print(d)
# d.pop()
# print(d)
# clear()
# d.clear()
# print(d)





# functions:- 
# def funct_name(parameter):
    # block of code 
# calling function 


# def add(a,b):
#     r=a+b
#     return r 
# print(add(12,13))

# def add(a,b):
#     r=a+b
#     print(r)
# a=int(input("enter any number: "))
# b=int(input("enter any number: "))
# add(a,b)


# type of arguments:- 
# 1. required positional arguments 
# def info(name,age,marks):
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"marks: {marks}")
# info("sakshi",25,90)

# 2. default arguments
# def info(name,age,marks=90):
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"marks: {marks}")
# info("sakshi",25)
# 3. keyword argument 
# def info(name,age,marks):
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"marks: {marks}")
# info(name="sakshi",age=25,marks=90)
# 4. arbitrary argument(*args)
# def info(name,age,*marks):
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"marks: {marks}")
# info("sakshi",25,90,89,98,90,98)
# 5. arbitrary keyword argument(**kwargs)
# def info(name,age,**marks):
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"marks: {marks}")
# info("sakshi",25,p=90,c=89,m=98,e=90,cs=98)

# scope of variables 
# local scope 
# def info():
#     a=12 
#     print(a)
# info()
# print(a)
# global scope 
# a=12
# def info():
#     global a 
#     a=14
#     print(a)
# info()
# print(a)
# enclosed /nonlocal scope 
# def outer():
#     a=12 
#     print(a)
#     def inner():
#         nonlocal a
#         a=14
#         print(a)
#     inner()
# outer()

# lambda function :
# var=lambda parameter:expression 
# add=lambda a,b:a+b
# print(add(12,13))

# map 
# l=[1,2,3,4,5,6,7,8,9,10]
# sq=list(map(lambda a:a**2,l))
# print(sq)

# filter 
# even=list(filter(lambda a:a%2==0,l))
# print(even)

# reduce 
# from functools import reduce 
# total=reduce(lambda a,b:a+b,l)
# print(total)