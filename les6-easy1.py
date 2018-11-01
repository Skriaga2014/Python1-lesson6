'''
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''

class tres:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def long(self, x1, x2, y1, y2):                         # Вычисление расстояния между точками
        return (float(abs(x1-x2)**2+abs(y1-y2)**2)**0.5)

    def perimetr(self):                                     # Вычисление периметра
        long1 = tres.long(self, t1.x, t2.x, t1.y, t2.y)
        long2 = tres.long(self, t2.x, t3.x, t2.y, t3.y)
        long3 = tres.long(self, t1.x, t3.x, t1.y, t3.y)
        return long1+long2+long3

    def high(self):                                         # Вычисление высоты
        long1 = tres.long(self, t1.x, t2.x, t1.y, t2.y)
        long2 = tres.long(self, t2.x, t3.x, t2.y, t3.y)
        long3 = tres.long(self, t1.x, t3.x, t1.y, t3.y)
        p = (long1+long2+long3)/2
        h = 2*((p*(p-long1)*(p-long2)*(p-long3))**0.5)/long1
        return h

    def square(self):                                       # Вычисление площади
        long = tres.long(self, t1.x, t2.x, t1.y, t2.y)
        h = tres.high(self)
        square = long * h / 2
        return square

t1 = tres(1, 2)
t2 = tres(6, 2)
t3 = tres(3, 5)

print("Периметр треугольника:", t1.perimetr())
print("Высота треугольника:", t1.high())
print("Площадь треугольника:", t1.square())
