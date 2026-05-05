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