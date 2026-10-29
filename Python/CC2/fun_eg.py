def greet(name, age = 33):   # default argument
    print("Name : ",name,"Age : ",age)

#      name = "mohan"   age = 23
greet("mohan",23)
#      name = 23  age = "mohan"
greet(23,"mohan")

greet(age = 23,name = "hari")  # keyword arguments

greet("karthick",43)