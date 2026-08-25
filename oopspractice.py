# Level 1 — OOP Basics
# Create a Student class with attributes name, age, and marks. Create an object and display the details.
class Student():
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)
s=Student('a',23,90)
s.display()

# Create an Employee class with name, salary, and department. Create 3 objects and display their information.
class Employee():
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)
e=Employee('sunitha',678900,'IT')
e.display()

# Create a Car class with attributes brand, model, and price. Add a method display_details().
class Car():
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display_details(self):
        print(self.brand)
        print(self.model)
        print(self.price)
c=Car('x','y',123456789)
c.display_details()

 

# Create a Rectangle class with length and width. Add methods to calculate:
# Area
# Perimeter
class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def display_area(self):
        print("area ",self.length*self.breadth)
    def display_perimeter(self):
        print('perimeter:',2*(self.length+self.breadth))
r=Rectangle(5,5)
r.display_area()
r.display_perimeter()
# Create a BankAccount class with:

# account_number
# name
# balance

# Add methods:

# deposit()
# withdraw()
# check_balance()
class BankAccount():
    def __init__(self,acc_num,name,balance):
        self.acc_num=acc_num
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
        print(self.balance)
    def withdraw(self,amt):
        if amt<=self.balance:
            print('withdraw',amt)
    def check_balance(self,amt):
        print(self.balance)
b=BankAccount(1,'a',23456)
b.withdraw(5200)

# Create a Book class with title, author, and price. Add a method to display book details.[]
class Book():
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def dispaly_bookdetails(self):
        print(self.author)
        print(self.title)
        print(self.price)
b=Book('1we','xcv',345)
b.dispaly_bookdetails()

# Create a Circle class with radius. Add methods to calculate area and circumference.
class Circle():
    def __init__(self,radius,pi):
        self.radius=radius
        self.pi=pi
    def display_area(self):
        print('area of circle:',self.pi*self.radius*self.radius)
    def display_circumference(self):
        print('circumference:',2*self.pi*self.radius)
c=Circle(3.14,10)
c.display_area()
c.display_circumference()
# Create a Person class with name and age. Add a method that checks whether the person is eligible to vote.
class person():
    def __init__(self,age):
        self.age=age
    def display(self):
        if self.age>=18:
            print('Eligible to vote')
        else:
            print("not Eligible to vote")
p=person(21)
p.display()
# 🟡 Level 2 — Constructor & self
# Create an Employee class where the constructor accepts name, id, and salary.
class Employee():
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display(self):
        print(self.name,self.id,self.salary)
e=Employee('a',22,8765432)
e.display()

# Create a Product class and use __init__() to initialize:

# product ID
# product name
# price
# quantity

# Calculate the total price.
class Product():
    def __init__(self,product_id,prod_name,price,quan):
        self.product=product_id
        self.prod_name=prod_name
        self.price=price
        self.quan=quan
    def total_price(self):
        return self.price*self.quan
p=Product(1,'lappy',70000,2)
p.total_price()
# Create a Student class where the constructor accepts marks of 3 subjects and calculates the average.
class Subject:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def calculate_avg(self):
        total_sum=(self.m1+self.m2+self.m3)
        avg=total_sum/3
s=Subject(50,60,70)
s.calculate_avg()
# Create a Car class with a default value for color.
class Car:
    def __init__(self,color="Black"):
        self.color=color
default_car=Car()
print(default_car.color)
custom_car=Car('RED')
print(default_car.color)

# Create a Mobile class with brand, model, and price. Add a method that applies a 10% discount.
class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def discount(self):
        discount=self.price*0.1
        print(discount)
m=Mobile('samsung','galaxy',555000)
m.discount()

# Create an Employee class and use self to distinguish between instance variables and local variables.
class Employee:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def display(self,id):
        print(id)
        print(self.name)
        print(self.dept)
e=Employee('sunitha','data science')
e.display(3253)

# 🟠 Level 3 — Instance, Class & Static Methods

# Create an Employee class with a class variable company = "ABC".
class emp():
    company="abc"
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
e=emp('sun')
e.display()
print(e.company) 
    
