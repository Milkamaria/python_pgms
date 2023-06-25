#area and perimeter rectangle 

"""l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

def area(l,b):
    ar = l * b
    print("Area :", ar)
area (l,b)

def perimeter(l,b):
    pe = 2 * (l + b)
    print("Perimeter is ", pe)
perimeter (l,b)"""

#sum of all numbers in a list

"""li = [1,2,3,4,5]

def sum(li):
    s = 0
    for i in li:
        s += i
    return s
print(sum(li))"""


#To accept string and count upper and lower string

s = input("Enter string: ")
l = 0
u = 0
def up(s):
    for i in s:
        if (i.islower()):
            l +=1
        else:
            u += 1

print(up(s))