a = [1,2,3,4,5]
print(a[5])

a = 10
b = 0
c = (a/b)
print(c)

a = ['Mango','apple','plum']
print(b)

#syntax error
a = 2
if a % 2 == 0
    print ("Even")

#type error
a = [1,2,3]
st = "hp"
c = a + st
print(c)

#factorial
num1=int(input("Enter number:"))
try:
    fact=1
    i=1
    while(i<=num1):
        fact=i*fact
        i+=1
    print(fact)
except:
    print("error")