#A. Data Types & Literals (1–7)
#
# Store your name, age, and city in variables and print them.
from ast import Add


name="Sunitha"
age=21
city="Nandyal"
print("Name:",name)
print("Age:",age)
print("City:",city)


#Create a tuple with 5 fruits and print the third fruit.
tuple1=("banana","apple","pineapple","custard apple","orange")
print(tuple1[2])

#Store marks of 3 subjects in a dictionary and print the marks of "Math".
marks={"math":80,"english":89,"telugu":90}
print(marks["math"])

       
#Write a program to store 3 integers and print their sum.
nums=[1,2,3]
sum=0
for i in nums:
    sum+=i
print(sum)
# a=reduce(lambda x,y:x+y,nums)
# print(a)
#Create a tuple of 4 colors and print the last color.
tup=("Pink","blue","black","red")
print(tup[-1])
# for i in tup:
#     if i==len(tup)-1:
#         print(i)
#Store employee details (name, ID, department) in a dictionary and print the department.
details={"name":"sunitha","Id":101,"department":"data science"}
print(details["department"])
#Write a program to store a float, int, and string in variables and print their types.
f=213.90
i=8
s="sunitha"
print(type(f))
print(type(i))
print(type(s))


#B. Strings (8–14)
#Check if "Python" is present in "I am learning Python programming".
s="I am learning Python programming"
if "python" in s:
    print("Found python in given string")


#Print only the first 5 characters of "Hello World".
s="Hello World"
print(s[:6:1])
# for i in range(5):
#     print(s[i],end="")
#Concatenate two strings "Good" and "Morning".
s1="Good"
s2="Morning"
print(s1+s2)
#Count how many times "o" appears in "Hello World".
count=0
s="hello world"
for i in s:
    if i=='o':
        count+=1
print(count)
#Reverse the string "Python".
s="python"
print(s[::-1])
#Check if a string entered by the user starts with "A".
# string=input("Enter a string:")
# if string.startswith("a"):
#     print("yes")
#Check if "apple" contains "p".
string="apple"
for i in string:
    if i=='p':
        print("yes string contains 'p'")

#C. Operators (15–21)
#Take two numbers and print their sum, difference, product, and quotient.
a=10
b=12
print("sum:",a+b)
print("difference:",a-b)
print("product:",a*b)
print("division:",a/b)
#Check if 25 is greater than 20 and less than 30.
a=25
if a >20 and a<30:
    print("yes")
#Ask the user for two numbers. Print "Both are positive" if both are greater than 0, else "At least one is not positive".
# c=int(input("Enter a number:"))
# d=int(input("Enter a number:"))
# if c and d >0:
#     print("both are positive")
# else:
#     print("one is not positive")
#Check if a number is divisible by both 2 and 3.
# num=int(input("enter a number:"))
# if num%2==0 and num%3==0:
#     print("give number is divisible by both 2 and 3")
#Check if "a" is in "apple".
s3="apple"
if "a" in s3:
    print("yes")
#Check if a number is between 1 and 100 (inclusive).
# num=int(input("Enter a number:"))
# if num <=100:
#     print("given number is between 1 and 100")
#Compare two strings "cat" and "dog".
s="cat"
s1="dog"
print(s==s1)

#D. Conditional Statements (22–30)
#Check if a number is positive, negative, or zero.
i=int(input("Enter a number:"))
if i==0:
    print("given number is zero")
elif i>0:
    print("Positive")
else:
    print("Negative")
#Ask the user to enter their age. If age ≥ 18, print "Eligible to vote", else "Not eligible".
# age=int(input("Enter your age:"))
# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible")
#Check if a given number is even or odd.
# num=int(input("Enter a number:"))
# if num%2==0:
#     print("Even number")
# else:
#     print("Odd number")
#Input a number and check if it is divisible by 5.
# num=int(input("Enter a number:"))
# if num%5==0:
#     print(" given number is divisible by 5")
#Ask the user to enter a password. If it matches ""admin123, print "Access Granted", else "Access Denied".
# password=input("Enter a password:")
# if password=="admin123":
#     print("Access Granted")
# else:
#     print("Access Denied")
#Check if a character entered by the user is a vowel or consonant.
# ch=input("Enter a character:")
# s=['a','e','i','o','u']
# if ch in s:
#     print("given character is vowel")
# else:
#     print("given character is consonant")

