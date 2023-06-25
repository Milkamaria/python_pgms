#sum using arbitrary function    #test question 

"""def sum(*x):
    print(type(x))
    s = 0
    for i in x:
        s += i
    return s

n = int(input("Enter number: "))
b = int(input("Enter number: "))
print(sum(n,b))"""

#Area and circumference of circle

"""r = int(input("Enter radius: "))

def area(ra):
    return (3.14 * r ** 2)

def circumference(ra):
    return (2 * 3.14 * r)

print("area is", area(r))
print("circumference is", circumference(r))"""

#
"""def fun(x,y):
    if (x==0):
        return 0
    else:
        return fun (x-1,x+y)
    
print(fun(22,10))"""

#sum and average using arbitrary

"""def sum(*n):
    print(type(n))
    s = 0
    for i in n:
        s = s + i
    return s

def add(p):
    print(p*6)

def avg(s):
    print(s/5)

sm = sum(10,20,30)
add (sm)
avg (sm)"""

#simple interest 

"""def si(x,y,z):
    i= x*y*z/100
    return i

p = int(input("Enter the principle amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time period: "))

i = si(p,r,t)
print("simple interest is: ", i)"""


#Simple interest using keyword parameter passing

"""def simple(p,t,r=5):
    i = p*r*t/100
    return i
p = int(input("Enter the principle amount: "))
ra = int(input("Enter the rate of interest: "))
t = int(input("Enter the time period: "))
i1 = simple(p,t)    #reference parameter 
print("Interest is1: ", i1)   
i2 = simple(p,ra,t)
print("Interest is2: ", i2)"""


#armstrong

"""def armstrong(n):
    s = 0
    t = n
    while t > 0:
        d = t % 10
        s += d ** l
        t = t // 10

    if n == s:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")

n = int(input("Enter number: "))
str1 = str(n)
l = len(str1)
armstrong(n)"""

#binary to decimal

n = int(input("Enter the number:"))

"""def bin(a):
    str1 = str(n)
    rev = str1[::-1]
    s = 0

    for i in range(0,len(str1)):
        r = rev [i]
        s = s + int(r) * (2**i)
    return s

print(bin(n))"""

def dec(a):    
    if n >= 1:
        i = n // 2
        c = n % 2
    print
