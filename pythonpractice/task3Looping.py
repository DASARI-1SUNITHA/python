# 3.Python Coding Statements
# 🔹 Break & Continue Practice
# Write a loop that prints numbers from 1 to 10, but stops completely when the number is 6.
for i in range(1,10):
    if i==6:
        break
    print(i)
# Write a loop that prints numbers from 1 to 10, but skips printing the number 5.
for i in range(1,10):
    if i==5:
        continue
    print(i)
# Write a loop that prints only odd numbers between 1 and 10 using continue.
for i in range(1,10):
    if i%2==0:
        continue
    print(i)
# Write a loop that prints numbers from 1 to 20, but breaks when the number is divisible by 7.
for i in range(1,20):
    if i%7==0:
        break
    print(i)

# Write a loop that prints numbers from 1 to 10, but skips all even numbers.
for i in range(1,10):
    if i%2==0:
        continue
    print(i)
# Write a loop that prints numbers from 1 to 10, but stops when the number is greater than 8.
for i in range(1,10):
    if i>8:
        break
    print(i)
# Write a loop that prints numbers from 1 to 15, but skips numbers divisible by 3.
for i in range(1,15):
    if i%3==0:
        continue
    print(i)
# Write a loop that prints numbers from 1 to 10, but breaks when the number is equal to 4.
for i in range(1,10):
    if i==4:
        break
    print(i)
# Write a loop that prints numbers from 1 to 10, but skips printing 2 and 7.
for i in range(1,10):
    if i==2 and i==7:
        continue
    print(i)
# Write a loop that prints numbers from 1 to 10, but breaks when the number is 9.
for i in range(1,10):
    if i ==9:
        break
    print(i)
# 🔹 Ternary Operator Practice
# Write a program that checks if a number is even or odd using a ternary operator.
x=int(input("enter a number:"))
print("even" if x%2==0 else "odd")
# Write a program that prints "Positive" if a number is greater than 0, otherwise "Negative or Zero".
print("positive" if x>0 else "negative")
# Write a program that prints "Adult" if age ≥ 18, otherwise "Minor".
print("Adult" if x>=18 else "Minor")
# Write a program that prints "Pass" if marks ≥ 40, otherwise "Fail".
marks=int(input("enter marks:"))
print('pass' if marks>=40 else "Fail")
# Write a program that prints "Big" if a number > 100, otherwise "Small".
print("Big" if x>100 else "Small")
# Write a program that prints "Equal" if two numbers are the same, otherwise "Not Equal".
n=1
n1=6
print("equal" if n==n1 else "Not equal")
# Write a program that prints "Divisible by 5" if a number is divisible by 5, otherwise "Not Divisible".
print('divisible by 5' if x%5==0 else "not divisible")
# Write a program that prints "Leap Year" if a year is divisible by 4, otherwise "Not Leap Year".
year=2345
print("leap year" if (year%4==0 and year%100!=0) or (year%400==0) else 'not leap year')
# Write a program that prints "Yes" if a number is positive, otherwise "No".
print('yes positive' if x>0 else 'No')
# Write a program that prints "First" if a > b, otherwise "Second".
a=8
b=6
print("first" if a>b else "Second")

