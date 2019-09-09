from deck import Deck
from board import Board

is_finished = False

special_values = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

board = Board()
deck = Deck()

center = None

board = []

while not is_finished:
    for clock in range(0, 12):
        drawn_card = deck.draw()
        board.append()
