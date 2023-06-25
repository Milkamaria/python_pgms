unit = int(input("Enter the unit: "))
if unit <= 100:
    cost = unit * 0.5
    print("The electricity bill for", unit, "is", cost)

elif unit <= 150:
    cost=100 * 0.5 + (unit - 100) * 0.75
    print("The electricity bill for", unit, "is", cost)

elif unit <= 200:
    cost = 100 * 0.5 + 50 * 0.75 + (unit - 150) * 1
    print("The electricity bill for", unit, "is", cost)

elif unit >= 200:
    cost = 100 * 0.5 + 50 * 0.75 + 50 * 1 + (unit - 200) * 2
    print("The electricity bill for", unit, "is", cost)