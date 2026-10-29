class Hi:
    def __init__(self,name,age,dept):  # constructor   .....   blueprint
        self.name = name  #  h.name = "mohan"
        self.age = age  # h.age = 23   
        self.dept = dept # h2.dept = "Mech"

    def disp(self):
        print("Name :",self.name,"Age : ",self.age,"Dept : ",self.dept)

h = Hi("mohan",23,"It") # 
h1 = Hi("raj",32,"ECE")
h2 = Hi("Manu",21,"Mech")
h3 = Hi("Karthi",20,"It")

h.disp()
h1.disp()
h2.disp()
h3.disp()



