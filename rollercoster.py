print("Welcome to the Rollercoaster")
height = int(input("Hey Babe What is your height"))

if height>=120:
    print("Go ahead you can ride on Rollercoaster")
    age=int(input("What is your age"))
    if age<12:
        bill=5
        print("Childrens Teckits are $5")
    elif age<=18:
        bill=7
        print("Youth teckits are $7")
    else :
        bill=12
        print("Adult teckits are $12")
want_photo = input("Do you want to take your photo ? Y or N")
if want_photo =="Y":
    bill=bill+3
else:
    print("Sorry you have to grow taller")

