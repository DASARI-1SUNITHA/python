#without thread
# class Hello:
#   def run(self):
#     for i in range(5):
#       print("hello")
# class hi:
#   def run(self):
#     for i in range(5):
#       print("hi")
# t1=Hello()
# t2=hi()
# t1.run()
# t2.run()
#implementation of thread usage by function based:
# from threading import Thread
# class Hello(Thread):
#   def run(self):
#     for i in range(5):
#       print("hello")
# class hi(Thread):
#   def run(self):
#     for i in range(5):
#       print("hi")
# t1=Hello()
# t2=hi()

# t1.start()
# t2.start()


##using sleep method:
# from time import sleep
# from threading import *
# class Hello(Thread):
#   def run(self):
#     for i in range(5):
#       print("hello")
#       sleep(1)

# class Hi(Thread):
#   def run(self):
#     for i in range(5):
#       print("hi")
#       sleep(1)
# t1=Hello()
# t2=Hi()

# t1.start()
# t2.start()


#using join method:
# from time import sleep
# from threading import *
# class Hello(Thread):
#   def run(self):
#     for i in range(5):
#       print("hello")
# class Hi(Thread):
#   def run(self):
#     for i in range(5):
#       print("hi")
# t1=Hello()
# t2=Hi()

# t1.start()
# t1.join()
# t2.start()
# t2.join()


#program using multiple threads without inheriting thread class
#here we didnot use class only used methods
# from threading import *

# def task1():
#     print("Task 1")

# def task2():
#     print("Task 2")

# def task3():
#     print("Task 3")

# t1 = Thread(target=task1)
# t2 = Thread(target=task2)
# t3 = Thread(target=task3)

# t1.start()
# t2.start()
# t3.start()
# using lock() method:
# from threading import *
# lock=Lock()
# balance=1000
# def withdraw(amount):
#     global balance
#     lock.acquire(timeout=5)
#     balance-=amount
#     lock.release()
#with lock:
#     pass
#if we mention lock by using with then we no need to explicitly mention acquire and release methods
# if we mention lock acquire then the programmer has to or its programmer responsilbility to release the lock that acquired.



#RLock() method:reentrant lock ,we us this when thread needs acquire same lock multiple times
# the thread already have the lock but sill wait for the lock  this condition is known as selfdead lock 
#reentrant lock tracks or counts how many time the lock has been applied to the same thread without unlocking it
# from threading import RLock
# lock=RLock()
# lock.acquire()
# lock.acquire()
# print("works")


#synchronization:
#example:
#without synchronization:
# from threading import Thread
# counter = 0
# def increment():
#     global counter

#     for i in range(100000):
#         counter += 1
# t1 = Thread(target=increment)
# t2 = Thread(target=increment)
# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(counter)
# #with synchronization using lock():
# from threading import Thread, Lock
# counter = 0
# lock = Lock()
# def increment():
#     global counter
#     for i in range(100000):
#         with lock:
#             counter += 1

# t1 = Thread(target=increment)
# t2 = Thread(target=increment)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print(counter)


#with synchronization using RLock():
# from threading import Thread,Lock , RLock
# counter = 0
# lock = RLock()
# def increment():
#     global counter
#     for i in range(100000):
#         with lock:
#             counter += 1

# t1 = Thread(target=increment)
# t2 = Thread(target=increment)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print(counter)


#with synchronization using semaphore():
from threading import Thread,Semaphore,Lock
counter = 0
lock = Semaphore(2)
def increment():
    global counter
    for i in range(100000):
        with lock:
            counter += 1

t1 = Thread(target=increment)
t2 = Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()

print(counter)