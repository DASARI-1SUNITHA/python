# Section 1: Basic Function Creation (Positional Arguments)
# Write a function add_numbers(a, b) that returns the sum of two numbers. Call it with add_numbers(3, 5).
def add_numbers(a,b):
    print(a+b)
add_numbers(3,5)
# Create a function multiply(x, y) that multiplies two numbers. Call it with positional arguments.
def multiply(x,y):
    print(x*y)
multiply(4,8)
# Define a function greet(name) that prints "Hello, <name>!". Call it with "Alice".
def greet(name):
    print("Hello",name,"!")
greet(name="Alice")
# Write a function power(base, exponent) that returns base ** exponent. Call it with power(2, 3).
def power(base,exponent):
    print(base**exponent)
power(2,3)
# Create a function area_rectangle(length, width) that returns the area. Call it with area_rectangle(10, 5).
def area_rectangle(length,breadth):
    print(length*breadth)
area_rectangle(10,5)
# 🔹 Section 2: Keyword Arguments
# Modify greet(name) to accept a keyword argument. Call it as greet(name="Bob").
def greet(name):
    return name
print(greet(name="Bob"))
# Write a function introduce(name, age) that prints "My name is <name> and I am <age> years old." Call it using keyword arguments.
def introduce(name,age):
    print(f"My name is {name} and I am{age} year old")
introduce(age=18,name="Sunitha")



# Create a function calculate_price(item, price) and call it with keyword arguments.
def calculate_price(item,price):
    return item,price
print(calculate_price(item="Box",price=200))
# Write a function student_info(name, grade) and call it as student_info(grade="A", name="John").
def student_info(name,grade):
    return(grade,name)
student_info(grade="A",name="John")
# Define book_details(title, author) and call it using keyword arguments.
def book_details(title, author):
    return title,author
print(book_details(title="XX",author="bbbbb"))
# 🔹 Section 3: Default Arguments
# Write a function greet(name="Guest") that prints "Hello, <name>!". Call it without passing a name.
def greet(name="Guest"):
    print("Hello",name)
greet()
# Create a function discount(price, percent=10) that applies a discount. Call it with and without the percent.
def discount(price,percent=10):
    print(price-(price*percent/100))
discount(100)
discount(100,20)
# Define welcome_message(message="Welcome to Python!"). Call it without arguments.
def welcome_message(message="Welcome to python!"):
    return messagex
print(welcome_message())

# Write a function circle_area(radius, pi=3.14) that calculates area. Call it with only radius.
def circle_area(radius,pi=3.14):
    area=(pi*radius*radius)
    return area
print(circle_area(10))

# Create print_date(day, month="March", year=2026) and call it with just day.
def print_day(day,month="March",year=2026):
    return day,month,year
print(print_day(5))


#  Section 4: Mixing Positional & Keyword Arguments
# Write order_food(item, quantity=1) and call it with order_food("Pizza").
def order_food(item,quantity=1):
    return item,quantity
print(order_food("Pizza"))
# Create travel(destination, days=7) and call it with travel("Paris", days=10).
def travel(destination,days=7):
    return destination,days
print(travel("Paris",days=10))
# Define movie_ticket(movie, price=200, seat="Regular"). Call it with positional and keyword arguments.
def movie_ticket(movie, price=200, seat="Regular"):
    return movie,price,seat
print(movie_ticket("Hit3",100,"Regular"))
print(movie_ticket(movie="Darling",seat="Regular",price=150))
# Write exam_score(student, subject="Math", score=100) and call it with mixed arguments.
def exam_score(student, subject="Math", score=100):
    return student,subject,score
print(exam_score(student="Sunitha"))
print(exam_score("sunitha"))
print(exam_score("Sunitha",subject="Science",score=100))
# Create car_rental(car, days=5, insurance=True) and call it with both positional and keyword arguments.
def car_rental(car,days=5, insurance=True):
    return car,days,insurance
