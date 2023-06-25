#multiplication table
num1=int(input("Enter number:"))
count=1
while (count<=10):
    mul=num1*count
    print(num1,"*",count,"=",mul)
    count+=1

#fact
num1=int(input("Enter number:"))
if num1<0:
    print("The number must be greater than zero")
elif num1==0 or num1==1:
    print("Fact=",1)
else:
    fact=1
    i=1
    while(i<=num1):
        fact=i*fact
        i+=1
    print(fact)