

# Task 1: Student Class
# Create a Student class with the following attributes:
# Name
# Roll Number
# Marks
# Create 3 student objects and display their details.
class Student:
  def __init__(self, name, roll_number, marks):
    self.name = name
    self.roll_number = roll_number
    self.marks = marks
  def display(self):
    print(f"Name: {self.name}")
    print(f"Roll Number: {self.roll_number}")
    print(f"Marks: {self.marks}")
s=Student("sunitha",'21091A3253',80)
s.display()
s1=Student("Angel",'21091A3261',85)
s1.display()
s2=Student("Grace","21091A3244",23)
s2.display()

# Task 2: Employee Class
# Create an Employee class with:
# Employee ID
# Employee Name
# Salary
# Initialize values using a constructor and print employee details.
class Employee:
  def __init__(self,id,name,salary):
    self.id=id
    self.name=name
    self.salary=salary
  def display(self):
    print(f"Employee ID: {self.id}")
    print(f"Employee Name: {self.name}")
    print(f"Salary: {self.salary}")
e=Employee(1,"John",50000)
e.display()

# Task 3: Car Class
# Create a Car class with:
# Brand
# Color
# Mileage
# Create 2 car objects and display their details.
class Car:
  def __init__(self,brand,color,mileage):
    self.brand=brand
    self.color=color
    self.mileage=mileage
  def display(self):
    print(f"Brand: {self.brand}")
    print(f"Color: {self.color}")
    print(f"Mileage: {self.mileage}")
c=Car("Toyota","Blue",20)
c.display()
c1=Car("BMW",'royal blue',25)
c1.display()

# Task 4: Modify Instance Variable
# Create a Student object.
# Update the student's name after object creation and display the details before and after modification.
class Student:
  def __init__(self,name,roll_number):
    self.name=name
    self.roll_number=roll_number
  def display_details(self):
    print("Name:",self.name)
    print("Roll Number:",self.roll_number)
s=Student("sunitha",53)
s.display_details()
s.name="Grace Angel"
s.display_details()

#Task 5: Mobile Class
# Create a Mobile class with:
# Brand
# Price
# Create two objects and update the price of only one object.
# Display the details of both objects.
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def display_details(self):
        print(f"Brand: {self.brand}, Price: {self.price}")
m=Mobile("iphone",160000)
m.display_details()
m.price=150000
m.display_details()

# Task 6: College Class Variable
# Create a class variable:
# college_name = "ABC College"
# Create multiple student objects and display the college name using each object.
class College:
  college_name="ABC College"
  def __init__(self,name,roll_number):
    self.name=name
    self.roll_number=roll_number
  def display_details(self):
    print("Name:",self.name)
    print("Roll Number:",self.roll_number)
    print("College Name:",College.college_name)
s=College("sunitha",53)
s.display_details()
s1=College("Grace Angel",44)
s1.display_details()

# Task 7: Update Class Variable
# Modify the class variable:
# college_name = "XYZ College"
# Verify the updated value using all objects.
class College:
  college_name="ABC College"
  def __init__(self,name,roll_number):
    self.name=name
    self.roll_number=roll_number
  def display_details(self):
    print("Name:",self.name)
    print("Roll Number:",self.roll_number)
    print("College Name:",College.college_name)
c=College("sunitha",53)
c.display_details()
c1=College("Grace Angel",44)
c1.display_details()
College.college_name="XYZ College"
c.display_details()
c1.display_details()

# Task 8: Student Average
# Create a Student class with:
# Subject1 Marks
# Subject2 Marks
# Subject3 Marks
# Create a method:
# find_average()
# Return the average marks.
class Student:
  def __init__(self,Subject1,Subject2,Subject3):
    self.Subject1=Subject1
    self.Subject2=Subject2
    self.Subject3=Subject3
  def find_average(self):
    return (self.Subject1+self.Subject2+self.Subject3)/3
s=Student(10,20,30)
print(s.find_average())

