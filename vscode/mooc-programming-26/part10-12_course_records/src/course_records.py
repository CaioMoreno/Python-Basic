# tee ratkaisusi tänne
class Info:
    def __init__(self):
        self.__grade = 0
        self.__credits = 0

    def add_course(self, grade: int, credits: int):
        if self.__grade<grade:
            self.__grade = grade
        self.__credits = credits

    def course(self):
        return self.__app

    def credits(self):
        return self.__credits
    
    def grade(self):
        return self.__grade


class Course:
    def __init__(self):
        self.__infocourse = {}

    def add_course(self, course: str, grade: int, credits: int):
        if course not in self.__infocourse:
            self.__infocourse[course] = Info()
        self.__infocourse[course].add_course(grade, credits)
    
    def get_course(self, course: str):
        if course not in self.__infocourse:
            print("no entry for this course")
            return

        print(f"{course} ({self.__infocourse[course].credits()} cr) grade {self.__infocourse[course].grade()}")

    def grade_dis(self):
        grade = {5: "", 4: "", 3: "", 2: "", 1: ""}
        
        for course in self.__infocourse:
            grade[self.__infocourse[course].grade()]+="x"
          
        for key, value in grade.items():
            print(f"{key}: {value}")

    def statistics(self):
        total_cred = 0
        total_grade = 0

        for course in self.__infocourse:
            total_cred += self.__infocourse[course].credits()
            total_grade += self.__infocourse[course].grade()

        print(f"{len(self.__infocourse)} completed courses, a total of {total_cred} credits")
        print(f"mean {round(total_grade/len(self.__infocourse),1)}")
        print(f"grade distribution")
        self.grade_dis()


class AppCourse:
    def __init__(self):
        self.__app = Course()
    
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__app.add_course(course, grade, credits)

    def get_course(self):
        course = input("course: ")
        self.__app.get_course(course)

    def statistics(self):
        self.__app.statistics()

    def execute(self):
        self.help()

        while True:
            print("")
            choice = int(input("command: "))
            if choice == 1:
                self.add_course()
            elif choice == 2:
                self.get_course()
            elif choice == 3:
                self.statistics()
            elif choice == 0:
                break


application=AppCourse()
application.execute()