#Check if a given year is a leap year.
# year=int(input("Enter  a year:"))
# if year%4==0 and year%100!=0 and year%400==0:
#     print("Leap year")
# else:
#     print("not a leap year")
#Ask the user for marks. Print "Grade A" if marks ≥ 90, "Grade B" if ≥ 75, "Grade C" if ≥ 50, else "Fail".
# marks=int(input("Enter marks:"))
# if marks>=90:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# elif marks>=50:
#     print("Grade C")
# else:
#     print("Fail")
#Check if a number is odd and greater than 50.
# number=int(input("Enter a number"))
# if number%2!=0 and number<=50:
#     print("Given number is odd and greater than 50")

#E. Tuples (31–35)
#Create a tuple with 6 numbers. Print the largest and smallest number.
t=(1,2,3,4,5,6)
print(max(t))
print(min(t))
# l=0

# s=0
# for i in t:
#     if i>l:
#         l=1
#         print(l)
#     elif i<s:
#         s=i
#         print(s)

#Check if 50 exists in (10, 20, 30, 40, 50, 60).
t=(10, 20, 30, 40, 50, 60)
if  50 in t:
    print("yes 50 is print")
#Store 5 colors in a tuple. Ask the user to enter a color name. Check if it exists.
t=("red","green","blue","black","yellow")
u=input("Enter a color name:")
if u in t:
    print("exists")

#Print the length of a tuple (1, 2, 3, 4, 5).
t=(1, 2, 3, 4, 5)
print(len(t))
#Create a tuple with 4 strings. Print them one by one using indexing.
t=("Sun","sunitha","suni","sunii")
for i in t:
    print(i)

print(t[0])
print(t[1])
print(t[2])
print(t[3])
#F. Dictionaries (36–41)
#Create a dictionary with 3 countries as keys and their capitals as values. Print the capital of "India".
di={"india":"Delhi","France":"Paris","russia":"Moscow"}
print(di["india"])
#Add a new country-capital pair to an existing dictionary.
di.update({"japan":"Tokyo"})
print(di)
#Given a dictionary of student marks, check if "Anita" is present as a key. If yes, print her marks.
student={"Anitha":80,"sunitha":90}
print(student["Anitha"])
#Create a dictionary with usernames and passwords. Ask the user to enter a username and password. If both match, print "Login Successful", else "Login Failed".
# di={"sunitha":"admin123","sun":"admin1"}
# username=input("Enter username:")
# password=input("Enter password")
# if username in di and di[username]==password:
#     print("login successful")
# else:
#     print("login failed")


#Print all keys of a dictionary.
print(di.keys())
#Create a dictionary with 3 items and their prices. Ask the user to enter an item name. Print the price if it exists, else "Item not found".
# di={"pen":100,"box":200,"book":150}
# user=input("Enter input:")
# price=di.get[user]
# if i  in price:
#     print("Item found")
# else:
#     print("Item not found")

#G. Lists (42–61)
#Create a list of 5 numbers and print the first and last elements.
lis=[1,2,3,4,5]
print(lis[0])
print(lis[-1])
#Add a new element to a list.
lis.append(6)
print(lis)
#Remove an element from a list.
lis.remove(6)
print(lis)
#Create a list of 4 colors and print its length.
colors=["pink","red","blue","black"]
print(len(lis))

#Check if "red" exists in a list of colors.
if "red" in colors:
    print("Exists")
