#  Functions Coding Questions
# 🔹 List-based Questions
# Write a function that takes a list of numbers and returns the sum
# from  functools  import reduce
n=[1,1,2,3,4]
def sum(n):
    sum=0
    for i in n:
        sum+=i
    return sum
print(sum(n))
# a=reduce(lambda x,y:x+y,n)
# print(a)
# Pass a list of strings to a function and return the longest string.
l=["sunitha","Sun","Angel"]
def st(l):
    large=l[0]
    for i in l:
        if i>l[0]:
            large=i
    return large
print(st(l))

# Create a function that accepts a list and returns a new list with duplicates removed.
l1=[1,2,3,1,4,2,5,6]
l2=[]
def fun(l1):
    for i  in l1:
        if i not in l2:
            l2.append(i)
    return l2
print(fun(l1))
# Write a function that takes a list of integers and returns only the even numbers.
l=[1,2,3,4,5,6,7,8,9,10,11]
def even(l):
     for i in l:
        if i%2==0:
            print(i)
even(l)
# Pass a list of numbers and return the maximum and minimum values.
def max_min(l):
    large=l[0]
    small=l[0]
    for i in l:
        if i>l[0]:
            large=i
        elif i<l[0]:
            small=i
    return large,small
print(max_min(l))
# Write a function that takes a list and returns it reversed.
l3=[]
def reverse(l):
    for i in range(len(l)-1,-1,-1):
        l3.append(i)
    return l3
print(reverse(l))
# Create a function that accepts a list of words and returns them sorted alphabetically.
l=["Sunitha","Angel","Banana","Dog","Cat"]
n=len(l)
def order(l):
    for i in range(n):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
print(order(l))
# Write a function that takes a list of integers and returns their average.
l=[1,2,3,4,5,6,7,8]
def avge(l):
    sum=0
    for i in l:
        sum+=i
    a=sum/len(l)
    return a
print(avge(l))
# Pass a list of strings and return a list of their lengths.
l=["Sunitha","Angel","Banana","Dog","Cat"]
l2=[]
def length(l):
    for i in l:
        a=len(i)
        l2.append(a)
    return l2
print(length(l))
# Write a function that takes a list of numbers and returns the product of all elements.
l=[1,2,3,4]
def product(l):
    product=1
    for i in l:
        product*=i
    return product
print(product(l))
# 🔹 Tuple-based Questions
# Write a function that takes a tuple of numbers and returns the sum.
t=(1,2,3,4)
def sum(t):
    sum=0
    for i in t:
        sum+=i
    return sum
print(sum(t))
# Pass a tuple of strings and return the shortest string.
l=("Sunitha","Angel","Banana","Dog","cat")
def short(l):
    small=l[0]
    for i in l:
        if i<l[0]:
            small=i
    return small
print(short(l))

# Write a function that takes a list of numbers and returns the product of all elements.
t=(1,2,3,4,5)
def product(t):
    product=1
    for i in t:
        product*=i
    return product
print(product(t))
# Create a function that accepts a tuple and returns it as a list.
t=(1,2,3,4)
def fun(t):
    return list(t)
print(fun(t))
# Write a function that takes a tuple of integers and returns the count of odd numbers.
t=(1,2,3,4,5,6,7)
def count(t):
    count=0
    for i in t:
        if i%2!=0:
            count+=1
    return count
print(count(t))
# Pass a tuple of numbers and return the second largest value.
t=(1,2,3,4,5,6,7)
def sec_large(t):
    sec=t[0]
    large=t[0]
    for i in t:
        if i>large:
            sec=large
            large=i
        elif i>sec and i!=large:
            sec=i
    return sec
print(sec_large(t))
# Write a function that takes a tuple and returns it reversed.
t1=(1,2,3,4)
def reverse(t1):
    t2=()
    for i  in range(len(t1)-1,-1,-1):
        t2+=(t1[i],)
    return t2
print(reverse(t1))

# Create a function that accepts a tuple of words and returns them joined into a single string.
t=("python","Programming","Language")
def join(t):
    result=""
    for i in t:
        result+=i+" "
    return result.strip()
print(join(t))
# Write a function that takes a tuple of integers and returns a tuple with each element squared.
t=(1,2,3,4,5)
def square(t):
    a=()
    for i in range(len(t)):
        a+=(t[i]**2,)   
    return a
print(square(t))

# Pass a tuple of strings and return the one with the maximum vowels.
t=("Sunitha","Angel","Banana","Dog","cat")

def maxvowels(t):
    vowels="aeiouAEIOU"
    maxcount=0
    result=""
    for word in t:
        count=0
        for i in word:
            if i  in vowels:
                count+=1
        if count>maxcount:
            maxcount=count
            result=word
    return result
print(maxvowels(t))
# Write a function that takes a tuple and returns the number of unique elements.	
t=(1,2,3,4,5,1,2,4,7,6)
def unique(t):
    t1=()
    for i in t:
        if i not in t1:
            t1+=(i,)
    return t1
print(unique(t))
# 🔹 String-based Questions
# Write a function that takes a string and returns it reversed.
s="Sunitha"
def rev(s):
    for i in range(len(s)-1,-1,-1):
        print(s[i])
