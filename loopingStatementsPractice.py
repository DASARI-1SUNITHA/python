# # Level 1 — Conditional Statements: Practice using if, elif, and else.
# # Positive, Negative, or Zero:Take a number as input.Check whether it is positive, negative, or zero.
# num1=8
# if num1>0:
#     print("positive")
# elif num1<0:
#     print("Negative")
# else:,
#     print("zero")
# # Even or Odd: Take an integer,Print whether it is even or odd.
# num2=6
# if num2%2==0:
#     print("Even")
# elif num2%2!=0:
#     print("Odd")
# # Largest of Two Numbers:Take two numbers.Print the larger number.
# a=4
# b=8
# if a>b:
#     print('a is larger')
# elif b>a:
#     print('b is larger')
# # Largest of Three Numbers:Take three numbers.Find the largest without using max().
# a=2
# b=5
# c=9
# if a>b and a>c:
#     print("a is larger")
# elif b>a and b>c:
#     print('b is larger')
# else:
#     print('c is larger')

# # Smallest of Three Numbers:Find the smallest number without using min().
# if a<b and b<c:
#     print('a is small')
# elif b<a and b<c:
#     print('b is small')
# else:
#     print('c is small')
# # Voting Eligibility:Input age.If age ≥ 18, print "Eligible".Otherwise print "Not Eligible".
# age=22
# if age>=18:
#     print("Eligible")
# else:
#     print("Not eligible")
# # Pass or Fail:Input marks.If marks ≥ 40 → Pass.Otherwise → Fail.
# marks=49
# if marks>=40 :
#     print("pass")
# else:
#     print("fail")
# # Grade Calculator
# # 90–100 → A,80–89 → B,70–79 → C,60–69 → D,Below 60 → F
# marks=75
# if marks>=90 and marks<=100:#90<=marks<=100
#     print("grade A")
# elif marks>=80 and marks<=89:
#     print("grade B")
# elif marks>=70 and marks<=79:
#     print("grade C")
# elif marks>60 and marks <69:
#     print("grade D")
# elif marks<60:
#     print("grade F")
# # Divisible by 5:Check whether a number is divisible by 5.
# num=35
# if num%5==0:
#     print('divisible by 5')
# else:
#     print('not divisible by 5')

# # Divisible by Both 3 and 5:heck whether a number is divisible by both 3 and 5.
# if num%3==0 and num%5==0:
#     print('number is divisile by both 3 and 5')
# else:
#     print('not divisible by 3 and 5')

# # 🟡 Level 2 — Conditional + Operators
# # Leap Year:Check whether a given year is a leap year.
# year=2345
# if (year%4==0 and year%100!=0) or year%400==0:
#     print('leap year')
# else:
#     print("not a leap year")
# # Character Type:Input one character.
# # Determine whether it is:
# # uppercase, lowercase,digit,special character
# ch='s'
# if ch.isupper():
#     print('uppercase')
# elif ch.islower():
#     print('lowercase')
# elif ch.isdigit():
#     print('digit')
# else:
#     print("special character")
# #Vowel or Consonant:Input a character.Check whether it is a vowel or consonant.
# ch1='a'

# vowels='aeiouAEIOU'
# if ch.isaplha():
#     if ch1 in vowels:
#         print('vowel')
#     else:
#         print('consonant')
# else:
#     print('not a letter')
# # Profit or Loss input cost price and selling price.Determine profit, loss, or no profit/no loss.
# cost_price=100
# selling_price=120
# if cost_price<selling_price:
#     print('profit')
# elif cost_price>selling_price:
#     print("loss")
# else:
#     print("no profit/no loss")
# # Electricity Bill:Calculate the bill based on units:
# # 0–100 → ₹2/unit,101–200 → ₹5/unit,Above 200 → ₹8/unit
# units=200
# bill=0
# if units<=100:
#     print("bill=",units*2)
# elif units<=200:
#     print("bill=",(100*2)+((units-100)*5))
# elif units>200:
#     print("bill=",(100*2)+(100*5)+((units-200)*8))

# # Simple Calculator:Input two numbers and an operator.
# # Support:+, -, *, /, %
# a=3
# b=5
# op=input("enter operaned:")
# if op=="+":
#     print(a+b)
# elif op=='-':
#     print(a-b)
# elif op=='*':
#     print(a*b)
# elif op=='/':
#     print(a/b)
# elif op=='%':
#     print(a%b)
# # Age Category:0–12 → Child,13–19 → Teenager,20–59 → Adult,# 60+ → Senior Citizen
# age=67
# if age<=12:
#     print('child')9
# elif age>=13 and age<=19:#13<=age<=19
#     print('Teenager')
# elif age>=20 and age<=59:
#     print('adult') 
# elif age>60:
#     print('senior Citizen')
# # Triangle Validity :Input three angles.
# # Check whether they can form a triangle.
# angle1=45
# angle2=45
# angle3=90
# sum=180
# if angle1+angle2+angle3==sum and angle1>0 and angle2>0 and angle3>0:
#     print('forms a triangle')
# else:
#     print('does  not form a triangle')
# # Triangle Type:Input three sides.
# # Determine:Equilateral,Isosceles,Scalene
# s1=4
# s2=5
# s3=6
# if s1==s2==s3:
#     print('equilateral triangle')
# elif s1==s2 or s2==s3 or s1==s3:
#     print('isosceles triangle')
# else:
#     print("scalene triangle")
# # Username and Password
# # Store a username and password.
# d={'sunitha':'admin123'}
# # Ask the user for both.Print "Login successful" if both match.
# username=input('enter username:')
# password=input("enter  password:")
# if username in d and d[username]==password:
#     print("login successsful")
# # else:
# #     print("invalid user")
# # # Level 3 — for and while Loops
# # # Print numbers from 1 to 10.
# # for i in range(1,11):
# #     print(i,end=" ")

