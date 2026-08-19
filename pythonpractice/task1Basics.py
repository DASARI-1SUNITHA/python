# Python Basic Programs

# A. Data Types & Literals (1–7)
# Store your name, age, and city in variables and print them.
# print("name:",'sunitha')
# print("age:",22)
# print("city:",'Nandyal')
# # Create a tuple with 5 fruits and print the third fruit.
# fruits=('orange','custard apple','banana','pine apple','fig')
# print(fruits[2])
# Store marks of 3 subjects in a dictionary and print the marks of "Math".
# marks={'maths':75,'science':80,'history':93}
# print(marks['maths'])
# Write a program to store 3 integers and print their sum.
# list1=[1,2,3]
# sum=0
# for i in list1:
#     sum+=i
# print(sum)
# Create a tuple of 4 colors and print the last color.
# tuple1=('balck','blue','yellow','red')
# print(tuple1[-1])
# Store employee details (name, ID, department) in a dictionary and print the department.
# employee_details={'name':'sunitha','ID':'21091A3253','department':'IT'}
# print(employee_details['department'])
# Write a program to store a float, int, and string in variables and print their types.
# float_value=23.40987
# int_value=90
# string_value='sunitha'
# print(type(float_value))
# print(type(int_value))
# print(type(string_value))
# B. Strings (8–14)
# Check if "Python" is present in "I am learning Python programming".
# string1="I am learning Python programming"
# if 'Python' in string1:
#     print("present")
# # Print only the first 5 characters of "Hello World".
# string2="Hello World"
# print(string2[0:6])
# Concatenate two strings "Good" and "Morning".
# str1="Good"
# str2="Morning"
# print(str1+str2)
# Count how many times "o" appears in "Hello World".
# string3="Hello World"
# count=0
# for i in string3:
#     if i=='o':
#         count+=1
# print(count)
# Reverse the string "Python".
# string1="Python"
# print(string1[::-1])
# Check if a string entered by the user starts with "A".
# string4=input("Enter a string:")
# if string4.startswith("A"):
#     print('YES .user extered string starts with A')
# Check if "apple" contains "p".
# string5='apple'
# for i in string5:
#     if i=='p':
#         print('p  character is in apple word')
# C. Operators (15–21)
# Take two numbers and print their sum, difference, product, and quotient.
# num1=9
# num2=8
# print(num1+num2,num1-num2,num1*num2,num1/num2)
# Check if 25 is greater than 20 and less than 30.
# num=int(input("enter a number:"))
# if num>20 and num<30:
#     print("given  number is greater than 20 and less than 30")
# # Ask the user for two numbers. Print "Both are positive" if both are greater than 0, else "At least one is not positive".
# num1=int(input("enter a number1:"))
# num2=int(input("enter a number2:"))
# if num1>0 and num2>0:
#     print("Both are positive")
# else:
#     print("At least one is not positive")

# Check if a number is divisible by both 2 and 3.
# num=int(input("Enter a number:"))
# if num%2==0 and num%3==0:
#     print('given number is divisble by 2 and 3')

