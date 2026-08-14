# # Level 3 — Functions + Loops
# # Write a function print_numbers(n) that prints numbers from 1 to n.
# def print_numbers(n):
#     for i in range(1,n+1):
#             print(i)
# print_numbers(10)
# # Write a function print_even(n) that prints all even numbers from 1 to n.
# def even_numbers(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i)
# even_numbers(10)
# # Write a function print_odd(n) that prints all odd numbers from 1 to n.
# def odd_numbers(n):
# #     for i in range(1,n+1):
# #         if i%2!=0:
# #             print(i)
# # odd_numbers(10)
# # # Write a function sum_numbers(n) that returns the sum from 1 to n.
# # def sum_num(n):
# #     sum=0
# #     for i in range(1,n+1):
# #         sum+=i
# #     return sum
# # print(sum_num(10))

# # # Write a function factorial(n) that returns the factorial of n.
# # def fact(n):
# #     f=1
# #     for i in range(1,n+1):
# #         f=f*i
# #     return f
# # print(fact(3))
# # # Write a function multiplication_table(n) that prints the multiplication table.
# # def mult(n):
# #     for i in range(1,11):
# #         print(n,"*",i,'=',n*i)
# # mult(2)
# # # Write a function count_digits(n) that returns the number of digits.
# # # Example:
# # # Input: 12345
# # # Output: 5
# # def count_digits(n):
# #     count=0
# #     while n>0:
# #         count+=1
# #         n//=10
# #     return count
# # print(count_digits(12345))

# # # Write a function reverse_number(n).
# # # Example:
# # # Input: 12345
# # # Output: 54321
# # def rev_num(n):
# #     rev=0
# #     while n>0:
# #         digit=n%10
# #         rev=rev*10+digit
# #         n//=10
# #     return rev
# # print(rev_num(12345))
# # # Write a function sum_of_digits(n).
# # # Example:
# # # Input: 12345
# # # Output: 15
# # def sum_digits(n):
# #     sum=0
# #     while n>0:
# #         digit=n%10
# #         sum+=digit
# #         n//=10
# #     return sum
# # print(sum_digits(12345))
# # # Write a function count_even_odd(n) that counts even and odd numbers from 1 to n.
# # def count_even_odd():
# #     c_e=0
# #     c_o=0
# #     for i in range(1,11):
# #         if i%2==0:
# #             c_e+=1
# #         elif i%2!=0:
# #             c_o+=1
# #     return c_e,c_o
# # print(count_even_odd())

# # 🟡 Level 4 — String Functions
# # Write a function reverse_string(s) without using slicing.
# s='sun'
# def reverse_string(s):
#     for i in range(len(s)-1,-1,-1):
#         print(s[i])
# reverse_string(s)
# # Write a function is_palindrome(s).
# s='madam'
# def is_palindrome(s):
#     temp=s
#     s1=""
#     for i in range(len(s)-1,-1,-1):
#         s1=s1+s[i]
#     if temp==s1:
#         print("palindrome")
#     else:
#         print("not a palindrome")
# is_palindrome(s)

# # Example:

# # madam → True
# # hello → False
# # Write a function count_vowels(s).
# s='sunitha'
# def count_vowels(s):
#     count=0
#     vowels='aeiouAEIOU'
#     for i in s:
#         if i in vowels:
#             count+=1
#     return count
# print(count_vowels(s))
# # Write a function count_consonants(s).
# s='sunitha'
# def count_vowels(s):
#     count=0
#     vowels='aeiouAEIOU'
#     for i in s:
#         if i  not in vowels:
#             count+=1
#     return count
# print(count_vowels(s))
# # Write a function count_characters(s) that returns the number of characters excluding spaces.
# s='hello world'
# def count_char(s):
#     count=0
#     for i in s:
#         if i!=" ":
#             count+=1
#     return count
# print(count_char(s))

    
# # Write a function count_words(sentence).
# s="Python programming is fun"
# def count_words(s):
#     count=0
#     for i in s.split(" "):
#         count+=1
#     return count
# print(count_words(s))

