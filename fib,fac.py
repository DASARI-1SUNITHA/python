# def fib(n):
#     int1=0
#     int2=1
#     if n==1:
#         print(n)
#     else:
#         print(int1)
#         print(int2)
#     for i in range(2,n):
#         int3=int1+int2
#         int1=int2
#         int2=int3
#         print(int3)
# fib(int(input("Enter a valid integer:")))
# #output:Enter a valid integer:10
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34



## factorial:
def factorial(n):
    number=1
    for i in range(1,n+1):
        number=number*i
    return number
fact=int(input("enter a valid integer:"))
result=factorial(fact)
print(result)
    
#output:enter a valid integer:5
# 120