#Print the second to fourth elements of a list.
print(lis[2:4])
#Print the last 3 elements of a list.
print(lis[-3:])
#Store 5 names in a list and print the name at index 2.
names=["sun","sunitha","suni","Angel","Grace"]
print(names[2])
#Reverse a list.
reverse = names[::-1]
print(reverse)
#Replace the second element of a list with "Python".
names.insert(1,"python")
print(names)
#Create a list of 5 numbers. Check if a number entered by the user exists in the list.

# l=[]
# print("Enter 5 number:")
# for i in range(5):
#     num=int(input("Enter a number:"))
#     l.append(num)
# val=int(input("Enter a number to check:"))
# if  val in l:
#     print("Exists")
# else:
#     print("Not exsists")

#Store 5 subjects in a list. Ask the user to enter a subject name. If it exists, print "Found", else "Not Found".
# l=[]
# print("Enter 5 subjects:")
# for i in range(5):
#     sub=input("Enter a subject:")
#     l.append(sub)
# val=input("Enter a subject to check:")
# if  val in l:
#     print("Found")
# else:
#     print("Not found")

#Create a list of marks. If the average is ≥ 50, print "Pass", else "Fail".
# marks=[]
# sum=0
# print("Enter marks of 5 subjects:")
# for i in range(5):
#     mark=int(input("Enter marks:"))
#     marks.append(mark)
#     sum+=mark
# average=sum/len(marks)
# if average>=50:
#     print("Pass")
# else:
#     print("Fail")
#Check if the first and last elements of a list are equal.
l=[2,3,4,5,6,2]
if l[0]==l[-1]:
    print("first and last are same elements")
#Create a list of strings. Print "Contains Python" if "Python" is in the list.
s=["python","maths","Java","c"]
for i in s:
    if i=="python":
        print("Conatins python")
#Create a list of 5 numbers. Print the largest and smallest numbers.
l=[2,3,4,5,6,2]
large=l[0]
small=l[0]
for i in l:
    if i>large:
        large=i
    if i<small:
        small=i
print(large)
print(small)

#Count how many times "apple" appears in a list.
l=["apple","banana","apple","orange","apple"]
count=0
for i in l:
    if i=="apple":
        count+=1
print(count)
#Store 5 numbers in a list. Print only the even numbers.
# l=[]
# print("Enter 5 numbers:")
# for i in range(5):
#     num=int(input("Enter a number:"))
#     if num%2==0:
#          l.append(num)
# print("even numbers are:",l)

#Check if a list is empty.
l=[]
if not l:
    print("list is empty")

#Create a list of 5 numbers. If all numbers are positive, print "All Positive", else "Contains Negative".
l=[1,-2,3,4,-5]
p=True
for i in l:
    if i<0:
        p=False
        break
if p:
    print("All positive")
else:
    print("Contains negative")
#H. Mixed Concept Questions (62–70)
#Store 5 numbers in a tuple. Check if the number 10 is present.
# t=()
# for i in range(5):
#     num=int(input("Enter a number:"))
#     t+=(num,)
# if 10 in t:
#     print("yes 10 is presnt ")

#Create a dictionary with student names as keys and marks as values. Check if "Rahul" is in the dictionary.
d={"Sunitha":90,"anitha":80,"rahul":70}
for i in d:
    if i=="rahul":
        print("yes rahul is present")
#Take a string input and check if it contains "Python".
# st=input("Enter a string:")
# if "python" in st:
#     print("yes ")
#Ask the user for two numbers. Print "Equal" if they are equal, "First is greater" if the first is larger, else "Second is greater".
# n1=int(input("Enter a number:"))
# n2=int(input("Enter a number:"))
# if n1==n2:
#     print("Equal")
# elif n1>n2:
#     print("n1 is greater")
# elif n2>n1:
#     print("n2 is greater")
#Check if a number is divisible by 2 OR 5.
# num=int(input("Enter a number:"))
# if num%2==0:
#     print("given number is divisible by 2")
# elif num%5==0:
#     print("given number is divisible by 5")
# elif num%2==0 and num%5==0:
#     print("given number is divisible by both 2 and 5")
# else:
#     print("given number is noit divisible by 2 and 5")
#Create a dictionary with 3 employees and their salaries. Print the salary of the employee with the highest pay.
s={"sunitha":50000,"anitha":60000,"rahul":55000}
high=0
for i  in s.values():
    if i>high:
        high=i
