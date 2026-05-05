#functions
def greet():
    print("hi")
    print("Good morning")
greet()
# output:hi
# Good morning
def add_sub(x,y):
    add=x+y
    sub=x-y
    return add,sub
result1,result2=add_sub(5,7)
print(result1,result2)
#output:12 -2
#functional arguments:
def update(x):
    x=0
    print(x)
a=10
update(a)
print(a)


#types of arguments:


#postional  arguments:
def person(name,age):
    print("name:",name)
    print("age:",age)
person('sun',21)


#keyword arguments;
def person(name,age):
    print("name:",name)
    print("age:",age)
person(age=23,name='sun')

#default arguments:
def person(name='sun',age=12):
    print("name:",name)
    print("age:",age)
person('puppy',21)


#varibale length arguments:
def sum(int1,*int2):
    print("int1:",int1)
    print("int2:",int2)
sum(20,6,60, 8)
#or
def sum(int1,*int2):
    c=int1
    for i in int2:
        c=c+i
    print(c)
sum(20,6,60, 8)


  ##keyword variables length arguments(**kargs):
def person(name,**data):
    print("name",name)
    for i,j in data.items():
        print(i,j)
person('sun',age=20,city='mumbai',pin='xxxxxx')


#global vs local:
a=10#global
def something():
    a=12#local
    print(a)
print(a)

a=10
def some():
    global a
    a=15
    print('in fun:',a)
some()
print("outside:",a)
# we have a global's  we can access the local variable address AND  global variable address
a=10
print(id(a))
def some():
    a=9
    print(id(a))
    x=globals()
    print('is fun:',a)
    print(id (a))
some()


#pass list to a function:
def count(list):
    even=0
    odd=0
    for i  in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
list=[1,2,3,4,5,6,7,8,9,10,11]
even,odd=count(list)
print("Even:{} and odd:{}".format(even ,odd))


