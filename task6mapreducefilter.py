#  Map (10 Coding Questions)
# Use map() to square each number in [2, 4, 6, 8].
num=[2,4,6,8]
s=map(lambda x:x*x,num)
print(list(s))
# Convert an array of strings ["apple", "banana", "cherry"] into uppercase using map().
strings=["apple", "banana", "cherry"]
s=map(lambda x:x.upper(),strings)
print(list(s))
# Extract the id property from an array of objects: [{id:1,name:"A"}, {id:2,name:"B"}, {id:3,name:"C"}]
objects=[{"id":1,"name":"A"}, {"id":2,"name":"B"}, {"id":3,"name":"C"}]
d=list(map(lambda x:x["id"],objects))
print(type(id))
# Add 5 to each element in [10, 20, 30] using map().
n=[10, 20, 30] 
s=map(lambda x:x+5 ,n)
print(list(s))
# Convert an array of numbers [1,2,3,4] into strings using map()
nu=[1,2,3,4]
s=map(lambda x:str(x),nu)
print(list(s))
# Use map() to append "!" to each word in ["hi","hello","hey"].
s=["hi","hello","hey"]
d=list(map(lambda x:x+("!"),s))
print(d)
# Create a new array of lengths from ["dog","elephant","cat"].
a=["dog","elephant","cat"]
l=list(map(lambda x:len(x),a))
print(l)
# Use map() to transform [true,false,true] into ["YES","NO","YES"].
s=["true","false","true"]
s=list(map(lambda x: "YES" if x=="true" else "NO",s))
print(s)
# Given [1,2,3], use map() to return [1,4,9].
l=[1,2,3]
s=list(map(lambda x:x**2 ,l))
print(s)
# Use map() to add a fullName property to each object in:[{first:"John",last:"Doe"}, {first:"Jane",last:"Smith"}]
names=[{"first":"John","last":"Doe"}, {"first":"Jane","last":"Smith"}]
name=list(map(lambda x:x["first"]+" "+x["last"],names ))
print(name)

# 🔹 Filter (10 Coding Questions)
# Use filter() to get even numbers from [1,2,3,4,5,6].
a=[1,2,3,4,5,6]
b=list(filter(lambda x:x%2==0 ,a))
print(b)
# Filter out words shorter than 4 letters from ["hi","hello","hey","world"].
s=["hi","hello","hey","world"]
b=list(filter(lambda x:x if len(x)<4 else "exit" ,s))
print(b)
# From [10,25,30,45], filter numbers greater than 20.
n=[10,25,30,45]
b=list(filter(lambda x:x>20,n))
print(b)
# Use filter() to get only truthy values from [0,1,false,2,"",3].
s=[0,1,"false",2,"",3]
t=list(filter(lambda x:x,s))
print(t)
# Filter out negative numbers from [5,-3,9,-1,0].
n=[5,-3,9,-1,0]
neg=list(filter(lambda x:x<0,n))
print(neg)
# Use filter() to get names starting with "A" from ["Alice","Bob","Andrew","Charlie"].
names=["Alice","Bob","Andrew","Charlie"]
Names=list(filter(lambda x:x.startswith("A"),names))
print(Names)

# From [100,200,300,400], filter numbers divisible by 200.
num=[100,200,300,400]
d=list(filter(lambda x:x%200==0,num))
print(d)
# Use filter() to get objects with age > 18 from:[{name:"Tom",age:15},{name:"Jerry",age:20}]
ob=[{"name":"Tom","age":15},{"name":"Jerry","age":20}]
d=list(filter(lambda x:x["age"]>18,ob))
print(d)
# Filter out duplicate values from [1,2,2,3,4,4,5] using filter().
values=[1,2,2,3,4,4,5]
d=list(filter(lambda x:values.count(x)==1 ,values))
print(d)
# From ["red","blue","green","yellow"], filter colors containing "e".
colors=["red","blue","green","yellow"]
c=list(filter(lambda x:x if "e" in colors else x,colors))
print(c)
# 🔹 Reduce (10 Coding Questions)
# Use reduce() to sum [1,2,3,4,5].
from functools import reduce
sum=[1,2,3,4,5]
r=reduce(lambda x,y:x+y,sum)
print(r)
# Find the maximum number in [10,25,30,5] using reduce().
max_num=[10,25,30,5]
m=reduce(lambda x,y:x if x>y else y,max_num)
print(m)
# Use reduce() to concatenate ["a","b","c"] into "abc".
concat=["a","b","c"]
c=reduce(lambda x,y:x+y,concat)
print(c)
# Count occurrences of each element in [1,2,2,3,3,3] using reduce().
elements=[1,2,2,3,3,3]
freq={}
e=reduce(lambda acc,x:{**acc,x:acc.get(x,0)+1},elements,{})
print(e)
# Use reduce() to flatten [[1,2],[3,4],[5]] into [1,2,3,4,5].
f=[[1,2],[3,4],[5]]
s=reduce(lambda x,y:x+y,f)
print(list(s))
# Calculate the product of [2,3,4] using reduce().
l=[2,3,4]
product=reduce(lambda x,y:x*y,l)
print(product)
# Use reduce() to find the longest word in ["cat","elephant","dog"].
s=["cat","elephant","dog"]
l=reduce(lambda x,y:x if len(x)>len(y) else y,s)
print(l)
# Build an object mapping names to ages from:[{name:"Tom",age:15},{name:"Jerry",age:20}]
obj=[{"name":"Tom","age":15},{"name":"Jerry","age":20}]
def fun(a,x):
    a[x["name"]]=x["age"]
    return a
res=reduce(fun,obj,{})
print(res)
# Use reduce() to reverse ["a","b","c"] into "cba".
a=["a","b","c"]
rev=[]
r=reduce(lambda x,y:y+x,a)
print(r)
# Calculate the average of [10,20,30,40] using reduce().
a=[10,20,30,40]
av=reduce(lambda x,y:x+y ,a)
avg=av/len(a)
print(avg)