print(high)
#Check if a string entered by the user contains both "a" and "b".
# s=input("Enter a string:")
# if "a" and "b" in s:
#     print("given string contains both a and b")
#Store 5 subjects in a tuple. Ask the user to enter a subject name. If it exists, print "Subject Found", else "Not Found".
# sub=()
# for i in range(5):
#     s=input("Enter a subject:")
#     sub+=(s,)
# v=input("Enter a subject to check:")
# if v in sub:
#     print("Subject found")
# else:
#     print("Not found")
#Check if a number entered by the user is both even and between 10 and 50.
# num=int(input("Enter a number:"))
# if num%2==0 and  num in range(10,51):
#     print("given number is even and between 10 and 50")


#I. Strings – Built-in Practice (71–80)
#Convert a string to uppercase.
# str=input("Enter a string:").lower()
# print(str.upper())
#Convert a string to lowercase.
# str=input("Enter a string:").upper()
# print(str.lower())
#Remove extra spaces from a string.
# str=input("Enter a string:").strip()
# print(str)
#Replace one word in a string with another.
# str="python is a programming language"
# str=str.replace("python","java")
# print(str)

#Split a string into a list of words.
str="python is a programming language"
words=str.split()
print(words)
#Join a list of words into a single string.
words=["python","is","a","programming","language"]
s=" ".join(words)
print(s)
#Count how many times a letter appears in a string.
str="hello world"
count=0
for i in str:
    if i=='l':
        count+=1
print(count)
#Find the position of a character in a string.
str="hello world"
p=str.find("o")
print(p)
#Check if a string contains only letters and numbers.
# str=input("Enter a string:")
# if str.isalpha():
#     print("given string contains only letters")
# elif str.isdigit():
#     print("given string contains only numbers")



#Check if a string contains only digits.
# str=input("Enter a string:")
# if str.isdigit():
#     print("given string contains only digits")

#Lists – Built-in Practice (81–90)
#add an element to the end of a list
l=[1,2,3,4]
l.append(6)
print(l)
# multiple elements to a list at once.
l1=[1,2,3]
l.extend(l1)
print(l)
#Insert an element at a specific position in a list.
l.insert(4,8)
print(l)
#Remove a specific element from a list.
l.remove(6)
print(l)
#Remove the last element from a list.
l.pop()
print(l)
#Arrange the elements of a list in ascending order.
l=[1,8,6,4,3]
for i in range(len(l)-1):
    for j in range(1,len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

#Reverse the order of elements in a list.
l.reverse()
print(l)
for i in range(len(l)-1):
    for j in range(1,len(l)-i-1):
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
#Find the position of an element in a list.
print(l.index(8))
#Count how many times a number appears in a list.
l=[1,2,3,3,4,5,6]
print(l.count(3))


#Remove all elements from a list.
l.clear()
print(l)

# K. Dictionaries – Built-in Practice (91–100)
# Print all keys of a dictionary.
d={1:"sun",2:3+7j,3:"sunitha",4:6.908}
print(d.keys())
# Print all values of a dictionary.
print(d.values())
# Print all key-value pairs of a dictionary.
print(d.items())
# Access the value of a key safely.
print(d.get(2))
# Add a new key-value pair to a dictionary.
d.update({5:"Java"})
print(d)
# Remove a specific key from a dictionary.
d.pop(4)
print(d)
# Remove the last inserted item from a dictionary.
d.pop(5)
print(d)
# Check if a key exists in a dictionary.
for i in d:
    if i==2:
        print("key exists")
# Create a dictionary with given keys and the same default value.
keys=[1,2,3,4]
defaultvalue="Sunitha"
dic=dict.fromkeys(keys,defaultvalue)
print(dic)
# Make a copy of a dictionary.
d=dic.copy()
print(d)