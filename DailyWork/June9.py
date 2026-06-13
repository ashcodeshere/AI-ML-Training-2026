# Inheritence :- 
# single inheritence:- 
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age 
#     def info1(self):
#         print(self.name)
#         print(self.age)
# class Student(Person):
#     def __init__(self,name,age,marks):
#         super().__init__(name,age)
#         self.marks=marks 
#     def info2(self):
#         print(f"name: {self.name}")
#         print(f"age: {self.age}")
#         print(f"marks: {self.marks}")
# objects
# s1=Student("abc",20,90)
# p1=Person("xyz",30)
# s1.info1()
# s1.info2()
# p1.info1()

# multiple inheritence:- 
# class Father:
#     def __init__(self,height):
#         self.height=height
#     def info1(self):
#         print(f"height as same as father: {self.height}")
# class Mother:
#     def __init__(self,color):
#         self.color=color 
#     def info2(self):
#         print(f"color as same as mother: {self.color}")
# class Kid(Father,Mother):
#     def __init__(self,height,color,name):
#         Father.__init__(self,height)
#         Mother.__init__(self,color)
#         self.name=name
#     def info3(self):
#         print(self.height)
#         print(self.color)
#         print(self.name)
# k1=Kid(163,"fair","abc")
# k1.info1()
# k1.info2()
# k1.info3()


# multilevel inheritence:- 
# base class (grandparent)
# intermediate class (parent )
# derived class (child)

# class grandparent:
#     def gp(self):
#         print("I am head of the family")
# class parent(grandparent):
#     def par(self):
#         print("i am second head of the family ")
# class kid(parent):
#     def kid1(self):
#         print("I am the future of the family")
# k1=kid()
# k1.gp()
# k1.par()
# k1.kid1()


# hybrid inheritence:- 
# class Vehicle:
#     def veh(self):
#         print("vehicle is moving")
# class car(Vehicle):
#     def car1(self):
#         print("car is running")
# class boat(Vehicle):
#     def boat1(self):
#         print("boat is moving on water")
# class ship(Vehicle):
#     def ship1(self):
#         print("ship is moving")
# class watervehicle(boat,ship):
#     def waveh(self):
#         print("water vehicle")

# wat=watervehicle()
# wat.veh()
# wat.boat1()
# wat.ship1()
# wat.waveh()

# hierarchical inhertience :- 

# encapsulation :- data binding (data members and methods )in a class 
# and restrict the direct access 

# access modifier 
# public access modifier 
# private access modifier
# protected access modifier


# encapsulation :- data binding (data members and methods )in a class 
# and restrict the direct access 

# access modifier 
# public access modifier 
# private access modifier
# protected access modifier 

# why use encapsulation :-
# data security 
# data validation 
# better maintence 
# controlled access 

# public member :- 
# class student:
#     def __init__(self,name):
#         self.name=name 

# s=student("sakshi")
# print(s.name)


# protected member:
# class student:
#     def __init__(self):
#         self.name="sakshi"
#         self._marks=90 
# s=student()
# print(s.name)
# print(s._marks)

# private member:- 
# class student:
#     def __init__(self):
#         self.__name="sakshi"
# s=student()
# print(s._student__name)


# getter and setter method 
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance     #private member 
#     def deposit(self,amount):
#         self.__balance+=amount 
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount 
#         else:
#             print("insufficient balance")
#     def get_balance(self):
#         return self.__balance
# object 
# acc=BankAccount(10000)
# acc.deposit(5000)
# acc.withdraw(7000)
# print(acc.get_balance())


# abstraction:- 
# python module :- abc 
# ABC:- Abstract Base Class 
# from abc import ABC, abstractmethod 
# class Animal(ABC):
    # abstract method 
#     @abstractmethod
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         print("woof")
# class Cat(Animal):
#     def speak(self):
#         print("meow")
# objects 
# d=Dog()
# d.speak()
# c=Cat()
# c.speak()