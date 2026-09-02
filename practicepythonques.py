# Beginner
# Reverse a string without using [::-1].
s='iam learning python'
def reverse(s):
    result=""
    for ch in s:
        result=ch+result
    print(result)
# reverse(s)
    

# Check whether a string is a palindrome.
s="madam"
def palindrome(s):
    temp=s
    res=""
    for ch in s:
        res=ch+res
    # print(res)
    if res==temp:
        print("palindrome")
    else:
        print("not a palindrome")
# palindrome(s)
# Find the largest and second-largest numbers in a list.
list1=[1,8,9,24,6]
def largest_sec_largest(list1):
    l=list1[0]
    sec=list1[0]
    for i in list1:
        if i >l:
            sec=l
            l=i
        elif i>sec and i !=l:
            sec=i
    return sec,l
# print(largest_sec_largest(list1))
# Remove duplicates from a list while preserving order.
l=[1,2,5,2,3,7,8,9,5]
def remove_deplicates(l):
    for i in range(len(l)-1,-1,-1):
        if l.count(l[i])>1:
            l.pop(i)
    return l
# print(remove_deplicates(l))
# Count the frequency of each character in a string.
s="i am learning python"
def freq_count(s):
    freq={}
    for i in s:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq
# print(freq_count(s))
# Find all duplicate elements in a list.
l=[1,2,5,2,3,7,8,9,5]
def duplicate_elements(l):
    freq={}
    for i in l:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    if freq[i]>1:
        print(freq[i])
# duplicate_elements(l)
# Check whether two strings are anagrams.
s='listen'
s1='silent'
def anagrams(s,s1):
    if sorted(s)==sorted(s1):
        print("anagram")
    else:
        print('not anagram')
# anagrams(s,s1)

# Find the factorial of a number using recursion.
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
# print(factorial(5))
# Generate the first n Fibonacci numbers.
def fibonacci(n):
    a=0
    b=1
    print(a,b)
    for i in range(n):
        a,b=b,a+b
        print(b)
# fibonacci(10)
# Find the missing number from an array containing numbers 1 through n.
l=[1,3,4,5,6]
def missing_number(l):
    for i in range(1,7):
        if i not in l:
            print(i)
# missing_number(l)
# Find the intersection of two lists.
l=[1,4,2,5,7]
l1=[4,7,2,9,3]
def intersection(l,l1):
    l2=[]
    for i in l:
        if i in l1:
            l2.append(i)
    return l2
# print(intersection(l,l1))
# Separate even and odd numbers from a list.
l=[1,2,5,3,4,6,7,8]
def sep_even_odd(l):
    for i in range(len(l)-1,-1,-1):
        for j in range(i):
            if l[j]%2==0:
                l[j],l[j+1]=l[j+1],l[j]
    return l
# print(sep_even_odd(l))

# Find the first non-repeating character in a string.
s='banana'
def non_repeating_char(s):
    freq={}
    for i in s:
        if  i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    if freq[i]==1:
        print(freq[i])
non_repeating_char(s)


# Implement FizzBuzz.
def fizzbuzz(n):
    for i in range(1,n):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i %3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
# fizzbuzz(100)
# Flatten a one-level nested list.
l=[[2,3,1],[2,6,0],[6,7]]
def flatten_list(l):
    f=[]
    for i in l:
        for item in i:
            f.append(item)
    return f
# print(flatten_list(l))



# Intermediate
# Given an array and target, solve Two Sum.
l=[2,7,9,8,0,11,15,5,4]
def sum_twos(l):
    target=9
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==target:
                print(l[i],l[j])
# sum_twos(l)

# Group a list of strings into anagram groups.
def group_anagrams(words):
    g={}
    for word in words:
        s="".join(sorted(word))
        if s not in g:
            g[s]=[]
        g[s].append(word)
    return list(g.values())
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Rotate an array by k positions.
l=[1,2,3,4,5]
def rotate_array(l):
    k=2
    for i in range(k):
        last_element=l.pop()
        l.insert(0,last_element)
    return l
print(rotate_array(l))

# Implement a stack using Python lists.
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)  
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop() 
        return "Stack is empty"
            
    def is_empty(self):
        return len(self.stack) == 0


s = Stack()
s.push(10)
s.push(20)
print(s.pop())   
# Implement a queue without using collections.deque.
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item) 
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) 
        return "Queue is empty"
        
    def is_empty(self):
        return len(self.queue) == 0
q = Queue()
q.enqueue("A")
q.enqueue("B")
print(q.dequeue())

