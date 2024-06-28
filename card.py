class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property    # rank = property(rank)
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit

    def __str__(self):  #  str(obj)
        return f"{self.rank}-{self.suit}"    

    def __repr__(self):  # repr(obj)
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card("4", "Diamonds")
    print(f"{c1.rank = }")   # implicitly calls Card.rank(c1)
    print(f"{c1.suit = }")
    print(f"{str(c1) = }")
    print(f"{c1 = }")
    
    print(c1)
    print(f"{c1._rank = }")
    print(f"{Card.rank = }")
    