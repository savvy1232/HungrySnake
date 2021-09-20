print("Welcome to the python Pizza Delivery")
size = input("what size do you Want? S,M,L!")
add_pepperoni = input("Do you want to add Pepperoni? Y or N!")
extra_cheese = input("Do you want to add extra_cheese? Y or N!")
bill=0
if size=="s":
    bill+=15
elif size=="m":
    bill+=20
else:
    bill+=25
if add_pepperoni=="Y":
    if size=='s':
        bill+=2
    else:
        bill+=3
  
if extra_cheese=="Y":
    bill+=1
print(f"Your final bill is {bill}")