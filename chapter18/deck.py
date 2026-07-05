import random
from card import Card


class Deck:
    """Определяет игральную колоду."""

    def __init__(self):
        self.cards: list[Card] = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, target: Deck, num: int):
        """Переносит карты в target"""
        for i in range(num):
            target.add_card(self.pop_card())

    def deal_hands(self, player_count: int, num: int):
        """Принимает два параметра: количество игроков и количество карт для каждого.
        Создает соответствующее количество объектов Hand, сдает соответствующее количество
        карт на одну руку и возвращает список объектов Hand.
        >>> deck = Deck()
        >>> hands = deck.deal_hands(2, 2)
        >>> len(hands)
        2
        >>> hands[0].label
        'player 1'
        >>> hands[1].label
        'player 2'
        >>> len(hands[0].cards)
        2
        >>> len(hands[1].cards)
        2
        """
        hands_list = []
        for i in range(player_count):
            hand = Hand(label=f"player {i + 1}")
            self.move_cards(hand, num)
            hands_list.append(hand)
        return hands_list


class Hand(Deck):
    """Определяет игральные карты в руке."""

    def __init__(self, label=""):  # Ругается почему-то, подчеркивая желтым
        self.cards = []
        self.label = label