# Task 9: Rectangle Area
# Create a Rectangle class with:
# Length
# Breadth
# Create a method:
# area()
# Return the area of the rectangle.
class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def area(self):
    return self.length*self.breadth
r=Rectangle(10,20)
r.area()

# Task 10: Bank Account
# Create a BankAccount class with:
# Account Holder Name
# Balance
# Create the following methods:
# get_balance()
# set_balance()
# Update and display the balance.
class BankAccount:
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance
  def get_balance(self):
    return self.balance
  def set_balance(self,new_balance):
    self.balance=new_balance
b=BankAccount("sunitha",10000)
print(b.get_balance())
b.set_balance(20000)
print(b.get_balance())

# Task 11: Product Management
# Create a Product class with:
# Product Name
# Price
# Use getter and setter methods to retrieve and update the price.
class Product:
  def __init__(self,name,price):
    self.name=name
    self.price=price
  def get_price(self):
    return self.price
  def set_price(self,new_price):
    self.price=new_price
p=Product("pen",10)
print(p.get_price())
p.set_price(20)
print(p.get_price())

# Task 12: Company Information
# Create a class variable:
# company = "TCS"
# Create a class method that returns the company name.
class Company:
  company="TCS"
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  @classmethod
  def get_company(cls):
    return cls.company
  def display_details(self):
    print("Name:",self.name)
    print("Salary:",self.salary)
c=Company("sunitha",10000)
c.display_details()
print(c.get_company())

# Task 13: School Information
# Create a School class with:
# school_name = "Delhi Public School"
# Create a class method to display the school information.
class Student:
  school_name="Delhi public School"
  def __init__(self,name,roll_number):
    self.name=name
    self.roll_number=roll_number
  @classmethod
  def display_school_info(cls):
    print("School Name:",cls.school_name)
s=Student("Sunitha",53)
s.display_school_info()

# Task 14: Calculator Using Static Method
# Create a static method:
# add(a, b)
# Return the sum of two numbers.
class Add:
  @staticmethod
  def display(a,b):
    sum=a+b
    print("Sum of two numbers:",sum)
a=Add()
a.display(1,2)

# Task 15: Utility Class
# Create static methods:
# square(number)
# cube(number)
# Display the square and cube of a given number.
class utility:
  @staticmethod
  def square(number):
    return number**2
  @staticmethod
  def cube(number):
    return number*number*number
u=utility()
u.square(3)
u.cube(2)

# Task 16: Laptop Management System
# Create a Laptop class with:
# Brand
# RAM
# Price
# Include:
# Constructor
# Instance Method
# Class Variable
# Class Method
# Static Method
# Display all details.

class Laptop:
    category="Electronics"
    def __init__(self,brand,RAM,Price):
        self.brand=brand
        self.Ram=RAM
        self.Price=Price
    def display(self):
        print(self.brand,self.Ram,self.Price)
    @classmethod
    def change_category(cls,newname):
        cls.change_category=newname
    @staticmethod
    def welcome():
        print("Welcome to laptop management Systen")
l=Laptop.welcome()
l=Laptop("hp","8gb",6000)
l.display()
l.change_category("Computers")
l.display()

    
# Task 17: Cricket Player
# Create a Player class with:
# Player Name
# Runs
# Matches
# Methods:
# display_player()
# average_runs()
# Display player information and average runs.
class CricketPlayer:
    def __init__(self,name,runs,matches):
        self.name=name
        self.runs=runs
        self.matches=matches
    def display_player(self):
        print(self.name,self.runs,self.matches)
    def avg_runs(self):
        if self.matches==0:
            return 0
        return self.runs/self.matches
p=CricketPlayer("Virat Kohil",13000,290)
p.display()

# Task 18: Movie Database
# Create a Movie class with:
# Movie Name
# Hero Name
# Rating
# Create 3 movie objects and display movies having rating greater than 8.

class Movie:
    def __init__(self,movie_name,hero_name,rating):
        self.movie_name=movie_name
        self.hero_name=hero_name
        self.rating=rating
    def display(self):
        print(self.moive_name,self.hero_name,self.rating)
m=Movie()    



