numberNames = {0: 'Zero',1: 'One', 2: 'Two',3: 'Three', 4: 'Four',5: 'Five',6: 'Six',7: 'Seven', 8: 'Eight',9: 'Nine'}
positionvalues = {0: 'Ones', 1: 'Tens', 2: 'Humdreds', 3: 'Thousands',4: 'Ten Thousands',5: 'Lakhs',6: 'Ten Lakhs', 
                7: 'Crore', 8: 'Ten crores'}
num=input("Enter any number")
result=""
l=len(num)-1
for ch in num:
    key = int(ch)
    value=numberNames[key]
    result=result + ' ' + value+' '+ positionvalues[1]
    l-=1
print("The number is : ", num)
print("The number Name is ", result)