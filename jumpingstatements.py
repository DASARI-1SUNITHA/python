# Level 7 — Jumping Statements

# break
# Print numbers from 1 to 20, but stop when the number reaches 10.
def print_numbers():
    for i in range(1, 21):
        print(i, end=" ")
        if i == 10:
            break

print_numbers()
# Print numbers from 1 to 100. Stop when you find the first number divisible by 7.
def factors():
    for i in range(1,100):
        if i%7==0:
            print(i)
            break
factors()

# Search for a number in a list.
numbers = [10, 20, 30, 40, 50]

# If the number is found, print "Found" and stop searching.
def search():
    for num in numbers:
        n=int(input('enter a number:'))
        if n in numbers:
            print("found")
            break
        else:
            print("not found")
search()


# Keep asking the user for numbers until they enter 0.
def search_zero():
    while True:
        n = int(input("Enter a number: "))
        if n == 0:
            break
search_zero()
# Keep asking for a password until the correct password is entered.
def check_password():
    correct_password = "secret123"
    while True:
        password = input("Enter password: ")
        if password == correct_password:
            print("Access granted")
            break

check_password()
# continue
# Print numbers from 1 to 20 but skip even numbers.
def skip_evens():
    for i in range(1, 21):
        if i % 2 == 0:
            continue
        print(i, end=" ")

skip_evens()
# Print numbers from 1 to 50 but skip numbers divisible by 5.
def skip_divisible_by_five():
    for i in range(1, 51):
        if i % 5 == 0:
            continue
        print(i, end=" ")

skip_divisible_by_five()
# Print only positive numbers from:
# numbers = [10, -5, 20, -3, 0, 15, -8]
def print_positives():
    numbers = [10, -5, 20, -3, 0, 15, -8]
    for num in numbers:
        if num <= 0:
            continue
        print(num, end=" ")

print_positives()
# Print only odd numbers from a list.
def print_odds():
    numbers = [10, 15, 20, 25, 30]
    for num in numbers:
        if num % 2 == 0:
            continue
        print(num, end=" ")

print_odds()
# Find the sum of positive numbers while ignoring negative numbers.
def sum_positives():
    numbers = [10, -5, 20, -3, 15]
    total_sum = 0
    for num in numbers:
        if num < 0:
            continue
        total_sum += num
    print(total_sum)

sum_positives()
# pass
# Create a loop from 1 to 10 and use pass when the number is 5.
def loop_with_pass():
    for i in range(1, 11):
        if i == 5:
            pass
        print(i, end=" ")

loop_with_pass()
# Create a function called login() but leave its implementation empty using pass.
def login():
    pass

login()
# Create an if condition for a future feature and use pass.
def future_feature_check():
    user_has_premium = True
    if user_has_premium:
        pass

future_feature_check()
# 🔥 Level 8 — Interview-Level Problems
# Fibonacci Series
# Input: 7

# Output:
# 0 1 1 2 3 5 8
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(7)
# Armstrong Number
# Input: 153

# 1³ + 5³ + 3³ = 153

# Output:
# Armstrong
def check_armstrong(num):
    temp = num
    sum_of_cubes = 0
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10

    if num == sum_of_cubes:
        print("Armstrong")
    else:
        print("Not Armstrong")

check_armstrong(153)
# Strong Number
# Input: 145

# 1! + 4! + 5! = 145
def check_strong(num):
    temp = num
    sum_of_factorials = 0
    while temp > 0:
        digit = temp % 10
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        sum_of_factorials += fact
        temp //= 10

    if num == sum_of_factorials:
        print("Strong Number")
    else:
        print("Not a Strong Number")

check_strong(145)
# Perfect Number
# Input: 28

