from src.board import Board
from src.game import play_game

b = Board()
b.show([])
i = 0
color = True
while True:
    play_game(b, color)
    color = not color
