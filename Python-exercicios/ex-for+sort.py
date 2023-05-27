student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

scores = []
for score in student_scores:
    scores.append(score)

scores.sort(reverse=True)
print("The highest score in the class is",scores[0]) 
