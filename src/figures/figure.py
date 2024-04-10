from colorama import Fore, Style

import src.board


class Figure(object):
    def __init__(self, letter: str, blue: bool = True):
        self.blue = blue
        self.__letter = letter

        if self.blue:
            self.__string = f'{Fore.BLUE}{self.__letter}{Style.RESET_ALL}'
        else:
            self.__string = f'{Fore.RED}{self.__letter}{Style.RESET_ALL}'

    def __str__(self):
        return self.__string

    @staticmethod
    def reshape_indexes(indexes: list[list[tuple[int, int]]]):
        # print(indexes[0], board.get_by_index(indexes[0][0], indexes[0][1]))
        answer = []
        for direction in indexes:
            for el in direction:
                answer.append(el)
        return answer

    def calculate_moves(self, y: int, x: int, board: 'src.board.Board') -> list[str]:
        pass

    def calculate_beat(self, y: int, x: int) -> list[tuple[int, int]]:
        pass

    def get_moves(self, direction: list[tuple[int, int]], board: 'src.board.Board') -> list[tuple[int, int]]:
        answer = []

        for new_y, new_x in direction:
            if 0 <= new_y <= 7 and 0 <= new_x <= 7:
                fig = board.get_by_index(new_y, new_x)
                if type(fig) != str:
                    if not fig.check_color(self.blue):
                        answer.append((new_y, new_x))
                    break
                answer.append((new_y, new_x))

        return answer

    def check_color(self, color: bool):
        return color == self.blue