# # Write a function remove_spaces(s) without using replace().
# s="Python programming is fun"
# def remove_spaces(s):
#     s1=""
#     for i in s.split(" "):
#            s1+=i
#     print(s1)
# remove_spaces(s) 
# # Write a function find_frequency(s, ch) that counts how many times a character occurs.
# s="python programming is fun"
# def find_frequency(s,ch):
#     count=0
#     for i in s:
#         if i==ch:
#             count+=1
#     return count
# print(find_frequency(s,"p"))

# # Write a function first_non_repeated_char(s)
# # Example:
# # Input: swiss
# # Output: w
# s='swiss'
# def first_non_repeated_char(s):
#     freq={}
#     for i in s:
#         if i not in freq:
#             freq[i]=1
#         else:
#             freq[i]+=1
#     for i in s:
#         if freq[i]==1:
#             print(i)
# first_non_repeated_char(s)
# # Write a function remove_duplicate_characters(s).

# # Example:

# # Input: programming
# # Output: progamin
# s='programming'
# def remove_duplicate_char(s):
#     freq={}
#     res=" "
#     for i in s:
#         if i not in freq:
#             freq[i]=True
#             res+=i
#     return res
# print(remove_duplicate_char(s))

# 🟡 Level 5 — List Functions
# Write a function find_largest(numbers) without using max().

n=[1,2,3,4,8,9,5]
def largest(n):
    l=0
    for i in n:
        if i>l:
            l=i
    return l
print(largest(n))

# Write a function find_smallest(numbers) without using min().
def smallest(n):
    s=float('inf')
    for i in n:
        if i<s:
            s=i
    return s
print(smallest(n))
# Write a function calculate_sum(numbers) without using sum().
def sum(n):
    sum=0
    for i in n:
        sum+=i
    return sum
print(sum(n))
# Write a function calculate_average(numbers).
def avg(n):
    sum=0
    for i in n:
        sum+=i
    average=sum/len(n)
    return average
print(avg(n))
# Write a function count_even(numbers).
def count_even(n):
    count=0
    for i in n:
        if i%2==0:
            count+=1
    return count
print(count_even(n))
# Write a function count_odd(numbers).
def count_odd(n):
    count=0
    for i in n:
        if i%2!=0:
            count+=1
    return count
print(count_odd(n))
# Write a function reverse_list(numbers) without using reverse() or slicing.
n=[1,2,3,4,8,9,5]
def rev(n):
    l1=[]
    for i in range(len(n)-1,-1,-1):
        l1.append(n[i])
    return l1
print(rev(n))
# Write a function remove_duplicates(numbers) without using set().
n=[1,3,4,2,5,2,1,5]
def remove_dup(n):
    l=[]
    for i in n:
        if i  not in l:
            l.append(i)
    return l
print(remove_dup(n))
        
# Write a function second_largest(numbers).
def sec_lar(n):
    sec=n[0]
    l=n[0]
    for i in n:
        if i>l:
            sec=l
            l=i
        elif i>sec and i!=l:
            sec=i
    return sec
print(sec_lar(n))
# Write a function find_common_elements(list1, list2).
l=[1,2,3,3,5,4]
l1=[1,3,2,5,7,8]
l3=[]
def common_elements(l,l1):
    for i in l:
        if i in l1 and i not in l3:
            l3.append(i)
    return l3
print(common_elements(l,l1))
# Write a function merge_lists(list1, list2) without using extend().
l=[1,2,3]
l1=[1,4,3]
l2=[]
def  merge(l,l1):
    for i in l:
        l2.append(i) 
    for i in l1:
        l2.append(i)
    return l2
print(merge(l ,l1))
# Write a function frequency_count(numbers).
# Example:
# [1, 2, 2, 3, 3, 3]
# Expected:
# {1: 1, 2: 2, 3: 3}
n=[1, 2, 2, 3, 3, 3]
def freq_count(n):
    freq={}
    for i in n:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq
print(freq_count(n))
# 🟠 Level 6 — *args
# Write a function using *args that returns the sum of all numbers.
# calculate(10, 20, 30, 40)
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum(10,20,30,40))
# Write a function using *args that returns the largest number.
def large(*args):
    l=args[0]
    for i in args:
        if i>l:
            l=i
    return l
