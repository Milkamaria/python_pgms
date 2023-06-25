#odd or even
num1=int(input("Enter a number:"))
if num1%2==0:
    print ("The number is even")
else:
    print ("The number is odd")

#vote eligibility
num1=int(input("Enter age:"))
if num1>=18:
    print ("You are eligible")
else:
    print ("You are not eligible")

#largest among 3 numbers
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1>num2 and num1>num3:
    print("First number is largest")
if num2>num3 and num2>num1:
    print("Second number is largest")
if num3>num1 and num3>num2:
    print("Third number is largest")

#grading
num1=int(input("Enter the first mark:"))
num2=int(input("Enter the second mark:"))
num3=int(input("Enter the third mark:"))
sum=num1+num2+num3
print("The total marks:",sum)
avg=sum/3
print("The average of the marks is:",avg)
if avg>=90:
    print("Grade is A")
elif avg>=80:
    print("Grade is B")
elif avg>=70:
    print("Grade is C")
elif avg>=60:
    print("Grade is D")
elif avg>=50:
    print("Grade is E")
else:
    print("Failed")

#leap year
year=int(input("Enter year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"is leap year")
else:
    print(year,"is not a leap year")
    

#div by 7 multiple by 5
num1=int(input("Enter the number:"))
if num1%7==0 and num1%5==0:
    print(num1,"is a multiple of 5 and divisible of 7")
else:
    print(num1,"is not a multiple of 5 and divisible of 7")


mylist=['apple', 34.7,'a']
print(type(mylist))
s=tuple(mylist)
print(s)
print(type(s))