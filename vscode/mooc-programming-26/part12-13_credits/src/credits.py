from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(courses: list):
    return reduce(lambda total_credits, course: total_credits + course.credits, courses, 0)

def sum_of_passed_credits(courses: list):
    passed_courses = filter(lambda course: course.grade >= 1, courses)
    return reduce(lambda total_credits, course: total_credits + course.credits, passed_courses, 0)

def average(courses: list):
    passed_courses = list(filter(lambda course: course.grade >= 1, courses))
    average_grade = reduce(lambda total_grade, course: total_grade + course.grade, passed_courses, 0)/len(passed_courses)
    return average_grade

