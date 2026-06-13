# Arithmetic Calculator - +, -, *, /, **

class ArithmeticCalc():
    def __init__(self):
        pass
    def add(self,args):
        sum=0
        for i in args:
            sum+=i
        return sum
    def subtract(self,a,args):
        res=a
        for i in args:
            res-=i
        return res
    def multiply(self,args):
        mul=1
        for i in args:
            mul*=i
        return mul
    def division(self,a,args):
        res=a
        for i in args:
            if i==0:
                print("DIvision By Zero Not Possible")
                return
            res/=i
        return res
    def power(self,a,args):
        pow=a
        for i in args:
            pow=pow**i
        return pow
    
print("1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Power\n")
msg=int(input("Enter Operation number to be executed: "))
res=ArithmeticCalc()
if msg==1:
    l=[]
    a=int(input("Enter Numbers of elements to be added: "))
    while a:
        e=int(input("\nEnter Number: "))
        l.append(e)
        a-=1
    print(f"Sum of {l} : {res.add(l)}")
elif msg==2:
    l=[]
    a=int(input("Enter Numbers of elements to be subtracted: "))
    x=int(input("\nEnter Number: "))
    while a-1!=0:
        e=int(input("\nEnter Number: "))
        l.append(e)
        a-=1
    print(f"Subtraction Result : {res.subtract(x,l)}")
elif msg==3:
    l=[]
    a=int(input("Enter Numbers of elements to be multiplied: "))
    while a:
        e=int(input("\nEnter Number: "))
        l.append(e)
        a-=1
    print(f"Multiplication of {l} : {res.multiply(l)}")
elif msg==4:
    l=[]
    a=int(input("Enter Numbers of elements to be divided: "))
    x=int(input("\nEnter Number: "))
    while a-1!=0:
        e=int(input("\nEnter Number: "))
        l.append(e)
        a-=1
    print(f"Division Result : {res.division(x,l)}")
elif msg==5:
    l=[]
    a=int(input("Enter Numbers of elements to be subtracted: "))
    x=int(input("\nEnter Number: "))
    while a-1!=0:
        e=int(input("\nEnter Number: "))
        l.append(e)
        a-=1
    print(f"Exponential Result : {res.power(x,l)}")
else:
    print("Enter Correct Number")