# # Check if "a" is in "apple".
# string1="apple"
# if 'a' in string1:
#     print('a is in apple')
# Check if a number is between 1 and 100 (inclusive).
# num=int(input("Enter a number:"))
# if num<=100:
#     print('given num is in between 1 and 100')
# # Compare two strings "cat" and "dog".
# str1='cat'
# str2='dog'
# if str1==str2:
#     print('Both are equal')
# D. Conditional Statements (22–30)
# # Check if a number is positive, negative, or zero.
# num=int(input("enter a number:"))
# if num>0:
#     print('Positive')
# elif num<0:
#     print("Negative")
# else:
#     print("zero")
# Ask the user to enter their age. If age ≥ 18, print "Eligible to vote", else "Not eligible".
# age=int(input("Enter age of a person:"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("Not Eligible")
# Check if a given number is even or odd.
# num=int(input("Enter a number:"))
# if num%2==0:
#     print("Even number")
# else:
#     print("Odd number")
# Input a number and check if it is divisible by 5.
# num=int(input("Enter a number:"))
# if num%5==0:
#     print('Divisble by 5')
# Ask the user to enter a password. If it matches "admin123", print "Access Granted", else "Access Denied".
# password=input("Enter a passsword:")
# if password=='admin123':
#     print("access granted")
# else:
#     print("access Denied")
# Check if a character entered by the user is a vowel or consonant.
# cha=input("enter a character:")
# vowels='AEIOUaeiou'
# if cha in vowels:
#     print('vowel')
# else:
#     print('consonant')
# Check if a given year is a leap year.
# year=int(input("enter a year:"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print('leap year')
# else:
#     print('not a leap year')
# # Ask the user for marks. Print "Grade A" if marks ≥ 90, "Grade B" if ≥ 75, "Grade C" if ≥ 50, else "Fail".
# marks=int(input("enter marks of a person:"))
# if marks>=90:
#     print("Grade A")
# elif marks>=75:
#     print('Grade B')
# elif marks>=50:
#     print("Grade C")
# else:
#     print("Fail")

# Check if a (number is odd and greater than 50.
# num=int(input("enter a number:"))
# if num%2!=0 and num>50:
#     print("number is odd and greater than 50")
# E. Tuples (31–35)
# # Create a tuple with 6 numbers. Print the largest and smallest number.
# t=(1,2,3,4,5,6)
# large=t[0]
# small=t[0]
# for i in t:
#     if i>large:
#         large=i
#     elif i<small:
#         small=i
# print(large,small)
# Check if 50 exists in (10, 20, 30, 40, 50, 60).
# t=(10, 20, 30, 40, 50, 60)
# if 50 in t:
#     print("exists")
# # Store 5 colors in a tuple. Ask the user to enter a color name. Check if it exists.
# t=[]
# colors=input("Enter colors:")
# for i in range(5):
#     colors=input("Enter colors:")
#     t.append(i)
# tuple1=tuple(t)
# color=int(input("enter a color name:"))
# if color in colors:
#     print('exists')

# Print the length of a tuple (1, 2, 3, 4, 5).
# t=(1,2,3,4,5)
# print(len(t))
# Create a tuple with 4 strings. Print them one by one using indexing.
# t=('a','we','Sdf','rtg')
# for i in t:
#     print(i)
# F. Dictionaries (36–41)
# Create a dictionary with 3 countries as keys and their capitals as values. Print the capital of "India".
# dic={'india':'delhi','japan':'tokyo','usa':'america'}
# # print(dic['india'])
# # Add a new country-capital pair to an existing dictionary.
# dic1={'wer':'hjk'}
# dic.update(dic1)
# print(dic)
# Given a dictionary of student marks, check if "Anita" is present as a key. If yes, print her marks.
# marks={'asd':40,'anitha':60}
# for k ,v in marks.items():
#     if k=='anitha':
#         print("exists",v)
# # Create a dictionary with usernames and passwords. Ask the user to enter a username and password. If both match, print "Login Successful", else "Login Failed".
# username=input("Enter a usename:")
# password=input("enter a password:")
# dic={'anitha':'admin123','user':'user123'}
# if username in dic and  dic[username]==password:
#     print("login successful")
# else:
#     print("not successful")
# # Print all keys of a dictionary.
# print(dic.keys())
# Create a dictionary with 3 items and their prices. Ask the user to enter an item name. Print the price if it exists, else "Item not found".
# dic={'pen':234,'book':23456,'box':7890}
# user_items=input("Enter an item name:")
# if user_items in dic:
#     print("exists")
# else:
#     print("item not exists")


# G. Lists (42–61)
# Create a list of 5 numbers and print the first and last elements.
# l=[1,2,3,4,5]
# print(l[0])
# print(l[-1])
# # Add a new element to a list.
# l.append(8)
# print(l)
# # Remove an element from a list.
# l.remove(3)
# print(l)
# # Create a list of 4 colors and print its length.
# l=['black','blue','red','yellow']
# print(len(l))
# # Check if "red" exists in a list of colors.
# for i in l:
#     if i=='red':
#         print('exists')

