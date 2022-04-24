import copy

# https://habr.com/ru/post/186608/

class Point2D():

    #--------------------------------------
    # ЧАСТЬ 1
    # --------------------------------------

    # вызывается при инициализации объекта
    def __init__(self, x, y):
        self.coord = [x,y]

    # Вызывается при печати (print) объекта
    def __str__(self):
        return f'Point: ({self.coord[0]}, {self.coord[1]})'

    # Вызывается при удалении объекта
    def __del__(self):
        del self.coord

    # для этого класса не корректно использовать длину вектора
    # Вызывается при запросе длины объекта. Требует возврат только целого числа (!)
    def __len__(self):
        return int((self.coord[0]**2+self.coord[1]**2)**0.5)

    def distance(self):
        return (self.coord[0]**2+self.coord[1]**2)**0.5

    # Вызывается при итерации объекта
    def __getitem__(self, key):  # под дефолту назначение item вместо key
        return self.coord[key]

    #--------------------------------------
    # ЧАСТЬ 2
    # --------------------------------------

    def __eq__(self, other):
        return ((self.coord[0] == other.coord[0]) and (self.coord[1] == other.coord[1]))

    def __lt__(self, other): # lt = меньше (<), gt = больше (>), le = меньше или равно (<=), ge = больше или равно (>=)
        return (self.distance() < other.distance())


    def __add__(self, other):  # сложение
        if isinstance(other, Point2D):
            return Point2D(self.coord[0] + other.coord[0], self.coord[1] + other.coord[1])
        if isinstance(other, int):
            return Point2D(self.coord[0] + other, self.coord[1] + other)

    def __float__(self):
        return self.distance()

    #--------------------------------------
    # ЧАСТЬ 2
    # --------------------------------------
    #--------------------------------------
    # ЧАСТЬ 3
    # --------------------------------------

    def __getstate__(self):
        return self.coord

    def __setstate__(self, state):
        self.coord = state

    #--------------------------------------
    # ЧАСТЬ 3
    # --------------------------------------

    #--------------------------------------
    # ЧАСТЬ 4
    # --------------------------------------

    # статические методы
    @staticmethod
    def stat_method_ex(x,y):
        if (x**2+y**2)**0.5 > 1:
            return 1
        return 0

    # метод класса
    @classmethod
    def class_method_ex(cls):
        point_list = []
        for i in range(10):
            point_list.append(cls(i, i+1))

        return point_list

    #--------------------------------------
    # ЧАСТЬ 4
    # --------------------------------------

    #--------------------------------------
    # ДОМАШНЕЕ ЗАДАНИЕ LITE
    def __le__(self, other): # lt = меньше (<), gt = больше (>), le = меньше или равно (<=), ge = больше или равно (>=)
        return (self.distance() <= other.distance())

    def __gt__(self, other): # lt = меньше (<), gt = больше (>), le = меньше или равно (<=), ge = больше или равно (>=)
        return (self.distance() > other.distance())

    def __ge__(self, other): # lt = меньше (<), gt = больше (>), le = меньше или равно (<=), ge = больше или равно (>=)
        return (self.distance() >= other.distance())

    def __repr__(self):
        return f'({self.coord[0]}, {self.coord[1]})'

    def __copy__(self): # при копировании "отзеркалим" координаты
        print('copying ...')
        my_copy = type(self)(self.coord[1], self.coord[0])
        return my_copy

if __name__ == '__main__':

    list_ = Point2D.class_method_ex()
    print(list_)

    for i in range(10):
        print(list_[i])

    print(Point2D.stat_method_ex(1,2))


    point1 = Point2D(2,1)


    print(point1)

    # del point1

    str1 = 'Volvo'
    list_test = [1,2,3,4]
    print(len(str1), len(list_test), len(point1))
    print(point1.distance())

    for item in str1:
        print(item)

    for item in list_test:
        print(item)

    print(1 in point1, 2 in point1)

    for coord in point1:
        print(coord)

    print(repr(point1))
    point3 = copy.copy(point1)
    print(point3)
    print(point1)



