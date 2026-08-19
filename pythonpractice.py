# Level 1: Python Basics (25 Questions)
# Print "Hello World".
# print('hello world')
# Take two numbers and print their sum.
# a=2
# b=3
# print(a+b)
# Swap two numbers (with third variable).
# a=2
# b=3
# # c=a
# # a=b
# # b=c
# # print(a,b)
# # Swap two numbers (without third variable).
# a,b=b,a
# print(a,b)
# Find the largest of two numbers.
# a=5
# b=8
# if a>b:
#     print('a is large',a)
# else:
#     print('b is large',b)

# Find the largest of three numbers.
# a=5
# b=9
# c=8
# if a>b and a>c:
#     print('a is large',a)
# elif b>a and b>c:
#     print('b is large',b)
# else:
#     print('c is large',c)
# Check if a number is even or odd.
# n=5
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")
# Check if a number is positive, negative, or zero.
# n=0
# if n==0:
#     print("Given num is zero")
# elif n>0:
#     print("positive")
# else:
#     print("Negative")
# # Find the factorial of a number.
# n=5
# fact=1
# while n>0:
#     fact*=n
#     n-=1
# print(fact)

# Find the square and cube of a number.
# n=2
# print(n**2)
# print(n**3)
# # Calculate the area of a circle.
# r=10
# pi=3.14
# print("area :",pi*r**2)

# # Convert Celsius to Fahrenheit.
# c=27
# print("fahrenheit:",(c*9/5)+32)
# # Convert Fahrenheit to Celsius.
# f=10
# print("celsius:",(5/9)*(f-32))
# # Check if a year is a leap year.
# year=2020
# if year%100!=0 and year%4==0:
#     print("leap year")
# elif year%400==0:
#     print("not a leap year")
# # Print all numbers from 1 to N.
# n=10
# for i in range(n):
#     print(i)
# Print all even numbers from 1 to N.
# n=20
# for i in range(n):
#     if i%2==0:
#         print(i)
# # Print all odd numbers from 1 to N.
# n=20
# for i in range(n):
#     if i%2!=0:
#         print(i)
# # Find the sum of first N natural numbers.
# n=10
# sum=0
# for i in range(n):
#     sum=(n*(n+1)/2)
# print(sum)
# Find the multiplication table of a number.
# n=2
# for i in range(1,11):
#     print(n,"*",i,'=',n*i)
# Reverse an integer.
# n=321
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)
# Count digits in a number.
# count=0
# n=1234
# for i in str(n):
#     count+=1
# print(count)
# Find the sum of digits.
# n=123
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n//=10
# print(sum)

# Find the product of digits.
# n=1234
# prod=1
# while n>0:
#     digit =n%10
#     prod*=digit
#     n//=10
# print(prod)
# Check if a number is divisible by both 3 and 5.
# n=15
# if n%3==0 and n%5==0:
#     print('given  num is divisible by 3 & 5')
# Find the ASCII value of a character.
# ch='a'
# print(ord(ch))
# Level 2: Pattern Questions (20 Questions)
# Right triangle
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()

# Inverted triangle
# n=5
# for i in range(n):
#     for j in range(n-i ):
#         print("*",end=" ")
#     print( )
# Pyramid
# for i in range(5+1):

#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()


    
# # Inverted pyramid
# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()
# # Diamond

# # Hollow square
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# # Hollow rectangle
# r=4
# c=6
# for i in range(r):
#     for j in range(c):
#         if i==0 or i==r-1 or j==0 or j==c-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# Pascal triangle

# Floyd triangle
# Number pyramid
# Character pyramid
# Butterfly pattern
# Sandglass pattern
# Hollow diamond
# X pattern
# Cross pattern
# Zigzag pattern
# Rhombus
# Hourglass
# Spiral pattern
# Level 3: String Questions (35 Questions)
# Reverse a string.
# s='banana'
# for i in range(len(s)-1,-1,-1):
#     print(s[i])
# Check palindrome.
# a=1234321
# temp=a
# rev=0
# while a>0:
#     digit=a%10
#     rev=rev*10+digit
#     a//=10
# if temp==rev:
#     print("palindrome")
# else:
#     print('not a palindrome')

