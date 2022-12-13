# "Крестики - нолики" итоговое практическое задание B5.6
field = [[' ', ' ', ' '] for i in range(3)]

def print_f():
    print('  0  1  2')
    print(f'0 {field[0][0]}  {field[0][1]}  {field[0][2]}')
    print(f'1 {field[1][0]}  {field[1][1]}  {field[1][2]}')
    print(f'2 {field[2][0]}  {field[2][1]}  {field[2][2]}')

def input_XY():
      x, y = map(int, input('Введите 2 координаты через пробел: ').split())
      while True:
            if 0 <= x <= 2 and 0 <= y <= 2:
                  if field[x][y] == ' ':
                        return x, y
                  else:
                        print('Ячейка занята')
            else:
                  print('Такого поля нет')


def check():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        a = []
        for i in cord:
            a.append(field[i[0]][i[1]])
        if a == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if a == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False

step = 0
while True:
    step += 1
    print_f()
    if step%2 != 0:
        print('Ходит X')
        x, y = input_XY()
        field[x][y] = 'X'
    else:
        print('Ходит 0')
        x, y = input_XY()
        field[x][y] = '0'
    if check():
        break
