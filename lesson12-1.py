# 1. Реализовать иерархию классов геометрических фигур. Базовый класс должен обязывать потомков реализовать методы - периметр и площадь. Потомки:
# 	Треугольник
#         конструктор: принимает список сторон и проверяет, что в списке сторон ровно 3
#         периметр
#         площадь
#
# 	Прямоугольник:
# 	    все аналогично треугольнику, только 2 стороны
# 	Круг:
#         все аналогично треугольнику, только принимает радиус


import math
class Figure:

    def P(self):
        raise Exception('no')

    def S():
        raise Exception('noo')

class Triangl(Figure):
    def __init__(self, St):
        self.s = St
        if len(St) != 3:
            raise Exception('ne treug')
    def P(self):
        return self.s[0] + self.s[1] + self.s[2]
    def S(self):
        return math.sqrt(self.P()/2 * (self.P()/2 - self.s[0]) * (self.P()/2 - self.s[1]) * (self.P()/2 - self.s[2]))

class Cyrc(Figure):
    def __init__(self, St):
        self.s = St
        if len(St) != 1:
            raise Exception('ne krug')
    def P(self):
        return math.pi * self.s[0] * 2
    def S(self):
        return math.pi * (self.s[0] ** 2)

class Pryam(Figure):
    def __init__(self, St):
        self.s = St
        if len(St) != 2:
            raise Exception('ne pryam')
    def P(self):
        return (self.s[0] + self.s[1]) * 2
    def S(self):
        return self.s[0] * self.s[1]


a = Triangl([3, 5, 7])
b = Pryam([3, 4])
c = Cyrc([6])
print(c.S())
print(a.P())
print(b.S())