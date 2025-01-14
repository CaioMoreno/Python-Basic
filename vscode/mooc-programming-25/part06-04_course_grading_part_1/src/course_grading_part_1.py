# Prompt user for file names
students_file = input("Student information: ")
exercises_file = input("Exercises completed: ")

# Initialize dictionaries for student names and exercise totals
students = {}
exercises = {}

# Read the students file
with open(students_file, "r") as file:
    for line in file:
        parts = line.strip().split(';')
        if parts[0] == "id":  # Skip the header
            continue
        # Map student ID to their full name
        students[parts[0]] = f"{parts[1]} {parts[2]}"

# Read the exercises file
with open(exercises_file, "r") as file:
    for line in file:
        parts = line.strip().split(';')
        if parts[0] == "id":  # Skip the header
            continue
        # Calculate the total exercises for the student
        exercises[parts[0]] = sum(int(x) for x in parts[1:])

# Print the total exercises for each student
for student_id, name in students.items():
    total_exercises = exercises.get(student_id, 0)
    print(f"{name} {total_exercises}")
