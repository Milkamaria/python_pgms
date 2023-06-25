"""#1.python pgm to use isalnum method
word="software"
print(word.isalnum())

#2. convert a string to a lower
w2="Software Developer"
print(w2.lower())

#3. write a program to use capitalize method
w3="software developer"
print(w3.capitalize())

#4. remove white spaces from the begining of a string
w4=" software developer"
print(w4.strip())

#5. write a python pgm to use ends with the method
w5="softwre developer"
print(w5.endswith("developer"))

#6. pgm to check whether a certain character is present or not
w6="p" in "python"
print(w6)

#7. pgm to find length of string
w7="software"
print(len(w7))

#8. pgm to split the strings into substrings 
w8="softwre developer"
print(w8.split())

#9. pgm to use the case fold method
w9="SOFTwARE"
print(w9.casefold())

#10. write a pgm to replace a string with other
txt="Welcome to python"
print(txt[0])
s=txt.replace('python','java')
print(s)

#11. get the characters from index 2 to index 4
txt = "Welcome to python" 
print(txt[2:5])

#12. Return the string without any whitespace at the beginning of the end. txt = " Welcome to python " 
txtt=" Welcome to python "
print(txtt.strip())

#13. Using the type() function assign the type of the variable to answer_1, then print it. 
# #14. men_stepped_on_the_moon=12 answer_1= 
#print(answer_1) 

v= "answer_1"
print(type(v))


#15. str="It's always darkest before dawn." Replace the (.) with (!) 
str="It's always darkest before dawn."
s=str.replace('.','!')
print(s)

#16. Reassign str so that, all its characters are lowercase. 
str="EVERY Strike Brings Me Closer to the Next Home run."
print(str.lower())

#17. Make the string so that everything is properly and 
# the first letter is capital str=" there are no traffic JamS Along with The extra " 
str=" there are no traffic JamS Along with The extra " 
print(str.strip())
print(str.capitalize())

#18. Print the types of two given variables with the print function. 
#v_1="1" 
#v_2=1 
v_1="1" 
v_2=1 
print(type(v_1))
print(type(v_2))

#19. What is the length of the given string? str="1.975.000"
str="1.975.000"
print(len(str))

#20. Write a Python program to add an item to a tuple.
b=('apple', 34.7, 'a')
se=list(b)
se.append('wes')
print(se)
ab=tuple(se)
print(ab)

#23. Write a Python program to convert a tuple to a string.
t=('apple', 34.7, 'a')
s=list(t)
print(s)
s.append('aw')
print(s)
a=tuple(s)
print(a)

#24. Write a Python program to find repeated items in a tuple.
my_tuple=(1,2,3,2,4,1,5,1)
repeated_item=[]
for item in my_tuple:
    if my_tuple.count(item)>1 and item not in repeated_item:
        repeated_item.append(item)
print("Repeated Items:",repeated_item)

#25. Write a Python program to get a list, sorted in increasing order by the last element in each tuple 
#from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

"""s1={1,2,3,4}
print(s1)
print(dir(set))
print(set())"""

myset={'apple','orange'}
print(myset.add('mango'))
print(myset)
myset.update([1,'kiwi'])
print(myset)
myset.discard('apple')
print(myset)
myset.remove('kiwi')
print(myset)
myset.discard('banana')
print(myset)
myset.remove('banana')
print(myset)
