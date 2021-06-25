# Tic_Tac_Toe
# Frontend GUI

field = []
play = True
turn = 1

def start():
    cells = 9 * ' '
    index = 0
    for _ in range(3):
        field.append(list(cells[index:index + 3]))
        index += 3


def display():
    print(f'''---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------''')


def coordinates():
    global turn
    choice = input('Enter the coordinates: ').replace(' ', '')
    if len(choice) == 2 and choice.isdigit():
        x, y = int(choice[0]) - 1, int(choice[1]) - 1
        if 0 <= x < 3 and 0 <= y < 3:
            if field[x][y] == ' ':
                if turn % 2 == 0:
                    field[x][y] = 'O'
                    turn += 1
                else:
                    field[x][y] = 'X'
                    turn += 1
            else:
                print('This cell is occupied! Choose another one!')
                coordinates()
        else:
            print('Coordinates should be from 1 to 3!')
            coordinates()
    else:
        print('You should enter numbers!')
        coordinates()


# Tic_Tac_Toe
# Backend game logic

def result():
    global play
    turns = ''.join([''.join(row) for row in field])
    error = False
    if abs(turns.count('X') - turns.count('O')) > 1:
        print('Impossible')
        play = False
        error = True

    draw = False
    if turns.count('X') + turns.count('O') == 9:
        draw = True

    lines = ['X', 'X', 'X'], ['O', 'O', 'O']
    vertical_field = [[field[0][index], field[1][index], field[2][index]] for index in range(3)]
    diag_1, diag_2 = [field[i][i] for i in range(3)], [field[i][2 - i] for i in range(3)]

    vertical = [col[0] for col in vertical_field if col in lines]
    horizontal = [row[0] for row in field if row in lines]
    diagonal = [diag[0] for diag in [diag_1, diag_2] if diag in lines]

    winner = vertical + horizontal + diagonal
    if not error and winner and len(winner) == 1:
        print(winner[0] + ' wins')
        play = False
    elif not winner:
        if draw:
            print('Draw')
            play = False
    else:
        print('Impossible')
        play = False



def play():
    start()
    display()
    while play:
        coordinates()
        display()
        result()

play()
