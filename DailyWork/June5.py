# oops:- object oriented programming language 
# class:- class is a blueprint or template for creating objects
# classes are created by class keyword 
# attributes:- variables inside the class
# methods:- functions inside the class 

# objects:- objects are instances of a class
# objects are created by calling the class as a function

# state:- attributes of an object at a given time
# behavior:- methods of an object which defines its behavior
# identity:- unique identifier for an object
# unique name to an object and enables one object 
# to interact with other object 

# how to create class :- 
# class class_name:
    # class body 
    # attributes
    # methods
    # concrete method / constructor method 
    # instance attribute 
# object creation
# method calling 

# creating a class for students 
# class Student:
#     def __init__(self,Id,name,age,marks):
#         self.Id=Id 
#         self.name=name
#         self.age=age
    #     self.marks=marks
    # def info(self):
    #     print(f"id: {self.Id}")
    #     print(f"name: {self.name}")
        # print(f"age: {self.age}")
        # print(f"marks: {self.marks}")
# object creation:- 
# s1=Student(101,"abc",20,90)
# method calling 
# object.method_name()
# s1.info()  

# Vehicle 
# Bird 
# Animal 
# Cricket 
# Banking 

# polymorphism:- poly:- many 
# morphism:- forms 
# operator polymorphism :-
# + operator:- 
# print(12+14)    # addition 
# print("hello "+"python")        #concatenation 

# functional polymorphism:- 
# len()
# l=[1,2,3,4,5,6,7,8,9]
# print(len(l))
# s="hello python"
# print(len(s))

# method overriding:- 
# class Shape:
#     def area(self):
#         pass 
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r 
#     def area(self):
#         return 3.14*(self.r**2)
# class Rectangle(Shape):
#     def __init__(self,l,w):
#         self.l=l
#         self.w=w 
#     def area(self):
#         return self.l*self.w
# object 
# r=Rectangle(12,19)
# c=Circle(4)
# method calling 
# print(c.area())
# print(r.area())


# method overloading:- 
# class Calculator:
#     def add(self,*a):
#         return sum(a)
# cal=Calculator()
# print(cal.add(1,2))
# print(cal.add(1,2,3))
# print(cal.add(1,2,3,4))
# print(cal.add(1,2,3,4,5))
# print(cal.add(1,2,3,4,5,6))

# recursion:- function calls itself directly or indirectly to solve the problem 
# by breaking it down into smaller and manageable subproblems 

# base case:- stopping condition for recursion to prevent infinite calls 

# recursive case:- the block of code where the function  executes 
# its logic and calls itself 

# def fact(n):
    # base case 
    # if n==0 or n==1:
    #     return 1
    # recursive case 
    # else:
    #     return n*fact(n-1)
# print(fact(5))

