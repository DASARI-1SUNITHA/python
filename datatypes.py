#None,Numeric,list,tuple,set,string,range,dictionary
num=2.8
print(type(num))
n=3
print(type(n))
num=3+8j
type(num)
a=6.7
b=int(a)
print(type(a))
k=float(b)
print(type(b))
c=complex(b,k)

print(c)
d=b<k
print(type(d))

lst=[1,5,4,8,7]
print(type(list))
set={1,5,8,9}
print(type(set))

tuple=(4,6,8,6)
print(type(tuple))

str='sum'
st='q' 
print(type(str))
print(type(st))

range(2,10)
print(list(range(2,10)))

print(list(range(2,10,2)))
print(type(range(2,10)))


dictionary1={1:"sun",2:3,3:2,4:"puppy",5:"sunitha",6:4.89,7:5+8j,8:2.908776}
print(dictionary1)
print(type(dictionary1))
print(dictionary1.keys())
print(dictionary1.values())