# Create 3 employees and demonstrate the difference between:

# instance variable
# class variable
class variables_Demo:
    college="ASDFG"
    def __init__(self,name,):
        self.name=name
    def display(self):
        print(self.name)
v=variables_Demo('mnbvc')
print(v.college)


# Create a Student class with a class variable school_name.
class Student:
    school_name="GSEMS"
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
s=Student('sunitha')
s.display()
print(s.school_name)

# Change the school name using a class method.
class School:
    school_name="XYZ"
    def __init__(self,name):
        self.name=name
    @classmethod
    def display(cls,new_name):
        cls.school_name=new_name
        print(cls.school_name)
s=School('sunitha')
School.display('GSEMS')
print(s.school_name)
# Create a MathOperations class with a static method:
# add(a, b)
class Static_demo:
    @staticmethod
    def add(a,b):
        sum=a+b
        print(sum)
s=Static_demo()
s.add(2,3)

    

# Return the sum without using any instance variables.
class Demo:
    @staticmethod
    def display(a,b):
        return a+b
d=Demo.display(12,2)
print(d)
# Create a Temperature class with:
# Celsius-Fahrenheit conversion methods.Use a static method where appropriate.
class Temp:
    @staticmethod
    def convert(c):
        return (c*(9/5)+32)
t=Temp()
t.convert(34)
# Create a Bank class that keeps track of the total number of accounts created using a class variable.
class Bank:
    total_accounts=0
    def __init__(self,acc_holder,balance):
        self.acc_holder=acc_holder
        self.balance=balance
      
    total_accounts+=1
    print(total_accounts)
acc=Bank('sunitha',852963)


# 🔵 Level 4 — Encapsulation

# Create a BankAccount class with a private variable __balance.
# Implement:
# deposit
# withdraw
# get_balance
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def dep(self,amt):
        self.__balance+=amt
        print(self.__balance)
    def withdraw(self,amt):
        self.amt=amt
        if self.amt<self.__balance:
            self.__balance-amt
            print(self.__balance-amt)
        else:
            print("Insuff balance")
    def get_balance(self):
        print(self.__balance)
d=BankAccount(100000)
d.dep(2000)
d.withdraw(2000)
d.get_balance()
    

# Create an Employee class with private __salary.
class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def display(self):
        print(self.__salary)

e=Employee(30000)
e.display()
# Create getter and setter methods with validation so salary cannot be negative.
class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def get_salary(self):
        print(self.__salary)
    def set_salary(self,new_salary):
        if new_salary>=0:
            self.__salary=new_salary
            print(self.__salary)
e=Employee(20000)
e.get_salary()
e.set_salary(40000)
    
# Create a Student class with private __marks.# Allow marks only between 0 and 100.

class Student:
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,new_marks):
        if 0<=new_marks<=100:
            self.__marks=new_marks
            print(self.__marks)
        else:
            print('enter valid marks between 0 to 100')
s=Student(90)
s.get_marks()
s.set_marks(95)
s.get_marks()

# Create a User class with a private password.
# class User:
#     def __init__(self,username,password):
#         self.username=username
#         self.__password=password
#     def display_info(self,user,passw):
#         if user==self.username and passw==self.__password:
#             print('Login successful')
#         else:
#             print('login not successful')
# u=User('sunitha','@admin123')
# u.display_info('sunitha','@admin123')

# Implement a method to verify whether a given password is correct.
class  User:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    def display_info(self,user,passw):
        if user==self.username and passw==self.__password:
            print('Login successful')
        else:
            print('login not successful')
u=User('sunitha','@admin123')
u.display_info('sunitha','@admin123')
# Explain and demonstrate the difference between:
# self.name
# _name
# __name
class Demo:
    def __init__(self,name,age):
        self.name=name
        self._name=name
        self.__name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self._name)
        print(self.__name)
        print(self.age)
d=Demo('Angel',21)
d.display()

# 🟣 Level 5 — Inheritance
# Create:
# Animal
#    ↓
# Dog
# Animal should have a method sound(). Override it in Dog.
class Animal:
    def sound(self):
        print("animal makes sound")

