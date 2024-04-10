from src.board import Board
from src.exceptions import BadIndexException, NotAFigureException, ImpossibleMoveException, NotYourFigureException
from src.services import check_index


def test_game(el, i, b):
    color = i % 2 == 0
    index = el[0]
    while True:
        try:
            check_index(index)
            spaces = b.set_available_spaces(index, color)
            assert spaces
            b.show(spaces)
            break
        except BadIndexException:
            print('Invalid index!')
            break
        except NotAFigureException:
            print('This is not a figure!')
        except NotYourFigureException:
            print('This is not your figure!')
        except AssertionError:
            print('You cant move this figure!')
    # time.sleep(5)
    while True:
        new_index = el[1]
        try:
            b.make_move(index, new_index, color)
            b.show([])
            break
        except ImpossibleMoveException:
            b.show([])
            print('Impossible move!')
    # time.sleep(5)


def start(path):
    i = 0
    moves = []

    bo = Board()
    bo.show([])

    with open(path) as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            mpos1, mpos2 = line.split('-')
            moves.append((mpos1, mpos2))
    for el in moves:
        test_game(el, i, bo)
        i += 1
        if bo.is_mate(i):
            if (i - 1) % 2 == 0:
                color = 'blue'
            else:
                color = 'red'
            bo.show([], message=f'Mate! {color} wins!')


start('test/test_4.txt')
start('test/test_1.txt')
start('test/test_2.txt')
start('test/test_3.txt')
start('test/test_5.txt')
