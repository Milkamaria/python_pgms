#STRINGS PROGRAMS

#Python program to check whether the string is Symmetrical or Palindrome


#Reverse words in a given String in Python
w1=input("Enter the word:")
rev=w1[::-1]
print(rev)

#Ways to remove i’th character from string in Python
stri = "Hello, World!"
i = 7 
new_string = stri[:i] + stri[i+1:]
print(new_string)

#Find length of a string in python (4 ways)
w2=input("Enter the word:")
print(len(w2))

#Python – Avoid Spaces in string length
w3 = input("Enter the word:")
c = 0
for char in w3:
    if char != ' ':
        c += 1
print("Length without spaces:", c)

#Python program to print even length words in a string
w4 = input("Enter a string: ") 
words = w4.split()
for word in words:
    if len(word) % 2 == 0:
        print(word)

#Python – Uppercase Half String
s = "hello world"
length = len(s)
half_length = length // 2
upper_half = s[:half_length].upper()
lower_half = s[half_length:]
result = upper_half + lower_half
print(result)

#Python program to capitalize the first and last character of each word in a string
w5 = input("Enter a string: ")
w = w5.split()
for i in range(len(w)):
    word = w[i]
    capitalized_word = word[0].capitalize()
    if len(word) > 1:
        capitalized_word += word[-1].capitalize()
        capitalized_word += word[1:-1].lower()
    w[i] = capitalized_word
output_string = ' '.join(w)
print(output_string)

#Python program to check if a string has at least one letter and one number
w6 = input("Enter a string: ") 
print(w6.isalnum())

#Python | Program to accept the strings which contains all vowels
vowels = ['a', 'e', 'i', 'o', 'u']
string = input("Enter a string: ")
string = string.lower()
if all(vowel in string for vowel in vowels):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")

#Python | Count the Number of matching characters in a pair of string
string1 = "Hello"
string2 = "Hippo"
count = 0
for char1 in string1:
    for char2 in string2:
        if char1 == char2:
            count += 1
print("Number of matching characters:", count)

#Python program to count number of vowels using sets in given string
string = input("Enter a string: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0
for char in string:
    if char.lower() in vowels:
        count += 1
print("Number of vowels:", count)

#Python Program to remove all duplicates from a given string
str1 = input("Enter a string: ")
u = " "
for char in str1:
    if char not in u:
        u +=char
print("String without duplicates:", u)

#Python – Least Frequent Character in String
str2 = input("Enter a string: ")
cc = {}
for char in str2:
    if char in cc:
        cc[char] += 1
    else:
        cc[char] = 1


#Python | Maximum frequency character in String


#Python – Odd Frequency Characters


#Python – Specific Characters Frequency in String List


#Python | Frequency of numbers in String


#Python | Program to check if a string contains any special character
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?', '<', '>', '|', '\\']
st = input("Enter a string: ")
f = False
for char in st:
    if char in special_chars:
        f = True
        break
if f:
    print("The string contains special characters.")
else:
    print("The string does not contain any special characters.")


#Generating random strings until a given string is generated


#Find words which are greater than given length k
text = "This is a sample text to demonstrate the word filtering process."
k = 5
words = text.split()
long_words = []
for word in words:
    if len(word) > k:
        long_words.append(word)
for word in long_words:
    print(word)

#Python program for removing i-th character from a string
s = input("Enter a string: ")
i = int(input("Enter the index of the character to remove: "))
if i < 0 or i >= len(s):
    print("Invalid index!")
else:
    new_string = ""
    for index in range(len(s)):
        if index != i:
            new_string += s[index]
    print("Modified string:", new_string)

#Python program to split and join a string
s1 = "Hello, world! How are you?"
words = s1.split()
j = "-".join(words)
print("Original string:", s1)
print("Split words:", words)
print("Joined string:", j)


#Python | Check if a given string is binary string or not
st1 = input("Enter a string: ")
for char in string:
    if char != '0' and char != '1':
        print("The given string is not a binary string.")
        break
else:
    print("The given string is a binary string.")


#Python | Find all close matches of input string from a list
wo = ["apple", "banana", "cherry", "grape", "lemon", "orange", "peach"]
input_string = "lemonn"
t = 2
c = []
for word in wo:
    diff_count = sum(a != b for a, b in zip(word, input_string))
    if diff_count <= t:
        c.append(word)
print("Close matches:", c)

#Python program to find uncommon words from two Strings
st1 = "Hello world! This is string 1."
st2 = "Hello there! This is string 2."
wo1 = set(st1.split())
wo2 = set(st2.split())
uncommon_words = wo1.symmetric_difference(wo2)
for word in uncommon_words:
    print(word)


#Python | Swap commas and dots in a String
strr = "Hello, everyone. This is a random string."
swapped_string = ""
for char in strr:
    if char == ',':
        swapped_string += '.'
    elif char == '.':
        swapped_string += ','
    else:
        swapped_string += char
print(swapped_string)

#Python | Permutation of a given string using inbuilt function


#Python | Check for URL in a String

string = "This is a sample string with a URL: https://www.example.com"
if "http://" in string or "https://" in string:
    print("URL found in the string")
else:
    print("No URL found in the string")

#Execute a String of Code in Python
code_string = """
a = 5
b = 10
print(a + b)
"""
exec(code_string)