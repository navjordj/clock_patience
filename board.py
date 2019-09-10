board = {}


class Board:

    def __init__(self):
        self.board = {}

        for i in range(12):
            self.board[i] = {'card': None, 'locked': None}

    def add_card(self, card, pos) -> None:
        self.board[pos]['card'] = card
        self.board[pos]['locked'] = False

    def all_locked(self) -> bool:
        if self.num_locked() == 12:
            return True
        else:
            return False

    def num_locked(self) -> int:
        counter = 0
        for pos in self.board:
            if self.board[pos]["locked"] is True:
                counter += 1
        return counter

    def __str__(self) -> str:
        return_string = ""
        for pos in self.board:
            return_string += f'{self.board[pos]} \n'
        return return_string

if __name__ == "__main__":
    from card import Card

    board = Board()
    board.add_card(Card("club", 5), 4)
    print(str(board))
    print(board.board[4]['card'])
