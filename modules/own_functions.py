import inspect
"""
набор вспомогательных функций:
    check_args(*args), check_grades(grade), check_instance(obj, parent_class),
    check_student_course(obj, course), check_lecture_course(obj, course) - отвечают за проверку входящих данных
    
    set_grade(obj, course, grade) - проставляет оценки
    
    calc_grade_average(obj, grade) - считает среднюю оценку для obj
    
    dispatcher(self, obj, parent_class, course, grade) - регламентирует действие всех вышеперечисленных
    функций в зависимости из какого класса его вызвали  
    
    average_for_all_on_course(obj_list, course_name) - функция для Задания №4  
"""

def dispatcher(self, obj, parent_class, course, grade):
    if check_args(obj, course, grade) is True:
        if check_grades(grade) is True:
            if check_instance(obj, parent_class) is True:
                if parent_class.__name__ == 'Student' and check_student_course(obj, course) is True:
                    set_grade(obj, course, grade)
                    calc_grade_average(obj, grade)
                elif parent_class.__name__ == 'Lecture' and check_student_course(self, course) is True:
                    if check_lecture_course(obj, course):
                        set_grade(obj, course, grade)
                        calc_grade_average(obj, grade)

def check_args(*args):
    """ проверяет переданы ли все аргументы при вызове функции """
    # скорее всего это лишнее, но было интересно реализовать
    if None not in args:
        return True
    else:
        module_name = inspect.stack()[2].filename
        line = inspect.stack()[2].lineno
        function_name = inspect.stack()[1].function
        print(f'ArgumentsError: {module_name}, строка {line}, {function_name}() передано недостаточно аргументов')
        # не уверен в необходимости возвращать False, поправтье, если не прав
        # return False

def check_grades(grade):
    if grade in range(1, 11):
        return True
    else:
        module_name = inspect.stack()[2].filename
        line = inspect.stack()[2].lineno
        function_name = inspect.stack()[1].function
        print(
            f'ValueError: {module_name}, строка {line}, {function_name}() {grade} не целое число в диапозоне от 1 до 10')
        # return False

def check_instance(obj, parent_class):
    if isinstance(obj, parent_class):
        return True
    else:
        print(f'ValueError: {obj} не является потомком {parent_class.__name__}()')
        # return False

def check_student_course(obj, course):
    """ проверяет обучается student на курсе или нет"""
    if course in obj.courses_in_progress:
        return True
    else:
        print(f'ValueError: {obj.name} {obj.surname} не является студентом курса {course}')
        # return False

def check_lecture_course(obj, course):
    """ провераяет закреплен lecture за курсом или нет"""
    if course in obj.courses_attached:
        return True
    else:
        print(f'ValueError: {obj.name} {obj.surname} не преподаёт {course}')
        # return False

def set_grade(obj, course, grade):
    """
    выставляет оценку
        args:
            obj(object): экземпляр класса для работы\n
            course(str): название курса\n
            grade(int): оценка\n
    """
    if course in obj.grades['history']:
        obj.grades['history'][course] += [grade]
    else:
        obj.grades['history'][course] = [grade]


def calc_grade_average(obj, grade):
    """ считает среднюю оценку """
    obj.grades['counter'] += 1
    obj.grades['sum'] += grade
    average = round(obj.grades['sum'] / obj.grades['counter'], 1)
    obj.grades['average'] = average

def get_average_for_all_on_course(obj_list, course_name):
    """
    считает среднюю оценку по конкретному курсу
    по дз и лекциям\n
    args:
        obj_list: кортеж объектов класса
        course_name: название курса
    return:
        float: среднее по курсу
    """
    summary = 0
    for counter, obj in enumerate(obj_list):
        if course_name in obj.grades['history']:
            summary += sum(obj.grades['history'][course_name])
        else:
            print(f'\nValueError: {obj.name} {obj.surname} не связан с курсом {course_name}\n')
    return round(summary / (counter + 1), 2)