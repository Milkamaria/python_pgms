nu=int(input("Enter num"))
if nu<0:
    print("Number should be greater than zero")
elif nu==1 or nu==0:
    print("Factorial=",1)
else:
    fact=1
    i=1
    while i<=nu:
        fact=fact*i
        i+=1
    print(fact)
