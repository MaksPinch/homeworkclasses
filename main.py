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

    def average_grade(self):
        all_grades = []

        for course, grades in self.grades.items():
            for grade in grades:
                all_grades.append(grade)

        if len(all_grades) > 0:
            return round(sum(all_grades) / len(all_grades), 1)
        return 0

    def __str__(self):
        avg_grade = self.average_grade()


        if self.courses_in_progress:
            courses_in_progress = ", ".join(self.courses_in_progress)
        else:
            courses_in_progress = "Нет"


        if self.finished_courses:
            finished_courses = ", ".join(self.finished_courses)
        else:
            finished_courses = "Нет"

        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):

        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


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

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []

        for course, grades_list in self.grades.items():
            for grade in grades_list:
                all_grades.append(grade)

        if len(all_grades) > 0:
            return round(sum(all_grades) / len(all_grades), 1)
        else:
            return "Нет"

    def __str__(self):
        avg_grade = self.average_grade()
        return (f"Имя: {self.name} \nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()



best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Alexandr', 'An')
cool_lecturer.courses_attached += ['Python']



# run the methods

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
#
best_student.rate_lecturer(cool_lecturer, 'Python', 7)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
print(" ! 1 и 2 задания !")

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

print()

# exercise 3
print(" ! 3 задание !")


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Alice', 'J', 'female')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['C++']


lecturer_1 = Lecturer('John', 'D')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Sarah', 'C')
lecturer_2.courses_attached += ['Java']


reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)


student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)

student_2.rate_lecturer(lecturer_2, 'Java', 8)
student_2.rate_lecturer(lecturer_2, 'Java', 7)


print(reviewer_1)
print()
print(lecturer_1)
print(lecturer_2)
print()
print(student_1)
print(student_2)
print()


print(f"{student_1.name} лучше {student_2.name}? {student_1 > student_2}")
print(f"{student_1.name} и {student_2.name} равны по оценкам? {student_1 == student_2}")


print(f"{lecturer_1.name} лучше {lecturer_2.name}? {lecturer_1 > lecturer_2}")
print(f"{lecturer_1.name} и {lecturer_2.name} равны по оценкам? {lecturer_1 == lecturer_2}")