# 1 + 2 + 4 + 7 + 14 = 28
def check_perfect(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if num == sum_of_divisors:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

check_perfect(28)
# Automorphic Number
# Input: 25

# 25² = 625

# Output: Automorphic
def check_automorphic(num):
    square = num ** 2
    temp = num
    digits_count = 0
    while temp > 0:
        digits_count += 1
        temp //= 10

    if square % (10 ** digits_count) == num:
        print("Automorphic")
    else:
        print("Not Automorphic")
check_automorphic(25)
# Harshad Number
# Check whether a number is divisible by the sum of its digits.

# Input: 18

# 1 + 8 = 9
# 18 % 9 = 0

# Output: Harshad
def check_harshad(num):
    temp = num
    sum_of_digits = 0
    while temp > 0:
        sum_of_digits += temp % 10
        temp //= 10

    if num % sum_of_digits == 0:
        print("Harshad")
    else:
        print("Not Harshad")

check_harshad(18)

# GCD of Two Numbers
# Input:
# 12 18

# Output:
# 6
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    print(a)

find_gcd(12, 18)
# LCM of Two Numbers
# Input:
# 12 18

# Output:
# 36
def find_lcm(a, b):
    num1, num2 = a, b
    while num2:
        num1, num2 = num2, num1 % num2
    gcd = num1
    lcm = (a * b) // gcd
    print(lcm)

find_lcm(12, 18)
# Reverse Without String Conversion
# Input: 12345
# Output: 54321

# Don't use:

# str()
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    print(reversed_num)

reverse_number(12345)
# Palindrome Without String Conversion
# Input: 1221
# Output: Palindrome
def check_palindrome(num):
    temp = num
    reversed_num = 0
    while temp > 0:
        digit = temp % 10
        reversed_num = (reversed_num * 10) + digit
        temp //= 10

    if num == reversed_num:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome(1221)
# Decimal to Binary
# Input: 10
# Output: 1010
def decimal_to_binary(num):
    binary_str = ""
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num //= 2
    print(int(binary_str))

decimal_to_binary(10)
# Binary to Decimal
# Input: 1010
# Output: 10
def binary_to_decimal(binary):
    decimal = 0
    base = 1
    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * base
        base = base * 2
        binary //= 10
    print(decimal)

binary_to_decimal(1010)
# 💪 Level 9 — Mixed Interview Problems
# Find the second largest digit in a number.
# Input: 58329
# Output: 8
def second_largest_digit(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10

    unique_digits = list(set(digits))
    unique_digits.sort()
    print(unique_digits[-2])

second_largest_digit(58329)
# Remove duplicate digits from a number.
# Input: 122334
# Output: 1234
def remove_duplicate_digits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10

    digits.reverse()
    unique_digits = []
    for d in digits:
        if d not in unique_digits:
            unique_digits.append(d)

    result = 0
    for d in unique_digits:
        result = (result * 10) + d
    print(result)

remove_duplicate_digits(122334)
# Count frequency of each digit.
# Input: 112233

# Output:
# 1 → 2
# 2 → 2
# 3 → 2
def digit_frequency(num):
    counts = {}
    while num > 0:
        digit = num % 10
        counts[digit] = counts.get(digit, 0) + 1
        num //= 10

    for digit in sorted(counts.keys()):
        print(f"{digit} → {counts[digit]}")

digit_frequency(112233)
# Find the first repeated digit.
# Input: 123245
# Output: 2
def first_repeated_digit(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()

    seen = []
    for d in digits:
        if d in seen:
            print(d)
            break
        seen.append(d)

first_repeated_digit(123245)
# Find the first non-repeated digit.
# Input: 1123455
# Output: 2
def first_non_repeated_digit(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()

    for d in digits:
        if digits.count(d) == 1:
            print(d)
            break

first_non_repeated_digit(1123455)
# Print numbers between 1 and 100 that are divisible by 3 or 5.
def divisible_by_three_or_five():
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            print(i, end=" ")

divisible_by_three_or_five()
# Print numbers between 1 and 100 that are divisible by 3 and 5.
def divisible_by_three_and_five():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")

divisible_by_three_and_five()
# Find the sum of numbers divisible by 3 but not by 5.
def sum_three_not_five():
    total_sum = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            total_sum += i
    print(total_sum)

sum_three_not_five()
# Count positive, negative, and zero values in a list.
def count_value_types():
    items = [10, -5, 0, 20, -3, 0, 15]
    positives = 0
    negatives = 0
    zeros = 0

    for item in items:
        if item > 0:
            positives += 1
        elif item < 0:
            negatives += 1
        else:
            zeros += 1

    print(f"Positives: {positives}, Negatives: {negatives}, Zeros: {zeros}")

count_value_types()
# Find the largest and smallest numbers in a list without using max() or min().
def find_extremes():
    items = [10, 20, 5, 40, 30]
    largest = items[0]
    smallest = items[0]

    for item in items:
        if item > largest:
            largest = item
        if item < smallest:
            smallest = item

    print(f"Largest: {largest}, Smallest: {smallest}")

find_extremes()
# Reverse a list using a loop.
def reverse_list():
    items = [1, 2, 3, 4, 5]
    reversed_list = []
    for i in range(len(items) - 1, -1, -1):
        reversed_list.append(items[i])
    print(reversed_list)

reverse_list()
# Find duplicate elements in a list using loops.
def find_list_duplicates():
    items = [1, 2, 2, 3, 4, 4, 5]
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    print(duplicates)

find_list_duplicates()
# Find common elements between two lists using loops.
def find_common_elements():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    print(common)

find_common_elements()
# Find the missing number from:
# [1, 2, 3, 5, 6]

# Expected:

# 4
def find_missing_number():
    items = [1, 2, 3, 5, 6]
    n = len(items) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(items)
    print(expected_sum - actual_sum)

find_missing_number()
# Find the longest consecutive sequence of numbers in a list.
def longest_consecutive_sequence():
    items = [100, 4, 200, 1, 3, 2]
    items_set = set(items)
    longest_streak = 0

    for item in items_set:
        if item - 1 not in items_set:
            current_item = item
            current_streak = 1
            while current_item + 1 in items_set:
                current_item += 1
                current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak

    print(longest_streak)

longest_consecutive_sequence()