mydict = {1:'apple', 2:34,3:[4,7,9]}
print(mydict)

mydict = dict({1:45,2:56,3:78})
print(mydict)
print(type(mydict))
#print(mydict[1])
#print(mydict.get(5))
mydict[2] = 65  #update
print(mydict)
mydict[4] = 90
print(mydict)

#remove 
print(mydict.pop(1))
print(mydict)
print(mydict.popitem())
print(mydict)

#clear all
print(mydict.clear())
print(mydict)

#delete 
del mydict
print(mydict)

marks = {}. fromkeys(['Eng','Sci','Mal'],99) #shows as dictionary
print(marks)
for x in marks.items(): #show as list
    print(x)

print(list(sorted(marks.keys())))

#convert two list in to a dictionary 
li1 = [1,2,3,4]
li2 = ['summer','autumn','fall']
result = dict(zip(li1,li2))
print(result)