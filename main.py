from random import randint


def get_user_symbol():
    while True:
        user_symbol = input('Enter symbol for game: ').strip(' ').upper()
        if user_symbol not in ('X', 'O'):
            print('Symbol is\'t X or O')
            continue
        else:
            return user_symbol


def show_field():
    for x in range(3):
        for y in range(3):
            print('|', end='')
            print(x + y + 1, end='')
        print('|')


if __name__ == '__main__':
    get_user_symbol()
    show_field()
