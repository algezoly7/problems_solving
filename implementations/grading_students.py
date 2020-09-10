#for more informations visit https://www.hackerrank.com/challenges/grading/problem
grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
def gradingStudents(grades):
    for i in range(0,grades_count):
        if(grades[i] < 38):
            print(grades[i])
        else:
            nextMultipleOf5 = 5 * ((grades[i] // 5) +1)
            differnce = nextMultipleOf5 - grades[i]
            if(differnce < 3):
                print(nextMultipleOf5)
            else:
                print(grades[i])
gradingStudents(grades)
