#TUPLE PROGRAMS
#Python program to Find the size of a Tuple
t=("python",18,72,30,"dev")
print(len(t))

#Python – Maximum and Minimum K elements in Tuple
t1= (1,2,3,4,5,6,7)
s=list(t1)
s.sort()
print("The minimum value is :", s[0])
print("The maximum value is :", s[-1])

#Create a list of tuples from given list having number and its cube in each tuple
num=[1,2,3,4,5]
r=[]
for n in num:
    cube=n**3
    r.append((n,cube))
print(r)

#Python – Adding Tuple to List and vice – versa
Li= [1,2,3,4]
Tu= (5,6,7)
Li += list(Tu)
print(Li)
Tu += tuple(Li)
print(Tu)

#Python – Sum of tuple elements
tu2= (1,2,3,4,5)
s=0
for n in tu2:
    s+=n
print("sum is :", s)

#Python – Modulo of tuple elements  
                                          #doubt
tu3 = (1,2,3,4,5)
m=0
for n in tu3:
    m = n%2
print("Modulo is :", m)

#Python – Row-wise element Addition in Tuple Matrix
                                                 #doubt
m = ((1,2,3),(4,5,6),(7,8,9))
r = []
for r in m:
    r=0
    for i in r:
        r += i
r.append(r)
print(r)

#Python – Update each element in tuple list
tu4 = [(1, 2), (3, 4), (5, 6)]
for i in range (len(tu4)):
        tu4[i]= tu4[i][0]+ 1, tu4[i][1]+ 1
for it in tu4:
    print(it)

#Python – Multiply Adjacent elements 
tu5 = [1, 2, 3, 4, 5]
re = [tu5[i] * tu5[i+1] for i in range(len(tu5)-1)]
print(re)

#Python – Join Tuples if similar initial element


#Python – All pair combinations of 2 tuples


#Python – Remove Tuples of Length K                         
 #doubt
tu6 = [(1, 2), (3, 4), (5, 6), (7, 8, 9), (10, 11, 12)]
k = 2
result = []
for tup in lst:
    if len(tup) != k:
        result.append(tup)
print(result)

#Python – Remove Tuples from the List having every element as None


#Sort a list of tuples by second Item
my_list = [(3, 5), (1, 2), (6, 1), (4, 9), (2, 7)]
my_list.sort(key=lambda x: x[1])
#lambda function extracts the second item from each tuple (x[1])
for item in my_list:
    print(item)

#Python – Sort Tuples by Total digits
tu7 = [(15, 99, 123), (7, 81), (42, 1000, 5), (9876, 1234, 5678, 1)]
sorted_tuples = sorted(tu7, key=lambda t: sum(len(str(num)) for num in t))
for t in sorted_tuples:
    print(t)

#Python – Elements frequency in Tuple


#Python – Filter Range Length Tuples
tu9 = [(1, 5), (2, 10), (3, 8), (4, 3), (5, 6)]
filtered_tuples = [t for t in tu9 if t[1] - t[0] > 5]
for t in filtered_tuples:
    print(t)

#Python – Assign Frequency to Tuples
#Python – Records with Value at K index
#Python – Test if tuple is distinct