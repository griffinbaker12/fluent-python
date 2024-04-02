from collections import namedtuple

# construct simple class to represent individual cards
# we use namedtuple to build classes of objects that are just bundles of attributes with no custom methods
Card = namedtuple("Card", ["rank", "suit"])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


# 2 of clubs is 0, and ace of spades is 51
def spades_high(card):
    return len(suit_values) * FrenchDeck.ranks.index(card.rank) + suit_values[card.suit]


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    # allows for FrenchDeck to be iterable
    # in now works as well because it is iterable
    def __getitem__(self, i):
        # delegates [] to self._cards
        return self._cards[i]
