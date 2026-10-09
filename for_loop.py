'''
for var_name  in sequence:
    statement
range() : start,stop,step
stop value always : -1
'''
'''
i = 0
i = 1
i = 2
i = 3
i = 4
0 1 2 3 4
'''


for i in range(5): # 0 - 4
    print(i,end = " ")

print(".......")

for i in range(10,15): # 0 - 4
    print(i,end = " ")

print("............")

for i in range(1,10,3): # 1
    print(i,end = " ")  # 1 4 7 

# OUTPUT : 10 9 8 7 6 5 4 3 2 1
print("...............")
for i in range(10,6,-1): # 10 9 8 7 
    print(i,end=" ")
print()
print()
"""
step value : -1
stop value : +1
"""
# nested for loop..

for i in range(5): # 0 1 2 3 4
    for j in range(i): # 01234
        print("*",end= " ") # 0000   11111
    print()

print("...................................")
for i in range(5,0,-1): # 0 1 2 3 4
    for j in range(i): # 01234
        print("*",end= " ") # 0000   11111
    print()