# # # Print numbers from 10 to 1.
# # for i in range(10,0,-1):
# #     print(i,end=" ")
# # num=10
# # while num>0:
# #     print(num)
# #     num-=1o0
# # # Print all even numbers from 1 to 50.
# # for i in range(1,50):
# #     if i%2==0:
# #         print(i)
# # # Print bffv  odd numbers from 1 to 50.
# # for i in range(1,50):
# #     if i%2!=0:
# #         print(i)
# # # Print numbers divisible by 3 between 1 and 100.
# # for i in range(1,100):
# #     if i%3==0:
# #         print(i)
# # # Find the sum of numbers from 1 to N.Example:Input: 5
# # # Output: 15
# n=5
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)
    
    
# # Find the sum of even numbers from 1 to N.
# n=10
# sum=0
# for i in range(1,n+1):h g
# #     if i%2==0:
# #         sum+=i
# # print(sum)
# # # Find the sum of odd numbers from 1 to N.
# # n=10
# # sum=0
# # for i in range(1,n+1):
# #     if i%2!=0:
# #         sum+=i
# # print(sum)  
# # # Print the multiplication table of a number.
# # # Input: 5 # 5 x 1 = 5
# # n=5
# # for i in range(1,11):
# #     print(n,'X',i,'=',n*i)

# # Count the number of digits in a number.
# # Input: 12345,Output: 5
# n=12345
# count=0
# while n>0:
#     count+=1
#     n//=10
# print(count)
# # 🟠 Level 4 — Number Problems Using Loops
# # Reverse a Number:Input: 12345,Output: 54321
# n=12345
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)
# # Palindrome Number:Input: 121,Output: Palindrome
# n=121
# temp=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# if rev==temp:
#     print('palindrome')
# else:
#     print("not a palindrome")
# # Sum of Digits:Input: 1234,Output: 10
# n=1234
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n//=10
# print(sum)
# # Product of Digits:Input: 123,Output: 6
# n=123
# prod=1
# while n>0:
#     digit=n%10
#     prod=prod*digit
#     n//=10
# print(prod)
# # Count Even Digits:Input: 123456,Output: 3
# n=123456
# count=0
# while n>0:
#     digit=n%10
#     if n%2==0:
#         count+=1
#     n//=10
# print(count)
# # Count Odd Digits:Input: 123456,Output: 3
# n=123456
# count=0
# while n>0:
#     digit=n%10
#     if n%2!=0:
#         count+=1
#     n//=10
# print(count)
# # Find Largest Digit:Input: 58329,Output: 9
# n=58329
# large=0
# while n>0:
#     digit=n%10
#     if digit>large:
#         large=digit
#     n//=10
# print(large)
# # Find Smallest Digit:Input: 58329,Output: 2
# # n=58329
# # small=float('inf')
# # while n>0:
# #     digit=n%10
# #     if digit<small:
# #         small=digit
# #     n//=10
# # print(small)
# # Factorial:Input: 5,Output: 120
# n=5
# fact=1
# while n>=0:
#     fact*=n
#     n-1
# print(fact)

# # Power of a Number:Input:2 5 Output:32
# base=2
# power=5
# res=1
# for i in range(power):
#     res*=base
# print(res)

# # 🔴 Level 5 — Prime Number Problems
# # Check whether a number is prime.
# n=5
# for i in range(2,int(n**0.5)+1):
#     if n%i==0:
#         print('not prime')
#         break
#     else:
#         print(" prime")
# # Print all prime numbers between 1 and 100.
# for i in range(2,100):
#     is_prime=True
#     for j in range(2,int(n**0.5)+1):
#         if n%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(n)


# # Count the number of primes between 1 and N.
# count=0
# for n in range(2,n+1): 
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             break
#     else:
#         count+=1
# print(count)
# # Find the sum of prime numbers between 1 and N.
# n=10
# sum=0
# for n in range(1,n+1):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             break
#     else:
#         sum+=n
# print(sum)
# # Find the first N prime numbers.
# n=5
# prime_list=[]
# while len(prime_list)<n:
#     for i in range(2,int(2**0.5)+1):
#         if n%i==0:
#             break
#     else:
#         prime_list.append(n)

# Check whether a number is composite.

# Print all factors of a number.:Input: 12,Output:1 2 3 4 6 12
# Count the number of factors.
# Find the sum of factors.
# Check whether a number is a perfect number.
# Example:6 → 1 + 2 + 3 = 6
# 🟣 Level 6 — Nested Loops / Patterns

# These are very common in beginner coding interviews.

# *
# **
# ***
# ****
# *****
n=6
for i in range(n):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("------------------------")
# *****
# ****
# ***
# **
# *
n=5
for i in range(n,0,-1):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("------------------------")
# 1
# 12
# 123
# 1234
# 12345
n=5
for i in range(n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("-----------------------")
# 1
# 22
# 333
# 4444
# 55555
for i in range(n):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print(" -----------------------")
# 12345
# 1234
# 123
# 12
# 1
for i in range(n,0,-1):
    for j in range(i+1):
        print(j,end=" ")
    print()
print('-----------------')
#     *
#    **
#   ***
#  ****
# *****
# *****
#  ****
#   ***
#    **
#     *
# 1
# 23
# 456
# 78910
for i in range(n):
    for j in range(1,i+1):
        print(i,end=" " )   
    print()
# A
# AB
# ABC
# ABCD
# ABCDE
for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end="")
    print()

# A
# BB
# CCC
# DDDD
# EEEEE
for i in range(1,6):
    for j in range(i):
        print(chr(64+i),end="")
    print()