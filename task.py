
n=6
for i in range(n):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("---------------")
n=6
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    print()
print("_____________")
n=6
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
print("_____________________")
n=6
for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()
print("---------------------")
n=6
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
print("---------------------------")
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1))

    


