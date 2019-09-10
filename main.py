from deck import Deck
from board import Board

num_success = 0
n = 100

for i in range(n):
    is_finished = False

    board = Board()
    deck = Deck()

    while not is_finished:
        for clock_pos in range(12):
            if len(deck) > 0:
                if board.board[clock_pos]['locked'] != True:
                    drawn_card = deck.draw()
                    board.add_card(drawn_card, clock_pos)

                    #print(board.board[clock_pos]['card'].rank, clock_pos)

                    if board.board[clock_pos]['card'].rank == clock_pos:
                        board.board[clock_pos]['locked'] = True
                        #print(f'Låser {clock_pos}')
            else:
                is_finished = True
                break
    if board.all_locked() == True:
        num_success += 1

print(f'{num_success} av {n}')
