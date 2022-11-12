# Домашняя работа по теме "Объекты и классы"

# Класс студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Подсчет среднего балла по всем курсам
    def average_grade(self):
        grade_sum = 0
        grade_count = 0
        for course, grades in self.grades.items():
            grade_count += len(grades)
            grade_sum += sum(grades)
        if grade_count:
            return grade_sum / grade_count

    # Выставление оценок лекторам
    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Перегрузка метода __str__
    def __str__(self):
        result = f"Имя: {self.name}\n"
        result += f"Фамилия: {self.surname}\n"
        result += f"Средняя оценка за домашние задания: {self.average_grade()}\n"
        result += f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
        result += f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return result

    # Перегрузка метода сравнения __gt__
    def __gt__(self, student):
        if isinstance(student, Student):
            return self.average_grade() > student.average_grade()


# Родительский класс Преподавателей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Класс Лекторов
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grade() > lecturer.average_grade()

    def average_grade(self):
        grade_sum = 0
        grade_count = 0
        for course, grades in self.grades.items():
            grade_count += len(grades)
            grade_sum += sum(grades)
        if grade_count:
            return grade_sum / grade_count

    def __str__(self):
        result = f"Имя: {self.name}\n"
        result += f"Фамилия: {self.surname}\n"
        result += f"Средняя оценка за лекции: {self.average_grade()}"
        return result


# Класс проверяющих
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка выставления оценки'

    def __str__(self):
        result = f"Имя: {self.name}\n"
        result += f"Фамилия: {self.surname}"
        return result


# Полевые испытания

student_1 = Student("Michelle", "Flaherty", "women")
student_2 = Student("Steve", "Stifler", "men")
student_3 = Student("Kevin", "Myers", "man")
student_4 = Student("Victoria", "Lathum", "women")

student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']

student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Git']

student_3.courses_in_progress += ['Python']
student_3.courses_in_progress += ['Git']

student_4.courses_in_progress += ['Python']
student_4.courses_in_progress += ['Git']

lecturer_1 = Lecturer("Vincent", "Gogh")
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer("Mark", "Shagal")
lecturer_2.courses_attached += ['Python']

student_1.rate_lc(lecturer_1, 'Python', 6)
student_2.rate_lc(lecturer_1, 'Python', 3)
student_3.rate_lc(lecturer_1, 'Python', 8)
student_4.rate_lc(lecturer_1, 'Python', 9)

student_1.rate_lc(lecturer_1, 'Git', 10)  # Оценка не выставится - курс завершен
student_2.rate_lc(lecturer_1, 'Git', 8)  # Оценка не выставится - курс завершен
student_3.rate_lc(lecturer_1, 'Git', 10)
student_4.rate_lc(lecturer_1, 'Git', 9)

student_1.rate_lc(lecturer_2, 'Python', 9)
student_2.rate_lc(lecturer_2, 'Python', 6)
student_3.rate_lc(lecturer_2, 'Python', 8)
student_4.rate_lc(lecturer_2, 'Python', 7)

reviewer_1 = Reviewer("Mihail", "Lermontov")
reviewer_2 = Reviewer("Sergey", "Esenin")

reviewer_1.courses_attached.append("Python")
reviewer_2.courses_attached.append("Python")
reviewer_2.courses_attached.append("Git")
# print(reviewer_1.courses_attached)
# print(reviewer_2.courses_attached)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_3, 'Python', 8)
reviewer_1.rate_hw(student_4, 'Python', 10)

reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 6)

reviewer_2.rate_hw(student_3, 'Git', 9)
reviewer_2.rate_hw(student_4, 'Git', 6)

print("Проверяющие: ")
print(reviewer_1)
print(reviewer_2)

print("\nЛекторы: ")
print(lecturer_1)
print(lecturer_2)
if lecturer_1 > lecturer_2:
    print(f"У {lecturer_1.name} {lecturer_1.surname} средний балл за лекции выше "
          f"{lecturer_2.name} {lecturer_2.surname}")
else:
    print(f"У {lecturer_1.name} {lecturer_1.surname} средний балл за лекции не выше "
          f"{lecturer_2.name} {lecturer_2.surname}")

print("\nСтуденты: ")
# print(student_1, student_2, student_3, student_4, sep="\n\n")

students = [student_1, student_2, student_3, student_4]
lecturers = [lecturer_1, lecturer_2]
for stud in students:
    print(stud, end='\n\n')

if student_1 > student_2:
    print(f"У {student_1.name} {student_1.surname} средний балл за домашние задания выше "
          f"{student_2.name} {student_2.surname}")
else:
    print(f"У {student_1.name} {student_1.surname} средний балл за домашние задания не выше "
          f"{student_2.name} {student_2.surname}")

if student_4 > student_3:
    print(f"У {student_4.name} {student_4.surname} средний балл за домашние задания выше "
          f"{student_3.name} {student_3.surname}")
else:
    print(f"У {student_4.name} {student_4.surname} средний балл за домашние задания не выше "
          f"{student_3.name} {student_3.surname}")


# Подсчет средней оценки домашней работы по курсу
def student_average_grade(student_list, course):
    sum_grades = 0
    student_count = 0
    for student in student_list:
        if isinstance(student, Student) and course in student.courses_in_progress:
            student_count += 1
            sum_grades += sum(student.grades[course]) / len(student.grades[course])
    if student_count:
        return sum_grades / student_count


# Подсчет средней оценки за лекции по курсу
def lecturer_average_grade(lecturer_list, course):
    sum_grades = 0
    lecturer_count = 0
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            lecturer_count += 1
            sum_grades += sum(lecturer.grades[course]) / len(lecturer.grades[course])
    if lecturer_count:
        return sum_grades / lecturer_count


print()
print("Средняя оценка у студентов за курс 'Python':", student_average_grade(students, 'Python'))
print("Средняя оценка у студентов за курс 'Git':", student_average_grade(students, 'Git'))
print()
print("Средняя оценка у лекторов за курс 'Python':", lecturer_average_grade(lecturers, 'Python'))
print("Средняя оценка у лекторов за курс 'Git':", lecturer_average_grade(lecturers, 'Git'))
