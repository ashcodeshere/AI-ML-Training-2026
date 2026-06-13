class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info1(self):
        print(self.name)
        print(self.age)
class student(Person):
    def __init__(self,name,age,marks):
        super.__init__(name,age)
# Pending to complete

# # Multiple Inheritence
# class Father:
#     def __init__(self,height):
#         self.h=height
#     def info1(self):
#         print(f"Height of Father is {self.h}")
# class Mother:
#     def __init__(self,color):
#         self.c=color
#     def info2(self):
#         print(f"Color of Mother is {self.c}")
# class Kid(Father,Mother):
#     def __init__(self, height,color,name):
#         Father.__init__(self,height)
#         Mother.__init__(self,color)   #Why comma????
#         self.name=name
#     def info3(self):
#         print(self.h)
#         print(self.c)
#         print(self.name)
# k1=Kid(161,"Fair","ABC") 
# k1.info1()
# k1.info2()
# k1.info3()


# # Multilevel Classes
# class Grandparent:
#     def gp(self):
#         print("I am Grandpa")
# class Parent(Grandparent):
#     def p(self):
#         print("I am Parent")
# class kid(Parent):
#     def k(self):
#         print("I am Kid")
# k1=kid()
# k1.gp()
# k1.p()
# k1.k()


# # Hybrid Inheriance
# class Vehicle:
#     def vehicle(self):
#         print("Vehicle is moving")
# class Car(Vehicle):
#     def car(self):
#         print("Car is running")
# class Boat(Vehicle):
#     def boat(self):
#         print("Boat is moving on water")
# class ship(Vehicle):
#     def sship(self):
#         print("ship is moving on water")
# class watervehicle(Boat,ship):
#     def waveh(self):
#         print("Water Vehicle")
# wav=watervehicle()
# wav.waveh()
# wav.boat()
# wav.sship()
# wav.vehicle()

# # Hierarchial Inheritance (Home Work to complete)
# class Principal:
#     def princi(self):
#         print("I am Principal")

# Encapsulation - Binding of data functions and methods in a classand restricting their direct access
# Access Modifiers - Public(By Default), Private, Protected(it is traditionally not used in Python)
# getter method and setter method + Name Mangling (for accessing encapsulated methods and data)
