import math

student_heights = input("Input a list of student heights in cm ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

all_heights = 0
for height in student_heights:
    all_heights += height

all_students = 0
for student in student_heights:
    all_students += 1

total = all_heights / all_students
math.floor(total)
print("The average height of all_heights is {:.{}f}cm".format(total,2))
