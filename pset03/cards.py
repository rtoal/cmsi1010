from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]


def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])


def deal(number_of_hands, cards_per_hand):
    # Return a list of sets, each containing the cards for one hand.
    # You must validate the input parameters according to the test
    # cases that you will find in cards_test.py. Make sure to remove
    # this comment and the pass statement below before submitting.
    if not isinstance(number_of_hands, int):
        raise TypeError("hands must be an int")
    if not isinstance(cards_per_hand, int):
        raise TypeError("cards per hand must be an int")
    if number_of_hands < 1:
        raise ValueError("Need a positive number of hands")
    if cards_per_hand < 1:
        raise ValueError("Need a positive number of cards per hand")
    if number_of_hands * cards_per_hand > 52:
        raise ValueError("I don't have that many cards")

    deck = shuffled_deck()
    result = []
    for hand in range(number_of_hands):
        result.append(set(deck[:cards_per_hand]))
        deck = deck[cards_per_hand:]
    return result


def poker_classification(hand):
    # Returns a string describing the poker hand. First, validate the input
    # to make sure it is a set of 5 cards, and raise the appropriate error
    # (TypeError or ValueError) if necessary.
    #
    # Then return one of the following strings:
    # "High Card", "One Pair", "Two Pair", "Three of a Kind",
    # "Straight", "Flush", "Full House", "Four of a Kind",
    # "Straight Flush", "Royal Flush"
    #
    # Make sure to remove this comment and the pass statement below
    # before submitting.
    if not isinstance(hand, set):
        raise TypeError("hand must be a set")
    if len(hand) != 5:
        raise ValueError("hand must contain exactly 5 cards")
    if not all(isinstance(card, Card) for card in hand):
        raise TypeError("all elements of hand must be Card instances")

    ranks = [card.rank for card in hand]
    suits = [card.suit for card in hand]
    rank_counts = {rank: ranks.count(rank) for rank in set(ranks)}
    is_flush = len(set(suits)) == 1
    is_straight = (sorted(ranks) == list(
        range(min(ranks), min(ranks) + 5))) or set(ranks) == {1, 10, 11, 12, 13}

    if is_straight and is_flush:
        if set(ranks) == {10, 11, 12, 13, 1}:
            return "Royal Flush"
        return "Straight Flush"
    if 4 in rank_counts.values():
        return "Four of a Kind"
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if 3 in rank_counts.values():
        return "Three of a Kind"
    if list(rank_counts.values()).count(2) == 2:
        return "Two Pair"
    if 2 in rank_counts.values():
        return "One Pair"
    return "High Card"