class Dog(Animal):
    def sound(self):
        print("barks")

d=Dog()
d.sound()
# Create:
# Employee
#    ↓
# Manager
# Employee has name and salary. Manager has an additional bonus.
# Calculate the manager's total salary.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_info(self):
        print(self.name)
        print(self.salary)
class manager(Employee):
    def __init__(self,name,salary,bonus):
         super().__init__(name,salary)
         self.bonus=bonus
    def calculate_bonus(self):
        self.salary+=self.bonus
    def display(self):
        print(self.bonus)
m=manager('sunitha',200000,3000)
m.display()


# Create:
# Vehicle
#    ↓
# Car
#    ↓
# ElectricCar
# Demonstrate multilevel inheritance.
class Vehicle:
    def start(self):
        print('vehicle starts')
    def stop(self):
        print('vehicle stops')
class Car(Vehicle):
    def type(self):
        print('its a  not sports car')
    def fuel(self):
        print('fuel not required')

class ElectricCar(Car):
    def display_cost(self):
        print('it cost around 400000')
e=ElectricCar()
e.display_cost()
e.type()
e.fuel()

# Create:
# Person
#    ↓
# Student
#    ↓
# CollegeStudent

# Add different attributes at each level.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(self.name)
        print(self.age)
class Student(person):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def display1(self):
        print(self.dept)
class CollegeStudent(Student):
    def __init__(self,name,age,dept,regno):
        super().__init__(name,age,dept)
        self.regno=regno
    def display(self):
        print(self.regno)
c=CollegeStudent('asd',21,'datascience',3253)
c.display_info()
c.display1()
c.display()
    


# Create:
# Animal
#    ↓
# Dog
#    ↓
# Puppy
# Use super() to call parent constructors.
class Animal:
    def __init__(self):
        print('this is my pet')
    def sound(self):
        print('animal make sound')

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        super().sound()
        print("dog barks")
class Puppy(Dog):
    def __init__(self):
        super().__init__()
    def sound(self):
        super().sound()
        print("woffff!....")
def sound(self):
    self.sound()
p=Puppy()
p.sound()
d=Dog()
d.sound()

# Create:
# Employee
#    ↓
# Developer
#    ↓
# SeniorDeveloper

# Each class should have its own method and demonstrate super().
class Employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print(self.name)
class Developer(Employee):
    def __init__(self,name,programming_lang):
        super().__init__(name)
        self.programming=programming_lang
    def write_code(self):
        print(self.name)
    def display(self):
        print(self.programming)
class SeniorDeveloper(Developer):
    def __init__(self,name,programming_lang,team):
        super().__init__(name,programming_lang)
        self.team=team
    def lead_team(self):
        print(self.team)
s=SeniorDeveloper('sunitha','python','Ai')
s.work()
s.write_code()
s.lead_team()

# 🔴 Level 6 — Multiple & Hierarchical Inheritance
# Create:
# Father       Mother
#    \           /
#     \         /
#       Child

# Use multiple inheritance and access methods from both parents.
class Father:
    def Property(self):
        print("land")
class Mother:
    def Car(self):
        print('car')
class child(Father,Mother):
    def education(self):
        print('Btech')
c=child()
c.education()
c.Car()
c.Property()
# Create:
# Employee
#  /      \
# Developer  Tester
# Demonstrate hierarchical inheritance.
class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def details(self):
        return self.name,self.emp_id,self.salary
class Developer(Employee):
    def __init__(self,name,emp_id,salary,lang):
        super().__init__(name,emp_id,salary)
        self.lang=lang
    def write_code(self):
        return self.name,self.lang
class Tester(Employee):
    def __init__(self, name, emp_id, salary, testing_tool):
        super().__init__(name, emp_id, salary)
        self.testing_tool = testing_tool
    def test_software(self):
        return self.name,self.testing_tool
dev=Developer('sunitha',1234,67890,'python')
tester=Tester('sdfg',456,23456,'selenium')
print(dev.write_code())
print(tester.test_software())


# Create
#  /    \
# Student Employee
#  \      /
#   CollegeEmployee

