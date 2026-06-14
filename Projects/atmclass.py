# Create an ATM Class that has functions
# 1) Pin Generation
# 2) Pin Validator
# 3) User Validator
# - Balance should be private

import hashlib

class ATM:
    def __init__(self,account_number,initial_balance=0.0):
        self.account_number=account_number
        self.__balance=float(initial_balance)
        self.__pin_hash=None
        self.__isLocked=False
        self.failed_pin_attempts=0

    def pin_generation(self,new_pin):
        if self.__isLocked:
            return "Error. Accont is Locked"
        if not (new_pin.isdigit() and len(new_pin) in [4,6]):
            return "Error. PIN must be exactly 4 or 6 digits."
        self.__pin_hash=hashlib.sha256(new_pin.encode()).hexdigest()
        return True
    
    def validate_pin(self,entered_pin):
        if self.__isLocked:
            return False
        if not self.__pin_hash:
            return False
        entered_hash=hashlib.sha256(entered_pin.encode()).hexdigest()
        if entered_hash==self.__pin_hash:
            self.failed_pin_attempts=0
            return True,"PIN Validated"
        else:
            self.failed_pin_attempts+=1
            if self.failed_pin_attempts>=3:
                self.__isLocked=True
                return False,"Incorrect PIN"
            return False, f"Incorrect PIN . Attempts remaining : {3-self.failed_pin_attempts}"
    
    def validate_user(self,entered_account):
        if self.__isLocked:
            return False,"Access Denied. Account is Locked."
        if entered_account!=self.account_number:
            return False,"Error. Invalid Account Number."
        return True,"User Authorized."
    
    def checkbalance(self,entered_pin):
        is_valid, message = self.validate_pin(entered_pin)
        if is_valid:
            return f"Your current balance is {self.__balance:.2f}"
        return message
    
    def deposit(self,entered_pin,amount):
        is_valid,message=self.validate_pin(entered_pin)
        if not is_valid:
            return message
        if amount<=0:
            return "Error: Deposit amount must be positive. "
        self.__balance+=amount
        return f"Successfully deposited {amount:.2f}. New Balance :{self.__balance:.2f}Rs"

    def withdraw(self,entered_pin,amount):
        is_valid, message=self.validate_pin(entered_pin)
        if not is_valid:
            return message
        if amount <=0:
            return "Error: Withdrawal Amount must be positive and greater than 0."
        if amount>self.__balance:
            return "Error: Insufficient Balance. Withdrawal can't be done"
        self.__balance-=amount
        return f"Successgully withdrew {amount:.2f}Rs. New Balance: {self.__balance:.2f}Rs"
    # Getter 
    def is__Locked(self):
        return self.__isLocked

print("===== Welcome to ATM of hypothetical bank =====") 
account_num=input("Create an Account number to initialize the ATM: ").strip()
initial_bal=float(input("Enter initial balance in account: "))
atm=ATM(account_number=account_num,initial_balance=initial_bal)
print("\n1.----- PIN Generation -----")
while True:
    pin_choice=input("Set a secure 4 or 6 digit PIN: ")
    result=atm.pin_generation(pin_choice)
    if result is True:
        print("PIN created Successfully")
        break
    else:
        print(result)
print("\n2.----- ATM Terminal Ready -----")
while True:
    print("\nAvailable Actions: \n1) Check Balance \n2) Deposit \n3) Withdraw \n4) Exit")
    choice=input("Select an option (1-4) : ").strip()
    if choice =='4':
        print("Thank You for using my ATM. GoodBye, Have a nice day")
        break

    input_acc=input("Enter your account number: ").strip()
    user_ok,user_msg=atm.validate_user(input_acc)
    if not user_ok:
        print(user_msg)
        if atm.is__Locked():
            break
        continue
    input_pin=input("Enter Your PIN: ").strip()
    if choice=='1':
        print(atm.checkbalance(input_pin))
    elif choice=='2':
        try:
            amount=float(input("Enter deposit amount: Rs"))
            print(atm.deposit(input_pin,amount))
        except ValueError:
            print("Error: Invalid Numeric Amount.")
    elif choice=='3':
        try:
            amount=float(input("Enter Amount to withdraw: "))
            print(atm.withdraw(input_pin,amount))
        except ValueError:
            print("Error: Invalid Numeric Amount")
    else:
        print("Invalid Choice selection.")
    if atm.is__Locked():
        print("\n!!! Program Termination due to security lookout !!!")
        break



    
    
