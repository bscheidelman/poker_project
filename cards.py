import itertools, random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


suit_li = ["Diamond", "Heart", "Spade", "Club"]
deck = [Card(suit, value) for value in range(1, 14) for suit in suit_li]

def shuffle():
    random.shuffle(deck)

shuffle()

class Player:
    def __init__(self, card_one, card_two):
        self.card_one = card_one
        self.card_two = card_two


player_one = Player(deck[0], deck[1])
player_two = Player(deck[2], deck[3])

class Board:
    def __init__(self, flop_one, flop_two, flop_three, turn, river):
        self.flop_one = flop_one
        self.flop_two = flop_two
        self.flop_three = flop_three
        self.turn = turn
        self.river = river

board = Board(deck[4], deck[5], deck[6], deck[7], deck [8])

pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]

def best_hand(pool):
    ordered_pool = []
    for x in range(7):
        cur = pool[0]
        for card in pool:
            if card.value > cur.value:
                cur = card
        pool.remove(cur)
        ordered_pool.append(cur)

    for card in ordered_pool:
        print(card.value)


    #Check Straight Flush
    for x in range(3):
        for index in range(5):
            continue_gate = True
            if !(ordered_pool[x + index].value = ordered_pool[x + index + 1].value -1) or !(ordered_pool[x + index].suit = ordered_pool[x + index + 1].suit):
                continue_gate = False
                break
        if continue_gate:
            ret_pool = [ordered_pool[x], ordered_pool[x + 1], ordered_pool[x + 2], ordered_pool[x + 3], ordered_pool[x + 4]]
            return ret_pool
       

    #Check Four of a Kind

    #Check Full House

    #Check Flush

    #Check Straight

    #Check Three of a Kind

    #Check Two Pair

    #Check Pair

    #Check High Card

best_hand(pool)