# Try implementing this using multiple/hybrid inheritance.
# class Student:
#     def __init__(self,id):
#         self.id=id
#     def study(self):
#         return self.id

# class Employee:
#     def __init__(self, employee_id, salary):
#         self.employee_id = employee_id
#         self.salary = salary
#     def work(self):
#         return f"{self.id} 's salary is{self.salary}"
# class CollegeEmployee(Student,Employee):
#     def __init__(self, name, student_id, major, employee_id, salary):
#         Student.__init__(self, student_id, major)
#         Employee.__init__(self, employee_id, salary)
#         self.name = name
#     def show_role(self):
#         return f'{self.name} balance both roles'
# g=CollegeEmployee('asdvb',12345,"IT","qwsdr43")
# print(g.show_role())
# print(g.study)
# Create two parent classes:
class Father:
    def skills(self):
        print("Driving")


class Mother:
    def skills(self):
        print("Cooking")

# Create a child class that inherits from both and calls both methods.
class child(Father,Mother):
    def education(self):
        print("Btech")
    def display(self):
        Father.skills(self)
        Mother.skills(self)
s=child()
s.education()
s.display()
# 🟤 Level 7 — Polymorphism
# Create Dog, Cat, and Cow classes. Each should have a sound() method.
# Use a loop to call sound() for all objects.
class Dog:
    def sound(self):
        print('barks')
class Cat:
    def sound(self):
        print('meow')

class Cow:
    def sound(self):
        print('.....')
d=Dog()
c=Cat()
cow=Cow()
animals=[d,c,cow]
for animal in animals:
    animal.sound()


# Create Circle, Rectangle, and Triangle classes with an area() method.
# Calculate areas polymorphically.
class Circle:
    def __init__(self,pi,r):
        self.pi=pi,
        self.r=r
    def area(self,pi,r):
        return self.pi*self.r*self.r
class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self,l,b):
        return self.l*self.b
class Triangle:
    def __init__(self,b,h):
            self.b=b
            self.h=h
    def area(self,b,h):
        return (1/2)*self.b*self.h

# shapes=[Circle(pi=3.14,r=10),Rectangle(l=10,b=10),Triangle(b=10,h=10)]
# for shape in shapes:
#     print(shape.area())
    
# Create Developer and Manager classes with a common method:
# calculate_salary()
# Show how the same method behaves differently.
class Devloper:
    def __init__(self,name,salary,working_hours):
        self.name=name
        self.salary=salary
        self.working_hrs=working_hours
    def calculate_salary(self):
        return self.salary+self.working_hrs
class manager:
    def __init__(self,name,salary,project_bonus):
        self.name=name
        self.salary=salary
        self.project_bonus=project_bonus
    def calculate_salary(self):
        return self.salary+self.project_bonus
# 





# Demonstrate method overriding using:
# Vehicle → Car
# Demonstrate duck typing using classes that have the same method but do not inherit from the same parent.

class Vehicle:
    def drive(self):
        print("The vehicle moves forward.")
class Car(Vehicle):
    def drive(self):
        print("The car zooms down the highway on four wheels!")

class Boat:
    def drive(self):
        print("The boat cuts through the waves across the water!")
travel_options=[Car(),Boat()]
for option in travel_options:
    option.drive()
# ⚫ Level 8 — Abstraction
# Create an abstract class Shape with an abstract method area().
# Create:
# Circle
# Rectangle
# Implement area() in both.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def area(self):
        print(self.pi*self.r*self.r)
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
c=Circle(3.14,10)
r=Rectangle(10,5)
c.area()
r.area()

# Create an abstract class Payment with:pay()
# Create:
# CreditCardPayment
# UPIPayment
# CashPayment
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class Creditcardpayment(Payment):
    def pay(self):
        print('credit card is used for payment')
class UPIpayment(Payment):
    def pay(self):
        print('Method used in this is UPI')
class Cashpayment(Payment):
    def pay(self):
        print('method used here is cash')
c=Creditcardpayment()
u=UPIpayment()
C=Cashpayment()
c.pay()
u.pay()
C.pay()


