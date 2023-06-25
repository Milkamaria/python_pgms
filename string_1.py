#string programs
word="Hello world "
d="good morning"
print(word)
print(word *5)
print(word[2:7])
print(word[-7:-2])
print(word[2:7:2])
print(word+d)

#revrse a word
word=input("Enter the word:")
rev=word[::-1]
print(rev)


#string functions
word="python programming"

print(word.upper())
print(word.lower())
print(word.capitalize())
print(word.split())

s=word.replace('python','java')
print(s)