print(large(20,50,60))
# Write a function using *args that counts how many arguments were passed.
def count_arg(*args):
    count=0
    for i in args:
        count+=1
    return count
print(count_arg(1,2,3,4,5,6))
# Write a function using *args that separates even and odd numbers.
# Write a function using *args that calculates the average.
# Write a function using *args that accepts numbers and returns only the positive numbers.
# 🟠 Level 7 — **kwargs
# Create a function using **kwargs that prints employee details.
# employee(
#     name="John",
#     age=25,
#     salary=50000,
#     department="IT"
# )
# Write a function using **kwargs that returns the number of employee attributes supplied.
# Write a function using **kwargs that prints only the keys.
# Write a function using **kwargs that prints only the values.
# Write a function that accepts both *args and **kwargs.

# Example:

# employee(101, 102, 103, name="John", department="IT")
# 🟠 Level 8 — Lambda + Functions
# Create a lambda function to add two numbers.
# Create a lambda function to find the square of a number.
# Create a lambda function to check whether a number is even.
# Use map() with a lambda to square every element in a list.
# Use filter() with a lambda to extract even numbers.
# Use filter() with a lambda to extract numbers greater than 50.
# Use sorted() with lambda to sort this list by the second element:
# students = [
#     ("John", 80),
#     ("Alice", 95),
#     ("Bob", 70)
# ]
# Use lambda to sort employees based on salary.
# employees = [
#     ("A", 50000),
#     ("B", 30000),
#     ("C", 70000)
# ]
# 🔴 Level 9 — Recursion
# Find factorial using recursion.
# Find the sum of numbers from 1 to n using recursion.
# Find the nth Fibonacci number using recursion.
# Reverse a string using recursion.
# Check whether a string is palindrome using recursion.
# Find the sum of digits using recursion.
# Count the digits of a number using recursion.
# Calculate a^b using recursion without using **.
# 🔴 Level 10 — Interview-Level Function Problems
# Write a function to find the second largest number in a list without sorting.
# Write a function to find all duplicate elements in a list.
# Write a function to find the missing number from:
# [1, 2, 3, 5, 6]

# Expected:

# 4
# Write a function to find pairs whose sum equals a target.
# numbers = [2, 4, 3, 5, 7, 8]
# target = 10

# Expected pairs:

# (2, 8)
# (3, 7)
# Write a function to rotate a list by k positions.
# Write a function to find the intersection of two lists without using built-in set operations.
# Write a function to flatten:
# [[1, 2], [3, 4], [5, 6]]

# into:

# [1, 2, 3, 4, 5, 6]
# Write a function to find the longest word in a sentence.
# Write a function to find the word with the highest frequency in a sentence.
# Write a function to check whether two strings are anagrams.
# listen
# silent

# Expected:

# True
# Write a function to return the top 3 highest numbers from a list without using sort().
# 🔥 Level 11 — Real Interview Problems
# Write a function that accepts a list of employee dictionaries and returns the employee with the highest salary.
# employees = [
#     {"name": "A", "salary": 50000},
#     {"name": "B", "salary": 70000},
#     {"name": "C", "salary": 60000}
# ]
# Write a function that groups employees by department.
# Write a function that calculates the average salary of employees.
# Write a function that returns employees whose salary is greater than 50000.
# Write a function that finds the highest salary in each department.
# Write a function that removes duplicate employee records.
# Write a function that accepts a list of dictionaries and converts it into a dictionary using employee ID as the key.
# Write a function to count the frequency of each word in a text file.
# Write a function that reads a CSV file and returns the employee with the highest salary.
# Write a function that accepts a list of transactions and calculates total sales.
# Write a function that separates valid and invalid records based on missing values.
# 🎯 Challenge Set — Do These Without Help

# For your mock interview, I recommend solving these 10 first:

# 1. is_prime(n)
# 2. factorial(n)
# 3. is_palindrome(s)
# 4. frequency_count(list)
# 5. second_largest(list)
# 6. remove_duplicates(list)
# 7. find_missing_number(list)
# 8. find_pairs(list, target)
# 9. employee_highest_salary(employees)
# 10. department_highest_salary(employees)