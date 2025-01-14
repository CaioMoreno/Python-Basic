# tee ratkaisu tänne
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam Points: ")
course_file= input('Course information: ')

students = {}
exercises = {}
exam = {}
course = []

# Read student information
with open(student_file) as file:
    for line in file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2]}"

# Read exercise information and calculate totals
with open(exercise_file) as file:
    for line in file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        exercises[parts[0]] = sum(int(x) for x in parts[1:])

with open(exam_file) as file:
    for line in file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue
        exam[parts[0]]=sum(int(x) for x in parts[1:])


with open(course_file) as file:
    for line in file:
        if 'name: ' in line:
            n_course = line.strip().split('name:')[1].strip()  
        elif 'study credits:' in line:
            c_course = line.strip().split('study credits:')[1].strip()
    course.append(f'{n_course}, {c_course} credits\n======================================\n')


info=f'{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade"}\n'

with open('results.txt', 'w') as txt_file:
    for item in course:
        txt_file.write(f"{item}")
    txt_file.write(f"{info}")
    for student_id, name in students.items():
        total_exercises = exercises[student_id]
        total_exercises=int(total_exercises/4)
        total_points=total_exercises+exam[student_id]
        if total_points<=14:
            grade=0
        elif total_points<=17:
            grade=1
        elif total_points<=20:
            grade=2
        elif total_points<=23:
            grade=3
        elif total_points<=27:
            grade=4
        elif total_points>=28:
            grade=5
        txt_file.write(f"{name:30}{exercises[student_id]:<10}{total_exercises:<10}{exam[student_id]:<10}{total_points:<10}{grade:<10}\n")

with open('results.csv', 'w') as csv_file:
    for student_id, name in students.items():
        total_exercises = exercises[student_id]
        total_exercises=int(total_exercises/4)
        total_points=total_exercises+exam[student_id]
        if total_points<=14:
            grade=0
        elif total_points<=17:
            grade=1
        elif total_points<=20:
            grade=2
        elif total_points<=23:
            grade=3
        elif total_points<=27:
            grade=4
        elif total_points>=28:
            grade=5
        csv_file.write(f"{student_id};{name};{grade}\n")


print('Results written to files results.txt and results.csv')