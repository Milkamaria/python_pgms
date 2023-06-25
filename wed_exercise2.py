#Exercise 1 - Write a shutting down program
"""n = input ("Enter yes or no: ")
def shut_down(s):
    if s == 'yes':
        return "Shutting Down"
    elif s == 'no':
        return "Shutting Aborted"
    else:
        return "Sorry"
print(shut_down(n))"""


#Exercise 3 - Cube

def cube (number):
    return number ** 3

def by_three (number):
    if number % 3 == 0:
        return cube (number)
    else:
        return "false"
    
n = int (input ("Enter number: ") )
res = by_three (n)

if res:
    print ("Cube: ", res)
else:
    print ("The number is not divisible by 3")