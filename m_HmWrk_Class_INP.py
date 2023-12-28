# Home work for theme: Objects and Classes. encapsulation inheritance polymorphism

# Task №1,2,3,4

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def Student_rate_hw(self, lector, course, grade): # Оценка лектора
        if isinstance(lector, Lecturer) and course in self.courses_in_progress:
            if course in lector.lecturer_grades:
                lector.lecturer_grades[course] += [grade]
            else:
                lector.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def Mean(self): # Средний бал студента
        y = 0
        if len(self.grades.values())>0:
            for x in self.grades.values():  ## Быстро не нашёл как преобразовать в лист и вывести через statistics.mean(*args) красиво
                x=x[0]
                y+=x
            return round(y/len(self.grades.values()),2)
        else:
            return None

    def __str__(self) -> str:
        finished_cours = ', '.join(self.finished_courses)
        courses_in_progr = ', '.join(self.courses_in_progress)
        return f'{__class__. __name__}\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.Mean()} \
                 \nКурсы в процессе изучения: {courses_in_progr}\nЗавершённые курсы: {finished_cours}\n'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []     
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_attached
        self.lecturer_grades = {}

    def Mean(self): # Средний бал лектора
        y = 0
        if len(self.lecturer_grades.values())>0:
            for x in self.lecturer_grades.values():  ## Быстро не нашёл как преобразовать в лист и вывести через statistics.mean(*args) красиво
                x=x[0]
                y+=x
            return round(y/len(self.lecturer_grades.values()),2)
        else:
            return None

    def __str__(self) -> str:                                                           
        return f'{__class__. __name__}\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.Mean()}\n'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_attached

    def Reviewer_rate_hw(self, student, course, grade): # Оценка студента
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f'{__class__. __name__}\nИмя: {self.name}\nФамилия: {self.surname}\n'
                     

class Comparison_Obj:  ## Сравнение
    def __init__(self, value,name):
        self.value = value
        self.name = name

    def Comparison(self,other):
        if self.value == other.value:
            return f'{self.name} такой же способный как и {other.name}\n'
        elif self.value > other.value:
            return f'{self.name} учится/преподаёт лучше {other.name}\n'
        elif self.value < other.value:
            return f'{self.name} учится/преподаёт хуже {other.name}\n'

 
Student_db = [
    Student('Ruoy', 'Eman', 'your_gender'),
    Student('Zhaman', 'dRugoy', 'your_gender'),
    Student('Omar', 'Vareniy', 'your_gender')
]

Lecturer_db = [
    Lecturer('Tamara', 'Vasilyeva'),
    Lecturer('Angela', 'Stryder')
]

Reviewer_db = [
    Reviewer('Zinaida', 'Petrova')
]

Student_db[0].courses_in_progress = ['Python','C++','IEC 61131-3']
Student_db[0].finished_courses += ['Введение в программирование']

Student_db[1].courses_in_progress += ['Python','IEC 61131-3']
Student_db[1].finished_courses += ['Введение в программирование']
            
Reviewer_db[0].courses_attached = ['Python','C++','IEC 61131-3']

Reviewer_db[0].Reviewer_rate_hw(Student_db[0],'Python',10)
Reviewer_db[0].Reviewer_rate_hw(Student_db[0],'C++',9)
Reviewer_db[0].Reviewer_rate_hw(Student_db[0],'IEC 61131-3',8)

Reviewer_db[0].Reviewer_rate_hw(Student_db[1],'Python',6)
Reviewer_db[0].Reviewer_rate_hw(Student_db[1],'IEC 61131-3',8)

Student_db[0].Student_rate_hw(Lecturer_db[0],'IEC 61131-3',5)
Student_db[0].Student_rate_hw(Lecturer_db[0],'C++',6)
Student_db[0].Student_rate_hw(Lecturer_db[0],'Python',7)

Student_db[1].Student_rate_hw(Lecturer_db[1],'IEC 61131-3',3)
Student_db[1].Student_rate_hw(Lecturer_db[1],'Python',2)

## Отладочная информация
#print('Отладочная информация')
#print(f'student: {Student_db[0].name} {Student_db[0].surname} {Student_db[0].grades}')
#print(f'student: {Student_db[1].name} {Student_db[1].surname} {Student_db[1].grades}')
#print(f'student: {Student_db[2].name} {Student_db[2].surname} {Student_db[2].grades}')
#print(f'lecturer: {Lecturer_db[0].name} {Lecturer_db[0].surname} {Lecturer_db[0].lecturer_grades}')
#print(f'lecturer: {Lecturer_db[1].name} {Lecturer_db[1].surname} {Lecturer_db[1].lecturer_grades}')
#print(f'reviewer: {Reviewer_db[0].name} {Reviewer_db[0].surname} {Reviewer_db[0].courses_attached}')
#print('\n')
##

for i,j in enumerate(Student_db): print(j)
for i,j in enumerate(Lecturer_db): print(j)
for i,j in enumerate(Reviewer_db): print(j)

# Сравнение    
a = Comparison_Obj(Student_db[0].Mean(),Student_db[0].name)
b = Comparison_Obj(Student_db[1].Mean(),Student_db[1].name)
print(a.Comparison(b))

# Функция для подсчёта средней оценки за домашние задания по всем студентам в рамках конкретного курса
def all_stdnt_mddl(db = Student_db, key = 'Python'):
    z=0
    r=0
    for x,y in enumerate(db):
        if y.grades.get(key) != None:
            r+=1
            zz_list = y.grades.get(key)
            z+=zz_list[0]
        else: continue
    print(f'Количество студентов на курсе: {key} = {r}\nСредний бал за ДЗ = {round(z/(r),2)}\n')
        
all_stdnt_mddl()

# Функция для подсчёта средней оценки за лекции всех лекторов в рамках курса
def all_lctr_mddl(db = Lecturer_db, key = 'C++'):
    z=0
    r=0
    for x,y in enumerate(db):
        if y.lecturer_grades.get(key) != None:
            
            r+=1
            zz_list = y.lecturer_grades.get(key)
            z+=zz_list[0]
        else: continue
    print(f'Количество лекторов на курсе: {key} = {r}\nСредний бал за лекции = {round(z/(r),2)}\n')

all_lctr_mddl()


