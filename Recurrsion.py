#recurrsion
# a function calling itself 
# def greet():
#     print("hello")
#     greet()
# greet()
#output :neaarly 1000 times it prints 'hello'
# import sys
# print(sys.getrecursionlimit())
# def greet():
#     print("hello")
#     greet()
# greet()
#we can even  set the limit by using (sys.setrecurrsionlimit(1223))

#factorial using recurrsion
# def fact(number):
#     if  number==0:
#         return 1
#     return number*fact(number-1)
# result=int(input("Enter a valid integer:"))
# result1=fact(result)
# print(result1)
# output:
# Enter a valid integer:7
# 5040


#anonymous function
# def square(number):
#     return number*number
# result=int(input("Enter a  valid integer:"))
# res=square(result)
# print(res)
# output:
# Enter a  valid integer:9
# 81

# by using lambda function

# res=lambda x:x*x
# result=int(input("Enter a  valid integer:"))
# print(res(result))
# Enter a  valid integer:6
# 36