print(car_rental("BMW"))
print(car_rental(car="THAR",insurance=True,days=10))
# 🔹 Section 5: Using *args
# Write a function sum_all(*args) that returns the sum of all numbers passed.
def sum_all(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum_all(1,2,3,4))

# Create print_names(*args) that prints all names given.
def print_names(*args):
    for i in args:
        print(i)
print_names("Sunitha","Suni","sun")
# Define multiply_all(*args) that multiplies all numbers.
def multiply_all(*args):
    result=1
    for i in args:
        result*=i
    return result
print(multiply_all(1,2,3))
# Write max_number(*args) that returns the largest number.
def max_number(*args):
    large=args[0]
    for i in args:
        if i>large:
            large=i
    return large
print(max_number(1,2,3,4))
# Create average(*args) that calculates the average of numbers.
def average(*args):
    sum=0
    for i in args:
        sum+=i
    # print("sum is :",sum)
    # print("Length is :",len(args))
        avg=sum/len(args)
    return avg
print(average(1,2,3,4))
# 🔹 Section 6: Using **kwargs
# Write a function print_info(**kwargs) that prints all key-value pairs.
def print_info(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j)
print_info(name="sunitha",marks=90,city="Nandyal")

# Create student_profile(**kwargs) that prints student details.
def student_profile(**kwargs):
    for i ,j in kwargs.items():
        print(i,":",j)
student_profile(name="Angel",age=21,Marks=80,percet=80)

# Define car_details(**kwargs) that prints car attributes.
def car_details(**kwargs):
    for i , j in kwargs.items():
        print(i,":",j)
car_details(car="BMW",insurance=True,days=10)
# Write employee_data(**kwargs) that prints employee info.
def employee_data(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j)
employee_data(employee_name="SunithaDasari",dep="IT",age=21,employeeID=101)
# Create settings(**kwargs) that prints configuration settings.
def settings(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j)
settings(theme="Dark",language="English",volume=60)
# 🔹 Section 7: Combining *args and **kwargs
# Write mixed_function(*args, **kwargs) that prints both.
def mixed_func(*args,**kwargs):
    for i in args:
        print(i)
    for i, j in kwargs.items():
        print(i,":",j)
mixed_func(1,2,3,4)
mixed_func(name="Sunitha",age=21)
# Create register_user(*args, **kwargs) that prints positional and keyword arguments.
def register(*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,":",j)
register("sunitha",21,dep="IT",ID=101)
# Define shopping_cart(*args, **kwargs) that prints items and details.
def shopping_cart(*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,":",j)
shopping_cart("kurta","box","jeans",kurta=500,box=100,jeans=800)

# Write event_details(*args, **kwargs) that prints event info.
def event_details(*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,":",j)
event_details("Marraige","25th",date="24/6/2025",Place="Nandyal")

# Create log_data(*args, **kwargs) that prints logs
def log_data(*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,":",j)
log_data("username","Passwod",username="Sunitha.Dasari",time="9:00AM")

# Section 8: Practice Challenges
# Write a function calculate_total(price, quantity=1, tax=5) that returns total cost.
def calculate_total(price, quantity=1, tax=5):
    print(price*quantity)
    print(((price*quantity)*tax)/100)
calculate_total(100,2,5)

# Create greet_people(*args, greeting="Hello") that greets multiple people.
def greet_people(*args,greeting="Hello"):
    for i in args:
        print(i,greeting)
greet_people("Sunitha","Angel","Grace")
# Define student_report(name, *args, **kwargs) that prints name, subjects, and extra info.
def student_report(name,*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,j)
student_report("sunitha",101,21,subjects="Maths",marks=75,branch="Data Science")
# Write recipe(ingredient1, ingredient2, *args, **kwargs) that prints recipe details.
def recipe(ingredients1,ingredients2,*args,**kwargs):
    for i in args:
        print(i)
    for i ,j in kwargs.items():
        print(i,j)
recipe("Sugar","Tea powder","Milk","cup",Prepare="Sugar+Tea powder+Milk")
# Create bank_account(name, balance=0, **kwargs) that prints account info.
def bank_account(name,balance=0,**kwargs):
    print(name,balance)
    for i,j in kwargs.items():
        print(i,j)
