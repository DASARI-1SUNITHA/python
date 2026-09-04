# ⭐ Level 1 — Basic Star Patterns
# 1. Increasing Triangle

# Print:

# *
# **
# ***
# ****
# *****
rows=6
cols=6
for row in range(1,rows):
    for col in range(1,cols):
        if row>=col:
            print("*",end=" ")
    print(' \n',end=" ")


# 2. Decreasing Triangle
# *****
# ****
# ***
# **
# *
for row in range(1,rows):
    for col in range(cols-row+1):
        print("*",end=" ")
    print('\n ',end=" ")
print("---------------------------------")
# 3. Right-Aligned Triangle
#     *
#    **
#   ***
#  ****
# *****
for row in range(1,rows+1):
    for spaces in range(cols-row):
        print(" ",end="")
    for col in range(row):
        print("*",end="")
    print()
# 4. Right-Aligned Decreasing Triangle
# *****
#  ****
#   ***
#    **
#     *
for row in range(1,rows+1):
    for spaces in range(row-1):
        print(" ",end="")
    for col in range(rows-row+1):
        print("*",end="")
    print()
# 5. Square Pattern
# *****
# *****
# *****
# *****
# *****
for i in range(rows):
    for j in range(cols):
        print("*",end="")
    print()
# 6. Hollow Square
# *****
# *   *
# *   *
# *   *
# *****
for i in range(1,rows+1):
    for j in range(1,cols+1):
        if i==1 or i==rows or j==1 or j==cols:
            print("*",end="")
        else:
            print(" ",end="")
    print()
# ⭐ Level 2 — Number Patterns
# 7. Increasing Numbers
# 1
# 12
# 123
# 1234
# 12345
for row in range(1,rows):
    for col in range(1,cols):
        if row>=col:
            print(col,end=" ")
    print()

# 8. Repeated Numbers
# 1
# 22
# 333
# 4444
# 55555
for row in range(1,rows):
    for col in range(1,rows+1):
        if row>=col:
            print(row,end="")
    print()
# 9. Same Number in Every Row
# 11111
# 22222
# 33333
# 44444
# 55555
for row in range(1,rows):
    for col in range(1,cols):
        print(row,end="")
    print()
# 10. Decreasing Numbers
# 12345
# 1234
# 123
# 12
# 1
for row in range(1,rows):
    for col in range(1,cols-row+1):
        print(col,end="")
    print()
# 11. Reverse Number Triangle
# 54321
# 5432
# 543
# 54
# 5
for row in range(1,rows):
    for col in range(5,row-1,-1):
        print(col,end="")
    print()
# 12. Row-Based Numbers
# 1
# 23
# 456
# 789
num=1
for row in range(1,rows):
    for col in range(1,row+1):
        if row>=col:
            print(num,end="")
        num+=1
    print()
# Try generating this dynamically rather than hardcoding the numbers.

# ⭐ Level 3 — Pyramid Patterns
# 13. Star Pyramid
#     *
#    ***
#   *****
#  *******
# *********
# 14. Inverted Pyramid
# *********
#  *******
#   *****
#    ***
#     *
# 15. Number Pyramid
#     1
#    123
#   12345
#  1234567
# 123456789
# 16. Repeated Number Pyramid
#     1
#    222
#   33333
#  4444444
# 555555555
# 17. Centered Increasing Numbers
#     1
#    121
#   12321
#  1234321
# 123454321
# ⭐ Level 4 — Hollow Patterns
# 18. Hollow Triangle
# *
# **
# * *
# *  *
# *****
# 19. Hollow Pyramid
#     *
#    * *
#   *   *
#  *     *
# *********
# 20. Hollow Inverted Pyramid
# *********
#  *     *
#   *   *
#    * *
#     *
# 21. Hollow Rectangle

# For rows = 5 and columns = 8:

# ********
# *      *
# *      *
# *      *
# ********
# ⭐ Level 5 — Character Patterns
# 22. Alphabet Triangle
# A
# AB
# ABC
# ABCD
# ABCDE
# 23. Repeated Alphabet
# A
# BB
# CCC
# DDDD
# EEEEE
# 24. Reverse Alphabet
# ABCDE
# ABCD
# ABC
# AB
# A
# 25. Alphabet Pyramid
#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI
# 26. Alphabet Row Pattern
# A
# BC
# DEF
# GHIJ
# KLMNO
# ⭐ Level 6 — Special Patterns
# 27. Diamond
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# 28. Hollow Diamond
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
# 29. X Pattern
# *   *
#  * *
#   *
#  * *
# *   *
# 30. Plus Pattern
#   *
#   *
# *****
#   *
#   *
# 31. Butterfly Pattern
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# 32. Sandglass Pattern
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
# 🔥 Level 7 — Interview-Level Patterns

# Try these without looking at solutions.

# 33. Pascal's Triangle

# For 5 rows:

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# 34. Floyd's Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 35. Binary Triangle
# 1
# 01
# 101
# 0101
# 10101
# 36. Alternating 0 and 1
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 37. Concentric Number Square

# For n = 4:

# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444
# 38. Number Diamond
#     1
#    123
#   12345
#  1234567
# 123456789
#  1234567
#   12345
#    123
#     1
# 39. Character Diamond
#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI
#  ABCDEFG
#   ABCDE
#    ABC
#     A
# 40. Palindrome Number Pyramid
#     1
#    121
#   12321
#  1234321
# 123454321
