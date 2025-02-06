class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if  isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 1 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return "Ошибка! оценка не находится в пределах от 1 до 10"
        else:
            return "Ученик и Лектор не находятся на одном курсе!"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}



best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Alex', 'An')
cool_lecturer.courses_attached += ['Python']



# run the methods

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(cool_lecturer, 'Python', 7)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

# show the results of the program
result1 = best_student.grades
result2 = cool_lecturer.grades
print(result1)
print(result2)

# examples with the False statement

another_student = Student('Alice', 'Johnson', 'female')
another_student.courses_in_progress += ['Python']

another_reviewer = Reviewer('Timothee', 'Chalamet')
another_reviewer.courses_attached += ['Java']

another_lecturer = Lecturer('The', 'Rock')
another_lecturer.courses_attached += ['Java']



result3 = another_reviewer.rate_hw(another_student, 'Python', 5)
result4 = another_student.rate_lecturer(another_lecturer, 'Python', 8)

print(result3)
print(result4)

