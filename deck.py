from card import Card

class Deck:

    def __init__(self):
        clubs = []
        diamonds = []
        hearts = []
        spades = []

        for i in range(13):
            clubs.append(Card("club", i))
            diamonds.append(Card("dimaond", i))
            hearts.append(Card("heart", i))
            spades.append(Card("spade", i))

        self.deck = clubs + diamonds + hearts + spades

    def __str__(self):
        return_string = ""
        for card in self.deck:
            return_string += str(card) + ' '
        return return_string

    def __len__(self):
        return len(self.deck)