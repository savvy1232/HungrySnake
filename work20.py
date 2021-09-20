operations = {
    "average" : lambda seq : sum(seq)/len(seq),
    "total" : sum,
    "top" : max
    }
students=[
     {"name":"Rolf","grades":(34,56,67,100)},
    {"name":"Joy","grades":(45,56,78,89)},
    {"name":"Sandy","grades":(14,56,34,67)},
]
for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"student:{name}")
    operation = input("Enter 'average','total' or 'top'")

    operation_function = operations[operation]
    print( operation_function(grades)) 