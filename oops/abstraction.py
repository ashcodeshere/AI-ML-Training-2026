# that hides the complex implementation details and shows only essential 
# functionality 

# abstract class:- blueprint class that cannot create objects from it directly

# abstarct method:-  a method declared in abstract class that has no implementation
# (empty body)

# abc module:- provides the necessary structure for defining abstract base class 
# abc:- abstract base class

# calculate shape area 
# from abc import ABC, abstractmethod 

# abstract class 
# class Shape(ABC):
#     @abstractmethod 
#     def area(self):
#         pass 
# concrete subclass 
# class Rectangle(Shape):
#     def __init__(self,l,w):
#         self.l=l
#         self.w=w 
#     def area(self):
#         return self.l*self.w 

# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14*(self.r**2)

# r=Rectangle(4,5)
# c=Circle(3)
# print(r.area())
# print(c.area())





