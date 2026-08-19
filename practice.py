# Python Coding Questions (Must Practice)
# Beginner (20)
# Reverse a string.
# s='sunitha'
# for i in range(len(s)-1,-1,-1):
#   print(s[i],end=" ")
# Check palindrome.
# s=123321
# rev=0
# temp=s 
# while s>0:
#   digit=s%10
#   rev=rev*10+digit
#   s//=10
# if temp==rev:
#     print("palindrome")
# else:
#     print("Not a palindrome")
    
# Count vowels.
# s="sunitha"
# vowels='aeiouAEIOU'
# count=0
# for i in s:
#     if i in vowels:
#         count+=1
# print(count)
# Factorial.
# n=5
# fact=1
# while n>0:
#     fact=fact*n
#     n-=1
# print(fact)
# Fibonacci.
# n=10
# a=0
# b=1
# for i in range(n):
#     print(a)
#     a,b=b,a+b
    
# Prime number.
# n=9
# factors=0
# for i in range(1,n+1):
#     if n%i==0:
#         factors+=1
# if factors==2:
#     print('prime')
# else:
#     print('not prime')

# Armstrong number.
# n=153
# temp=n
# sum=0
# power=len(str(n))
# while n>0:
#     digit=n%10
#     sum+=digit**power
#     n//=10
# if sum==temp:
#     print("Amstrong number")
# else:
#     print("not amstrong")



# Perfect number.
# n=28
# div_sum=0
# for i in range(1,(n//2)+1):
#     if n%i==0:
#         div_sum+=1
# if div_sum==n:
#     print("Perfect number")
# else:
#     print("not perfect number")


# Remove duplicates from a list.
# l=[1,2,3,4,2,4,6,5,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
# Find second largest element.
# l=[1,2,3,4,2,5,6]
# lar=l[0]
# sec=l[0]
# for i in l:
#     if i>lar:
#         sec=lar
#         lar=i
#     elif i>sec and i!=lar:
#         sec=i
# print(sec)

    
# Count character frequency.
# s='apple'
# freq={}
# for i in s:
#     if i not in freq :
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)

# Find missing number.
# l=[1,2,3,4,5]
# n=6
# exp_num=(n*(n+1))//2
# act_sum=sum(l-)
# miss_num=exp_num-act_sum
# print(miss_num)
# Merge two lists.
# l=[1,2,3,4]
# l1=[1,7,8,9]
# l.extend(l1)
# print(l)
# Rotate a list.
l=[1,2,3,4,5]
for i in range(2):
    last_item=l.pop()
    l.insert(0,last_item)
print(l)
    
# Find duplicate elements.
# Two Sum.
# Maximum element.
# Sort dictionary by value.
# Count words.
# Print star patterns.
# Intermediate (20)
# Anagram check.
# String compression.
# Longest substring without repeating characters.
# Group anagrams.
# Merge intervals.
# Binary search.
# Quick sort.
# Merge sort.
# LRU cache.
# Custom iterator.
# Custom decorator.
# CSV parser.
# Log file analyzer.
# Producer-consumer using threads.
# Matrix multiplication.
# Spiral matrix.
# Validate parentheses.
# Queue using stacks.
# Stack using queues.
# Top K frequent elements.
# Advanced (10)
# Design an LRU Cache.
# Implement Trie.
# Implement Graph (BFS/DFS).
# Dijkstra's algorithm.
# Producer-consumer with multithreading.
# Asynchronous API calls using asyncio.
# Mini ATM system (OOP).
# Inventory management system.
# File deduplication tool using hashing.
# ETL pipeline that reads CSV, transforms data, and writes results.
# SQL Coding Questions (Must Practice)
# Beginner (20)
# Find employees with salary > 50,000.
# Display distinct departments.
# Find employees hired after 2023.
# Count employees in each department.
# Find the highest salary.
# Find the second-highest salary.
# Display employees in descending salary order.
# Find duplicate email addresses.
# Update employee salaries by 10%.
# Delete inactive users.
# Use CASE to categorize salaries.
# Find employees with names starting with 'A'.
# Count NULL values in a column.
# Retrieve the top 5 highest-paid employees.
# Calculate average salary by department.
# Find employees with no manager.
# Retrieve unique cities.
# Use COALESCE to replace NULLs.
# Filter records with BETWEEN.
# Use IN and NOT IN.
# Intermediate (20)
# Inner join employees and departments.
# Left join customers and orders.
# Find departments without employees.
# Employees earning above department average.
# Top 3 salaries per department.
# Running total of sales.
# Rank employees by salary.
# Find consecutive login dates.
# Find duplicate rows.
# Use LEAD and LAG for salary comparisons.
# Recursive CTE for employee hierarchy.
# Pivot monthly sales.
# Unpivot quarterly data.
# Calculate moving averages.
# Find gaps in sequences.
# Detect overlapping date ranges.
# Self-join to find manager names.
# Correlated subquery for latest order.
# Use EXISTS to find customers with orders.
# Window functions with partitions.
# Advanced (10)
# Design a normalized schema for an e-commerce application.
# Optimize a slow query using indexes.
# Write a recursive query for an organizational hierarchy.
# Detect and resolve duplicate records.
# Build a sales dashboard query using CTEs and window functions.
# Compare ROW_NUMBER, RANK, and DENSE_RANK.
# Find the median salary.
# Calculate cohort retention.
# Implement Slowly Changing Dimension (SCD Type 2) logic.
# Explain an execution plan and suggest optimizations.
# Mock Interview Strategy

# When an interviewer asks, structure your answer like this:

# Definition: "A dictionary is a mutable collection of key-value pairs."
# Why it's used: "It provides fast lookups (average O(1)) using keys."
# Real-world use case: "In a Data Engineering pipeline, a dictionary can map customer IDs to customer details after reading data from an API."
# Simple example: Show a short code snippet.
# Complex example: Demonstrate a realistic scenario (e.g., counting product frequencies from transaction data).
# Complexity: Mention time and space complexity if relevant.
# Edge cases: Point out special cases (empty input, duplicates, NULL values, etc.).
