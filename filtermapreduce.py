#filter 
#filter is used for filtering the values from a particular list
#syntax:filter(function,iterable)
def is_even(num):
    return num%2==0
n=[1,5,6,2,3,7,8,9,4]
result=list(filter(is_even,n))
print(result)
# Output:
# [6, 2, 8, 4]

#using lambda function

result1=list(filter(lambda num: num%2==0,n))
print(result1)


#Map()
#used to update the value in a particular list
#syntax:map(function,iterable)
def update(num):
    return num*num
n=[1,5,6,2,3,7,8,9,4]
result=list(map(update,n))
print(result)
#using lambda function
result1=list(map(lambda num:num*2,n))
print(result1)


#reduce:
  