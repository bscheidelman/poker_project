import itertools, random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]

def shuffle():
    random.shuffle(deck)

shuffle()

class Player:
    def __init__(self, card_one, card_two):
        self.card_one = card_one
        self.card_two = card_two


#player_one = Player(deck[0], deck[1])
#player_two = Player(deck[2], deck[3])

class Board:
    def __init__(self, flop_one, flop_two, flop_three, turn, river):
        self.flop_one = flop_one
        self.flop_two = flop_two
        self.flop_three = flop_three
        self.turn = turn
        self.river = river

#board = Board(deck[4], deck[5], deck[6], deck[7], deck [8])


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
                if (non_duplicate_pool[x + index].suit != non_duplicate_pool[x + index + 1].suit):
                    continue_gate = False
                    break
                elif (non_duplicate_pool[x + index].value != non_duplicate_pool[x + index + 1].value + 1):
                    if (non_duplicate_pool[x + index].value != 2 or non_duplicate_pool[0].value != 14):
                        continue_gate = False
                        break
            if continue_gate:
                ret_pool = [non_duplicate_pool[x], non_duplicate_pool[x + 1], non_duplicate_pool[x + 2], non_duplicate_pool[x + 3], non_duplicate_pool[x + 4]]
                return (8, ret_pool)

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
                    add_last = card
                    gate = False
                if card.value == cur.value:
                    ret_pool.append(card)
            ret_pool.append(add_last)
            return (7, ret_pool)

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
                    for card in ordered_pool:
                        if card.value == cur.value and gate > 0:
                            ret_pool.append(card)
                            gate -= 1
                    return (6, ret_pool)

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
            return (5, ret_pool)

    #Check Straight
    if len(non_duplicate_pool) >= 5:
        for x in range(len(non_duplicate_pool) - 4):
            continue_gate = True
            for index in range(4):
                if (non_duplicate_pool[x + index].value != non_duplicate_pool[x + index + 1].value + 1):
                    if (non_duplicate_pool[x + index].value != 2 or non_duplicate_pool[0].value != 14):
                        continue_gate = False
                        break
            if continue_gate:
                ret_pool = []
                for index in range(x, x + 5):
                    ret_pool.append(non_duplicate_pool[index])
                return (4, ret_pool)

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
                if card.value == cur.value:
                    ret_pool.append(card)
            for card in ordered_pool:
                if card.value != cur.value and gate > 0:
                    ret_pool.append(card)
                    gate -= 1
            return (3, ret_pool)

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
                    for card in ordered_pool:
                        if card.value == old_cur.value or card.value == cur.value:
                            ret_pool.append(card)
                            continue
                    for card in ordered_pool:
                        if card.value != old_cur.value and card.value != cur.value:
                            ret_pool.append(card)
                            break
                    return (2, ret_pool)

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
            for card in ordered_pool:
                if gate > 0 and card.value != cur.value:
                    ret_pool.append(card)
                    gate -= 1
            return (1, ret_pool)


    #Check High Card
    ret_pool = []
    for x in range(5):
        ret_pool.append(ordered_pool[x])
    return (0, ret_pool)

def check_winner(hand_one, hand_two):
    # 1 == hand_one is better, 2 == hand_two is better, 0 == tie
    if hand_one[0] > hand_two[0]:
        return 1
    elif hand_one[0] < hand_two[0]:
        return 2
    else:
        if hand_one[0] == 8:
            for x in range(5):
                if hand_one[1][x].value >  hand_two[1][x].value:
                    return 1
                elif hand_one[1][x].value <  hand_two[1][x].value:
                    return 2
            return 0
        elif hand_one[0] == 7:
            if hand_one[1][0].value > hand_two[1][0].value:
                return 1
            elif hand_one[1][0].value < hand_two[1][0].value:
                return 2
            elif hand_one[1][4].value > hand_two[1][4].value:
                return 1
            elif hand_one[1][4].value < hand_two[1][4].value:
                return 2
            else:
                return 0
        elif hand_one[0] == 6:
            if hand_one[1][0].value > hand_two[1][0].value:
                return 1
            elif hand_one[1][0].value < hand_two[1][0].value:
                return 2
            elif hand_one[1][4].value > hand_two[1][4].value:
                return 1
            elif hand_one[1][4].value < hand_two[1][4].value:
                return 2
            else:
                return 0
        elif hand_one[0] == 5:
            for x in range(5):
                if hand_one[1][x].value >  hand_two[1][x].value:
                    return 1
                elif hand_one[1][x].value <  hand_two[1][x].value:
                    return 2
            return 0
        elif hand_one[0] == 4:
            if hand_one[1][0].value > hand_two[1][0].value:
                return 1
            if hand_one[1][0].value < hand_two[1][0].value:
                return 2
            return 0
        elif hand_one[0] == 3:
            if hand_one[1][0].value > hand_two[1][0].value:
                return 1
            if hand_one[1][0].value < hand_two[1][0].value:
                return 2
            for x in range(3,5):
                if hand_one[1][x].value >  hand_two[1][x].value:
                    return 1
                elif hand_one[1][x].value <  hand_two[1][x].value:
                    return 2
            return 0
        elif hand_one[0] == 2:
            if hand_one[1][0].value > hand_two[1][0].value:
                return 1
            if hand_one[1][0].value < hand_two[1][0].value:
                return 2
            if hand_one[1][2].value > hand_two[1][2].value:
                return 1
            if hand_one[1][2].value < hand_two[1][2].value:
                return 2
            if hand_one[1][4].value > hand_two[1][4].value:
                return 1
            if hand_one[1][4].value < hand_two[1][4].value:
                return 2
            return 0
        elif hand_one[0] == 1:
            if hand_one[1][0].value > hand_two[1][0].value:
                return 1
            if hand_one[1][0].value < hand_two[1][0].value:
                return 2
            for x in range(2,5):
                if hand_one[1][x].value > hand_two[1][x].value:
                    return 1
                if hand_one[1][x].value < hand_two[1][x].value:
                    return 2
            return 0
        else:
            for x in range(5):
                if hand_one[1][x].value > hand_two[1][x].value:
                    return 1
                if hand_one[1][x].value < hand_two[1][x].value:
                    return 2
            return 0





def calculate_equity(c1, c2):
    num_tied = num_won = num_lost = 0
    

    player_one = Player(c1, c2)

    for card in deck:
        if (card.value == player_one.card_one.value and card.suit == player_one.card_one.suit):
            deck.remove(card)
        elif (card.value == player_one.card_two.value and card.suit == player_one.card_two.suit):
            deck.remove(card)

    print(len(deck))

    count = 0

    for combination in itertools.combinations(deck, 7):

        player_two = Player(combination[5], combination[6])

        board = Board(combination[0],combination[1],combination[2],combination[3],combination[4])

        pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]
        pool_two = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two.card_one, player_two.card_two]

        result = check_winner(best_hand(pool), best_hand(pool_two))

        print(result)

        if result == 0:
            num_tied += 1
        elif result == 1:
            num_won += 1
        else:
            num_lost += 1

        count += 1

        if count >= 500000:
            break


    total = num_won + num_lost + num_tied
    print("Num Wom:", 100*num_won/total, "%")
    print("Num Lost:", 100*num_lost/total, "%")
    print("Num Tied:", 100*num_tied/total, "%")
    print(total)

c1 = Card("Hearts", 10)
c2 = Card("Hearts", 11)

calculate_equity(c1, c2)