# Print the second to fourth elements of a list.
# print(l[1])
# print(l[3])
# # Print the last 3 elements of a list.
# print(l[1:5])
# Store 5 names in a list and print the name at index 2.
# names=['a','b','c','d','e']
# # print(names[2])
# # Reverse a list.
# print(names[::-1])
# for i in range(len(names)-1,-1,-1):
#     print(names[i])
# # Replace the second element of a list with "Python".
# l[1]=('python')
# print(l)
# # Create a list of 5 numbers. Check if a number entered by the user exists in the list.
# l=[1,2,3,4,5]
# num=int(input("enter a number:"))
# for i in l:
#     if i==num:
#         print('exists')
# Store 5 subjects in a list. Ask the user to enter a subject name. If it exists, print "Found", else "Not Found".
# subjects=[]
# for i in range(5):
#     subject=input("Enter subject name:")
#     subjects.append(subject)
# user_sub=input("Enter a subject name:")
# if user_sub in subjects:
#     print('found')
# else:
#     print("not found")
# Create a list of marks. If the average is ≥ 50, print "Pass", else "Fail".
# marks=[]
# for i in range(5):
#     mark=input("Enter subject marks:")
#     marks.append(mark)
# user_marks=int(input("Enter a subject marks:"))
# if user_marks>=50:
#     print('pass')
# else:
#     print("fail")
# Check if the first and last elements of a list are equal.
# l=[1,2,3,4,5,1]
# if l[0]==l[-1]:
#     print('equal')
# else:
#     print("not equal")
# Create a list of strings. Print "Contains Python" if "Python" is in the list.
# l=['a','python']
# for i in l:
#     if i=='python':
#         print('contains python')

# # Create a list of 5 numbers. Print the largest and smallest numbers.
# l=[6,7,0,9,8,7,6]
# large=l[0]
# s=l[0]
# for i in l:
#     if i>large:
#         large=i
#     elif i<s:
#         s=i
# print(large,s)
# # Count how many times "apple" appears in a list.
# l= ["apple", "banana", "apple", "orange", "apple"]
# count=0
# for i in l:
#     if i=='apple':
#         count+=1
# print(count)
# # Store 5 numbers in a list. Print only the even numbers.
# l=[]
# # for i in range(5):
# #     nums=int(input("enter numbers:"))
# #     l.append(nums)
# # for i in l:
# #     if i%2==0:
# #         print(i)
# # Check if a list is empty.
# if not l:
#     print('list is empty')
# Create a list of 5 numbers. If all numbers are positive, print "All Positive", else "Contains Negative".
# l=[1,-2,3,4,-5]
# p=True
# for i in l:
#     if i<0:
#         p=False
#         break
# if p:
#     print("All positive")
# else:
#     print("Contains negative")
# H. Mixed Concept Questions (62–70)
# Store 5 numbers in a tuple. Check if the number 10 is present.
# l=()
# for i in range(5):
#     nums=int(input("enter numbers:"))
#     l+=(nums,)
# for i in l:
#     if i==10:
#         print('10 is present')

# Create a dictionary with student names as keys and marks as values. Check if "Rahul" is in the dictionary.
# dic={'rahul':89,'sun':87}
# for k,v in dic.items():
#     if k=='rahul':
#         print('exists')
# Take a string input and check if it contains "Python".
# string1='i like python programming'
# for i in string1:
#     if i=='python':
#         print('contains python')
# # Ask the user for two numbers. Print "Equal" if they are equal, "First is greater" if the first is larger, else "Second is greater".
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# if num1>num2:
#     print('num1 is greater')
# else:
#     print("num2 is greater")
# # Check if a number is divisible by 2 OR 5.
# num=int(input("Enter a number:"))
# if num%2==0:
#     print('divisible by 2')
# elif num%5==0:
#     print("divisible by 5")