# Create an abstract Vehicle class with:
# start()
# stop()
# Implement them in Car and Bike.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car is started")
    def stop(self):
        print('car has stop')
class Bike(Vehicle):
    def start(self):
        print("bike is started")
    def stop(self):
        print("car has stop")
c=Car()
c.start()
c.stop()
b=Bike()
b.start()
b.stop()
    
# 🔥 Level 9 — Interview-Level Programs
# Create an Employee management system using OOP.

# Operations:

# 1. Add employee
# 2. Display employees
# 3. Search employee
# 4. Update salary
# 5. Delete employee
class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
employee=[]
def add_emp():
    emp_id=int(input("enter id of emp:"))
    name=input("enter emp name:")
    salary=float(input("Enter salary of emp:"))
    employee.append(Employee(emp_id,name,salary))
def display_emp():
    for emp in employee:
        print(emp.emp_id,emp.name,emp.salary)

def search_emp():
    emp_id=int(input("enter emp id:" ))
    for emp in employee:
        if emp.emp_id==emp_id:
            print(emp.name,emp.salary)
        else:
            print("Employee not found")
def update_salary():
    emp_id=int(input("enter emp_id to update salary:"))
    for emp in employee:
        if emp.emp_id==emp_id:
            new_salary=float(input("Enter new salary:"))
            emp.salary=new_salary
            print("salary is updated")
        else:
            print("employee not found")
def delete_employee():
    emp_id=int(input("enter  emp_id u want to delete:"))
    for emp in employee:
        if emp.emp_id==emp_id:
            employee.remove(emp)
            print("employee is removed")
        else:
            print("employee is not found")
def main():
    while True:
        print("1.Add Emp")
        print('2.Display emp')
        print('3.search emp')
        print('4.update salary')
        print('5.delete emp')
        print('6.exit')
        choice=input("enter your choice(1-6):")
        if choice=="1": add_emp()
        elif choice=='2':display_emp()
        elif choice=='3':search_emp()
        elif choice=='4':update_salary()
        elif choice=='5':delete_employee()
        elif choice=='6':break
        else:
            print("invalid choice")
if __name__=='__main__':
    main()



# Create a Banking System using OOP.

# Implement:
# Create account
# Deposit
# Withdraw
# Check balance
# Transfer money
class BankingSystem:
    def ___init__(self,account_number,name,balance=0):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.amount+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print('Insufficient balance')
    def check_balance(self):
        print(self.balance)
    def transfer(self,other_acc,amount):
        if amount<=self.balance:
            self.balance-=amount
            other_acc+=amount
            print("transfer successful")
        else:
            print('Insufficient balance')
a=BankAccount(101,'sun',123456)
a.deposit(2345)
a.withdraw(234)
a.transfer(1000)
a.check_balance()

# Create a Library Management System.
# Classes:
# Book
# Student
# Library
# Operations:
# Add book
# Issue book
# Return book
# Search book
# Display available books
class Book:
    def __init__(self,book_id,title):
        self.book_id=book_id
        self.title=title
        self.available=True
class Student:
    def __init__(self,name):
        self.borrowed_books=[]
        self.name=name
class Library:
    def __init__(self):
        self.books=[]
        self.students=[]
    def add_book(self,title,author):
        new_book=Book(title,author)
        self.books.append(new_book)
        print(title)
    def dispaly_book(self):
        for book in self.books:
            if book.is_available:
                print(book.title)
    def search_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                status = "Available" if book.is_available else "Borrowed"
                print(f"Found: '{book.title}' by {book.author} | Status: {status}")
                return
        print("Book not found.")
    

    def issue_book(self, student_name, book_title):
        # Find the book and the student
        for book in self.books:
            if book.title.lower() == book_title.lower() and book.is_available:
                book.is_available = False
                print(f"'{book.title}' has been given to {student_name}.")
                return
        print("Sorry, book is either not found or already borrowed.")


    def return_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower() and not book.is_available:
                book.is_available = True
                print(f"'{book.title}' is now returned to the library.")
                return
        print("This book was not borrowed.")
