# Tuple Based Questions

# Q1)
# msg=input("Enter items sepearated by ',' : ")
# tup=tuple(msg.split(","))
# print("(",end="")
# for i in tup:
#     print(i,end=", ")
# print(")")

# Q2)
# msg=input("Enter Elements: ")
# tup=tuple(int(item) for item in msg.split())
# sum=0
# for i in tup:
#     sum+=i
# print(f"Sum of {tup} elements of tuple is : {sum}")

# Q3)
# msg=input("Enter elements: ")
# tup=tuple(int(item) for item in msg.split())
# even=odd=0
# for i in tup:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"No of Even and Odd elements in tuple {tup} is : {even} and {odd} respectively")

# Q4)
msg=input("Enter Elements: ")
tup=tuple(int(item) for item in msg.split())
print(f"Elements of {tup} at even index positions: ")
for i in range(len(tup)):
    if i%2==0:
        print(tup[i]," ")
# Q5)
# Q6)
# Q7)
# Q8)
# Q9)
# Q10)