import src.board
from .figure import Figure
from ..services import get_letter_index


class Rook(Figure):
    def __init__(self, color: bool = True):
        super().__init__('R', color)

    def calculate_moves(self, y: int, x: int, board: 'src.board.Board') -> list[str]:
        indexes = [
            self.get_moves([(y - i, x) for i in range(1, 8)], board),
            self.get_moves([(y + i, x) for i in range(1, 8)], board),
            self.get_moves([(y, x - i) for i in range(1, 8)], board),
            self.get_moves([(y, x + i) for i in range(1, 8)], board)
        ]

        answer = self.reshape_indexes(indexes)
        return [get_letter_index(x, y) for y, x in answer]
