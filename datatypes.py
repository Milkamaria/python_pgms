#swap two numbers with 3rd variable
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("The values before swapping:",a,b)
temp=a
a=b
b=temp
print("The values after swapping:",a,b)

#swap two numbers without 3rd variable
a,b=1,2
print("The values before swapping:",a,b)
a,b=b,a
print("The values after swapping:",a,b)
