import random
from modules.own_classes import Student, Lecture, Reviewer
from modules.own_functions import get_average_for_all_on_course

# ПОЛЕВЫЕ ИСПЫТАНИЯ
# создаем экзепляры классов
lecture_01 = Lecture('Доктор', 'Стрэндж')
lecture_01.courses_attached += ['Python', 'Git']

lecture_02 = Lecture('Профессор', 'Икс')
lecture_02.courses_attached += ['SQL', 'Django']

student_01 = Student('Джон', 'Константин', 'Male')
student_01.courses_in_progress += ['Python', 'Git', 'SQL', 'Django']

student_02 = Student('Серебряный', 'Сёрфер', 'Male')
student_02.courses_in_progress += ['Python', 'Git', 'SQL', 'Django']

reviewer_01 = Reviewer('Судья', 'Дредд')
reviewer_01.courses_attached += ['Python', 'Git', 'SQL', 'Django']

reviewer_02 = Reviewer('Соколиный', 'Глаз')
reviewer_02.courses_attached += ['Python', 'Git', 'SQL', 'Django']

# проставляем оценки
def set_lecture_grades(student, lecture):
    courses = [*lecture.courses_attached]
    for c in courses:
        for grade in [random.randint(1, 10) for i in range(4, 10)]:
            student.rate_lecture(lecture, c, grade)

def set_student_grades(reviewer, student):
    courses = [*reviewer.courses_attached]
    for c in courses:
        for grade in [random.randint(1, 10) for i in range(4, 10)]:
            reviewer.rate_hw(student, c, grade)


set_lecture_grades(student_01, lecture_01)
set_lecture_grades(student_02, lecture_02)
set_student_grades(reviewer_01, student_01)
set_student_grades(reviewer_02, student_02)

# выводим историю оценок
objects = (student_01, student_02, lecture_01, lecture_02)
for obj in objects:
    print(f'{obj.name} {obj.surname} история оценок:\n{obj.grades}\n')

# проверям переопределение __str__
print(lecture_01, '\n')
print(lecture_02, '\n')
print(student_01, '\n')
print(student_02, '\n')
print(reviewer_01, '\n')
print(reviewer_02, '\n')

# средняя оценка студента и лектора
print(f'Средняя оценка {student_01.name} {student_01.surname} за домашние задания {student_01.average_grade()}')
print(f'Средняя оценка {student_02.name} {student_02.surname} за домашние задания {student_02.average_grade()}', '\n')
print(f'Средняя оценка {lecture_01.name} {lecture_01.surname} за лекции {lecture_01.average_grade()}')
print(f'Средняя оценка {lecture_02.name} {lecture_02.surname} за лекции {lecture_02.average_grade()}', '\n')

# сравниваем средние оценки
print(student_01.average_grade() > student_02.average_grade())
print(lecture_01.average_grade() < lecture_02.average_grade(), '\n')


# ЗАДАНИЕ №4
students = (student_01, student_02)
course = 'Git'
print(f'Средний балл студентов курса {course}: {get_average_for_all_on_course(students, course)}')

students = (student_01, student_02)
course = 'SQL'
print(f'Средний балл студентов курса {course}: {get_average_for_all_on_course(students, course)}')

lectures = (lecture_01, lecture_02)
course = 'Git'
print(f'Средний бал лекторов курса {course}: {get_average_for_all_on_course(lectures, course)}')

lectures = (lecture_01, lecture_02)
course = 'SQL'
print(f'Средний бал лекторов курса {course}: {get_average_for_all_on_course(lectures, course)}')