first = "mohan 124@$%^"
last = "raj"
a = 10
b = 20

print(a + b) # 
print(first +"     gfhg "+ last) # merge   , concat
print("Name : " + first +"  "+ last)


# length....

print(len(first))
print(len(last))

print("H" in "Python")              
# \n : new line...
print("Hello fhfg  \n   World")  


print("He said \"Hi\"")

# 0 1 2 3 4 5
# P y t h o n

text = "Python"

print(text)
print(text[4])
print(text[0])
print(text[-2])

print(text[0:4])  
print(text[2:5])  
print(text[::-1])
print(text[::2])

# for var in sequence:

for i in text:  # P y t h o n
    print(i,end="   ")


print()
# string built-in functions..

name = " mohan is a    "
print(name.strip())

date = ["2025", "01", "15"]
print(date)
print("      rg".join(date))   



name = "Ravi"
age = 20
dept = "IT"
#print("Name:", name +","+"Age:", age +","+ "Dept :",dept)           

print(f"Name : {name} , Age : {age} , Dept : {dept}")




name = "madam"
#  "python" == "nohtyp"  F
if name == name[::-1]:
    print("Polindrome")
else:
    print("Not Polindrome")