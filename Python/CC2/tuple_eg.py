list1 = [1,2,3,4] # mutable 

num = (1,2,3,4)   # immutable

print(type(list1))
print(type(num))
print(num[0])

student = ("Meera", 22, "Computer Science")
print(student[0])       # Meera
print(student[-1])      # Computer Science
print(student[0:2])     
print(len(student))

a = (1, 2, 2,2,3)
b = (4, 5)
print(a + b)         
print(b*3)
print(student.count(22))     
