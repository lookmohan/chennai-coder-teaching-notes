set1 = {1,2,3,4,2,1,3,5,6} # set # unique....
set2 = {"a","b","c","d","e"}

print(set1)
print(set2)

fruits = {"apple", "banana", "cherry", "apple"} 
print(fruits)                


list1 = []
tuple1 = ()
set1 = set()
dict1 = {}

print(type(list1))
print(type(tuple1))
print(type(set1))
print(type(dict1))

colors = {"red", "green"}
colors.add("blue")             # add a single item -> {'red', 'green', 'blue'}
colors.update(["yellow", "pink"])  # add multiple items at once
colors.remove("red")           # remove an item (error if not found)
colors.discard("r")  
print(colors)      # remove if present, NO error if missing
print(len(colors))                # count of items
print("blue" in colors)  
print(colors) 


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)             # using the | operator
print(a.union(b))         

print(a & b)                  # using the & operator
print(a.intersection(b))       


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)                
print(a.difference(b))  
print(b - a)     

print(a ^ b)                        
print(a.symmetric_difference(b))     

