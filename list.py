list1=[1,2,3 ,'sunitha',2,4.89,9.0,3+3j]
# list1.append("sun")
print(list1)
list2=[2,5,'sun',9.8]
print(list2)
list1.extend(list2)
print(list1)
list1.insert(2,'puppy')
print(list1)
list1.remove(1)
print(list1)
list1.pop(5)
print(list1)
list3=[1,8,9,4,7,3,0,9,27,89]
list3.sort()
print(list3)
list1.reverse()
print(list1,list2,list3)
list3.clear()
print(list3)
print(len(list1))
print(len(list2))
print(len(list3))
list3=[1,3,6,8,0,4,5,6,6]
print(sum(list3))
print(min(list3))
print(max(list3))
print([list3[0:7:2]])
#list comprehension:
#new=[expresssion for item in iterable  if condition]
list4=[i *i for i in list3 if i%2==0]
print(list4)
list5=[i**2 for i in list4 if i%2==0]
print(list5)