my_lib=Library()
my_lib.add_book("Harry Potter", "J.K. Rowling")
my_lib.add_book("The Hobbit", "J.R.R. Tolkien")
my_lib.display_books()
my_lib.search_book("The Hobbit")
my_lib.issue_book("Alice", "Harry Potter")
my_lib.display_books()

# Create a Shopping Cart system.

# Classes:

# Product
# Cart
# Customer

# Implement:

# Add product
# Remove product
# Calculate total
# Apply discount
# Display cart
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = [] 
    def add_product(self, product):
        self.items.append(product)
        print(product.name)
    def remove_product(self, product_name):
        for product in self.items:
            if product.name.lower() == product_name.lower():
                self.items.remove(product)
                print(product.name)
                return
        print(product_name)
    def calculate_total(self):
        total = 0
        for product in self.items:
            total += product.price
        return total
    def apply_discount(self, discount_percentage):
        current_total = self.calculate_total()
        discount_amount = (discount_percentage / 100) * current_total
        final_total = current_total - discount_amount
        print(discount_amount,discount_percentage)
    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        for product in self.items:
            print(f"• {product.name} - ${product.price}")
        print(f"Total Bill: ${self.calculate_total()}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()
customer = Customer("Alice")
print(f"Welcome, {customer.name}!")
laptop = Product("Laptop", 999.99)
headphones = Product("Headphones", 149.99)
mouse = Product("Wireless Mouse", 25.00)
customer.cart.add_product(laptop)
customer.cart.add_product(headphones)
customer.cart.add_product(mouse)
customer.cart.display_cart()
customer.cart.remove_product("Wireless Mouse")
customer.cart.display_cart()
final_bill = customer.cart.apply_discount(10)
print(f"Final Amount to Pay: ${final_bill:.2f}")
# Create a Hospital Management System.

# Classes:

# Person
# Doctor
# Patient
# Hospital

# Implement basic registration and appointment functionality.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization


class Patient(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []

    def register_doctor(self, doctor):
        self.doctors.append(doctor)
        print("Doctor registered successfully")

    def register_patient(self, patient):
        self.patients.append(patient)
        print("Patient registered successfully")

    def book_appointment(self, patient, doctor):
        self.appointments.append((patient.name, doctor.name))
        print("Appointment booked successfully")


# Create hospital
hospital = Hospital()

# Create doctor
doctor = Doctor("Ravi", 35, "Cardiologist")

# Create patient
patient = Patient("Sunitha", 25)

# Register
hospital.register_doctor(doctor)
hospital.register_patient(patient)

# Appointment
hospital.book_appointment(patient, doctor)

print("\nDoctor:")
print(doctor.name)
print(doctor.specialization)

print("\nPatient:")
print(patient.name)
print(patient.age)

print("\nAppointments:")
print(hospital.appointments)
# Create an ATM system using OOP.

# Implement:

# PIN verification
# Check balance
# Deposit
# Withdraw
# Mini statement
# Exit
class ATM:
    def __init__(self):
        self.pin = 1234
        self.balance = 10000
        self.transactions = []

    def verify_pin(self):
        pin = int(input("Enter PIN: "))

        if pin == self.pin:
            print("PIN verified successfully")
            return True
        else:
            print("Wrong PIN")
            return False

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self):
        amount = float(input("Enter deposit amount: "))

        self.balance += amount
        self.transactions.append("Deposited: " + str(amount))

        print("Amount deposited successfully")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))

        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append("Withdrawn: " + str(amount))
            print("Please collect your cash")
        else:
            print("Insufficient balance")

    def mini_statement(self):
        print("\nMini Statement")

        if len(self.transactions) == 0:
            print("No transactions")
        else:
            for transaction in self.transactions:
                print(transaction)


# Create ATM object
atm = ATM()

# PIN verification
if atm.verify_pin():

    while True:

        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Mini Statement")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            atm.check_balance()

        elif choice == 2:
            atm.deposit()

        elif choice == 3:
            atm.withdraw()

        elif choice == 4:
            atm.mini_statement()

        elif choice == 5:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")