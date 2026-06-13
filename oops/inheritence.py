# super keyword 
# Single Inheritence 
# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age 
#     def display(self):
#         print("Name:",self.n)
#         print("Age:",self.a)
# class Student(Person):
#     def __init__(self,name,age,rollno,marks):
#         super().__init__(name,age)
#         self.r=rollno
#         self.m=marks
#     def display(self):
#         super().display()
#         print("Roll No:",self.r)
#         print("Marks:",self.m)
# s=Student("Alice",20,101,85)
# s.display()
# p=Person("Bob",30)
# p.display()


# multiple Inheritence
# class Father:
#     def __init__(self,height):
#         self.h=height
#     def info1(self):
#         print("Height:",self.h)
# class Mother:
#     def __init__(self,color):
#         self.c=color
#     def info2(self):
#         print("Color:",self.c)
# class Kid(Father,Mother):
#     def __init__(self,height,color):
#         Father.__init__(self,height)
#         Mother.__init__(self,color)
#     def info3(self):
#         print(self.h)
#         print(self.c)
# creating object of Kid class
# k=Kid(150,"Fair")
# k.info3()
# k.info1()
# k.info2()

# Multilevel Inheritence
# class Grandfather:
#     def __init__(self,lastname):
#         self.l=lastname
#     def info1(self):
#         print("Last Name:",self.l)
# class Father(Grandfather):
#     def __init__(self,lastname,middlename):
#         super().__init__(lastname)
#         self.m=middlename
#     def info2(self):
#         super().info1()
#         print("Middle Name:",self.m)
# class Son(Father):
#     def __init__(self, lastname, middlename,firstname):
#         super().__init__(lastname, middlename)
#         self.f=firstname
#     def info3(self):
#         super().info2()
#         print("First Name:",self.f)
#         print("Full Name:",self.f,self.m,self.l)
# s=Son("Mukesh","Nitin","Neil")
# s.info3()


# Heirachical Inheritence
# class Parent:
#     def __init__(self,lastname):
#         self.l=lastname
#     def info1(self):
        # pass
#         print("Last Name:",self.l)
# class Kid1(Parent):
#     def __init__(self,lastname,name1):
#         super().__init__(lastname)
#         self.f=name1
#     def info2(self):
#         super().info1()
#         print("Full Name:",self.f,self.l)
# class Kid2(Parent):
#     def __init__(self,lastname,name2):
#         super().__init__(lastname)
#         self.f=name2
#     def info3(self):
#         super().info1()
#         print("Full Name:",self.f,self.l)
# k1=Kid1("Rehal","Sakshi")
# k1.info2()
# k2=Kid2("Rehal","Kartik")
# k2.info3()


# hybrid Inheritence
# class Animal:
#     def __init__(self,species):
#         self.s=species
#     def ani(self):
#         print("species:",self.s)
# class Mammal(Animal):
#     def __init__(self,species,legs):
#         super().__init__(species)
#         self.l=legs
#     def mammal_info(self):
#         super().ani()
#         print("Legs:",self.l)
# class Bird(Animal):
#     def __init__(self,species,wings):
#         super().__init__(species)
#         self.w=wings
#     def bird_info(self):
#         super().ani()
#         print("Wings:",self.w)
# class Bat(Mammal,Bird):
#     def __init__(self,species,legs,wings):
#         Mammal.__init__(self,species,legs)
#         Bird.__init__(self,species,wings)
#     def bat_info(self):
        # super().mammal_info()
        # super().bird_info()

#         print("Bat is a mammal that can fly.")
# b=Bat("Bat",2,2)
# b.bat_info()    
# print(Bat.__mro__)


# heirarchical inheritence 
# class Parent:
#     def __init__(self,lastname):
#         self.l=lastname
#     def info1(self):
#         print(f"last name: {self.l}")
# class Kid1(Parent):
#     def __init__(self,lastname,firstname1):
#         super().__init__(lastname)
#         self.f=firstname1 
#     def info2(self):
#         super().info1()
#         print(f"full name of fisrt kid: {self.f} {self.l}")
# class Kid2(Parent):
#     def __init__(self,lastname,firstname2):
#         super().__init__(lastname)
#         self.f=firstname2
#     def info3(self):
#         super().info1()
#         print(f"full name of second kid: {self.f} {self.l}")   

# k1=Kid1("rehal","sakshi")
# k1.info2()
# k2=Kid2("rehal","kartik")
# k2.info3()

# hybrid inheritence 
# class Vehicle:
#     def veh(self):
#         print("vehicle is moving")
# class Car(Vehicle):
#     def car1(self):
#         print("car is running")
# class Boat(Vehicle):
#     def boat1(self):
#         print("boat is moving on water")
# class Ship(Vehicle):
#     def ship1(self):
#         print("ship is moving")
# class WaterVehicle(Boat,Ship):
#     def wv(self):
#         print("water vehicle")
# wat=WaterVehicle()
# wat.veh()
# wat.boat1()
# wat.ship1()
# wat.wv()
# print(WaterVehicle.__mro__)
    

