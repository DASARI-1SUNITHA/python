#  2 . Python Coding Questions 
# 🔄 Lists
# Write a loop that prints only the even numbers from a list.
# l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     if i%2==0:
#         print(i)

# Given a list of integers, use a loop and conditionals to separate positive and negative numbers into two new lists.
# l=[1,-9,-8,3,4,5]
# p=[]
# n=[]
# for i in l:
#     if i>0:
#         p.append(i)
#     if i<0:
#         n.append(i)
# print(p)
# print(n)
# Write a loop that prints "Big" if a list element is greater than 50, otherwise print "Small".
# l=[56,90,43,67]
# for i in l:
#     if i>50:
#         print("Big")
#     else:
#         print("small")
# # Use a loop to count how many elements in a list are divisible by 3.
# l=[3,9,6,15,89,765]
# # count=0
# # for i in l:
# #     if i%3==0:
# #         count+=1
# # print(count)
# # Write a loop that replaces all negative numbers in a list with 0.
# # l=[1,-9,-8,3,4,5]
# # for i in range(len(l)):
# #     if l[i]<0:
# #         l[i]=0
# # print(l)
# # 🔄 Tuples
# # Write a loop that prints elements of a tuple only if they are greater than 10.
# # t=(6,10,73,89)
# # for i in t:
# #     if i>10:
# #         print(i)
# # Given a tuple of numbers, use a loop to print "Odd" or "Even" for each element.
# t=(23,43,89,765)
# # for i in t:
# #     if i %2==0:
# #         print("even")
# #     else:
# #         print("odd")
# # Write a loop that finds the largest odd number in a tuple.
# l=t[0]
# for i in t:
#     if i%2!=0 and i>l:
#             l=i
# print(l)
# # Use a loop to count how many elements in a tuple are prime numbers.
# t=(1,2,3,4,5,6,7,8,9,10)
# count=0
# for i in t:
#     factors=0
#     for i in range(1,i+1):
#       if i%i==0:
#             factors+=1
#     if factors==2:
#          count+=1
# print(count)
    


# # Write a loop that prints "High" if a tuple element is above 100, otherwise "Low".
# t=(789,87,345,7896)
# for i in t:
#     if i>100:
#         print("high")
#     else:
#          print('low')
# # 🔄 Sets
# # Write a loop that prints only odd numbers from a set.
# s={1,2,4,3,5,6,7}
# for i in s:
#     if i%2!=0:
#         print(i)
# # Given a set of integers, use a loop to remove all numbers less than 5.
# s={1,2,4,3,5,6,7}
# for i in s:
#     if i<5:
#         continue
#     print(i)
# # Write a loop that prints "Found" if the set contains the number 10, otherwise "Not Found".
# s={1,28,5,9,10,90,80}
# if 10 in s:
#     print('found')
# else:
#     print("not found")
# # Use a loop to build a new set containing only squares of even numbers from another set.
# s={1,2,3,4,5,6,7}
# s1=set()
# for i in s:
#     if i%2==0:
#         s1.add(i**2)
# print(s1)


# # Write a loop that prints "Duplicate" if an element already exists in a set while iterating through a list.
# s={1,2,3,1,4,5}
# s1={}
# for i in s:
#     if i in s1:
#         print("duplicate")
#     else:s1={i,}

# # 🔄 Strings
# # Write a loop that counts vowels in a string using conditionals.
# s="sunitha grace"
# v='aeiouAEIOU'
# count=0
# for i in s:
#     if i in v:
#         count+=1
# print(count)
# # # Use a loop to print "Digit" if a character is numeric, otherwise print "Letter".
# # string1=input("enter a character:")
# # for i in string1: 
# #     if i.isdigit():
# #         print('numbers')
# #     else:
# #         print('letters')
# # Write a loop that prints only uppercase characters from a string.
# s="SUNitHA"
# for i in s:
#     if i.isupper():
#         print(i)
# # Given a string, use a loop to count how many times "a" appears.
# string1='sunasdtsa'
# count=0
# for i in string1:
#     if i=='a':
#         count+=1
# print(count)
# # Write a loop that prints "Palindrome" if a string reads the same forward and backward, otherwise "Not Palindrome".
# s="madam"
# s1=s
# if s==s1[::-1]:
#     print('palindrome')
# else:
#     print("not a palindrome")
# # 🔄 Dictionaries
# # Write a loop that prints dictionary keys only if their values are greater than 50.
# d={'a':80,'b':90,'c':34}
# for k,v in d.items():
#     if v>50:
#         print(k,v)
# # Given a dictionary of student names and marks, use a loop to print "Pass" if marks ≥ 40, otherwise "Fail".
# d={'Alice': 85, 'Bob': 92, 'Charlie': 78}
# for k,v in d.items():
#     if v>=40:
#         print('pass')
#     else:
#         print('fail')
# # Write a loop that counts how many dictionary values are even.
# count=0
# for k,v in d.items():
#     if v%2==0:
#         count+=1
# print(count)
# # Use a loop to print "Starts with A" if a key begins with "A", otherwise print "Other".
# for k ,v in d.items():
#     if k.startswith('A'):
#         print("begins with a")
#     else:
#         print('other')
# # Write a loop that finds the maximum value in a dictionary and prints the corresponding key.m
# for k,v in d.items():
#     max_val=d["Alice"]
#     max_key=""
#     if v>max_val:
#         max_val=v
#         max_key=k
# print(max_key,max_val)
    


# # 🔄 Mixed Loops + Conditionals
# # Write a loop that prints numbers from 1 to 20, but skips multiples of 5.
# for i in range(1,20):
#     if i%5==0:
#         continue
#     print(i)
# Use a loop to print numbers from 1 to 15, but stop when you reach 10.
# for i in range(1,15):
#     if i==10:
#         break
#     print(i)
# Write a loop that prints "Prime" if a number is prime, otherwise "Not Prime", for numbers 2–20.
for i in range(2,21):
    factors=0
    for j in range(1,i+1):
        if i%j==0:
            factors+=1
    if factors==2:
        print("Prime")
    else:
        print("Not Prime")


#Use a loop to print squares of numbers from 1 to 10, but only if the square is less than 50.
for i in range(1,11):
    if i**2<50:
        print(i**2,end=" ")
#Write a loop that iterates through a list of tuples (name, age) and prints "Adult" if age ≥ 18, otherwise "Minor".
people = [("Alice", 30), ("Bob", 15), ("Charlie", 25), ("David", 10)]
for name ,age  in people:
    if age>=18:
        print("Adult")
    else:
        print("Minor")