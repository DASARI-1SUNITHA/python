# Level 3 — Encapsulation
# 9. Bank Account Security
# Create a BankAccount class where balance cannot be directly modified.
# Implement:
# deposit()
# withdraw()
# get_balance()
# Use a private variable.
# Concept: encapsulation, private attributes.
class BankAccount:
    def __init__(self,balance,amount):
        self.__amount=amount
        self.balance=balance
    def deposit(self):
        self.balance+=self.__amount
        print(self.balance)
    def withdraw(self):
        if 0<self.__amount<=self.balance:
            self.balance-=self.__amount
            print(self.__amount)
    def get_balance(self):
        print(self.balance)
b=BankAccount(200000,4000)
b.deposit()
b.withdraw()
b.get_balance()

# 10. Employee Salary

# Create an Employee class with private salary.
# Implement:
# set_salary()
# get_salary()
# Do not allow negative salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = 0
        self.set_salary(salary)

    def set_salary(self, amount):
        if amount >= 0:
            self.__salary = amount
        else:
            print("Error: Salary cannot be negative!")

    def get_salary(self):
        return self.__salary
emp = Employee("Alice", 50000)
print(emp.get_salary())
emp.set_salary(55000)
print(emp.get_salary())

# 11. Student Marks

# Create a Student class with private marks.
# Rules:
# marks >= 0
# marks <= 100
# If invalid marks are provided, display an error
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = 0
        self.set_marks(marks)

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Error: Marks must be between 0 and 100!")
    def get_marks(self):
        return self.__marks
student = Student("Sunitha", 85)
print(student.get_marks())

student.set_marks(105)
print(student.get_marks())
# Level 4 — Inheritance
# 12. Animal → Dog
# Create:
# Animal
#    ↓
#   Dog
# Animal should have:
# eat()
# sleep()
# Dog should have:
# bark()
class Animal:
    def eat(self):
        print('eating')
    def sleep(self):
        print('sleeping')
class Dog(Animal):
    def bark(self):
        print('barks')
dog=Dog()
dog.eat()
dog.sleep()
dog.bark()

# 13. Vehicle → Car
# Create:
# Vehicle
#    ↓
# Car
# Vehicle:
# start()
# stop()
# Car:
# drive()
class Vehicle:
    def start(self):
        print("Vehicle started")
    def stop(self):
        print("Vehicle stopped")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
my_car = Car()
my_car.start()
my_car.drive()
my_car.stop()
    
# 14. Employee → Manager
# Create:
# Employee
#    ↓
# Manager

