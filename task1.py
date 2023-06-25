bus={
    "Routeno":5,
    "Driver":"kiran",
    "Cleaner": "Manu",
    "points":["karamana", "PMG","pattom"]
}
print(bus["Driver"])
print (bus.get("cleaner"))
bus.keys()
#print(bus)
bus.values()
print(bus)
bus.items()
print(bus)
bus["color"]="Red"
print(bus)

bus ["Driver"]="Mohan" 
print(bus)
bus.pop("fare")
print(bus)
bus.popitem()
print(bus)
del bus["Fare"]
print(bus)
del bus
print(bus)
bus.clear()
print(bus)

for x in bus: 
    print(x)
for x in bus: 
    print (bus [x])