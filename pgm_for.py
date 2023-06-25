#program to print 1-50 using for loop
for i in range (1,51):
    print(i)

#break with 10
for i in range (1,51):
    if i==10:
        break
    print (i)

#
for i in 'python developer':
    if i=='t':
        continue
    print(i)


#count the number of even and odd numbers in a series of numbers
li=[1,2,3,4,5,6,7,8,9]
count=0
o=0
for i in li:
    if i%2==0:
        count+=1
        
    else:
        o+=1
        
print ("even numbers",count)
print ("odd numbers",o)

#
for i in range (1,51):
    if i%3==0 and i%5==0:
        print ("FizzBuzz")
    elif i%5==0:
        print ("Buzz")
    elif i%3==0:
        print ("Fizz")
    elif i%3!=0 and i%5!=0:
        print (i)
print ("loop end")

#maximum in list
list=[1,2,3,4,5]
print(max(list))

