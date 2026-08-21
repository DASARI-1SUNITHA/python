# 1. Numbers – Practice Questions
# Check whether a number is positive, negative, or zero.
def positive_negative(num):
    if num>0:
        print("Positve")
    elif num<0:
        print("negative")
    else:
        print('zero')
# positive_negative(12)
# Check whether a number is even or odd.
def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
# even_odd(2)
# Find the largest of two numbers.
def large_number(num1,num2):
    if num1>num2:
        print('num1 is greater')
    else:
        print('num2 is greater')
# large_number(8,9)

# Find the largest of three numbers.
def large_numbers(num1,num2,num3):
    if num1>num2 and num2>num3:
        print('num1 is larger')
    elif num2>num3 and num2>num1:
        print('num2 is larger')
    else:
        print('num3 is  larger')
# large_numbers(1,2,3)
# Find the smallest of three numbers.
def smallest_numbers(num1,num2,num3):
    if num1<num2 and num2<num3:
        print('num1 is smaller')
    elif num2<num3 and num2<num1:
        print('num2 is smallerr')
    else:
        print('num3 is  smaller')
# smallest_numbers(3,2,5)
# Calculate the sum of digits of a number.
def sum_of_digits(n):
    sum=0
    while n!=0:
        digit=n%10
        sum+=digit
        n//=10
    print(sum)
# sum_of_digits(1234)

# Count the number of digits in a number.
def count_of_digits(n):
    count=0
    while n!=0:
        digit=n%10
        count+=1
        n//=10
    print(count)
# count_of_digits(122345)

# Reverse a number.
def reverse_num(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    print(rev)
# reverse_num(5432)
# Check whether a number is a palindrome.
def palindrome_num(n):
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    print(rev)
    if temp==rev:
        print("palindrome")
    else:
        print("not a palindrome")
# palindrome_num(12321)
# # Find the factorial of a number.
def factorial(n=5):
    if n==0:
        return 1
    return n*factorial(n-1)
# res=factorial(5)
# print(res)

# Intermediate
# Check whether a number is prime.
def is_prime(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True
# print(is_prime(12))
# Print all prime numbers between 1 and 100.
# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# for num in range(1,100):
#     if is_prime(num):
#         print(num,end=" ")
    

# Find the sum of all prime numbers from 1 to 100.
sum=0
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
# for num in range(1,100):
#     if is_prime(num):
#         sum+=num
#     print(sum)


# Find the Fibonacci series up to n terms.
def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n):
        a,b=b,a+b
        print(b,end=" ")
# fibonacci(10)
    
# Check whether a number belongs to the Fibonacci series.
l=[]
def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n):
        a,b=b,a+b
        l.append(b)
# num=int(input("Enter a number between 1to 100:"))
# if num in l:
#     print("belongs to fibonacci series")
# else:
#     print("not in fib series")
# fibonacci(10)

# Find the GCD of two numbers.
def gcd(num1,num2):
    while num2!=0:
        num1,num2=num2,num1%num2
    return num1
# print(gcd(12,18))

# Find the LCM of two numbers.
import math
def lcm(a,b):
    if a==0 or b==0:
        return 0
    return (a*b)//math.gcd(a,b)
# print(lcm(12,18))
# Check whether a number is an Armstrong number.
def amstrong(n):
    temp=n
    p=len(str(n))
    sum=0
    while n>0:
        digit=n%10
        sum+=digit**p
        n//=10
    print(sum==temp)
amstrong(153)
# Print all Armstrong numbers between 1 and 1000.
def amstrong(n):
    temp=n
    p=len(str(n))
    sum=0
    while n>0:
        digit=n%10
        sum+=digit**p
        n//=10
    return sum==temp
# for i in range(1,1001):
#     if amstrong(i):
#         print(i)
# Check whether a number is a perfect number.
def perfect(n):
    temp=n
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==temp
# print(perfect(6))

# Interview Level
# Find the second-largest digit in a number.
def sec_large_num(n):
    large=0
    sec=0
    while n>0:
        digit=n%10
        if digit>large:
            sec=large
            large=digit
        elif digit>sec and digit!=large:
            sec=digit
        n//=10
    print(sec)
sec_large_num(12345)
# Find the second-smallest digit in a number.
def sec_large_num(n):
    s=float('inf')
    sec=float('inf')
    while n>0:
        digit=n%10
        if digit<s:
            sec=s
            s=digit
        elif digit<sec and digit!=s:
            sec=digit
        n//=10
    print(sec)
sec_large_num(12345)
# Find the frequency of each digit in a number.
def frequency_digit(n):
    freq={}
    while n>0:
        digit=n%10
        if digit not in freq:
            freq[digit]=1
        else:
            freq[digit]+=1
        n//=10
    return freq
print(frequency_digit(123423))
# Find the largest digit in a number without converting it to a string.
def large_digit(n):
    large=0
    while n>0:
        digit=n%10
        if digit>large:
            large=digit
        n//=10
    return large
print(large_digit(1234567))

# Find the smallest digit in a number without converting it to a string.
def small_digit(n):
    small=float('inf')
    while n>0:
        digit=n%10
        if digit<small:
            small=digit
        n//=10
    return small
print(small_digit(1234567))
# Remove duplicate digits from a number.
def remove_duplicates(n):
    l=""
    while n>0:
        digit =n%10
        if str(digit) not in l:
            l+=str(digit)
        n//=10
    print(l)
remove_duplicates(112323765)

# Find the sum of even digits and odd digits separately.
def sum_even_odd(n):
    even_sum=0
    odd_sum=0
    while n>0:
        digit=n%10
        if digit%2==0:
            even_sum+=digit
        else:
            odd_sum+=digit
        n//=10
    print(even_sum,odd_sum)
sum_even_odd(12345)
# Check whether a number is a strong number.
def strong_number(n):
    temp=n
    sum=0
    while n>0:
        digit=n%10
        sum+=math.factorial(digit)
        n//=10
    if sum==temp:
        print("strong number")
    else:
        print("not a strong number")
strong_number(145)
# Find all factors of a number.
def factors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l
print(factors(12))

# Find the number of trailing zeros in a factorial.
def count_trailing_zeros(n):
    zeros=0
    d=5
    while n>=d:
        zeros+=n//d
        d*=5
    return zeros
print(count_trailing_zeros(5))