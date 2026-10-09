'''
syntax :

if condition:
    #statement

else:
    #statement
'''
age = 12

if age >=18:   # 12 >= 18  = False
    print("Eligible to vote")

else:
    print("Not Eligible to Vote..")

print(".......................")

number = 10
 
if number % 2 == 0:  # 10 % 2 == 0    0 == 0 = T
    print(number, "is Even")
else:
    print(number, "is Odd")        

print("Elif ..")

marks = 82
 
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")           
elif marks >= 60:
    print("Grade C")
else:
    print("Needs improvement")


print("after if statement..!!")



age = 25
has_ticket = True

#    25 >= 18 and True => T and T = T
if age >= 18 and has_ticket:
    print("Welcome in!")
#  25 < 5 or 25 > 60
if age < 5 or age > 60:
    print("Free entry")
 
if not has_ticket:
    print("Please buy a ticket first")
