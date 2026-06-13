# polymorphism:- same name but work differently
# operator polymorphism
# print(10+20) # addition
# print("abc"+"def") # concatenation
# function polymorphism
# list1=[1,2,3,4,5,6,7]
# tuple1=(1,2,3,4,5,6,7)
# print(len(list1)) # 7
# print(len(tuple1)) # 7
# polymorphism in class method 
# method overriding:- when we have same method in parent and child 
# class then it is called method overriding

# method overloading:- when we have same method in same class
# with different parameters then it is called method overloading

# duck typing:- when we have same method in different class then it is called duck typing
# example of duck typing
# class Dog:
#     def speak(self):
#         print("woof")
    
# class Cat:
#     def speak(self):
#         print("meow")

# def talk(animal):
#     print(animal.speak())
# talk(Dog())
# talk(Cat())


# method overriding example
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

# c=Circle(5)
# r=Rectangle(4,5)
# print(c.area()) # 78.5
# print(r.area()) # 20


# method overloading example
# class Calculator:
#     def mul(self, *args):
#         res=1
#         for i in args:
#             res=res*i
#         print(res)

# c=Calculator()
# c.mul(2,3)
# c.mul(2,3,4,5,6,7,8,9)


















































