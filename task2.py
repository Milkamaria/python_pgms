contactlist={}
n=int(input("Enter the number of contacts : "))
for i in range(1,n+1):
    name=input("Enter the contact name :") 
    phno=int(input("Enter the phone number :")) 
    contactlist[name]=phno 
print("Keys")
for x in contactlist.keys():
    print(x)
print("Values")
for x in contactlist.values():
    print(x)
print("Keys-value pairs")
for x,y in contactlist.items(): 
    print(x, "-",y)