# encapsulation:- data binding (bundling of data and methods )
# and restricting access to some parts of objects 
# access modifiers :- 
# public:- accessible from anywhere
# private:- accessible only within the class (name mangling) 
# protected:- accessible within the class and its subclass 

# public access modifier
# class BankAccount:
#     def __init__(self,amount):
#         self.a=amount
# acc=BankAccount(1000)
# print(acc.a) # accessing public variable


# private access modifier(__)
# class BankAccount:
#     def __init__(self,balance):
#         self.__b=balance # private variable
#     def deposit(self,amount):
#         self.__b=self.__b+amount
#     def withdraw(self,amount):
#         if 0<amount<=self.__b:
#             self.__b-=amount
#     def get_b(self):
#         return self.__b 
# acc=BankAccount(1000)
# acc.deposit(500)
# acc.withdraw(700)
# name mangling
# print(acc._BankAccount__b)
# print(acc.get_b())
# print(acc.__b)


# protected access modifiers 
# print(s1._age)

