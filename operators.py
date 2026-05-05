#Aritmetic operations

# Prices of items
laptop_price = 50000      
mouse_price = 1000        
quantity = 2              
discount = 5000          

# 1. Addition (+) → total cost of items
total_price = laptop_price + mouse_price
print("Addition (+):", total_price)

# 2. Multiplication (*) → cost based on quantity
total_quantity_price = total_price * quantity
print("Multiplication (*):", total_quantity_price)

# 3. Subtraction (-) → apply discount
final_price = total_quantity_price - discount
print("Subtraction (-):", final_price)

# 4. Division (/) → split bill between 2 friends
split_bill = final_price / 2
print("Division (/):", split_bill)

# 5. Floor Division (//) → whole amount each person pays
floor_split = final_price // 2
print("Floor Division (//):", floor_split)

# 6. Modulus (%) → remaining amount after equal split
remainder = final_price % 2
print("Modulus (%):", remainder)

# 7. Exponentiation (**) → reward points calculation
reward_points = quantity ** 2
print("Exponentiation (**):", reward_points)

#assignment operators
# Initial balance
balance = 10000   # = (assignment)
print("Initial Balance:", balance)

# Deposit money
balance += 2000   # balance = balance + 2000
print("After Deposit (+=):", balance)

# Withdraw money
balance -= 1500   # balance = balance - 1500
print("After Withdrawal (-=):", balance)

# Salary credited (double bonus)
balance *= 2      # balance = balance * 2
print("After Bonus (*=):", balance)

# Paying EMI (division)
balance /= 2      # balance = balance / 2
print("After EMI (/=):", balance)

# Floor division (round off)
balance //= 3     # removes decimals
print("After Floor Division (//=):", balance)

# Modulus (remaining amount)
balance %= 1000
print("Remaining Balance (%=):", balance)

# Power (investment growth)
balance **= 2
print("After Investment (**=):", balance)


#relational operators
## == != < > <= >=
age = 22              
marks = 75            
experience = 2       

# 1. Equal to (==)
print("Equal to (==):", age == 22)

# 2. Not equal to (!=)
print("Not Equal (!=):", marks != 50)

# 3. Greater than (>)
print("Greater than (>):", marks > 60)

# 4. Less than (<)
print("Less than (<):", experience < 5)

# 5. Greater than or equal (>=)
print("Greater than or equal (>=):", age >= 21)

# 6. Less than or equal (<=)
print("Less than or equal (<=):", marks <= 100)

#logical operators :and or not
# Student details
marks = 65            # int
attendance = 80       # int
has_certificate = False   # bool
blacklisted = False       # bool

# 1. AND → both conditions must be True
eligible_marks_attendance = (marks >= 60) and (attendance >= 75)
print("AND:", eligible_marks_attendance)

# 2. OR → at least one condition must be True
eligible_with_certificate = eligible_marks_attendance or has_certificate
print("OR:", eligible_with_certificate)

# 3. NOT → reverse the condition
final_eligibility = eligible_with_certificate and (not blacklisted)
print("NOT:", final_eligibility)

#unary operator:+,-,not
# Temperature reading (can be negative)
temperature = -10   # int

# System status
system_active = False   # bool

# 1. Unary Plus (+) → keeps value as it is
print("Unary Plus (+):", +temperature)

# 2. Unary Minus (-) → changes sign
print("Unary Minus (-):", -temperature)

# 3. NOT → reverses boolean value
print("NOT:", not system_active)
#output:Unary Plus (+): -10
# Unary Minus (-): 10
# NOT: True