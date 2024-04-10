from string import ascii_lowercase

from src.exceptions import BadIndexException


def get_letter_index(x: int, y: int) -> str:
    index = f'{ascii_lowercase[x]}{8 - y}'
    return index


def check_index(index) -> (int, int):
    """
    Return index of matrix by string of index
    Ex: e1 ->

    :param index:
    :return:

    :raises:
        BadIndexException: if index is not correct
    """
    if len(index) != 2:
        raise BadIndexException()
    if not index[0].isalpha() or not index[1].isdigit() or index[0].lower() not in ascii_lowercase[:8]:
        raise BadIndexException()
    x = ascii_lowercase.index(index[0].lower())
    y = 8 - int(index[1])
    if not (0 <= x <= 7) or not (0 <= y <= 7):
        raise BadIndexException()
    return x, y
