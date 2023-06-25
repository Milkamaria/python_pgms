student={"name":"Milka",
         "age":24,
         "mark1":72,
         "mark2":65}
student["name"]
student.get("name")
student.keys()
student.values()


student["name"]="Manu"
student["phone"]=9857463210
student.update({"name":"Nikhil"})
student.update({"Address":"Ernakulam"})


student.pop("name")
student.popitems()
del student["name"]
del student
student.clear()
candidate=student.copy()
candidate=dict(student)
