# collections:
# list, tuple,set, dict
# array : multiple values but same datatype 
# list : ordered

list_eg = [1,2,3,4,5,6,7]
print(list_eg)
print(type(list_eg))

mixed_datatypes = [12,23,"mohan",True,1.2,43.9]
print(mixed_datatypes)



fruits = ["apple", "banana", "cherry", "mango"]
# accessing a values from a list
print(fruits[1])
print(fruits[1:3])

a = [1, 2, 3]
b = [4, 5]
print(a + b)        

print(len(b))

for i in fruits: #
    print(i)

# add : 1,append 2, insert

# append : end of the list
fruits = ["apple", "banana", "cherry", "mango"]

fruits.append("watermelon")
fruits.append("kiwi")
print(fruits)

# insert
fruits.insert(2,"green apple")
print(fruits)

# delete : 1, remove   2, pop

fruits.remove("green apple")
#fruits.remove("ki")
print(fruits)

popped = fruits.pop()  # delete and return  the deleted value
print(popped)
popped = fruits.pop(2)
print(popped)
print(fruits)