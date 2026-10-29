for number in range(1, 11): # 7,8,9,10
    if number%2  != 0: # 3 == 3 ? T
        continue  # skip the cuurent iteration...
    print(number, end = " ") # 1 2 3 4 5 

"""
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60

"""
number = int(input("Enter a number: "))
 
print("Multiplication table of", number)
for i in range(1, 101):
    print(number,"x",i,"=", number*i)  # 3 * 1 = 3
