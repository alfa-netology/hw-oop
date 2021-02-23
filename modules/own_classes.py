import modules.own_functions as functions

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = []
        """
        grades:
            'average' - срендяя оценка
            'counter' - количество оценок
            'sum' - сумма всех проставленных оценко
            'history' : { 'course_name' : [grades] }
        """
        self.grades = {'average': 0, 'counter': 0, 'sum': 0, 'history': {}}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания :  {self.grades['average']}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.grades['average'] < other.grades['average'] \
               or self.grades['average'] == other.grades['average']

    def rate_lecture(self, lecture=None, course=None, grade=None):
        """ выставляет оценку лектору """
        functions.dispatcher(self, lecture, Lecture, course, grade)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        """
        grades:
            'average' - срендяя оценка
            'counter' - количество оценок
            'sum' - сумма всех проставленных оценко
            'history' : { 'course_name' : [grades] }
        """
        self.grades = {'average': 0, 'counter': 0, 'sum': 0, 'history': {}}

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self.grades['average']}"

    def __lt__(self, other):
        return self.grades['average'] < other.grades['average'] \
               or self.grades['average'] == other.grades['average']


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student=None, course=None, grade=None):
        """ проставляет оценки студентам за дз"""
        functions.dispatcher(self, student, Student, course, grade)