rev(s)
# Pass a string and return the count of vowels.
s="sunitha"
def count(s):
    vowels="aeiouAEIOU"
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count
print(count(s))
# Create a function that accepts a string and returns whether it is a palindrome.
# s=input("Enter a string:")
# def palindrome(s):
#     temp=s
#     rev=""
#     for i in range(len(s)-1,-1,-1):
#         rev+=s[i]
#     print(rev,end="")
#     if temp==rev:
#         print("palindrome")
#     else:
#         print("Not a palindrome")
# palindrome(s)

# Write a function that takes a string and returns the frequency of each character.
s="programming"
def frequency(s):
    fre={}
    for ch in s:
        if ch in fre:
            fre[ch]+=1
        else:
            fre[ch]=1
    return fre
print(frequency(s))
# Pass a string and return the first non-repeated character.
s="madam"
def repet(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    for ch in s:
        if freq[ch]==1:
            print(ch)
print(repet(s))
    
    
# Write a function that takes a string and returns it in uppercase.
s="sunitha"
def upper(s):
    return s.upper()
print(upper(s))
# Create a function that accepts a string and returns the number of words.
s1="Hello world"
def number(s):
    words=s1.split( )
    count=len(words)

    return count
print(count(s1))
# Write a function that takes a string and returns all unique characters.
s="madam"
def unique(s):
    s1=""
    for ch in s:
        if ch not in s1:
            s1+=ch
    return s1
print(unique(s))
# Pass a string and return the most frequent character.
s="banana"
def freq_character(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    if freq[ch]>=2:
        print("most frequent character",ch)
    else:
        print("No frequent character")
freq_character(s)    
# Write a function that takes a string and returns it without spaces.
s="   python is a programming language"
def space(s):
    s1=""
    for ch in s:
        if ch !=" ":
            s1+=ch
    return s1
print(space(s))
# 🔹 Dictionary-based Questions
# Write a function that takes a dictionary and returns the sum of all values.
d={1:2,2:3,3:4}
def sum_values(d):
    sum=0
    for i in d.values():
        sum+=i
    return sum
print(sum_values(d))
# Pass a dictionary and return the key with the maximum value.
dic={1:2,2:3,3:4}
def max_value(d):
    maxv=0
    maxkey=""
    for key,value in dic.items():
        if value>maxv:
            maxv=value
            maxkey=key
    return maxkey,maxv
print(max_value(s))
# Create a function that accepts a dictionary and returns a list of all keys.
def key(d):
    return d.keys()
print(key(d))
# Write a function that takes a dictionary and returns a list of all values.
def d_values(d):
    return d.values()
print(key(d))
# Pass a dictionary and return a new dictionary with keys and values swapped.
dic={"a":1,"b":2,"c":3}
def new_dic(dic):
    dic1={}
    for key,value in dic.items():
        dic1[value]=key
    return dic1
print(new_dic(dic))
# Write a function that takes a dictionary and returns the number of items.
dic={"a":1,"b":2,"c":3}
def no_items(dic):
    return len(dic)
print(no_items(dic))
# Create a function that accepts a dictionary and returns whether a given key exists.
dic={"a":1,"b":2,"c":3}
def dictionary(dic,key):
        if key in dic.keys():
            return True
        else:
            return False
print(dictionary(dic,"a"))

# Write a function that takes a dictionary and returns the average of numeric values.
d={1:2,2:3,3:4,4:5}
def dic(d):
    sum=0
    count=0
    for value in d.values():
        sum+=value
        count+=1
    if count==0:
        return None
    return sum/count
print(dic(d))    


# Pass a dictionary and return the key with the longest string value.
dic1={1:"Sunitha",3:"Sun",2:"Angel"}
def new_dic(dic):
    dic1={}
    max_len=0
    max_key=None
    for key,value in dic.items():
        if len(value)>max_len:
            max_len=len(value)
            max_key=key
    return max_key
print(new_dic(dic1))
# Write a function that takes a dictionary and returns a sorted list of keys.
dic1={1:"Sunitha",3:"Sun",2:"Angel"}
def sorting(d):
    l=[]
    for key in dic1:
        l.append(key)
    for i in range(len(dic1)):
        for j in range(0,len(dic1)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
print(sorting(dic1))



# 🔹 Mixed Data Structure Questions
# Write a function that takes a list of tuples and returns the tuple with the largest sum.
t=[(1,2),(3,4),(4,5)]
def sumtuple(t):
    maxsum=0
    maxtuple=None
    currsum=0
    for i in range(len(t)):
        currsum+=sum(t[i])
        if currsum>maxsum:
            maxsum=currsum
            maxtuple=t[i]
    return maxtuple
print(sumtuple(t))
# Pass a dictionary of lists and return the length of the longest list.
dic={1:[1,2,3],2:[1,2,3,4,5],3:[1,2,3,4,5,6,7]}
def maxlis(dic):
    maxlength=dic[1]
    maxkey=None
    for key ,value in dic.items():
        if len(value)>len(maxlength):
            maxlength=value
            maxkey=key
    return maxkey,maxlength
print(maxlis(dic))
# Create a function that accepts a list of strings and returns a dictionary with word lengths.
l=["apple", "bat", "carrot", "dog"]
def fun(l):
    d={}
    for i in l:
        d[i]=len(i)
    return d
print(fun(l))

# Write a function that takes a tuple of strings and returns a dictionary with frequency of each word.
t = ("apple", "banana", "apple", "orange", "banana", "apple")
def fre(t):
    freq={}
    for i in t:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
print(fre(t))
# Pass a list of dictionaries and return the dictionary with the maximum value for a given key.
t=[{1:1},{2:3},{3:4}]
def dic(t):
    maxvalue=0
    maxdic=None
    for i in t:
        for key,value in i.items():
            if value > maxvalue:
                maxvalue=value
                maxdic=i
    return maxdic
print(dic(t))
# Write a function that takes a string and returns a dictionary with counts of each word.
s="python is a programming language"
def countword(s):
    fre={}
    s1=s.split()
    for i in s1:
        if i in fre:
            fre[i]+=1
        else:
            fre[i]=1
    return fre
print(countword(s))
# Create a function that accepts a list of numbers and returns a tuple of (sum, average, max, min).
l=[1,2,3,4,5,6,7,8]
def fun(l):
    sum=0
    large=0
    small=l[0]
    for i in l:
        sum+=i
        if i>large:
            large=i
        if i<small:
            small=i
    avg=sum/len(l)
    return (sum,large,small,avg)
print(fun(l))    
# Write a function that takes a tuple of strings and returns a list of strings sorted by length.
t=("Sunitha","sun","Angel","Grace")
def sorting(t):
    l=list(t)
    for i in range(len(l)):
        for j in range(0,len(l)-i-1):
            if len(l[j])>len(l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]
    return l
print(sorting(t))
# Pass a dictionary of tuples and return the tuple with the maximum length.
d={1:(1,2),2:(1,2,3),3:(1,2,3,4)}
def maxtup(d):
    maxlength=d[1]
    maxkey=None
    for key ,value in d.items():
        if len(value)>len(maxlength):
            maxlength=value
            maxkey=key
    return maxkey,maxlength
print(maxtup(d))
# Write a function that takes a list of strings and returns a dictionary grouping them by their first letter.
s=["Sunitha","sun","Grace"]
def fun(s):
    d={}
    for i in s:
        firstletter=i[0]
        if firstletter not in d:
            d[firstletter]=[]
        d[firstletter].append(i)
    return d
print(fun(s))



# 🔢 Integer Function Questions (51–60)
# 51. Write a function that takes an integer and returns whether it is prime.
# p=int(input("Enter an integer:"))
# def prime(p):
#     factors=0
#     for i in range(2,n+1):
#         if n%i==0:
#             factors+=1
#         if factors==2:
#             return True
#         else:
#             return False
# if  prime(p):
#     print("Prime")
# else:
#     print("Not Prime")
# 52. Pass an integer to a function and return its factorial.
# n=int(input("Enter an integer:"))
# def fac(n):
#     fact=1
#     if n==0:
#         return 1
#     while n>0:
#         fact=fact*n
#         n-=1
#     return fact
# print(fac(n))
# 53. Create a function that accepts an integer and returns the sum of its digits.
# n=int(input("Enter a integer:"))
# def sumdigit(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit
#         n//=10
#     return sum
# print(sumdigit(n))
# 54. Write a function that takes an integer and returns whether it is an Armstrong number.
# n=int(input("Enter a number:"))
# def armstrong(n):
#     temp=n
#     sum=0
#     digits=len( str(n))
#     while n>0:
#         digit=n%10
#         sum+=digit**digits
#         n//=10
#     return sum==temp
# if armstrong(n):
#     print("Armstrong number")
# else:
#     print("Not a Armstrong number")
    

# 55. Pass an integer and return the reverse of its digits.
n=153
def reverse(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    return rev
print(reverse(n))

# 56. Write a function that takes an integer and returns whether it is a palindrome number.
p=12344321
def palindrome(p):
    temp=p
    rev=0
    while p>0:
        digit=p%10
        rev=rev*10+digit
        p//=10
    if rev==temp:
        print("Palindrome number")
    else:
        print("Not a palindrome number")
palindrome(p)
# 57. Create a function that accepts an integer and returns the count of even digits in it.
n=12344
def count(n):
    count=0
    while n>0:
        n//=10
        count+=1
    return count
print(count(n))
# 58. Write a function that takes an integer and returns the next Fibonacci number after it.
def fib(n):
    a=0
    b=1
    while b<=n:
        a,b=b,a+b
    return b
n=8
print(fib(n))

# 59. Pass an integer and return the greatest common divisor (GCD) of that integer and another fixed number.
def gcd(n):
    f=24
    for i in range(min(n,f),0,-1):
        if n%i==0 and f%i==0:
            return i
n=36
print(gcd(n))

# 60. Write a function that takes an integer and returns a list of all its divisors.
def divisors(n):
    r=[]
    for i in range(1,n+1):
        if n%i==0:
            r.append(i)
    return r
print(divisors(n=12))


