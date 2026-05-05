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