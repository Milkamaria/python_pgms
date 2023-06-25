#SET PROGRAMS:
#Find the size of a Set in Python
my_set = {1, 2, 3, 4, 5}
print(len(my_set))

#Iterate over a set in Python
set1 = {1, 2, 3, 4, 5}
for item in set1:
    print(item)
    
#Python – Maximum and Minimum in a Set
set2 = {12, 2, 36, 49, 5}
print(max(set2))
print(min(set2))

#Python – Remove items from Set
set3 = {1,334,622,3}
print(set3.pop())

#Python – Check if two lists have at-least one element common
li1 = [1,2,3,4,5]
li2 = [4,5,6,7,8]

set1 = set(li1)
set2 = set(li2)
ce = set1 & set2
if ce:
    print ("The list have at least one common element")
else:
    print ("The list do not have any common element")

#Python program to find common elements in three lists using sets
li3 = [1,2,3,4,5]
li4 = [4,5,6,7]
li5 = [5,6,7,8,9]

set3 = set(li3)
set4 = set(li4)
set5 = set(li5)

c = set3.intersection(set4, set5)
print("Common elements: ", c)

#Python – Find missing and additional values in two lists
# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

missing_list1 = [] # Find missing values in list1
for item in list1:
    if item not in list2:
        missing_list1.append(item)

missing_list2 = []  # Find missing values in list2
for item in list2:
    if item not in list1:
        missing_list2.append(item)

additional_list1 = []  # Find additional values in list1
for item in list1:
    if item not in list2:
        additional_list1.append(item)

additional_list2 = []  # Find additional values in list2
for item in list2:
    if item not in list1:
        additional_list2.append(item)

print("Missing values in list1:", missing_list1)
print("Missing values in list2:", missing_list2)
print("Additional values in list1:", additional_list1)
print("Additional values in list2:", additional_list2)

#Python program to find the difference between two lists
list3 = [1, 2, 3, 4, 5]
list4 = [3, 4, 5, 6, 7]
diff = [x for x in list3 if x not in list4]
print("The difference between the two lists is:", diff)

#Python Set difference to find lost element from a duplicated array
arr = [1, 2, 3, 4, 5, 5, 6, 7, 8]
original_array = [1, 2, 3, 4, 5, 6, 7, 8]
lost_element = list(set(original_array) - set(arr))
print("Lost element:", lost_element[0])

#Python program to count number of vowels using sets in given string
string = input("Enter a string: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0
for char in string:
    if char.lower() in vowels:
        count += 1
print("Number of vowels:", count)

#Concatenated string with uncommon characters in Python
string1 = "abcdef"
string2 = "defxyz"
result = ""
for char in string1:
    if char not in string2:
        result += char
for char in string2:
    if char not in string1:
        result += char
print(result)

#Python – Program to accept the strings which contains all vowels
vowels = ['a', 'e', 'i', 'o', 'u']
accepted_strings = []
while True:
    string = input("Enter a string (or 'q' to quit): ")
    if string.lower() == 'q':
        break
    if all(vowel in string.lower() for vowel in vowels):
        accepted_strings.append(string)
print("Accepted strings:")
for string in accepted_strings:
    print(string)

#Python – Check if a given string is binary string or not


#Python set to check if string is pangram
alphabet = "abcdefghijklmnopqrstuvwxyz"
sentence = "The quick brown fox jumps over the lazy dog"
is_pangram = all(letter in sentence.lower() for letter in alphabet)
print(is_pangram)

#Python Set – Pairs of complete strings in two sets
set1 = {"apple", "banana", "orange"}
set2 = {"banana", "kiwi", "orange"}
pairs = []
for string1 in set1:
    for string2 in set2:
        if string1 == string2:
            pairs.append((string1, string2))
for pair in pairs:
    print(pair)

#Python program to check whether a given string is Heterogram or not
string = input("Enter a string: ").lower()
is_heterogram = True
for char in string:
    if char.isalpha() and string.count(char) > 1:
        is_heterogram = False
        break
if is_heterogram:
    print("The given string is a heterogram.")
else:
    print("The given string is not a heterogram.")


#Python program to convert Set into Tuple and Tuple into Set
set_data = {1, 2, 3, 4, 5} 
tuple_data = ()
for item in set_data:
    tuple_data += (item,)

print("Set:", set_data)
print("Tuple:", tuple_data)


tuple_data = (1, 2, 3, 4, 5)  
set_data = {item for item in tuple_data}
print("Tuple:", tuple_data)
print("Set:", set_data)

#Python program to convert set into a list
my_set = {1, 2, 3, 4, 5}
my_list = []
for element in my_set:
    my_list.append(element)
print(my_list)

#Python program to convert Set to String
my_set = {1, 2, 3, 4, 5}
set_string = "{" + ", ".join(str(item) for item in my_set) + "}"
print(set_string)

#Python program to convert String to Set
string = "Hello, World!"
output_set = set()
for char in string:
    output_set.add(char)
print(output_set)

#Python – Convert a set into dictionary
my_set = {'apple', 'banana', 'cherry'}
my_dict = {}
for item in my_set:
    my_dict[item] = None
# Print the dictionary
print(my_dict)