# # Count vowels.
# s='sunitha'
# count=0
# vowels='aeiouAEIOU'
# for i  in s:
#     if i in vowels:
#         count+=1
# print(count)


# Count consonants.
# s='sunitha'
# v='aeiouAEIOU'
# count=0
# for i in s:
#     if i not in v:
#         count+=1
# print(count)
# # Count words.
# w='i love python programming'
# count=0
# for i in w.split():
#     count+=1
# print(count)
# Count uppercase letters.
# s='pYTHon'
# count=0
# for i in s:
#     if i.isupper():
#         count+=1
# print(count)
# # Count lowercase letters.
# s='sunITHA'
# count=0
# for i in s:
#     if i.islower():
#         count+=1
# print(count)
# Count digits.
# d='1234sun'
# count=0
# for i in d:
#     if i.isdigit():
#         count+=1
# print(count)

# Count special characters.
# s='@#$%231SUM'
# specialchar='@#$!%^&*'
# count=0
# for i in s:
#     if i in specialchar:
#         count+=1
# print(count)

# # Find frequency of each character.
# freq={}
# s='banana'
# for i in s: 
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)
# Find first non-repeating character.
# s='banana'
# freq={}
# for i  in s:
#     if i not in freq:
#         freq[i]=1
#     else:freq[i]+=1
# for i in s:
#     if freq[i]==1:
#         print(i)
# Find first repeating character.
# s='banana'
# freq={}
# for i in s:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for i in s:
#     if freq[i]>=2:
#         first_repeat=i
# print(first_repeat)

# Remove duplicate characters.
# s='banana'
# freq=[]
# for i in s:
#     if i not in freq:
#         freq.append(i)
# print(freq)

# Remove spaces.
# w='i love python programming'
# s=''
# for i in w:
#     if i!=" ":
#         s+=i
# print(s)


# Replace spaces with hyphens.
# w='i love python programming'
# s=w.replace(" ","-")
# print(s)
# Check anagram.
# s='listen'
# s1='silent'
# if sorted(s)==sorted(s1):
#     print("anagram")
# else:
#     print("not anagram")
# Compress string (aaabbcc → a3b2c2).
# s='aaabbaacceec' 
# count=1
# result=""
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         count+=1
#     else:
#         result+=s[i]+str(count)
#         count=1
# result+=s[-1]+str(count)
# print(result)
# # Expand compressed string.
# s='a3b2c2'
# result="" 
# i=0
# while i<len(s):
#     char=s[i]
#     count=int(s[i+1])
#     result+=char*count
#     i+=2
# print(result)


# Find longest word.
# s= 'i love programming'
# l=""
# for i in s.split():
#     if len(i)>len(l):
#         l=i
# print(l)
    

# Find shortest word.
# s= 'i love programming'
# l=""
# for i in s.split():
#     if len(i)<len(l):
#         l=i
# print(l)
# Reverse each word.
# s= 'i love programming'
# res=[]
# for word in s.split():
#     resversed=""
#     for i in range(len(s)-1,-1-1):
#         reversed+=word[i]
#     res.append(reversed)
# result=" ".join(res)
# print(result)
# # Reverse word order.
# words=s.split()
# result="".join(words[::-1])
# print(S)
# # Capitalize every word.
# s='i love python'
# print(s.title())
# # Toggle case. 
# print(s.swapcase())
# # Check substring.
# subst='python'
# print( subst in s)
# Find substring occurrences.
# s='banana'
# sub='an'
# print(s.count(sub))
# Find longest common prefix.
# Longest palindrome substring.
# Longest substring without repeating characters.
# Check rotation of strings.
# Remove vowels.
# Count each word frequency.
# Remove punctuation.
# Compare two strings lexicographically.
# Find all permutations of a string.
# Level 4: List Questions (40 Questions)
li=[9,8,7,6,6,4,2,3,4]
# # Find maximum.
# print(l.max())

# # Find minimum.
# print(l.min())
# # Find second largest.
# l=0
# sec =0
# for i in li:
#     if i >l:
#         sec=l
#         l=i
#     elif i>sec and i!=l:
#         sec=i
# print(sec)

