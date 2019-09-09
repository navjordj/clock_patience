from card import Card

import random

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
        random.shuffle(self.deck)

    def draw(self) -> Card:
        """Draw random card from deck."""
        random.shuffle(self.deck) #Unødvendig

        return self.deck.pop() 

    def __str__(self) -> str:
        return_string = ""
        for card in self.deck:
            return_string += str(card) + ' '
        return return_string

    def __len__(self) -> int:
        return len(self.deck)