#function pgm to count vowels 

"""li = ['a', 'b', 'c', 'd', 'e']
def sum(li):
    vo = ['a', 'e', 'i', 'o', 'u']
    c = 0
    for i in li:
        if i in vo:
            c +=1
    return c
print("The count of vowels is : ", sum(li))"""


#function pgms to palindrome 

"""n = int(input("Enter the number : "))

def palindrome(n):
    s = str(n)
    if s == s [::-1]:
        print("palindrome")
    else:
        print("not palindrome")
    return n
print(palindrome(n))"""


#sum of digit 

n = int(input("Enter the number : "))

def sum(n):
    s = 0
    str1 = str(n)
    for i in str1:
        s = s + int(i)
    return s
print(sum(n))



