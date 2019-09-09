board = {}


class Board:
    
    def __init__(self):
        self.board = {}

        for i in range(12):
            self.board[i] = {'card': None, 'locked': None}

    def all_locked(self):
        for pos in self.board:
            if pos["locked"] == False:
                return False
        return True

    def __str__(self):
        return_string = ""
        for pos in self.board:
            return_string += f'{str(self.board[pos])}\n'
        return return_string

if __name__ == "__main__":
    board = Board()
    print(str(board))