import sys

from src.board import Board
from src.exceptions import BadIndexException, NotAFigureException, ImpossibleMoveException, NotYourFigureException
from src.services import check_index


def set_figure(b: Board, color: bool, index: str):
    check_index(index)
    spaces = b.set_available_spaces(index, color)
    assert spaces
    b.show(spaces)
    return spaces


def place_figure(b: Board, color: bool, index: str, new_index: str):
    b.make_move(index, new_index, color)
    b.show([])


def play_game(b: Board, color: bool):
    b.show([])
    while True:
        try:
            index = input('Enter first index: ')
            spaces = set_figure(b, color, index)
            break
        except BadIndexException:
            print('Invalid index!')
        except NotAFigureException:
            print('This is not a figure!')
        except NotYourFigureException:
            print('This is not your figure!')
        except AssertionError:
            print('You cant move this figure!')

    while True:
        try:
            new_index = input('Enter new index: ')
            place_figure(b, color, index, new_index)
            break
        except ImpossibleMoveException:
            print('Impossible move!')
    if b.is_mate(not color):
        if color:
            col = 'blue'
        else:
            col = 'red'
        b.show([], message=f'Mate! {col} wins!')
        return index, new_index
    return index, new_index
