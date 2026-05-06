# LIST Create a list of 5 numbers and print all elements
#Add an element at the end and at the beginning
#Remove a specific element from the list
# Find the largest and smallest element in a list
# Reverse a list without using built-in functions
#Count how many times an element appears Remove duplicates from a list
#Rotate list by k positions
#Find the second largest number without using sort() Flatten a nested list
list_1 = [1,4,7,2,8,]

print(list_1)
list_1.insert(0,344)
print(list_1)
list_1.insert(11,890)
print(list_1)
list_1.remove(8)
print(list_1)
print(max(list_1))
print(min(list_1))
list_2=[]
for i in range(len(list_1)-1,-1,-1):
  list_2.append(i)
print(list_2)
print(list_1.count(7))
print(list_1)
print(max(list_1))
list_1.remove(max(list_1))
#k rotations
k = 3

n = len(list_1)
k = k % n

rotated = []
for i in range(n - k, n):
    rotated.append(list_1[i])


for i in range(0, n - k):
    rotated.append(list_1[i])

print(rotated)

#Create a tuple with 5 elemet nts and print them
#Access first and last element Count occurrences of an element
#Find max and min values in a tuple
#Convert tuple → list → modify → back to tuple Slice a tuple to get middle elements
#Check if an element exists in a tuple Swap two tuples
#Find all pairs in tuple whose sum = target Remove duplicates from tuple manually

tuple=(2,4,6,8,9)
print(tuple[0])
print(tuple[-1])
print(tuple.count(2))
print(max(tuple))
print(min(tuple))
print(list(tuple))
print(tuple)
print(tuple[1:len(tuple)-1])
tuple_1=(1,7,3,8)
tuple,tuple_1=tuple_1,tuple
print(tuple,tuple_1)

t=(2,4,6,8,9)
target = int(input("Enter a number:"))
for i in range(len(t)):
    for j in range(i+1, len(t)):
        if t[i] + t[j] == target:
            print((t[i], t[j]))



#set
set={2,6,9,3,7,8}
print(set)
set.add(5)
print(set)
set.remove(2)
print(set)
s=int(input("Enter a valid integer:"))
print(s in set)
s1={2,7,4,0,6}
print(set | s1)
print( set & s1)
print(set -s1)

s2={6,7,3,5,4,7,3}
print(list(set))

s1={2,4,6,8,4,6,1,7,0}
s2={3,63,8,44}
s3={}
print((s1 - s2) | (s2- s1) )
print(s1 .isdisjoint(s2))
s1={2,4,6,8,4,6,1,7,0}
s2={3,63,8,44}
s3={4,8,1,0,5}
print(s1 & s2 & s3)
#Create a dictionary and print keys & values
#Add and update a key-value pair
#Delete a key from dictionary
#Count frequency of elements in a list using dictionary
#Merge two dictionaries
#Sort dictionary by values
#Get key with maximum value Group words by their length
# Find first non-repeating character in a string
# Build a student management system using dictionary
dict1={1:"sun",2:5,3:6+3j,4:6}
print(dict1)
print(dict1.keys())
print(dict1.values())
dict1[5]=77
print(dict1)
print(dict1.pop(4))


dict2={6:4,7:90}
print(dict1,dict2)

dict2={}
if i in dict:
  if i in dict2:
    dict2[i] += 1
  dict1[i]=1
print(dict2)
d = {"a": 10, "b": 50, "c": 30}

max_key = max(d, key=d.get)
print(max_key)
words = ["hi", "hello", "hey", "python"]

group = {}

for w in words:
    l = len(w)
    if l not in group:
        group[l] = []
    group[l].append(w)

print(group)

s = "afvhjhuyhugygy"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break


dic={"name":"Sunitha","rollno":401,"subject":"python"}
print(dic)