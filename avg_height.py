"""You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146
The average height can be calculated by adding all the heights together and dividing by the total number of heights."""

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#Write your code below this row 
total_heights = 0
for height in student_heights:
    total_heights = total_heights + height
#print(total_heights)
  
number_of_students = 0
for student in student_heights:
    number_of_students += 1
#print(number_of_students)

avg_of_heights = total_heights / number_of_students
print(round(avg_of_heights))

    


