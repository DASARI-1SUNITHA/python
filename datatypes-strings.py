# 3. Strings – Practice Questions
# Beginner
# Reverse a string.
# Example:
# Python
# Expected:
# nohtyP
s='Python'
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end="")
def rev_string(s):
    rev=""
    for ch in s:
        rev=ch+rev
    print(rev)
# rev_string(s)
# Check whether a string is a palindrome.
s='madam'

def palindrome_string(s):
    rev=""
    for ch in s:
        rev=ch+rev
    if rev==s:
        print("palindrome")
    else:
        print("not palindrome")
# palindrome_string(s)
# Count the number of vowels.
s="python"
def count_vowels(s):
    count=0
    vowels='aeiouAEIOU'
    for ch in s:
        if ch in vowels:
            count+=1
    print(count)
# count_vowels(s)

# Count the number of consonants.
s="python"
def count_consonants(s):
    count=0
    vowels='aeiouAEIOU'
    for ch  in s:
        if ch not in vowels:
            count+=1
    print(count)
# count_consonants(s)
# Count digits in a string.
s='python123'
def count_digits(s):
    count=0
    for ch in s:
        if ch.isdigit():
            count+=1
    print(count)
# count_digits(s)
# Count spaces in a string.
s= 'python programming Language'
def count_spaces(s):
    count=0
    for ch in s:
        if ch==' ':
            count+=1
    print(count)
# count_spaces(s)
# Convert lowercase characters to uppercase without using .upper().
s= 'python programming Language'
def lower_uppercase(s):
    result=""
    for ch in s:
        if 'a'<=ch<='z':
            result+=chr(ord(ch)-32)
        else:
            result+=ch
    print(result)
# lower_uppercase(s)

# Convert uppercase characters to lowercase without using .lower().
s= 'PYTHoN PROGRAMmING LANgUAGE'
def upper_lowercase(s):
    result=""
    for ch in s:
        if 'A'<=ch<='Z':
            result+=chr(ord(ch)+32)
        else:
            result+=ch
    print(result)
# upper_lowercase(s)

# Find the length of a string without using len().
s='PYTHON PROGRAMMING LANGUAGE'
def len_string(s):
    count=0
    for ch in s:
            count+=1
    print(count)
# len_string(s)
# Remove all spaces from a string.
def remove_spaces(s):
    res=""
    for ch in s:
        if ch!=' ':
            res+=ch
    print(res)
# remove_spaces(s)                                                    
# Intermediate
# Count the frequency of each character.
# Example:
# banana
# Expected:
# b: 1
# a: 3
# n: 2
s='banana'
def freq_string(s):
    freq={}
    for ch in s:
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1
    print(freq)
# freq_string(s)

# Find the first non-repeated character.
s='banana'
def first_non_repeated_char(s):
    freq={}
    for ch in s:
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1
    for ch in freq:
        if freq[ch]==1:
            print(ch)
# first_non_repeated_char(s)
# Find the first repeated character.
s='banana'
def first_repeated_char(s):
    freq={}
    for ch in s:
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1
    if freq[ch]>=2:
        print(ch)
# first_repeated_char(s)
# Remove duplicate characters.
# Example:
# programming

# Expected:
# progamin
s='programming'
def  remove_duplicates(s):
    res=""
    for ch in s:
        if ch not in res:
            res+=ch
    print(res)
# remove_duplicates(s) 

# Find the most frequent character.
s='programming'
def freq_char(s):
    freq={}
    for ch in s:
        if ch not in freq:
            freq[ch]=1
        else:freq[ch]+=1
    for ch in freq:
        if freq[ch]>=2:
            print(ch)
# freq_char(s)        
# Find the least frequent character.
s='programming'
def freq_char(s):
    freq={}
    for ch in s:
        if ch not in freq:
            freq[ch]=1
        else:freq[ch]+=1
    least_char=""
    min_count=0
    for ch in freq:
        if freq[ch]<min_count:
            min_count=freq[ch]
            least_char=ch
    print(least_char)
# freq_char(s)
# Count the number of words in a sentence.
s='python programming languange'
def count_words(s):
    count=0
    for ch in s.split(' '):
        count+=1
    print(count)
# count_words(s)

# Reverse each word in a sentence.

# Example:
s= "Python is easy"
# Expected:
# "nohtyP si ysae"
def reverse_words(s):
    words=s.split(" ")
    result=[]
    for word in words:
        rev_word=""
        for ch in range(len(word)-1,-1,-1):
            rev_word+=word[ch]
        result.append(rev_word)
    print(" ".join(result))
# reverse_words(s)
# Reverse the order of words.

# Example:

# "Python is easy"

# Expected:

# "easy is Python"
def reverse_words(s):
    rev=" "
    for ch in s.split(" "):
        rev=ch+rev
    print(rev)
# reverse_words(s)
# Find the longest word in a sentence.
s="Python is easy"
def long_word(s):
    max_word=s[0]
    maxlength=len(s[0])
    for word in s.split(): 
        if len(word)>maxlength:
            max_word=word
            maxlength=len(word)
    print(max_word)
# long_word(s)

# Interview Level
# Check whether two strings are anagrams.

# Example:

# "listen"
# "silent"
s="listen"
s1='silent'
def anagrams(s,s1):
    if sorted(s)==sorted(s1):
        print('anagram')
    else:
        print("not anagram")
# anagrams(s,s1)
# Expected:

# True

# Find all duplicate characters.
s='programming'
def  remove_duplicates(s):
    res=""
    d=[]
    for ch in s:
        if ch in res and ch not in d:
            d.append(ch)
        else:
            res=ch+res
    print(" ".join(d))
remove_duplicates(s) 
# Find the longest substring without repeating characters.

# Example:

# "abcabcbb"

# Expected:

# "abc"
s='abcabcbb'
def long_substring(s):

# Find the number of occurrences of a substring without using .count().
# Check whether one string is a rotation of another.

# Example:

# "abcd"
# "cdab
s='abcd'
def string_rotation(s):
    s1=""
    for i in range(2):
        last_char=s.trim()
        s1=i+s1
    print(s1)
string_rotation(s)
# Expected:

# True
# Find the longest palindrome substring.
s='babad'
def longest_substr_palindrome(s):
    longest=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            substring=s[i:j+1]
            if substring==substring[::-1]:
                if len(substring)>len(longest):
                    longest=substring

    print(longest)
longest_substr_palindrome(s)

# Remove all duplicate words from a sentence.
def remove_duplicates_words(s):
    words=s.split()
    unique_words=[]
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    print(" ".join(unique_words))
remove_duplicates_words(s)
# Find the word with the highest frequency.
def high_word_freq(s):
    words=s.split()
    freq={}
    for word in words:
        if word not in words:
            freq[word]=1
        else:
            freq[word]+=1
    max_word=""
    max_count=0
    for word in freq:
        if freq[word]>max_count:
            max_count=freq[word]
            max_word=word
    print(max_word)
high_word_freq(s)

it 

# Compress a string.

# Example:

s="aaabbcccc"

# Expected:

# "a3b2c4"
res=""
count=1
def compress_str(s):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            res+=s[i]+str(count)
            count=1
    result+=s[-1]+str(count)
    print(result)
compress_str(s)
