# 2. Lists – Practice Questions
# Find the largest element in a list.
l=[1,4,3,7,9]
def large_num(l):
    large=0
    for i in l:
        if i>large:
            large=i
    print(large)
# large_num(l)
# Find the smallest element in a list.
l=[1,4,3,7,9]
def small_num(l):
    small=float('inf')
    for i in l:
        if i<small:
            small=i
    print(small)
# small_num(l)
# Find the sum of all elements in a list.
l=[1,2,3,4]
def sum_of_digits(l):
    sum=0
    for i in l:
        sum+=i
    print(sum)
# sum_of_digits(l)
# Count the number of elements in a list without using len().
l=[1,2,3,4,5,6,7,8,9,0]
def no_of_elements(l):
    count=0
    for i in l:
        count+=1
    print(count)
# no_of_elements(l)

# Find the average of elements in a list.
l=[1,2,3,4,5,6,7,8,9,0]
def average(l):
    sum=0
    for i in l:
        sum+=i
    a=sum/len(l)
    print(a)
# average(l)
# Count how many even and odd numbers are present.
def count_even_odd(l):
    count_even=0
    count_odd=0
    for i in l:
        if i%2==0:
            count_even+=1
        else:
            count_odd+=1
    print(count_even,count_odd)
# count_even_odd(l)

# Print only positive numbers from a list.
l=[1,9,-5,-2,9,7,2]
def positive_num(l):
    p=[]
    for i in l:
        if i>0:
            p.append(i)
    return p
# print(positive_num(l)) 
# Print only negative numbers from a list.
l=[1,9,-5,-2,9,7,2]
def negative_num(l):
    n=[]
    for i in l:
        if i<0:
            n.append(i)
    return n
# print(negative_num(l))

# Reverse a list without using reverse().
l=[1,0,3,2,4]
def rev(l):
    for i in range(len(l)-1,-1,-1):
        print(i,end=" ")
# rev(l)
# Check whether an element exists in a list.
# n=int(input("enter a number:"))
# def elem_exists(l):
#         if n in l:
#             print('element exists')
#         else:
#             print("not exists")
# elem_exists([1,0,3,2,4,5,6,7])

# Intermediate
# Find the second-largest element.
l=[10, 20, 5, 30, 25]
# Expected:
# 25
def sec_large(l):
    large=l[0]
    sec=l[0]
    for i in l:
        if i>large:
            sec=large
            large=i
        elif i>sec and  sec!=large:
            sec=i
    print(sec)
# sec_large(l)
# Find the second-smallest element.
def sec_small(l):
    small=l[0]
    sec=l[0]
    for i in l:
        if i<small:
            sec=small
            small=i
        elif i<sec and  sec!=small:
            sec=i
    print(sec)
# sec_small(l)
# Remove duplicate elements from a list.
# Example:
l=[10, 20, 10, 30, 20, 40]
# Expected:
# [10, 20, 30, 40]
def remove_duplicates(l):
    for i in range(len(l)-1,0,-1):
        if l.count(l[i])>1:
            l.pop(i)
    print(l)
# remove_duplicates(l)

# Count the frequency of each element.
l=[10, 20, 10, 30, 20, 40]
def count_frequency(l):
    freq={}
    for i in l:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    print(freq)
# count_frequency(l)
# Find the elements that occur more than once.
l=[10, 20, 10, 30, 20, 40]
freq={}
def count_frequency(l):
    for i in l:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
        if freq[i]>1:
            print(i)
# count_frequency(l)
# Find the elements that occur only once.
l=[10, 20, 10, 30, 20, 40]
def count_frequency(l):
    freq={}
    for i in l:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    for i in freq:
        if freq[i]==1:
            print(i)
# count_frequency(l)
# Find common elements between two lists. 
l=[1,4,3,5,7,2]
l1=[1,4,2,9,8,0]
def common_elements(l,l1):
    l2=[]
    for i in l:
        if i in l1:
            l2.append(i)
    print(l2)
