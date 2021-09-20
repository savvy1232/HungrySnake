def average (sequence):
    return sum(sequence)/len(sequence)

students =[
    {"name":"Rolf","grades":(34,56,67,100)},
    {"name":"Joy","grades":(45,56,78,89)},
    {"name":"Sandy","grades":(14,56,34,67)},
]
for student in students:
    print(average(student["grades"]))