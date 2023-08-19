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
c2 = Card("Heart", 9)
c3 = Card("Club", 5)
c4 = Card("Club", 3)
c5 = Card("Club", 1)
c6 = Card("Spade", 2)
c7 = Card("Spade", 10)

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


    non_duplicate_pool = [ordered_pool[0]]
    for x in range(len(ordered_pool)):
        continue_gate = True
        for card in non_duplicate_pool:
            if card.value == ordered_pool[x].value:
                continue_gate = False
                break
        if continue_gate:
            non_duplicate_pool.append(ordered_pool[x])





    #Check Straight Flush
    if len(non_duplicate_pool) >= 5:
        for x in range(len(non_duplicate_pool) - 4):
            continue_gate = True
            for index in range(4):
                if (non_duplicate_pool[x + index].value != non_duplicate_pool[x + index + 1].value + 1) or (non_duplicate_pool[x + index].suit != non_duplicate_pool[x + index + 1].suit):
                    continue_gate = False
                    break
            if continue_gate:
                ret_pool = [non_duplicate_pool[x], non_duplicate_pool[x + 1], non_duplicate_pool[x + 2], non_duplicate_pool[x + 3], non_duplicate_pool[x + 4]]
                #return ret_pool
                break
       

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
            break

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
            break

    #Check Flush
    for x in range(3):
        count = 0
        cur = ordered_pool[x]
        for index in range(7-x):
            if ordered_pool[x + index].suit == cur.suit:
                count += 1
        if count >= 5:
            ret_pool = []
            count = 0
            for card in ordered_pool:
                if card.suit == cur.suit and count < 5:
                    count += 1
                    ret_pool.append(card)
            break

    #Check Straight
    if len(non_duplicate_pool) >= 5:
        for x in range(len(non_duplicate_pool) - 4):
            continue_gate = True
            for index in range(4):
                if (non_duplicate_pool[x + index].value != non_duplicate_pool[x + index + 1].value + 1):
                    continue_gate = False
                    break
            if continue_gate:
                ret_pool = []
                for index in range(x, x + 5):
                    ret_pool.append(non_duplicate_pool[index])
                break

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
            break

    #Check Two Pair
    for x in range(4):
        count = 0
        cur = ordered_pool[x]
        for index in range(7-x):
            if ordered_pool[x + index].value == cur.value:
                count += 1
        if count == 2:
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
                    gate = True
                    for card in ordered_pool:
                        if card.value == old_cur.value or card.value == cur.value:
                            ret_pool.append(card)
                            continue
                        if gate:
                            ret_pool.append(card)
                            gate = False
                    break

    #Check Pair
    for x in range(6):
        count = 0
        cur = ordered_pool[x]
        for index in range(7-x):
            if ordered_pool[x + index].value == cur.value:
                count += 1
        if count == 2:
            ret_pool = []
            gate = 3
            for card in ordered_pool:
                if card.value == cur.value:
                    ret_pool.append(card)
                elif gate > 0:
                    ret_pool.append(card)
                    gate -= 1
            break


    #Check High Card
    ret_pool = []
    for x in range(5):
        ret_pool.append(ordered_pool[x])

best_hand(pool)
