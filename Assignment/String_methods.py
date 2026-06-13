from collections import Counter

# Q1
# message=input("Enter Message: ")
# ctr=0
# for i in message:
#     if i.lower() in ['a','e','i','o','u']:
#         ctr+=1
# print(f"No of Vowels in {message} are {ctr}")

# Q2
# msg=input("Enter Message: ")
# l=0
# u=0
# for i in msg:
#     if i.islower():
#         l+=1
#     elif i.isupper():
#         u+=1
# print(f"No of lower and uppercase letters in {msg} are {l} and {u} respectively")

# Q3
# strmsg=str(input("Enter Message: "))
# for i in range(len(strmsg)-1,-1,-1):
#     print(strmsg[i],end="")

# Q4
# msg=input("Enter Message: ")
# dict={}
# for i in range(len(msg)):
#     dict[msg[i]]=0
# for i in msg:
#     dict[i]+=1
# for i in dict:
#     print(f"{i}:{dict[i]}",end="\n")

# Q5
# msg=input("Enter Message : ")
# bool=True
# for i in msg:
#     if not i.isalpha():
#         bool=False
# if bool==False:
#     print(f"{msg} contains some non-alphabets")
# else:
#     print(f"{msg} contains only alphabets")

# Q6
# msg=input("Enter Message: ")
# print(msg.strip())

# Q7
# msg=input("Enter Message: ")
# ctr=0
# l=msg.split()
# for i in l:
#     ctr+=1
# print(f"There are {ctr} no of words : {l}")

# Q8
# msg=input("Enter Message: ")
# temp=""
# for i in msg:
#     if i.lower() in ['a','e','i','o','u']:
#         temp+=i.upper()
#     else:
#         temp+=i
# msg=temp
# print(msg)

# Q9
# msg=input("Enter Message: ").lower()
# n=len(msg)
# if msg[0:n:1]==msg[n:0:-1]+msg[0]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# Q10 - Same as Q4

# Q11
# msg=input("Enter Message: ")
# l=msg.split()
# d={}
# for i in l:
#     d[i]=len(i)
# max=0
# word=""
# for i in d:
#     if d[i]>max:
#         max=d[i]
#         word=i
# print(f"Longest word is {word} with length: {max}")

# Q12
# msg=input("Enter Message: ")
# digit=0
# letters=0
# special=0
# for i in msg:
#     if i.isdigit():
#         digit+=1
#     elif i.isalpha():
#         letters+=1
#     else:
#         special+=1
# print(f"Digit:{digit},Letters:{letters},Special Characters:{special}")

# Q13
# msg=input("Enter Message: ")
# seen=[0]*256
# result=""
# for i in msg:
#     ascii_val=ord(i)
#     if not seen[ascii_val]:
#         result+=i
#         seen[ascii_val]=1
# print(result)

# Q14
# msg=input("Enter Message: ")
# lis=msg.split()
# msgresult=[]
# for i in lis:
#     i=i[-1]+i[1:-1]+i[0]
#     msgresult.append(i)
# print(f"Original Message: {msg}\nAltered Message: {" ".join(msgresult)}")

# Q15
# msg1=input("Enter 1st word: ")
# msg2=input("Enter 2nd word: ")
# # if sorted(msg1.replace(" ","")) == sorted(msg2.replace(" ","")):
# #     print(f"{msg1} and {msg2} are Anagrams")
# # or
# # if Counter(msg1.replace(" ","")) == Counter(msg2.replace(" ","")):
# #     print(f"{msg1} and {msg2} are Anagrams")
# # else:
# #     print(f"{msg1} and {msg2} are not Anagrams")