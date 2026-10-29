

dict_eg = {
    "name" : "mohan",
    "age" : 23,
    "contact" : 34567809
}

# key always needs to be unique

student = {
    "name": "Ravi",
    "age": 20,
    "city": "Chennai",
    "score": 88.5
}

print(student)

print(type(student))
print(len(student))


# accessing..
print(student["name"])
print(student["score"])
print(student.get("dept"))
print(student.get("age"))

student["dept"] = "Mech"
student["state"] = "TamilNadu"
print(student)

student["name"] = "Mohan"
print(student)

del student["city"]
del student["state"]
print(student)

removed = student.pop("age")
print(removed)           # Output: 21
print(student)           

 
print(student.keys())    
print(student.values())
print(student.items())

for i,j in student.items():
    print(i," : ",j)

for i in student.values():
    print(i)

classroom = {
    "Ravi":  {"age": 20, "score": 88},
    "Priya": {"age": 19, "score": 95},
    "Arjun": {"age": 21, "score": 72},
}

print(classroom["Ravi"]["score"])


l = []
t = ()
s = set()
d = {}

print(type(l))
print(type(t))
print(type(s))
print(type(d))