# Create a dictionary with 3 employees and their salaries. Print the salary of the employee with the highest pay.
# dic={'a':50000,'b':89000,'c':67800}
# max_sal=0
# max_key=""
# for k,v in dic.items():
#     if v>max_sal:
#         max_sal=v
#         max_key=k
# print(max_key,max_sal)
# # Check if a string entered by the user contains both "a" and "b".
# string1="banana" 
# if 'a' and 'b' in string1:
#         print("contains both a and b")

# # Store 5 subjects in a tuple. Ask the user to enter a subject name. If it exists, print "Subject Found", else "Not Found".
# sub=[]
# for i in range(5):
#     subjects=input("enter subject names:")
#     sub.append(subjects)
# user_sub=input("Enter a number:")
# if user_sub in sub:
#     print("subject found")
# else:
#     print("not found")
# # Check if a number entered by the user is both even and between 10 and 50.
# num=int(input("enter a number:"))
# if num%2==0 and num in range(10,50):
#         print('even and betweeen 10 and 50')
# I. Strings – Built-in Practice (71–80)
# Convert a string to uppercase.
# s='sun'
# print(s.upper())
# # Convert a string to lowercase.
# s="PYTHON"
# print(s.lower())
# # Remove extra spaces from a string.
# s='     sun     '
# print(s.strip())
# Replace one word in a string with another.
# s='i like python'
# s1=s.replace('i','u')
# print(s1)
# Split a string into a list of words.
s='i like python'
print(s.split())

# Join a list of words into a single string.
s=['i', 'like', 'python']
s1="" 
for i in s:
    s1+=i
print(s1)
# Count how many times a letter appears in a string.
# string1='Programs Python Python314 python'
# count=0
# for i in string1:
#     if i=='P':
#         count+=1
# print(count)
# Find the position of a character in a string.
# a='python programming'
# print(a.find('g'))
# # Check if a string contains only letters and numbers.
# s='123sum'
# if s.isdigit():
#     print('numbers')
# if s.isalpha():
#     print('letters')
# else:
#     print('alpha numeric')
# Check if a string contains only digits.
# s='123456' 
# if s.isdigit():
#     print('digits') 
# J. Lists – Built-in Practice (81–90)
# Add an element to the end of a list.
# l=[12,90,36,56]
# l.append(78)
# print(l)
# Add multiple elements to a list at once.
l=[12,3,4,5,6,7]
# l1=[5,7,8,9]
# l.extend(l1)
# print(l)
# Insert an element at a specific position in a list.
l.insert(4,9)
print(l)
# Remove a specific element from a list.
l.remove(12)
print(l)
# Remove the last element from a list.
l.pop()
print(l)
# Arrange the elements of a list in ascending order.
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
print(l)
# Reverse the order of elements in a list.
for i in range(len(l)-1,-1,-1):
    print(l[i])
# Find the position of an element in a list.
print(l.index(4))
# Count how many times a number appears in a list.
l=[1,2,3,4,1,2,1,3]
print(l.count(1))
# Remove all elements from a list.
l.clear()
print(l)
# K. Dictionaries – Built-in Practice (91–100)
# Print all keys of a dictionary.
dic={'a':3,'b':5,'c':6}
print(dic.keys())
# Print all values of a dictionary.
print(dic.values())
# Print all key-value pairs of a dictionary.
print(dic.items())
# Access the value of a key safely.
print(dic['a'])
# Add a new key-value pair to a dictionary.
dic1={'d':90}
dic.update(dic1)
print(dic)
# Remove a specific key from a dictionary.
dic.pop('a')
print(dic)
# Remove the last inserted item from a dictionary.
dic.pop('d')
print(dic)
# Check if a key exists in a dictionary.
for k,v in dic.items():
    if k=='a':
        print('key exists')
# Create a dictionary with given keys and the same default value.
keys=[1,2,3,4,5]
default_value="sun"
dic1=dict.fromkeys(keys,default_value)
print(dic1)
    
# Make a copy of a dictionary.
dic2={}
dic1.copy()
print(dic2)



