# Password Validator
# 1) Must be greater than or equal to 8 characters
# 2) Must include at least one lowercase, uppercase, special characters and digit

# Using Object Oriented Programming Approach
class Pvalidate:
    def _init__(self):
        pass
    def validate(self,Passwd):
        if len(Passwd)<8:
            print("Not a valid Password because length<8")
        else:
            lcase=ucase=schar=digit=0
            for i in Passwd:
                if i.islower():
                    lcase+=1
                elif i.isupper():
                    ucase+=1
                elif i.isdigit():
                    digit+=1
                else:
                    schar+=1
            if lcase>=1 and ucase>=1 and schar>=1 and digit>=1:
                print(f"{Passwd} can be a Valid Password")
            else:
                print(f"{Passwd} cannot be a Valid Password because:")
                if lcase==0:
                    print("No Lowercase Letter")
                if ucase==0:
                    print("No Uppercase Letter")
                if digit==0:
                    print("No Digit included")
                if schar==0:
                    print("No special character included.")
msg=input("Enter Password: ")
Obj=Pvalidate()
Obj.validate(msg)


# Normal Approach
msg=input("Enter Message: ")
if len(msg)>=8:
    lcase=ucase=schar=digit=0
    for i in msg:
        if i.islower():
            lcase+=1
        elif i.isupper():
            ucase+=1
        elif i.isdigit():
            digit+=1
        else:
            schar+=1
    if lcase>=1 and ucase>=1 and schar>=1 and digit>=1:
        print(f"{msg} can be a Valid Password")
    else:
        print(f"{msg} cannot be a Valid Password because:")
        if lcase==0:
            print("No Lowercase Letter")
        if ucase==0:
            print("No Uppercase Letter")
        if digit==0:
            print("No Digit included")
        if schar==0:
            print("No special character included.")
else:
    print(f"{msg} cannot be a Valid Password because length of password is less than 8")