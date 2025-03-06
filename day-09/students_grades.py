student_scores = {
    'Harry': 88,
    'Mary': 78,
    'John': 95,
    'Adam': 75,
    'Sue': 60,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91 and student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81 and student_scores[student] <= 90:
        student_grades[student] = "Exceeeds Expectations"
    elif student_scores[student] >= 71 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] <= 70:
        student_grades[student] = "Fail"
    
print(student_grades)
