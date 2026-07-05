class Card:
    """Определяет обычную игральную карту."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names_gen = ["треф", "бубен", "червей", "пик"]
    rank_names = [None, "Туз", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король"]

    def __str__(self):
        """
        >>> str(Card())
        '2 треф'
        """
        return f"{Card.rank_names[self.rank]} " f"{Card.suit_names_gen[self.suit]}"

    def __lt__(self, other: "Card") -> bool:
        """Проверка на 'меньше'. Сравнение идет сначала по масти, затем по рангу.
        >>> c1 = Card(1, 10)
        >>> c2 = Card(2, 10)
        >>> c3 = Card(1, 11)
        >>> c1 < c2
        True
        >>> c1 < c3
        True
        >>> c2 < c1
        False
        """
        return (self.suit, self.rank) < (other.suit, other.rank)

    def __le__(self, other: "Card") -> bool:
        """Проверка на 'меньше или равно'.
        >>> c1 = Card(1, 10)
        >>> c2 = Card(1, 10)
        >>> c3 = Card(2, 10)
        >>> c1 <= c2
        True
        >>> c1 <= c3
        True
        >>> c3 <= {c1}
        Traceback (most recent call last):
        TypeError: cannot use 'card.Card' as a set element (unhashable type: 'Card')
        """
        return (self.suit, self.rank) <= (other.suit, other.rank)

    def __eq__(self, other: "Card") -> bool:
        """Проверка на 'равно'.
        >>> c1 = Card(1, 10)
        >>> c2 = Card(1, 10)
        >>> c3 = Card(2, 10)
        >>> c1 == c2
        True
        >>> c1 == c3
        False
        """
        return (self.suit, self.rank) == (other.suit, other.rank)

    def __gt__(self, other: "Card") -> bool:
        """Проверка на 'больше'.
        >>> c1 = Card(2, 10)
        >>> c2 = Card(1, 10)
        >>> c1 > c2
        True
        >>> c2 > c1
        False
        """
        return (self.suit, self.rank) > (other.suit, other.rank)

    def __ge__(self, other: "Card") -> bool:
        """Проверка на 'больше или равно'.
        >>> c1 = Card(1, 10)
        >>> c2 = Card(1, 10)
        >>> c3 = Card(2, 10)
        >>> c1 >= c2
        True
        >>> c3 >= c1
        True
        """
        return (self.suit, self.rank) >= (other.suit, other.rank)
