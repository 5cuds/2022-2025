class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def meow(self):
        print(f"{self.name} Says Meow")

    def play(self):
        print(f"You Played {self.name}")

    def info(self):
        print(f"{self.name} is {self.age} years old")

cat = Cat("Bob", 5)

cat.meow()
cat.play()
cat.info()


# Adding Objects to Classes

class Student:
    def __init__(self, name, age, grade, year):
        self.name = name
        self.age = age
        self.grade = grade
        self.year = year

    def get_grade(self):
        print(f"{self.name}'s Grade: {self.grade}")

    def get_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\nSchool Year: {self.year}")


student = Student("Bob", 5, 75, "2022")
student_2 = Student("Sally", 6, 89, "2021")
student_3 = Student("Jill", 7, 85, "2020")

# Get The Object

class Course:
    def __init__(self, name, max_student) -> None:
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.grade
        print("Average Grade: ", total / len(self.students))


course = Course("Python", 2)

course.add_student(student)
course.add_student(student_2)
course.add_student(student_3)

course.get_average_grade()


