'''
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
'''

class school:
    def __init__(self, surname, initials):
        self.surname = surname
        self.initials = initials

    @property
    def fullname(self):
        self.full_name = self.surname + ' ' +self.initials
        return self.full_name

class teacher(school):
    def __init__(self, surname, initials, predmet, klass):
        school.__init__(self, surname, initials)
        self.klass = klass
        self.predmet = predmet
        self.full_name = self.fullname

        global teacher_predmets
        global teacher_fullnames
        global teacher_klasses

        teacher_klasses.append(self.klass)
        teacher_predmets.append(self.predmet)
        teacher_fullnames.append(self.full_name)



class pupil(school):
    def __init__(self, surname, initials, klass, mom, dad):
        school.__init__(self, surname, initials)
        self.klass = klass
        self.mom = mom
        self.dad = dad
        self.full_name = self.fullname

        global pupil_moms
        global pupil_dads
        global pupil_classes
        global pupil_fullnames
        pupil_moms.append(self.mom)
        pupil_dads.append(self.dad)
        pupil_classes.append(self.klass)
        pupil_fullnames.append(self.full_name)

teacher_predmets = []
teacher_fullnames = []
teacher_klasses = []
pupil_fullnames = []
pupil_classes = []
pupil_moms = []
pupil_dads = []

p1 = pupil('Саломатин', 'И.А.', '5А', 'Саломатина Г.Г.', 'Саломатин А.И.')
p2 = pupil('Чичерова', 'Е.A.','7Б', 'Чичерова Н.Н.', 'Чичеров А.В.')
p3 = pupil('Владимиров', 'И.А.', '5А', 'Владимирова Г.Г.', 'Владимиров А.И.')
p4 = pupil('Чижиков', 'Е.A.','6Б', 'Чижикова Н.Н.', 'Чижиков А.В.')
p5 = pupil('Николаев', 'И.А.', '7А', 'Николаева Г.Г.', 'Николаев А.И.')
p6 = pupil('Михальчикова', 'Е.A.','6А', 'Михальчикова Н.Н.', 'Михальчиков А.В.')
p7 = pupil('Некрасова', 'И.А.', '5Б', 'Некрасова Г.Г.', 'Некрасов А.И.')
p8 = pupil('Огурцов', 'Е.A.','6А', 'Огурцова Н.Н.', 'Огурцов А.В.')
p9 = pupil('Неверов', 'И.А.', '7А', 'Неверова Г.Г.', 'Неверов А.И.')
p10 = pupil('Туполева', 'Е.A.','6Б', 'Туполева Н.Н.', 'Туполев А.В.')
p11 = pupil('Бигмаков', 'И.А.', '7А', 'Бигмакова Г.Г.', 'Бигмаков А.И.')
p12 = pupil('Харькова', 'Е.A.','6Б', 'Харькова Н.Н.', 'Харьков А.В.')
p13 = pupil('Клемнев', 'Е.A.','7Б', 'Клемнева Н.Н.', 'Клемнев А.В.')
p14 = pupil('Зайцев', 'И.А.', '5А', 'Зайцева Г.Г.', 'Зайцев А.И.')
p15 = pupil('Зайчихин', 'Е.A.','6Б', 'Зайчихина Н.Н.', 'Зайчихин А.В.')
p16 = pupil('Соболева', 'И.А.', '7А', 'Соболева Г.Г.', 'Соболев А.И.')
p17 = pupil('Толокнин', 'Е.A.','6А', 'Толокнина Н.Н.', 'Толокнин А.В.')
p18 = pupil('Попова', 'И.А.', '5Б', 'Попова Г.Г.', 'Попов А.И.')
p19 = pupil('Хайнс', 'Е.A.','6А', 'Хайнс Н.Н.', 'Хайнс А.В.')
p20 = pupil('Патрушева', 'И.А.', '7А', 'Патрушева Г.Г.', 'Патрушев А.И.')

t1 = teacher('Лотиков','И.А.','Математика',['5А','6А','7А'])
t2 = teacher('Колотовкина','Н.С.','Математика',['5Б','6Б','7Б'])
t3 = teacher('Русич','Г.А.','Русский язык',['5А','6А','7А'])
t4 = teacher('Бастрыкина','И.Н.','Русский язык',['5Б','6Б','7Б'])
t5 = teacher('Физрук','А.С.','Физика',['6А','7А','7Б'])
t6 = teacher('Савченко', 'Л.Н.', 'География', ['5А','5Б','6Б'])

# 1. Получить полный список всех классов школы
print('Классы в школе:', sorted(set(pupil_classes)))

print('\nСписок учеников по классам:')
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
for i in sorted(set(pupil_classes)):
    r = []
    n2 = 0
    for n in pupil_classes:
        if i == n:
            r.append(pupil_fullnames[n2])
        n2 += 1
    print(f'В классе {i}: {r}')

print('\nСписок "Ученик --> Класс --> Учителя --> Предметы":')
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
teachers = []
predmets = []
for n in range(len(pupil_fullnames)):
    name = pupil_fullnames[n]
    klass = pupil_classes[n]
    for i in range(len(teacher_fullnames)):
        if pupil_classes[n] in teacher_klasses[i]:
            teachers.append(teacher_fullnames[i])
            predmets.append(teacher_predmets[i])
    print(f'\n{n+1}. Ученик {name}\nКласс {klass}\nУчителя {teachers}\nПредметы {predmets}')
    teachers = []
    predmets = []

# 4. Узнать ФИО родителей указанного ученика
print('\nСписок родителей учеников:')
for n in range(len(pupil_fullnames)):
    print(f'\n{n+1}. Ученик {pupil_fullnames[n]}\nМать {pupil_moms[n]}\nОтец {pupil_dads[n]}')

# 5. Получить список всех Учителей, преподающих в указанном классе
print('\nСписок учителей по классам:')
for i in sorted(set(pupil_classes)):
    r = []
    n2 = 0
    for n in teacher_klasses:
        if i in n:
            r.append(teacher_fullnames[n2])
        n2 += 1
    print(f'В классе {i} препадают: {r}')