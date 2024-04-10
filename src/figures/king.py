import src.board
from .figure import Figure
from ..services import get_letter_index


class King(Figure):
    def __init__(self, color: bool = True):
        super().__init__('K', color)

    def calculate_moves(self, y: int, x: int, board: 'src.board.Board') -> list[str]:
        indexes = [
            (y + 1, x),
            (y, x + 1),
            (y - 1, x),
            (y, x - 1),
            (y - 1, x - 1),
            (y + 1, x + 1),
            (y - 1, x + 1),
            (y + 1, x - 1),
        ]
        indexes = [self.get_moves([index], board) for index in indexes]
        indexes = self.reshape_indexes(indexes)
        return [get_letter_index(x, y) for y, x in indexes]
