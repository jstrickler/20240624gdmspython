import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    #  'this' same as 'self'

    def __init__(self):
        self._make_deck()
    
    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    def __str__(self):
        my_type = type(self)
        return f"{my_type.__name__}:{len(self._cards)}"

    def __repr__(self):
        my_type = type(self)
        return f"{my_type.__name__}()"

    @classmethod
    def get_ranks(cls): # passes in the CLASS object
        return cls.RANKS
    
if __name__ == "__main__":
    cd1 = CardDeck()
    print(f"{cd1 = }\n", cd1)
    cd1.shuffle()  #   CardDeck.shuffle(self)
    print(f"{cd1.cards = }\n")
    for _ in range(5):
        card = cd1.draw()
        print(f"{card = }", card)
    print()
    print(f"{cd1.get_ranks() = }")
    print(f"{CardDeck.get_ranks() = }")
        