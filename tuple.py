#👉 Tuple is introduced to store multiple values as a fixed, immutable collection, 
# ensuring data safety, better performance, and support for use as dictionary keys, 
# which is not possible with mutable data types like lists.
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