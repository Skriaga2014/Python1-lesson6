'''
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
'''

class trap:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def proverka(self):
        long_1 = (t1.x, t2.x, t1.y, t2.y)
        long_2 = (t2.x, t3.x, t2.y, t3.y)
        long_3 = (t3.x, t4.x, t3.y, t4.y)
        long_4 = (t4.x, t1.x, t4.y, t1.y)
        parall = []                                 # Список горизонтальных прямых
        storony = []                                # Список НЕ горизонтальных прямых
        parall.append(long_1) if long_1[2] == long_1[3] else storony.append(long_1)
        parall.append(long_2) if long_2[2] == long_2[3] else storony.append(long_2)
        parall.append(long_3) if long_3[2] == long_3[3] else storony.append(long_3)
        parall.append(long_4) if long_4[2] == long_4[3] else storony.append(long_4)
        if trap.long(self, *storony[0]) == trap.long(self, *storony[1]) and \
            trap.long(self, *parall[0]) != trap.long(self, *parall[1]):
            return "Фигура ЯВЛЯЕТСЯ равнобедренной трапецией"
        print("Фигура НЕ является равнобедренной трапецией. ВЫХОД!")
        quit()

    def long(self, x1, x2, y1, y2):                         # Вычисление расстояния между точками
        return (float(abs(x1-x2)**2+abs(y1-y2)**2)**0.5)

    def perimetr(self):                                     # Вычисление периметра
        long1 = trap.long(self, t1.x, t2.x, t1.y, t2.y)
        long2 = trap.long(self, t2.x, t3.x, t2.y, t3.y)
        long3 = trap.long(self, t3.x, t4.x, t3.y, t4.y)
        long4 = trap.long(self, t4.x, t1.x, t4.y, t1.y)
        return long1+long2+long3+long4

    def square(self):                                       # Вычисление площади

        long_1 = (t1.x, t2.x, t1.y, t2.y)
        long_2 = (t2.x, t3.x, t2.y, t3.y)
        long_3 = (t3.x, t4.x, t3.y, t4.y)
        long_4 = (t4.x, t1.x, t4.y, t1.y)
        parall = []                                         # Список горизонтальных прямых
        storony = []                                        # Список НЕ горизонтальных прямых
        parall.append(long_1) if long_1[2] == long_1[3] else storony.append(long_1)
        parall.append(long_2) if long_2[2] == long_2[3] else storony.append(long_2)
        parall.append(long_3) if long_3[2] == long_3[3] else storony.append(long_3)
        parall.append(long_4) if long_4[2] == long_4[3] else storony.append(long_4)
        vysota = abs(parall[0][2]-parall[1][2])
        square = (abs(parall[0][0]-parall[0][1])+abs(parall[1][0]-parall[1][1]))*vysota/2
        return square

t1 = trap(1, 2)
t2 = trap(2, 5)
t3 = trap(6, 5)
t4 = trap(7, 2)


print("\n*** Программа работает лишь с располагающимися горизонтально трапециями ***\n")
print(t1.proverka())
print("Длина стороны AB:", t1.long(t1.x, t2.x, t1.y, t2.y))
print("Длина стороны BC:", t1.long(t2.x, t3.x, t2.y, t3.y))
print("Длина стороны CD:", t1.long(t3.x, t4.x, t3.y, t4.y))
print("Длина стороны DA:", t1.long(t4.x, t1.x, t4.y, t1.y))
print("Периметр:        ", t1.perimetr())
print("Площадь:         ", t1.square())



