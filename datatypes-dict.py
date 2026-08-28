# 4. Dictionary – Practice Questions
# Beginner
# Create a dictionary containing student names and marks and print each student's details.
d={"A": 80,"B": 90,"C": 70}
def details_std(d):
    for i ,j in d.items():
        print(i,j)
# details_std(d)
# Find the sum of all dictionary values.

# Example:

# marks = {
#     "A": 80,
#     "B": 90,
#     "C": 70
# }

# Expected:
# 240
def details_std(d):
    sum=0
    for j in d.values():
        sum+=j
    print(sum)
# details_std(d)

# Find the maximum value in a dictionary.
def max_value(d):
    maxv=0
    for j in d.values():
        if j >maxv:
            maxv=j
    print(maxv)
# max_value(d)
# Find the minimum value in a dictionary.
def min_value(d):
    minv=float('inf')
    for j in d.values():
        if j<minv:
            minv=j
    print(minv)
# min_value(d)
# Check whether a key exists.
def key_exists(d):
    k=input("enter a key:")
    if k in d.keys():
        print('key exists')
    else:
        print('not exists')
# key_exists(d)
# Count the number of keys without using len().
def count_keys(d):
    count=0
    for k in d.keys():
        count+=1
    print(count)
# count_keys(d)
# Print all keys.
def print_keys(d):
    for i in d.keys():
        print(i)
print_keys(d)
# Print all values.
def print_values(d):
    for i in d.values():
        print(i)
# print_values(d)
# Print key-value pairs.
def print_pairs(d):
    for i,j in d.items():
        print(i,":",j)
# print_pairs(d)
# Merge two dictionaries.
def merge_dict(d):
    d1={'D':98,'E':85}
    d.update(d1)
    print(d)
# merge_dict(d)
# Intermediate
# Count the frequency of each character using a dictionary.

# Example:

# "hello"

# Expected:

# h: 1
# e: 1
# l: 2
# o: 1
s='hello'
def frequency(s):
    freq={}
    for ch in s:
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1
    for i,j in freq.items():
        print(i,":",j)
# frequency(s)

# Count the frequency of words in a sentence.
s="python is easy and python is fun"
def word_freq(s):
    words=s.split()
    freq={}
    for word in s.split():
        if word not in freq:
            freq[word]=1
        else:
            freq[word]+=1
    for k,v in freq.items():
        print(k,":",v)
# word_freq(s)

# Find the key with the highest value.

# Example:

d={"A": 80, "B": 95, "C": 70}

# Expected:

# B
def max_v_k(d):
    maxv=0
    maxk=d['A']
    for k,v in d.items():
        if v>maxv:
            maxv=v
            maxk=k
    print(maxk,":",maxv)
# max_v_k(d)

# Find the key with the lowest value.
def min_v_k(d):
    minv=float('inf')
    mink=d['A']
    for k,v in d.items():
        if v<minv:
            minv=v
            mink=k
    print(mink,":",minv)
# min_v_k(d)
# Sort a dictionary based on values.
def sort(d):
    sort_values=sorted(d.values())
    sort_dict={}
    for v in sort_values:
        for k in d:
            if d[k]==v:
                sort_dict[k]=v
    print(sort_dict)
# sort(d)
# Sort a dictionary based on keys.
d={1:'A',3:'B',4:'C',2:'D'}

def dict_sort_keys(d):
    keys=list(d.keys())
    keys.sort()
    sorted_dic={}
    for key in keys:
        sorted_dic[key]=d[key]
    print(sorted_dic)
# dict_sort_keys(d)
    

# Remove a key from a dictionary without using pop().
d={'A': 30, 'B': 10, 'C': 20}
def remove_key(d):
    k=input("enter a key:")
    if k in d:
        del d[k]
    print(d)
# remove_key(d)
# Swap keys and values.

# Example:

# {"a": 1, "b": 2}

# Expected:

# {1: "a", 2: "b"}
def swap_keys_values(d):
    for k,v in d.items():
        d[v]=k
    print(d)
# swap_keys_values(d)
# Find common keys between two dictionaries.
d={'a':1,'b':2}
d1={'b':2}
def common_keys(d,d1):
    for k in d.keys():
        if k in d1:
            print(k)
# common_keys(d,d1)

# Find keys that exist in the first dictionary but not in the second.
d = {'a': 1, 'b': 2, 'c': 3}
d1 = {'b': 2, 'd': 4}
def unique_to_first(d, d1):
    for k in d:
        if k not in d1:
            print(k)
# unique_to_first(d,d1)

# Interview Level
# Find duplicate values in a dictionary.
d={'a':100,'b':234,'c':234}
def dup_values(d):
    seen=set()
    de_values=set()
    for k ,v in d.items():
        if v in seen:
            de_values.add(v)
        else:
            seen.add(v)
    print(list(de_values))
# dup_values(d)


# Find the second-highest value in a dictionary.
# Group words based on their first character.

# Example:

# ["apple", "ant", "ball", "bat", "cat"]

# Expected:

# {
#     "a": ["apple", "ant"],
#     "b": ["ball", "bat"],
#     "c": ["cat"]
# }
# Convert two lists into a dictionary.

# Example:

# keys = ["name", "age", "city"]
# values = ["Sunitha", 23, "Hyderabad"]
# Combine two dictionaries and add values for common keys.

# Example:

# d1 = {"a": 10, "b": 20}
# d2 = {"a": 30, "c": 40}

# Expected:

# {"a": 40, "b": 20, "c": 40}
# Find the most frequent word in a sentence using a dictionary.
# Create a dictionary from a list where the key is the element and the value is its frequency.
# Find all keys having the same value.
# Flatten a nested dictionary.
# Find the maximum salary from an employee dictionary.
