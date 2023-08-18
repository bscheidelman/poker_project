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

#pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]

c1 = Card("Club", 7)
c2 = Card("Heart", 8)
c3 = Card("Diamond", 7)
c4 = Card("Club", 11)
c5 = Card("Club", 2)
c6 = Card("Spade", 7)
c7 = Card("Heart", 2)

pool = [c1, c2, c3, c4, c5, c6, c7]

def best_hand(pool):
    ordered_pool = []
    for x in range(len(pool)):
        cur = pool[0]
        for card in pool:
            if card.value > cur.value:
                cur = card
        pool.remove(cur)
        ordered_pool.append(cur)

    for card in ordered_pool:
        print(card.value)
    print("end of ordered pool")


    #Check Straight Flush
    for x in range(3):
        continue_gate = True
        for index in range(4):
            if (ordered_pool[x + index].value != ordered_pool[x + index + 1].value + 1) or (ordered_pool[x + index].suit != ordered_pool[x + index + 1].suit):
                continue_gate = False
                break
        if continue_gate:
            ret_pool = [ordered_pool[x], ordered_pool[x + 1], ordered_pool[x + 2], ordered_pool[x + 3], ordered_pool[x + 4]]
            #return ret_pool
       

    #Check Four of a Kind
    for x in range(4):
        count = 0
        cur = ordered_pool[x]
        for index in range(7 - x):
            if ordered_pool[x + index].value == cur.value:
                count += 1
        if count == 4:
            ret_pool = []
            gate = True
            for card in ordered_pool:
                if card.value != cur.value and gate:
                    ret_pool.append(card)
                    gate = False
                if card.value == cur.value:
                    ret_pool.append(card)
            #return ret_pool

    #Check Full House
    for x in range(5):
        count = 0
        cur = ordered_pool[x]
        for index in range(7-x):
            if ordered_pool[x + index].value == cur.value:
                count += 1
        if count == 3:
            old_cur = cur
            for x in range(6):
                count = 0
                cur = ordered_pool[x]
                if cur.value == old_cur.value:
                    continue
                for index in range(7-x):
                    if ordered_pool[x + index].value == cur.value:
                        count += 1
                if count >= 2:
                    ret_pool = []
                    gate = 2
                    for card in ordered_pool:
                        if card.value == old_cur.value:
                            ret_pool.append(card)
                        if card.value == cur.value and gate > 0:
                            ret_pool.append(card)
                            gate -= 1

    #Check Flush

    #Check Straight

    #Check Three of a Kind
    for x in range(5):
        count = 0
        cur = ordered_pool[x]
        for index in range(7-x):
            if ordered_pool[x + index].value == cur.value:
                count += 1
        if count == 3:
            ret_pool = []
            gate = 2
            for card in ordered_pool:
                if card.value != cur.value and gate > 0:
                    ret_pool.append(card)
                    gate -= 1
                if card.value == cur.value:
                    ret_pool.append(card)

    #Check Two Pair

    #Check Pair

    #Check High Card

best_hand(pool)
