class Car:  # class..
    color = "Black"
    brand = "BMW"
    def start(self):
        print("The car started..!!")
    
car = Car()  # object....
car2 =  Car() # object2
a = Car()

print(car.color)
print(a.brand)
car2.start()



# class is a blueprint, and an object is created from that blueprint.
# you can create many objects from the same class..