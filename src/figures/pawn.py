import src.board
from .figure import Figure
from ..services import get_letter_index


class Pawn(Figure):
    def __init__(self, blue: bool = True):
        super().__init__('P', blue)

    def calculate_moves(self, y: int, x: int, board: 'src.board.Board') -> list[str]:
        indexes = []
        if self.blue:
            if type(board.get_by_index(y - 1, x)) == str:
                indexes.append((y - 1, x))
            if type(board.get_by_index(y - 2, x)) == str and y == 6:
                indexes.append((y - 2, x))
        else:
            if type(board.get_by_index(y + 1, x)) == str:
                indexes.append((y + 1, x))
            if type(board.get_by_index(y + 2, x)) == str and y == 1:
                indexes.append((y + 2, x))
        indexes = list(filter(lambda pos: 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7, indexes))
        indexes = self.get_moves(indexes, board) + self.__calculate_beat(y, x, board)

        return [get_letter_index(x, y) for y, x in indexes]

    def __calculate_beat(self, y: int, x: int, board: 'src.board.Board') -> list[str]:
        if self.blue:
            indexes = [(y - 1, x + 1), (y - 1, x - 1)]
        else:
            indexes = [(y + 1, x + 1), (y + 1, x - 1)]
        indexes = list(filter(lambda pos: 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7, indexes))
        indexes = list(filter(lambda pos: type(board.get_by_index(pos[0], pos[1])) != str, indexes))
        return indexes
