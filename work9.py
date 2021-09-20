print("Enter Marks")
marks=float(input())

if marks<25:
    print("Grade F")
elif marks>=25 and marks<=45:
    print("Grade E")
elif marks>=45 and marks<=50:
    print("Grade D")
elif marks>=50 and marks<=60:
    print("Grade C")
elif marks>=60 and marks<=80:
    print("Grade B")
elif marks>80 and marks<=100 :
        print("Grade Distinction")
else:
    print("School Can't Teach You Buddy")