bank_account("sunitha",10000,Bankname="SBI",savings=10000)
# 🔹 Section 9: Real-Life Scenarios
# Write flight_booking(destination, *args, **kwargs) that prints booking details.
def filght_booking(destination,*args,**kwargs):
    print(destination)
    for i in args:
        print(i)
    for i ,j in kwargs.items():
        print(i,j)
filght_booking("Paris","Extra Baggage", "Window Seat",name="Sunitha",age=21,travel_class="Business",date="2026-06-26",
    passport="X1234567")
# Create hotel_reservation(name, nights=1, **kwargs) that prints reservation info.
def hotel_reservation(name,nights=1,**kwargs):
    print(name,nights)
    for i,j in kwargs.items():
        print(i,j)
hotel_reservation("Sunitha",nights=2,cost=400,room_type="Deluxe",check_in="2026-06-10",check_out="2026-06-13",
    guests=2)

# Define order_summary(item, quantity=1, *args, **kwargs) that prints order details.
def order_summary(item,quantity=1,*args,**kwargs):
    print(item,quantity)
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,j)
order_summary("Sunitha","Pizza", "Burger", "Coke",order_id=101,payment="UPI",address="Nandyal",delivery_time="30 mins",
    total=450)

# Write game_score(player, *args, **kwargs) that prints scores.
def game_score(player,*args,**kwargs):
    print(player)
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,j)
game_score("Sunitha",50, 30, 20,game="Cricket",level="Intermediate",bonus=15,time_played="2 hours")
# Create conference_registration(name, *args, **kwargs) that prints registration details.
def conference_registration(name,*args,**kwargs):
    print(name)
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,j)
conference_registration( "SunithaDasari","AI Workshop", "Data Science Talk",reg_id=2026,organization="TechWorld",
    ticket_type="VIP",date="2026-07-15",venue="Hyderabad Convention Center")
# 🔹 Section 10: Advanced Practice
# Write calculator(operation, *args) that performs sum, multiply, etc.
def calculator(operation,*args):
    if operation=="sum":
        result=0
        for num in args:
            result+=num
        return  result
    elif operation=="sub":
        result=args[0]
        for num in args[1:]:
            result-=num
        return result
    elif operation=="mul":
        result=1
        for num in args:
            result*=num
        return result
    elif operation=="div":
        result=args[0]
        for num in args[1:]:
            result/=num
        return result
    else:
        print("Exit")
print(calculator("sum",1,2,3,4))
print(calculator("sub",1,2,3,4))
print(calculator("mul",1,2,3,4))
print(calculator("div",1,2,3,4))
# Create profile(name, age, *args, **kwargs) that prints full profile.
def profile(name,age,*args,**kwargs):
    print(name)
    print(age)
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,j)
profile("sunitha",21,"python","sql","AWS","walking","dancing",address="Nandyal,AP",eamil="sunitha.dasari@gmail.com")
# Define task_manager(task, priority="Medium", *args, **kwargs) that prints task details.
def task_manager(task,priority="Medium",*args,**kwargs):
    print(task)
    print(priority)
    for i in args:
        print(i)
    for i, j in kwargs.items():
        print(i,j)
task_manager("Assignment","inprogress","in review","todo","done",assignmentname="AI chatbot",deadline="21/5/26",status="progress")
# Write music_playlist(*args, **kwargs) that prints songs and playlist info.
def music_playlist(*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,j)
music_playlist( "Chill Vibes","Shape of You", "Believer", "Perfect",creator="Alice",genre="Pop",total_songs=3,duration="12 mins",
    platform="Spotify")
# Create smart_home(device, *args, **kwargs) that prints device settings.
def smart_home(device,*args,**kwargs):
    print(device)
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(i,j)
smart_home("Smart Light", "Smart TV", "Security Camera",location="Hyderabad",wifi_status="Connected",temperature="24C",
    security_mode="ON",voice_assistant="Alexa")
