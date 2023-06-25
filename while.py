"""#multiplication table
num1=int(input("Enter number:"))
count=1
while (count<=10):
    mul=num1*count
    print(num1,"*",count,"=",mul)
    count+=1

#factorial
num1=int(input("Enter number:"))
if num1<0:
    print("The number must be greater than zero")
elif num1==0 or num1==1:
    print(" Factorial of 1 and 0 is 1 ")
else:
    fact=1
    i=1
    while(i<=num1):
        fact=i*fact
        i+=1
    print(fact)

#sum of list
li=[3,6,7,9,5]
i=0
s=0
while i<len(li):
    s=s+li[i]
    i+=1
print("Sum of list is:",s)
"""

#prime numbers
num=int(input("Enter number:"))
a=0
i=2
while i<=num/2:
    if num%i==0:
        f=1
        break
    i=i+1
if a==0:
    print("The number is a prime number")
else:
    print("The number is not a prime number")

"""#divisible by 7 and multiples of 5, between 1500 and 2700 (both included)
num=int(input("Enter number:"))
if num>=1500 and num<=2700:
    if num%7==0 and num%5==0:
        print(num,"is a multiple of 5 and divisible of 7")
    else:
        print(num,"is not a multiple of 5 and divisible of 7") 

else:
    print("The number should be between 1500 and 2700")

#prints all the numbers from 0 to 6 except 3 and 6
i=-1
while i<6:
    i=i+1
    if(i==3 or i==6):
        continue
    print(i)"""