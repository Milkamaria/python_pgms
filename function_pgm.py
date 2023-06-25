#swap using function

def swap():
    a=20
    b=10
    a,b=b,a
    print(a,b)
swap()

#factorial using function

n = int(input("Enter the number: "))
def fact():
    if n < 0:
        print("The number should be greater than 0")
    elif n == 0 and n == 1:
        print("The factorial is 1")
    else:
        f = 1
        i = 1
        while (i <= n):
            f = i * f
            i += 1
        print(f)
fact()
    
