#  Student Management System

from abc import ABC, abstractmethod
# Abstraction
class BaseManagementSystem(ABC):
    @abstractmethod
    def add_record(self,entity):
        pass
    @abstractmethod
    def view_records(self):
        pass
    @abstractmethod
    def delete_record(self,unique_id):
        pass



class Person:               #Parent Class
    # Encapsulation
    def __init__(self,name,age):
        self.__name=""
        self.__age=1
        self.name=name
        self.age=age 
    # Getter
    @property               #Built-in decorator
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @name.setter                    # @attribute.setter
    def name(self,value):
        if isinstance(value,str) and value.strip():
            self.__name=value
    @age.setter
    def age(self, value):
        try:
            value=int(value)
            if value>0:
                self.__age=value
        except ValueError:
            print("Invalid Age")
    def __str__(self):     # Print method overriding
        return f"Name: {self.__name} | Age: {self.__age}"
        


class Student(Person):          #Inheritance - Child Class
    def __init__(self, rollno, name, age, course):
        super().__init__(name, age)
        self.__roll_no=rollno
        self.course=course
    @property
    def roll_no(self):
        return self.__roll_no
    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self,value): 
        if isinstance(value,str) and value.strip():
            self.__course=value
    def __str__(self):
        return f"Roll No: {self.__roll_no} | {super().__str__()} | Course: {self.course}"



class StudentManagementSystem(BaseManagementSystem):
    def __init__(self):
        self.__students={}
    
    def add_record(self, sobj):
        if not isinstance(sobj,Student):
            print("Invalid Student Object")
            return False
        if sobj.roll_no in self.__students:
            print("\nError: Student with this roll no already exists!")
            return False
        self.__students[sobj.roll_no]=sobj
        print(f"\n Student: '{sobj.name}', Added Successfully")
        return True
    
    def view_records(self):
        if not self.__students:
            print("\nNo student record found.")
            return
        print("\n ----- Student Records -----")
        for i in self.__students.values():
            print(i)
    
    def search_record(self, roll_no):
        student=self.__students.get(roll_no)
        if student:
            print("\nStudent Found:")
            print(student)
            return student
        else:
            print("\nStudent not found.")
            return None
    
    def update_record(self,roll_no):
        student=self.search_record(roll_no)
        if not student:
            return
        print(f"\nUpdating details for {student.name}")
        new_name=input(f"Enter new name ({student.name}): ")
        new_age=input(f"Enter new age ({student.age}): ")
        new_course=input(f"Enter new course ({student.course}): ")
        if new_name.strip(): student.name=new_name
        if new_age.isdigit() : student.age=new_age
        if new_course.strip() : student.course=new_course
        print("\nStudent details Updated successfully!!")
    
    def delete_record(self,roll_no):
        if roll_no in self.__students:
            del self.__students[roll_no]
            print(f"\nStudent with Roll No {roll_no} deleted successfully.")
        else:
            print("\nStudent not found.")


# ------------------------------------------------------------------------------------------------------------


def add_students():
    roll=input("Enter Roll No: ")
    if not roll.isdigit() or not roll.strip():
        print("Roll no Can't be empty and should contain digits only.")
        return
    name=input("Enter Name: ")
    if not name.strip():
        print("Name cannot be empty!")
        return
    try:
        age_input=input("Enter Age: ")
        if not age_input.isdigit():
            print("Age can't be empty and should contain valid digits only")
            return 
        age=int(age_input)
        if age<=0: print("Age should be greater than 0")
    except ValueError:
        print("Invalid Age!")
        return
    course=input("Enter Course: ")
    if not course.strip():
        print("Course cannot be empty")
        return
    student=Student(roll,name,age,course)
    sms.add_record(student)

def search_student():
    roll=input("Enter Roll Number to search: ")
    if not roll.strip():
        print("Roll no Can't be empty")
        return
    sms.search_record(roll)

def update_student():
    roll=input("Enter Roll Number to update: ")
    if not roll.strip():
        print("Roll no Can't be empty")
        return
    sms.update_record(roll)

def delete_student():
    roll=input("Enter Roll Number to delete: ")
    if not roll.strip():
        print("Roll no Can't be empty")
        return
    sms.delete_record(roll)

sms=StudentManagementSystem()
while True:
    print("="*40)
    print("\n  OOPs Student Management System")
    print("="*40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice=input("\nEnter Choice (1-6): ")
    if choice=='1':
        add_students()
    elif choice=='2':
        sms.view_records()
    elif choice=='3':
        search_student()
    elif choice=='4':
        update_student()
    elif choice=='5':
        delete_student()
    elif choice=='6':
        print("\nExiting System. Good Bye")
        break
    else:
        print("\nInvalid Choice!")

