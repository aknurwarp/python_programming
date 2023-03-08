student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        Grade = "Outstanding"
    
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        Grade = "Exceeds Expectation"
    #student_scores[scores] = grades
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        Grade = "Acceptable"
    #student_scores[scores] = grades
    else:
        Grade = "Fail"
    
    student_grades[key] = Grade

print(student_grades)