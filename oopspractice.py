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
# 🔵 Level 4 — Encapsulation

# Create a BankAccount class with a private variable __balance.

# Implement:

# deposit
# withdraw
# get_balance

# Create an Employee class with private __salary.

# Create getter and setter methods with validation so salary cannot be negative.

# Create a Student class with private __marks.

# Allow marks only between 0 and 100.

# Create a User class with a private password.

# Implement a method to verify whether a given password is correct.

# Explain and demonstrate the difference between:
# self.name
# _name
# __name
# 🟣 Level 5 — Inheritance
# Create:
# Animal
#    ↓
# Dog

# Animal should have a method sound(). Override it in Dog.

# Create:
# Employee
#    ↓
# Manager

# Employee has name and salary. Manager has an additional bonus.

# Calculate the manager's total salary.

# Create:
# Vehicle
#    ↓
# Car
#    ↓
# ElectricCar

# Demonstrate multilevel inheritance.

# Create:
# Person
#    ↓
# Student
#    ↓
# CollegeStudent

# Add different attributes at each level.

# Create:
# Animal
#    ↓
# Dog
#    ↓
# Puppy

# Use super() to call parent constructors.

# Create:
# Employee
#    ↓
# Developer
#    ↓
# SeniorDeveloper

# Each class should have its own method and demonstrate super().

# 🔴 Level 6 — Multiple & Hierarchical Inheritance
# Create:
# Father       Mother
#    \           /
#     \         /
#       Child

# Use multiple inheritance and access methods from both parents.

# Create:
# Employee
#  /      \
# Developer  Tester

# Demonstrate hierarchical inheritance.

# Create:
# Person
#  /    \
# Student Employee
#  \      /
#   CollegeEmployee

# Try implementing this using multiple/hybrid inheritance.

# Create two parent classes:
# class Father:
#     def skills(self):
#         print("Driving")


# class Mother:
#     def skills(self):
#         print("Cooking")

# Create a child class that inherits from both and calls both methods.

# 🟤 Level 7 — Polymorphism
# Create Dog, Cat, and Cow classes. Each should have a sound() method.

# Use a loop to call sound() for all objects.

# Create Circle, Rectangle, and Triangle classes with an area() method.

# Calculate areas polymorphically.

# Create Developer and Manager classes with a common method:
# calculate_salary()

# Show how the same method behaves differently.

# Demonstrate method overriding using:
# Vehicle → Car
# Demonstrate duck typing using classes that have the same method but do not inherit from the same parent.
# ⚫ Level 8 — Abstraction
# Create an abstract class Shape with an abstract method area().

# Create:

# Circle
# Rectangle

# Implement area() in both.

# Create an abstract class Payment with:
# pay()

# Create:

# CreditCardPayment
# UPIPayment
# CashPayment
# Create an abstract Vehicle class with:
# start()
# stop()

# Implement them in Car and Bike.

# 🔥 Level 9 — Interview-Level Programs
# Create an Employee management system using OOP.

# Operations:

# 1. Add employee
# 2. Display employees
# 3. Search employee
# 4. Update salary
# 5. Delete employee
# Create a Banking System using OOP.

# Implement:

# Create account
# Deposit
# Withdraw
# Check balance
# Transfer money
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
# Create a Hospital Management System.

# Classes:

# Person
# Doctor
# Patient
# Hospital

# Implement basic registration and appointment functionality.

# Create an ATM system using OOP.

# Implement:

# PIN verification
# Check balance
# Deposit
# Withdraw
# Mini statement
# Exit