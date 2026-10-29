# infi

age = 20

#    20 >= 18 ? T 

# update value 

while age >= 18: # 17 >= 18 ? F
    print(age) # 20 19 18
    age -= 1  # age = age - 1        20-1 = 19  18  17


print("outside while loop")

#   !=  Not equal
# 10 == 10 = True
# 10 != 10
a = 10
b = 10

print(a == b) # T
print(a != b) # F



pwd = ""

while pwd == "mohan":  # "mohan" != "mohan"  => F
    pwd = input("Enter the password : ")

print("Access Granted!!")