# Find second smallest.
# s=s[0]
# sec =s[0]
# for i in li:
#     if i <s:
#         sec=l
#         s=i
#     elif i<sec and i!=s:
#         sec=i
# print(sec)
# # Remove duplicates.
# l=[]
# for i in li:
#     if i not in l:
#         l.append(i)
# print(l)
# # Find duplicate elements.
# l=[1,2,3,2,4,2,5,7]
# l1={}
# for i in  l:
#     if i not in l1:
#         l1[i]=1
#     else:
#         l1[i]+=1
# for i in l1:
#     if l1[i]>=2:
#         print(l1[i])

# Merge two lists.
l=[1,2,3,6,7]
l1=[2,3,4]
# l.extend(l1)
# print(l)
# Find common elements.
l3=l.intersection(l1)
print(l3)
# Union of lists.
l.union(l1)
pri
# Difference of lists.
# Rotate left.
# Rotate right.
# Reverse a list.
# Sort ascending.
# Sort descending.
# Bubble sort.
# Selection sort.
# Insertion sort.
# Merge sort.
# Quick sort.
# Binary search.
# Linear search.
# Move zeros to end.
# Move negatives to one side.
# Find missing number.
# Find repeating number.
# Find unique element.
# Two Sum.
# Three Sum.
# Kadane's Algorithm.
# Maximum product subarray.
# Majority element.
# Intersection of three arrays.
# Merge intervals.
# Product except self.
# Rotate matrix.
# Spiral matrix.
# Diagonal traversal.
# Flatten nested list.
# Chunk a list into equal sizes.
# Level 5: Tuple Questions (10 Questions)
# Convert tuple to list.
# Convert list to tuple.
# Count occurrences.
# Find index.
# Nested tuple traversal.
# Tuple unpacking.
# Swap values using tuple.
# Find repeated values.
# Concatenate tuples.
# Slice tuples.
# Level 6: Dictio
# Level 6: Dictionary Questions (30 Questions)
# Count character frequency.
# Count word frequency.
# Merge dictionaries.
# Invert dictionary.
# Sort by key.
# Sort by value.
# Find key with maximum value.
# Find key with minimum value.
# Group words by first letter.
# Group anagrams.
# Nested dictionary traversal.
# Convert list to dictionary.
# Dictionary comprehension.
# Remove duplicate values.
# Update nested dictionary.
# Merge employee records.
# Find duplicate values.
# Flatten nested dictionary.
# JSON to dictionary.
# Dictionary to JSON.
# Student marks management.
# Inventory management.
# Phone book application.
# Word count.
# Frequency of numbers.
# Reverse key-value pairs.
# Find common keys.
# Find missing keys.
# Merge two dictionaries with duplicate keys.
# Cache implementation using dictionary.
# Level 7: Set Questions (15 Questions)
# Union
# Intersection
# Difference
# Symmetric difference
# Remove duplicates
# Check subset
# Check superset
# Common elements
# Unique words
# Unique characters
# Find missing numbers
# Remove duplicates from string
# Student attendance comparison
# Recommendation system using sets
# Find pair with target sum
# Level 8: Functions & Recursion (20 Questions)
# Factorial using recursion.
# Fibonacci using recursion.
# GCD using recursion.
# Power using recursion.
# Sum of digits using recursion.
# Reverse string recursively.
# Tower of Hanoi.
# Binary search recursively.
# Merge sort recursively.
# Quick sort recursively.
# Lambda to sort list.
# Lambda with multiple keys.
# map() to square numbers.
# filter() even numbers.
# reduce() product.
# Decorator for execution time.
# Decorator for logging.
# Generator for Fibonacci.
# Prime number generator.
# Infinite number generator.
# Level 9: OOP (25 Questions)
# Student class.
# Employee class.
# Bank account.
# ATM system.
# Shopping cart.
# Hospital management.
# Library management.
# Vehicle inheritance.
# Animal inheritance.
# Multiple inheritance.
# Multilevel inheritance.
# Hybrid inheritance.
# Method overriding.
# Operator overloading.
# Encapsulation example.
# Abstraction using abstract classes.
# Polymorphism.
# Singleton class.
# Logger class.
# Inventory system.
# E-commerce product class.
# Restaurant billing.
# Movie ticket booking.
# Hotel booking.
# Online banking.