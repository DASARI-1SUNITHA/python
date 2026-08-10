# Lists
#Write a loop that prints only the even numbers from a list.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
for i in num:
    if i%2==0:
        print(i,end=" ")

# ans=list(filter(lambda x:x%2==0,num))
# print(ans)
# a=(lambda x:x%2==0,num)
# print(a)

#Given a list of integers, use a loop and conditionals to separate positive and negative numbers into two new lists.
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
p=[]
n=[]
for i in range(len(numbers)):
    if numbers[i]>0:
        p.append(numbers[i])
    elif numbers[i]<0:
        n.append(numbers[i])
print(n)
print(p)

#Write a loop that prints "Big" if a list element is greater than 50, otherwise print "Small".
values = [10, 55, 30, 80, 25]
for i in range(len(values)):
    if values[i]>50:
        print("Big",i)
    else:
        print("Small")
#Use a loop to count how many elements in a list are divisible by 3.
count=0
for i in values:
    if i%3==0:
        print(i)
        count+=1
print(count)
#Write a loop that replaces all negative numbers in a list with 0.
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10,0]
n=[]
for i in range(len(numbers)):
    if numbers[i]<0 and numbers[i]==0:
        n.append(numbers[i])
print(n)
#Tuples
#Write a loop that prints elements of a tuple only if they are greater than 10.
my_tuple = (5, 15, 25, 3, 8)
for i in my_tuple:
    if i>10:
        print(i)
#Given a tuple of numbers, use a loop to print "Odd" or "Even" for each element.
numbers = (1, 2, 3, 4, 5)
for i in numbers:
    if i%2==0:
        print("Even")
    else:
        print("Odd")
#Write a loop that finds the largest odd number in a tuple.
my_tuple = (5, 15, 25, 3, 8)
largest_odd=0
for i in my_tuple:
    if i%2!=0 and i>largest_odd:
        largest_odd=i
print(largest_odd)
# ans=max(filter(lambda x :x%2!=0,my_tuple))
# print(ans)
#Use a loop to count how many elements in a tuple are prime numbers.
t=(2, 3, 4, 5, 6, 7, 8, 9, 10)
count=0
for i in t:
    if i<=1:
       continue
    fact=0
    for i in range(1,i+1):
        if i%i==0:
            fact+=1
    if fact==2:
        count+=1
print(count)
#Write a loop that prints "High" if a tuple element is above 100, otherwise "Low".
t=(50, 150, 30, 200, 80)
for i in t:
    if i>100:
        print("High")
    else:
        print("Low")

# Sets
#Write a loop that prints only odd numbers from a set.
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in s:
    if i%2!=0:
        print(i,end=" ")
# ans=list(filter(lambda x:x%2!=0,s))
# print(ans)
#Given a set of integers, use a loop to remove all numbers less than 5.
s={1,2,3,4,5,8,9,7}
for i in s:
    if i>=5:
        print(i,end=" ")

#Write a loop that prints "Found" if the set contains the number 10, otherwise "Not Found".
s={1,2,3,4,5,6,7,8,9,10,11}
if 10 in s:
    print('Found')
else:
    print("not found")
# ans=lambda x:"found" if 10 in s else "not found"
# print(ans(s))
#Use a loop to build a new set containing only squares of even numbers from another set.
s={1,2,3,4,5,6,7,8,9,10}
set=set()
for i in s:
    if i%2==0:
        set.add(i**2)
print(set)
# a=filter(lambda x:x%2==0 and x**2,s)
# print(a)
#Write a loop that prints "Duplicate" if an element already exists in a set while iterating through a list
l=[1,2,6,4,3,5]
s={}
for i in l:
    if i in s:
        print("Duplicate")
    else:
        s={i,}
# Strings

#Write a loop that counts vowels in a string using conditionals.
s="hello world"
count=0
for i in s:
    if i in ['a','e','i','o','u']:
        count+=1
print(count)
#Use a loop to print "Digit" if a character is numeric, otherwise print "Letter".
s="hello123"
for i in s:
    if i.isdigit():
        print("Digit")
    elif i.isalpha():
        print("Letter")
#Write a loop that prints only uppercase characters from a string.
s="Hello World"
for i in s:
    if i.isupper():
        print(i)
#Given a string, use a loop to count how many times "a" appears.
s="banana"
count=0
for i in s:
    if i=="a":
        count+=1
print(count)
#Write a loop that prints "Palindrome" if a string reads the same forward and backward, otherwise "Not Palindrome".
num=int(input("enter a number:"))
rev=0
temp=num
for i in str(num):
    digit=num%10
    rev=rev*10+digit
    num//=10
if temp==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")    
#Dictionaries
#Write a loop that prints dictionary keys only if their values are greater than 50.
my_dict = {'a': 30, 'b': 60, 'c': 45, 'd': 80}
for k,v in my_dict.items():
    if v>50:
        print(k)
#Given a dictionary of student names and marks, use a loop to print "Pass" if marks ≥ 40, otherwise "Fail".
students = {'Alice': 85, 'Bob': 35, 'Charlie': 60, 'David': 25}
for k,v in students.items():
    if v>=40:
        print("Pass")
    else:
        print("Fail")
#Write a loop that counts how many dictionary values are even.
my_dict = {'a': 31, 'b': 60, 'c': 45, 'd': 80}
count=0
for k,v in my_dict.items():
    if v%2==0:
        count+=1
print(count)
#Use a loop to print "Starts with A" if a key begins with "A", otherwise print "Other".
my_dict = {'Alice': 85, 'Angel': 35, 'Charlie': 60, 'sunitha': 25}
for k in my_dict.keys():
    if k.startswith("A"):
        print("Starts with A")
    else:
        print("Other")

#Write a loop that finds the maximum value in a dictionary and prints the corresponding key.
my_dict = {'a': 31, 'b': 60, 'c': 45, 'd': 80}
maxx=my_dict['a']
for k,v in my_dict.items():
    if v>maxx:
        maxx=v
print(k,v)
        
        
#Mixed Loops + Conditionals
#Write a loop that prints numbers from 1 to 20, but skips multiples of 5.
for i in range(1,21):
    if i%5==0:
        continue
    print(i,end=" ")
#Use a loop to print numbers from 1 to 15, but stop when you reach 10.
for i in range(1,15):
    if i<10:
        print(i,end=" ")
#Write a loop that prints "Prime" if a number is prime, otherwise "Not Prime", for numbers 2–20.
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