# common_elements(l,l1)
# Find elements present in the first list but not in the second.
l=[1,4,3,5,7,2]
l1=[1,4,2,9,8,0]
def identify_elements(l,l1):
    l2=[]
    for i in l:
        if i not in l1:
            l2.append(i)
    print(l2)
# identify_elements(l,l1)
# Merge two lists without duplicates.
l=[1,4,3,5,7,2]
l1=[1,4,2,9,8,0]
def merge_lists(l,l1):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    for i in l1:
        if i not in l2:
            l2.append(i)
    print(l2)
# merge_lists(l,l1)
# Find the intersection of two lists without using set().
l=[1,4,3,5,7,2]
l1=[1,4,2,9,8,0]
def intersection_elements(l,l1):
    for i in l:
        if i in l1:
            print(i)
# intersection_elements(l,l1)
# Interview Level
# Find the missing number from a list containing numbers from 1 to n.
# Example:
n= [1, 2, 3, 5, 6]
# Expected:
# 4
def missing_elements(n):
    l=set(n)
    m=max(n)
    for i in range(1,max(n)+1):
        if i not in n:
            print(i) 
# missing_elements(n)
# Find duplicate elements in a list.
l=[1,3,2,4,3,3,2,5,6,2]
def duplicates(l):              
    dup=[ i for i  in l if l.count(i)>1]
    return list(set(dup))
# print(duplicates(l))
# Find the first non-repeated element.
l=[1,3,2,4,3,3,2,5,6,2]
def non_repeated_firstnumber(l):
    for i in l :
        if l.count(i)==1:
            return  i
# print(non_repeated_firstnumber(l))

# Find the first repeated element.
l=[1,3,2,4,3,3,2,5,6,2]
def repeated_firstnumber(l):
    for i in l:
        if l.count(i)>1:
            return i
print(repeated_firstnumber(l))
# Move all zeros to the end.
l=[0, 1, 0, 3, 12]
def moving_zeros(l):
    for i in range(len(l)-1,-1,-1):
        for j in range(i):
            if l[j]==0:
                l[j],l[j+1]=l[j+1],l[j]
    print(l)
# moving_zeros(l)

# Separate even and odd numbers.
# Example:
l=[1, 2, 3, 4, 5, 6]
# Expected:
# [2, 4, 6, 1, 3, 5]
# def separate_even_odd(l):
#     for i in range(len(l)-1,-1,-1):
#         for j in range(i):
#             if l[j]%2!=0:
#                 l[j],l[j+1]=l[j+1],l[j]
#     print(l)
# separate_even_odd(l)
def separate_even_odd(l):
    even=[x for x in l if x%2==0]
    odd=[x for x in l if x%2!=0]
    return even+odd
print(separate_even_odd(l))



# Find the maximum difference between two elements.
l1=[1,2,3,0,4,5,7,8]
def max_diff(l):
    l=l1[0]
    s=float('inf')
    for i in l1:
        if i >l:
            l=i
        elif i<s:
            s=i
    return l-s
print(max_diff(l1))
        

# Find the pair of elements whose sum equals a given target.
# Example:

# numbers = [2, 7, 11, 15]
# target = 9
# Expected:
# 2, 7
l=[]
num=[7,2,11,15]
def sum_target(num):
    target=9
    for i in range(len(num)-1,-1,-1):
        if num[i]+num[i-1]==target:
            l.append(num[i])
            l.append(num[i-1])
    return l
print(sum_target(num))

# Find all pairs whose sum equals the target.
l=[4,5,8,9,1,5,2,3,4,2]
def pairs_sum_target(l):
    t=10
    s=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==t:
                s.append(l[i])
                s.append(l[j])
    return s
print(pairs_sum_target(l))
# Find the longest consecutive sequence in a list.
l = [100, 4, 200, 1, 3, 2, 1, 2] 
def longest_consecutive(l):
   l.sort()
   max_length=1
   curr_length=1
   for i in range(1,len(l)):
        if l[i]==l[i-1]:
           continue
        elif l[i]==l[i-1]+1:
           curr_length+=1
        else:
            max_length=max(max_length,curr_length)
            curr_length+=1
        return max(max_length,curr_length)
print(longest_consecutive(l))





