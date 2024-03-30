WAND = 0
FNAME = 1
LNAME = 2
students = {
    "G1": ["Unicorn Cherry Wand", "Neville", "Longbottom" ],
    "S1": ["Elder Wand", "Tom", "Riddle"]
}

print(students["S1"][FNAME])

looking_for = "G1"
if looking_for in students:
    print(f"{looking_for} is a student")
else:
    print(f"{looking_for} is not a student")
for student_id in students:
    student = students[student_id]
    print(f"{student[FNAME]} {student[LNAME]} uses {student[WAND]}")