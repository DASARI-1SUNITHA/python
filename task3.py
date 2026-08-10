# Python Coding Statements
# 🔹 Break & Continue Practice
# Write a loop that prints numbers from 1 to 10, but stops completely when the number is 6.

for i in range(1,11):
    if i==6:
        break
    print(i,end=" ")
# Write a loop that prints numbers from 1 to 10, but skips printing the number 5.
for i in range(1,11):
    if i==5:
        continue
    print(i,end=" ")
# Write a loop that prints only odd numbers between 1 and 10 using continue.
for i in range(1,11):
    if i%2==0:
        continue
    print(i)
# Write a loop that prints numbers from 1 to 20, but breaks when the number is divisible by 7.
for i in range(1,21):
    if i%7==0:
        break
    print(i)
# Write a loop that prints numbers from 1 to 10, but skips all even numbers.
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

# Write a loop that prints numbers from 1 to 10, but stops when the number is greater than 8.
for i in range(1,11):
    if i>8:
        break
    print(i)
# Write a loop that prints numbers from 1 to 15, but skips numbers divisible by 3.
for i in range(1,16):
    if i%3==0:
        continue
    print(i)

# Write a loop that prints numbers from 1 to 10, but breaks when the number is equal to 4.
for i in range(1,11):
    if i==4:
        break
    print(i)
# Write a loop that prints numbers from 1 to 10, but skips printing 2 and 7.
for i in range(1,11):
    if i==2 or i==7:
        continue
    print(i,end=" ")
    

# Write a loop that prints numbers from 1 to 10, but breaks when the number is 9.
for i in range(1,11):
    if i==9:
        break
    print(i,end=" ")
# 🔹 Ternary Operator Practice
# Write a program that checks if a number is even or odd using a ternary operator.
num=int(input("Enter a integer:"))
print("even") if num%2==0 else print("Odd")
# Write a program that prints "Positive" if a number is greater than 0, otherwise "Negative or Zero".
number=int(input("Enter a number"))
print("Positive ") if num>0 else print("Negative or Zero")
# Write a program that prints "Adult" if age ≥ 18, otherwise "Minor".
age=int(input("Enter your age:"))
print("Adult") if age>=18 else print("Minor")
# Write a program that prints "Pass" if marks ≥ 40, otherwise "Fail".2
marks=int(input("Enter your marks:"))
print("Pass") if marks>=40 else print("Fail")
# Write a program that prints "Big" if a number > 100, otherwise "Small".
num=int(input("Enter a number:"))
print("BIG" if num>100 else "Small")
# Write a program that prints "Equal" if two numbers are the same, otherwise "Not Equal".
num1=int(input("Enter 1st integer:"))
num2=int(input("Enter 2nd integer:"))
print("Equal" if num1==num2 else "Not Equal")
# Write a program that prints "Divisible by 5" if a number is divisible by 5, otherwise "Not Divisible".
number=int(input("Enter a number:"))
print("Divisible by 5" if number%5==0 else "Not Divisible")
# Write a program that prints "Leap Year" if a year is divisible by 4, otherwise "Not Leap Year".
year=int(input("Enter a year:"))
print("Leap year" if year%4==0 else "Not leap year")
# Write a program that prints "Yes" if a number is positive, otherwise "No".
num=int(input("Enter a number:"))
print("Yes" if num>0 else "No")
# Write a program that prints "First" if a > b, otherwise "Second".
a=int(input("Enter first integer:"))
b=int(input("Enter second integer:"))
print("First" if a>b else "second")