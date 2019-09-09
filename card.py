class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f'{self.suit} {self.rank}'
