# file handling:- 
# types of files:- 
# text files
# binary files 
# csv 
# file handling modes:- 
# r:- read mode 
# w:- write mode 
# a:- append mode
# r+:- read and write mode 
# w+:- write and read 
# b:- binary mode 
# wb:- write binary 
# rb:- read binary 

# opening a file :- 
# file= open("abc.txt","x")


# writing a file:- 
# write()
# file=open("abc.txt","w")
# file.write("hello world")
# file.write("\nwelcome to python programming")
# file.close()


# reading a file:- 
# # read()
# file=open("abc.txt","r")
# content=file.read()
# print(content)
# file.close()


# read(n):-
# file=open("abc.txt","r")
# content=file.read(10)
# print(content)
# file.close()

# readline()
# file=open("abc.txt","r")
# content=file.readlines()
# print(content)
# file.close()

# append mode:- 
# file=open("abc.txt","a")
# file.write("\nthis is append mode")
# file.close()

# file=open("abc.txt","r")
# content=file.read()
# print(content)
# file.close()


# using with statement:- 

# with open("abc.txt","r") as file:
#     content=file.read()
#     print(content)

# import os 
# print(os.getcwd())
# print(os.path.exists("abc.txt"))

# if os.path.exists("abc.txt"):
#     os.remove("abc.txt")
#     print("file removed successfully")
# else:
#     print("file does not exist")


# exception handling:-
# zero division error 
# try:
#     a=int(input("enter any number: "))
#     b=int(input("enter any number: "))  
#     result=a/b
# except ZeroDivisionError:
#     print("division by zero is not allowed")
# except ValueError:
#     print("invalid input")
# except Exception as e: 
#     print("an error occurred:",e)
# else:
#     print("result:",result) 
# finally:
#     print("this block will always execute")


# file not found error:- 
# try:
#     f=open("file.txt","r")
# except FileNotFoundError:
#     print("file not found")
# else:
#     content=f.read()
#     print(content)
#     f.close()
# finally:
#     print("file handling completed")