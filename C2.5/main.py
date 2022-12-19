from random import randint

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x}, {self.y})'

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Точка за пределами доски"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли сюда"

class BoardWrongShipException(BoardException):
    pass

class Ship:
    def __init__(self, l, bow, o):
        self.l = l
        self.bow = bow
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

