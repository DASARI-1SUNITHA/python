print("Hello wOrld")

#ceating list
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
#output:
# Hello wOrld
# [1, 2, 3, 'sunitha', 2, 4.89, 9.0, (3+3j)]
# [2, 5, 'sun', 9.8]
# [1, 2, 3, 'sunitha', 2, 4.89, 9.0, (3+3j), 2, 5, 'sun', 9.8]
# [1, 2, 'puppy', 3, 'sunitha', 2, 4.89, 9.0, (3+3j), 2, 5, 'sun', 9.8]
# [2, 'puppy', 3, 'sunitha', 2, 4.89, 9.0, (3+3j), 2, 5, 'sun', 9.8]
# [2, 'puppy', 3, 'sunitha', 2, 9.0, (3+3j), 2, 5, 'sun', 9.8]
# [0, 1, 3, 4, 7, 8, 9, 9, 27, 89]
# [9.8, 'sun', 5, 2, (3+3j), 9.0, 2, 'sunitha', 3, 'puppy', 2] [2, 5, 'sun', 9.8] [0, 1, 3, 4, 7, 8, 9, 9, 27, 89]
# []
# 11
# 4
# 0
# 39
# 0
# 8
# [[1, 6, 0, 5]]
# [36, 64, 0, 16, 36, 36]
# [1296, 4096, 0, 256, 1296, 1296]
#tuple
tuple1=(1,3,4,6,8 ,8,6,7,'sun',9.8,3+7j)
print(tuple1)
print(tuple1.count(8))
print(tuple1.index(3))
print(tuple1.index(8))
print("length:",len(tuple1))
tuple2=(1,7,9,3,5,7)
print(min(tuple2))
print(max(tuple2))
print(sum(tuple2))
print(tuple2[3:7:2])
print(tuple1+tuple2)
print(20 in tuple2)
# output:
# (1, 3, 4, 6, 8, 8, 6, 7, 'sun', 9.8, (3+7j))
# 2
# 1
# 4
# length: 11
# 1
# 9
# 32
# (3, 7)
# (1, 3, 4, 6, 8, 8, 6, 7, 'sun', 9.8, (3+7j), 1, 7, 9, 3, 5, 7)
# False





#set:

set1={1,2,3,'sun',5,6,8,8,9}
print(set1)
set1.add(28)
print(set1)
set2={2,5,7,9.7,98}
set2.update(set1)
print(set2)
set2.remove(3)
print(set2)
set1.discard(2)
print(set1)
print(set1.pop())
print(set2.clear())
#output:
# {1, 2, 3, 5, 6, 8, 9, 'sun'}
# {1, 2, 3, 5, 6, 8, 9, 'sun', 28}
# {1, 2, 98, 3, 5, 6, 7, 8, 9.7, 9, 'sun', 28}
# {1, 2, 98, 5, 6, 7, 8, 9.7, 9, 'sun', 28}
# {1, 3, 5, 6, 8, 9, 'sun', 28}
# 1
# None
set3={1,3,5,7,9,3,8}
print(set1.union(set3))# print(set1|set2)
print(set1.intersection(set3))#print(set1&set2)
print(set1.difference(set3))#print(set1-set3)
print(set1.symmetric_difference(set3))#print(set1^set3)
#output:
# {1, 3, 'sun', 5, 6, 7, 8, 9, 28}
# {8, 9, 3, 5}
# {'sun', 28, 6}
# {1, 'sun', 6, 7, 28}




#Dictionary
dictionary1={1:"sun",2:3,3:2,4:"puppy",5:"sunitha",6:4.89,7:5+8j,8:2.908776}
print(dictionary1)
print(dictionary1.keys())
print(dictionary1.values())
print(dictionary1.items())
print(dictionary1.pop(2))
print(dictionary1)
dictionary2={2:3,9:4.90}
print(dictionary2)
dictionary1.update(dictionary2)
print(dictionary1)
dictionary1.popitem()
print(dictionary1)
print(dictionary1.get(6))
dictionary2.clear()
print(dictionary2)
 #output:
#  {1: 'sun', 2: 3, 3: 2, 4: 'puppy', 5: 'sunitha', 6: 4.89, 7: (5+8j), 8: 2.908776}
# dict_keys([1, 2, 3, 4, 5, 6, 7, 8])
# dict_values(['sun', 3, 2, 'puppy', 'sunitha', 4.89, (5+8j), 2.908776])
# dict_items([(1, 'sun'), (2, 3), (3, 2), (4, 'puppy'), (5, 'sunitha'), (6, 4.89), (7, (5+8j)), (8, 2.908776)])
# 3
# {1: 'sun', 3: 2, 4: 'puppy', 5: 'sunitha', 6: 4.89, 7: (5+8j), 8: 2.908776}
# {2: 3, 9: 4.9}
# {1: 'sun', 3: 2, 4: 'puppy', 5: 'sunitha', 6: 4.89, 7: (5+8j), 8: 2.908776, 2: 3, 9: 4.9}
# {1: 'sun', 3: 2, 4: 'puppy', 5: 'sunitha', 6: 4.89, 7: (5+8j), 8: 2.908776, 2: 3}
# 4.89
# {}