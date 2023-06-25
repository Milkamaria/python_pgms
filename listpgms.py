#LIST PROGRAMS:

#Python program to interchange first and last elements in a list
l=[1,3,2,5,4]
a=len(l)
temp=l[0]
l[0]=l[a-1]
l[a-1]=temp
print("After interchanging:",l)

#Python program to swap two elements in a list
l1=[1, 2, 3, 4, 5]
l1[0],l1[1]=l1[1],l1[0]
print("After swapping:",l1)

#Python – Swap elements in String list
li=['Ekm','ktm','tsr','Pkd']
li[0],li[2]=li[2],li[0]
print("After swapping:",li)

#Python | Ways to find length of list
l3=[1, 2, 3, 4, 5]
length=len(l3)
print("Length is:", length)

#Maximum of two numbers in Python
a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
m=max(a,b)
print("Maximum is:",m)

#Minimum of two numbers in Python
num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
mi=min(num1,num2)
print("Minimum is:",mi)

#Python | Ways to check if element exists in list
my_list=[1,2,3,4,5]
i=4
if i in my_list:
    print("Element exists")
else: 
    print("Element doesn't exist")

#Different ways to clear a list in Python
my_list=[1,2,3,4,5]
my_list.clear()
print(my_list)

#Python | Reversing a List
my_list=[1, 2, 3, 4, 5]
rl = my_list[::-1]
print(rl)

#Python | Cloning or Copying a list
lis=[1, 2, 3, 4, 5]
cl_lis=lis[:]
print("Cloned list is: ", cl_lis)

#Python | Count occurrences of an element in a list
li1=[1,4,2,7,2,1,3,2,2,4,3,1,2,2]
e=2
o=li1.count(e)
print("Number of occurences:", o)

#Python Program to find sum and average of List in Python
l=[1,2,3,4,5]
c=0
for i in l:
    c+=i
average=c/len(l)
print("Sum is: ", c)
print("Average is: ",average)

#Python | Sum of number digits in List
lis1=[222,111,221]
s=0
for n in lis1:
    while n>0:
        s+=n%10
        n//=10
print("Sum of digits:",s)

#Python | Multiply all numbers in the list
lis2=[1,2,3]
r=1
for n in lis2:
    r*=n
print("After multiplying all numbers: ",r)

#Python program to find smallest number in a list
lis3=[12,20,50,1]
sm=lis3[0]
for n in lis3[1:]:
    if n<sm:
        sm=n
print("The smallest number is:", sm)


#Python program to find largest number in a list
lis4=[12,20,50,1]
ln=lis4[0]
for n in lis4[1:]:
    if n>ln:
        ln=n
print("The largest number is:", ln)

#Python program to find second largest number in a list
lis5=[16,22,12,9,90]
lis5.sort()
print(lis5[-2])

#Python program to print even numbers in a list
nn=[1,2,3,4,6]
for n in nn:
    if n%2==0:
        print("Even numbers :", n)

#Python program to print odd numbers in a List
nn1=[1,2,3,4,5,6]
for n in nn1:
    if n%2!=0:
        print("Odd numbers :", n)

#Python program to print all even numbers in a range
start=int(input("Enter the starting number: "))
end=int(input("Enter the ending number: "))
for n in range(start, end+1):
    if n%2==0:
        print("Even numbers :", n)

#Python program to print all odd numbers in a range
startt=int(input("Enter the starting number: "))
endd=int(input("Enter the ending number: "))
for n in range(startt, endd+1):
    if n%2!=0:
        print("Even numbers :", n)

#Python program to count Even and Odd numbers in a List
nw=[1,2,3,4,5,6]
ec=0
oc=0
for n in nw:
    if n%2==0:
        ec+=1
    else:
        oc+=1
print("Even numbers:", ec)
print("Odd numbers:", oc)

#Python program to print positive numbers in a list
w=[1,-1,2,-2,3,-3,4,-4,5,6]
for n in w:
    if n>0:
        print("Positive numbers:", n)

#Python program to print negative numbers in a list
w=[1,-1,2,-2,3,-3,4,-4,5,6]
for n in w:
    if n<0:
        print("Negative numbers: ", n)

#Python program to print all positive numbers in a range
st=int(input("Enter the starting number: "))
en=int(input("Enter the ending number: "))
for n in range(st, en+1):
    if n>0:
        print("Positive numbers :", n)

#Python program to print all negative numbers in a range
sta = int(input("Enter the starting number: "))
enn = int(input("Enter the ending number: "))
for n in range(sta, enn+1):
    if n < 0:
        print("Negative numbers :", n)

#Python program to count positive and negative numbers in a list
num = [2, -5, 10, -3, 0, 8, -1, -7, 4, 6]
pc = 0
nc = 0
for n in num:
    if n > 0:
        pc+= 1
    elif n < 0:
        nc+= 1
print("Positive numbers count :", pc)
print("Negative numbers count :", nc)

#Remove multiple elements from a list in Python
Li = [1,2,3,4,5,6]
print("Before removing the elements: ", Li)
for i in Li:
    Li.remove(i)
print("After removing the elements: ",Li)

#Python | Remove empty tuples from a list
Li1=[(1,2,3),(),(1,3,2,4),(),(),(99,0)]
Li1= [t for t in Li1 if t]
print(Li1)

#Python | Program to print duplicates from a list of integers
nu= [1, 2, 3, 4, 5, 3, 6, 7, 2, 7]
print("Duplicate numbers:")
for n in nu:
    if nu.count(n)>1:
        print(n)