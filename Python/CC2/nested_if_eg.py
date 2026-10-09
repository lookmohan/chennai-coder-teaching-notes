age = int(input("Enter Your Age"))
has_id = "no"
 
if age >= 18:  # 15 >=18 
    if has_id == "yes":  #  no == yes => F
        print("Entry allowed.")
    else:
        print("Please bring your ID.")
else:
    print("Sorry, only 18 and above.")
