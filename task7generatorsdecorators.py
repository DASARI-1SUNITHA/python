
#  Generators 
# Write a generator that yields numbers from 1 to 20, but only if they are even.
# def gen_numbers():
#     for num in range(1,21):
#         if num%2==0:
#             yield num
# s=gen_numbers()
# for i in s:
#     print(i)

# Create a generator that yields squares of numbers from 1 to 10 using a for loop.
# def gen_numbers():
#     for num in range(1,11):
#             yield num**2
# s=gen_numbers()
# for i in s:
#     print(i)

# Implement a generator that yields numbers divisible by 3 up to 30.
# def gen_numbers():
#     for num in range(1,31):
#         if num%3==0:
#             yield num
# s=gen_numbers()
# for i in s:
#     print(i)

# Write a generator that yields characters of a string, but skip vowels.
# def gen_string(string):
#     vowels="aeiouAEIOU"
#     for ch in string:
#         if ch not in vowels:
#             yield ch
# s=gen_string("Sunitha")

# Create a generator that yields Fibonacci numbers up to n using a while loop.
# def fib(n):
#     a=0
#     b=1
#     while a<=n:
#         yield a
#         a,b=b,a+b
# for num in fib(20):
#     print(num)


# Implement a generator that yields prime numbers less than 50 (use conditionals).
# def prime(n):
#     num=2
#     while num<=n:
#         factors=0
#         for i in range(1,num+1):
#             if num%i==0:
#                 factors+=1
#         if factors==2:
#             yield num
#         num+=1
# for p in prime(50):
#     print(p)


# Write a generator that yields numbers from 1 to 10, but stops if the number is greater than 7.
# def num():
#     for n in range(1,11):
#         if n>7:
#             break
#         yield n
# s=num()
# for i in s:
#     print(i)

# Create a generator that yields odd numbers up to 15 using if conditions.
# def gen_numbers():
# #     for num in range(1,16):
# #         if num%2!=0:
# #             yield num
# # s=gen_numbers()
# # for i in s:
# #     print(i)

# # Implement a generator that yields factorials of numbers from 1 to 5.
# # n=5
# # def factorial():
# #     for n in range(1,6):    
# #         fact=1
# #         for i in range(1,n+1):
# #             fact*=i
# #         yield fact
# # for value in factorial():
# #     print(value)

    
# # Write a generator that yields multiples of 5 up to 50.
# # def gen_numbers():
# #     for num in range(1,51):
# #         if num%5==0:
# #             yield num
# # s=gen_numbers()
# # for i in s:
# #     print(i)

# # Create a generator that yields numbers from 1 to n, but only if they are not divisible by 2.
# n=int(input("Enter a number:"))
# def gen_numbers():
#     for i in range(1,n+1):
#         if i%2!=0:
#             yield i
# s=gen_numbers()
# for j in s:
#     print(j)

# # Implement a generator that yields the running sum of numbers in a list.
# # n=int(input("Enter a number:"))
# # s=[]
# # for i in range(n):
# #     s.append(int(input("Enter")))
# # def gen_numbers(lst):
# #     sum=0
# #     for s in lst :
# #         sum+=i
# #         yield sum
# # g=gen_numbers(s)
# # for i in g:
# #     print(i)
# # Write a generator that yields binary representations of numbers from 1 to 10.
# def gen_binary():
#     for num in range(1,11):
#         yield bin(num)[2:]
# for b in gen_binary():
#     print(b)
# # Create a generator that yields elements of a list, but skips duplicates.
# l=[1,2,3,1,5,4,6,2,3]
# s=[]
# def duplicates(l):
#     for i in l:
#         if i not in s:
#             s.append(i)
#             yield i
# d=duplicates(l)
# for j in d:
#     print(j)
# # Implement a generator that yields rows of Pascal’s Triangle up to n.
# def pascal(n):
#     row=[1]
#     for _ in range(n):
#         yield row
#         next_row=[1]
#         for i in range(len(row)-1):
#             next_row.append(row[i]+row[i+1])
#         next_row.append(1)
        
#         row=next_row 
# for i in pascal(5):
#     print(i)



# Decorators
# Write a decorator that prints "Function is starting" before running a function.
def main(fun):
    def inner():
        print('function is starting')
        fun()
    return inner
@main
def func():
    print('hi')
func()
# Create a decorator that prints "Function has ended" after running a function.
def main(fun):
    def inner():
        fun()
        print('function ended')
    return inner
@main
def func():
    print("bye")
func()
# Implement a decorator that prints the arguments passed to a function using a loop.
def main(fun):
    def inner(*data):
        print('arguments are:')
        fun(data)
    return inner
@main
def func(*args):
    for i in args:
        print(i)
func(1,3,2,4,5)
        

# Write a decorator that checks if the input number is positive before running a function.
# Create a decorator that runs a function twice using a for loop.
# Implement a decorator that converts the output of a function to uppercase.
# Write a decorator that prints "Start" before and "End" after a function runs.
# Create a decorator that counts how many times a function has been called.
# Implement a decorator that multiplies the return value of a function by 2.
# Write a decorator that only allows a function to run once.
# Create a decorator that prints the name of the function being executed.
# Implement a decorator that checks if the user is "admin" before running a function.
# Write a decorator that retries a function up to 3 times if it fails.
# Create a decorator that prints all items in a list returned by a function using a loop.
# Implement a decorator that ensures a function always returns a dictionary.