# Employee:
# name
# salary
# display()
# Manager:
# team_size
# display()
# Use super().
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name,self.salary)
class Manager(employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size
    def dispaly(self):
        super().dispaly()
        print(self.team_size)
mng=Manager('sunitha',896325,5)
mng.display()
# 15. Multilevel Inheritance
# Create:
# Person
#    ↓
# Employee
#    ↓
# Manager
# Each class should have its own attributes and methods.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
    def work(self):
        print(self.employee_id,self.name)
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department
    def manage(self):
        print(self.department)
mgr = Manager("Bob", 40, "E101", "Sales")
mgr.introduce()
mgr.work()
mgr.manage()       
    

# 16. Multiple Inheritance

# Create:

# Father
# Mother
#    ↓
# Child

# Give Father and Mother different methods.

# Make Child inherit from both.
class Father:
    def garden(self):
        print("Gardening skill inherited from Father")
class Mother:
    def cook(self):
        print("Cooking skill inherited from Mother")

class Child(Father, Mother):
    def play(self):
        print("Child is playing")
c=Child()
c.garden()
c.cook()
c.play()
# Level 5 — Polymorphism
# 17. Method Overriding

# Create:

# Animal
#    ↓
# Dog
#    ↓
# Cat

# Each class should have:

# sound()

# Output:

# Animal → Some sound
# Dog → Bark
# Cat → Meow
class Animal:
    def sound(self):
        print("Some sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
animal = Animal()
dog = Dog()
cat = Cat()
animal.sound()
dog.sound()
cat.sound()

# 18. Polymorphism with Different Classes

# Create:

# Dog
# Cat
# Cow

# Each should have:

# sound()

# Create a list:

# animals = [Dog(), Cat(), Cow()]

# Loop through the list and call:

# animal.sound()
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
class Cow:
    def sound(self):
        print("Moo")
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.sound()
# 19. Payment System

# Create:

# CreditCard
# UPI
# NetBanking

# Each class should have:

# pay(amount)

# Call the same method for all payment types.
class CreditCard:
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")
class UPI:
    def pay(self, amount):
        print(f"Paid ${amount} using UPI")
class NetBanking:
    def pay(self, amount):
        print(f"Paid ${amount} using NetBanking")
def process_payment(payment_method, amount):
    payment_method.pay(amount)
methods = [CreditCard(), UPI(), NetBanking()]
for method in methods:
    process_payment(method, 100)
# Level 6 — Abstraction
# 20. Shape
# Create an abstract class:
# Shape
# with an abstract method:
# area()
# Create:
# Circle
# Rectangle
# Triangle

# Each class should implement area().
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
circle = Circle(5)
rectangle = Rectangle(4, 5)
triangle = Triangle(3, 6)
print(circle.area())
print(rectangle.area())
print(triangle.area())
# 21. Vehicle Abstraction
# Create an abstract class:
# Vehicle
# with:
# start()
# stop()
# Implement:
# Car
# Bike
# Bus
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car engine started")
    def stop(self):
        print("Car engine stopped")
class Bike(Vehicle):
    def start(self):
        print("Bike kicked into gear")

    def stop(self):
        print("Bike engine turned off")
class Bus(Vehicle):
    def start(self):
        print("Bus heavy engine ignited")

    def stop(self):
        print("Bus heavy engine shutdown")
vehicles = [Car(), Bike(), Bus()]
for v in vehicles:
    v.start()
    v.stop()

# 22. Employee Abstraction
# Create an abstract class:
# Employee
# with:
# calculate_salary()
# Create:
# FullTimeEmployee
# PartTimeEmployee
# ContractEmployee

# Each should calculate salary differently.
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
class ContractEmployee(Employee):
    def __init__(self, project_fee):
        self.project_fee = project_fee
    def calculate_salary(self):
        return self.project_fee
employees = [FullTimeEmployee(5000), PartTimeEmployee(20, 80), ContractEmployee(3000)]
for emp in employees:
    print(emp.calculate_salary())

# 23. Class Method

# Create a Student class with:

# school_name

# Create a class method to change the school name.
class Student:
    school_name="GSEMS"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_school(cls,new_name):
        cls.school_name=new_name
s=Student("Sunitha")
print(Student.school_name)
Student.change_school("gsems")
print(Student.school_name)
# 24. Static Method

# Create a Calculator class with static methods:
# add()
# subtract()
# multiply()
# divide()
# No object-specific data should be required.
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def divide(a, b):
        if b!=0:
            return a/b
        else:
            print("cannot divide by zero")
print(Calculator.add(10, 5))
print(Calculator.subtract(10, 5))
print(Calculator.multiply(10, 5))
print(Calculator.divide(10, 5))
# 25. Employee Factory
# Create an Employee class.
# Create a class method:
# from_string()
# Input:
# "John-50000-IT"
# Output should create:
# name = John
# salary = 50000
# department = IT
class StaffEmployee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    @classmethod
    def  from_string(cls,emp_str):
        name, salary, department = emp_str.split("-")
        return cls(name, int(salary), department)
emp_obj = StaffEmployee.from_string("John-50000-IT")
print(emp_obj.name)
print(emp_obj.salary)
print(emp_obj.department)

# 26. __str__()
# Create a Student class.
# When you execute:
# print(student)
# It should display
# Name: Sunitha, Age: 22, Marks: 85
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def __str__(self):
        return f'name:{self.name},age :{self.name},marks:{self.marks}'
s=student("sunitha",22,90)
print(s)
# 27. __len__()
# Create a class Team.
# If:
# team = Team(["A", "B", "C", "D"])
# then:
# len(team)
# should return
# 4
class Team:
    def __init__(self,members):
        self.members=members
    def __len__(self):
        return len(self.members)
team=Team(['A','B','E',"Sun"])
print(len(team))

# 28. __add__()
# Create a Salary class.
# Example:
# s1 = Salary(50000)
# s2 = Salary(30000)
# Then:
# s3 = s1 + s2
# should produce:
# 80000
class salary:
    def __init__(self,amount):
        self.amount=amount
    def __add__(self,other):
        return self.amount+other.amount
s1=salary(500000)
s2=salary(300000)
s3=s1+s2
print(s3)
