list_of_cells = list(range(1, 10))
win_position = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def get_user_symbol():
    while True:
        user_symbol = input('Enter symbol for game: ').strip(' ').upper()
        if user_symbol not in ('X', 'O'):
            print('Symbol is\'t X or O')
            continue
        else:
            return user_symbol


def draw_field():
    for i in range(3):
        print(f'| {list_of_cells[0 + 3 * i]} | {list_of_cells[1 + 3 * i]} | {list_of_cells[2 + 3 * i]} |')


def choose_position(user_symbol):
    while True:
        value_of_position = input(f'Select the position of {user_symbol}:  ')
        if int(value_of_position) not in range(1, 10):
            print('Position must be in range from 1 to 9')
            continue
        else:
            value_of_position = int(value_of_position)
        if str(list_of_cells[value_of_position - 1]) in "XO":
            print('This cell is empty')
            continue
        else:
            list_of_cells[value_of_position - 1] = user_symbol
            break


def check_win():
    for each in win_position:
        if (list_of_cells[each[0] - 1]) == (list_of_cells[each[1] - 1]) == (list_of_cells[each[2] - 1]):
            return True
    return False


def get_second_user_symbol(first_user_symbol):
    if first_user_symbol == 'X':
        return 'O'
    else:
        return 'X'


if __name__ == '__main__':
    coun_step = 0
    first_user_symbol = get_user_symbol()
    second_user_symbol = get_second_user_symbol(first_user_symbol)
    while True:
        draw_field()
        if coun_step % 2 == 0:
            choose_position(first_user_symbol)
        else:
            choose_position(second_user_symbol)
        if coun_step > 3:
            winner = check_win()
            if winner:
                draw_field()
                if coun_step % 2 == 0:
                    print(first_user_symbol, 'is win')
                else:
                    print(second_user_symbol, 'is win')
                break
        coun_step += 1
        if coun_step > 8:
            draw_field()
            print('Is draw')
            break
