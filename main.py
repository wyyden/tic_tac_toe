import sys
import time


list_of_cells = list(range(9))
win_position = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
user_turn = True
ai_turn = False
user_symbol = 'X'
ai_symbol = 'O'


def draw_field():
    for i in range(3):
        print(f'| {list_of_cells[0 + 3 * i]} | {list_of_cells[1 + 3 * i]} | {list_of_cells[2 + 3 * i]} |')


def choose_position(list_of_cells):
    field = list_of_cells.copy()
    while True:
        value_of_position = input(f'Select the position of {user_symbol}:  ')
        if int(value_of_position) not in range(9):
            print('Position must be in range from 0 to 8')
            continue
        else:
            value_of_position = int(value_of_position)

        if str(field[value_of_position]) in "XO":
            print('This cell is\'n empty')
            continue
        else:
            field[value_of_position] = user_symbol
            return field


def check_win(feild, is_user_step):
    for each in win_position:
        if (feild[each[0]]) == (feild[each[1]]) == (feild[each[2]]):
            if is_user_step:
                return 'USER WIN'
            else:
                return 'AI WIN'
    return False


def get_ai_symbol(user_symbol):
    if user_symbol == 'X':
        return 'O'
    else:
        return 'X'


def minimax(field, depth, is_user_step):
    if check_win(field, is_user_step) == 'AI WIN':
        return scores[ai_symbol]
    elif check_win(field, is_user_step) == 'USER WIN':
        return scores[user_symbol]
    elif is_draw(field):
        return scores['is draw']

    if is_user_step:
        best_score = sys.maxsize
        for cell in field:
            if str(cell) not in 'XO':
                cell_num = field[cell]
                field[cell] = user_symbol
                score = minimax(field, depth + 1, ai_turn)
                field[cell] = cell_num
                best_score = min(best_score, score)
    else:
        best_score = - sys.maxsize
        for cell in field:
            if str(cell) not in 'XO':
                cell_num = field[cell]
                field[cell] = ai_symbol
                score = minimax(field, depth + 1, user_turn)
                field[cell] = cell_num
                best_score = max(best_score, score)

    return best_score


def get_ai_position(list_of_cells):
    move = None
    best_score = -sys.maxsize
    field = [cell for cell in list_of_cells]
    for cell in field:
        if str(cell) not in 'XO':
            num_cell = cell
            field[cell] = ai_symbol
            score = minimax(field, 0, user_turn)
            field[cell] = num_cell
            if score > best_score:
                best_score = score
                move = cell

    return move


def is_draw(field):
    count = 0
    for cell in field:
        if str(cell) in 'XO':
            count += 1
    return count == 9


scores = {
    user_symbol: 100,
    ai_symbol: -100,
    'is draw': 0
}


def first_step():
    while True:
        answer = input('Enter \'X\' if you want the computer to go first else enter \'O\': ').strip(' ').lower()
        if answer != 'XO':
            print('Symbol is\'t x or y')
            continue

        if answer == 'x':
            return True
        else:
            return False

if __name__ == '__main__':
    coun_step = 0
    is_user_step = first_step()
    while True:
        if is_user_step:
            draw_field()
            list_of_cells = choose_position(list_of_cells)
        else:
            move = get_ai_position(list_of_cells)
            if move is not None:
                list_of_cells[move] = ai_symbol
        if coun_step > 3:
            if check_win(list_of_cells, is_user_step) == 'AI WIN':
                draw_field()
                print(check_win(list_of_cells, is_user_step))
                break
            elif check_win(list_of_cells, is_user_step) == 'USER WIN':
                draw_field()
                print(check_win(list_of_cells, is_user_step))
                break
        coun_step += 1
        if is_draw(list_of_cells):
            draw_field()
            print('Is draw')
            break
        if is_user_step:
            is_user_step = False
        else:
            is_user_step = True
    time.sleep(10)