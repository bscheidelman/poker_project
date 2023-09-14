from bases import Card, Player, Board, best_hand, check_winner
import itertools, random



sample_size = 100
vs_sample = 100

def calculate_equity_preflop(c1, c2):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]

    random.shuffle(deck)

    num_tied = num_won = num_lost = 0
    

    player_one = Player(c1, c2)

    for card in deck:
        if (card.value == player_one.card_one.value and card.suit == player_one.card_one.suit):
            deck.remove(card)
        elif (card.value == player_one.card_two.value and card.suit == player_one.card_two.suit):
            deck.remove(card)

    for x in range(sample_size):

        nums = list(range(0, len(deck)))
        random.shuffle(nums)
        combination = []
        for x in range(7):
            combination.append(deck[nums[x]])


        player_two = Player(combination[5], combination[6])

        board = Board(combination[0],combination[1],combination[2],combination[3],combination[4])

        pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]
        pool_two = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two.card_one, player_two.card_two]

        result = check_winner(best_hand(pool), best_hand(pool_two))


        if result == 0:
            num_tied += 1
        elif result == 1:
            num_won += 1
        else:
            num_lost += 1


    total = num_won + num_lost + num_tied
    equity = num_won/total + 0.5 * num_tied/total
    return equity

def calculate_equity_preflop_vs(c1, c2, c3, c4):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]

    random.shuffle(deck)

    num_tied = num_won = num_lost = 0
    

    player_one = Player(c1, c2)
    player_two = Player(c3, c4)

    for card in deck:
        if (card.value == player_one.card_one.value and card.suit == player_one.card_one.suit):
            deck.remove(card)
        elif (card.value == player_one.card_two.value and card.suit == player_one.card_two.suit):
            deck.remove(card)
        elif (card.value == player_two.card_one.value and card.suit == player_two.card_one.suit):
            deck.remove(card)
        elif (card.value == player_two.card_two.value and card.suit == player_two.card_two.suit):
            deck.remove(card)

    for x in range(vs_sample):

        nums = list(range(0, len(deck)))
        random.shuffle(nums)
        combination = []
        for x in range(7):
            combination.append(deck[nums[x]])

        board = Board(combination[0],combination[1],combination[2],combination[3],combination[4])

        pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]
        pool_two = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two.card_one, player_two.card_two]

        result = check_winner(best_hand(pool), best_hand(pool_two))


        if result == 0:
            num_tied += 1
        elif result == 1:
            num_won += 1
        else:
            num_lost += 1


    total = num_won + num_lost + num_tied
    equity = num_won/total + 0.5 * num_tied/total
    return equity

def calculate_equity_flop(c1, c2, b1, b2, b3):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]

    random.shuffle(deck)

    num_tied = num_won = num_lost = 0
    

    player_one = Player(c1, c2)

    for card in deck:
        if (card.value == player_one.card_one.value and card.suit == player_one.card_one.suit):
            deck.remove(card)
        elif (card.value == player_one.card_two.value and card.suit == player_one.card_two.suit):
            deck.remove(card)
        elif(card.value == b1.value and card.suit == b1.suit):
            deck.remove(card)
        elif(card.value == b2.value and card.suit == b2.suit):
            deck.remove(card)
        elif(card.value == b3.value and card.suit == b3.suit):
            deck.remove(card)

  


    for x in range(sample_size):

        nums = list(range(0, len(deck)))
        random.shuffle(nums)
        combination = []
        for x in range(4):
            combination.append(deck[nums[x]])

        player_two = Player(combination[2], combination[3])

        board = Board(b1,b2,b3,combination[0],combination[1])

        pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]
        pool_two = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two.card_one, player_two.card_two]

        result = check_winner(best_hand(pool), best_hand(pool_two))


        if result == 0:
            num_tied += 1
        elif result == 1:
            num_won += 1
        else:
            num_lost += 1


    total = num_won + num_lost + num_tied
    equity = num_won/total + 0.5 * num_tied/total
    return equity

def calculate_equity_flop_vs(c1, c2, c3, c4, b1, b2, b3):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]

    random.shuffle(deck)

    num_tied = num_won = num_lost = 0
    

    player_one = Player(c1, c2)
    player_two = Player(c3, c4)

    for card in deck:
        if (card.value == player_one.card_one.value and card.suit == player_one.card_one.suit):
            deck.remove(card)
        elif (card.value == player_one.card_two.value and card.suit == player_one.card_two.suit):
            deck.remove(card)
        elif (card.value == player_two.card_one.value and card.suit == player_two.card_one.suit):
            deck.remove(card)
        elif (card.value == player_two.card_two.value and card.suit == player_two.card_two.suit):
            deck.remove(card)
        elif(card.value == b1.value and card.suit == b1.suit):
            deck.remove(card)
        elif(card.value == b2.value and card.suit == b2.suit):
            deck.remove(card)
        elif(card.value == b3.value and card.suit == b3.suit):
            deck.remove(card)

    for x in range(vs_sample):

        nums = list(range(0, len(deck)))
        random.shuffle(nums)
        combination = []
        for x in range(7):
            combination.append(deck[nums[x]])

        board = Board(b1,b2,b3,combination[0],combination[1])

        pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]
        pool_two = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two.card_one, player_two.card_two]

        result = check_winner(best_hand(pool), best_hand(pool_two))


        if result == 0:
            num_tied += 1
        elif result == 1:
            num_won += 1
        else:
            num_lost += 1


    total = num_won + num_lost + num_tied
    equity = num_won/total + 0.5 * num_tied/total
    return equity


def calculate_equity_turn(c1, c2, b1, b2, b3, b4):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]

    random.shuffle(deck)

    num_tied = num_won = num_lost = 0
    

    player_one = Player(c1, c2)

    for card in deck:
        if (card.value == player_one.card_one.value and card.suit == player_one.card_one.suit):
            deck.remove(card)
        elif (card.value == player_one.card_two.value and card.suit == player_one.card_two.suit):
            deck.remove(card)
        elif(card.value == b1.value and card.suit == b1.suit):
            deck.remove(card)
        elif(card.value == b2.value and card.suit == b2.suit):
            deck.remove(card)
        elif(card.value == b3.value and card.suit == b3.suit):
            deck.remove(card)
        elif(card.value == b4.value and card.suit == b4.suit):
            deck.remove(card)


    for x in range(sample_size):

        nums = list(range(0, len(deck)))
        random.shuffle(nums)
        combination = []
        for x in range(3):
            combination.append(deck[nums[x]])

        player_two = Player(combination[1], combination[2])

        board = Board(b1,b2,b3,b4,combination[0])

        pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]
        pool_two = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two.card_one, player_two.card_two]

        result = check_winner(best_hand(pool), best_hand(pool_two))


        if result == 0:
            num_tied += 1
        elif result == 1:
            num_won += 1
        else:
            num_lost += 1


    total = num_won + num_lost + num_tied
    equity = num_won/total + 0.5 * num_tied/total
    return equity


def calculate_equity_turn_vs(c1, c2, c3, c4, b1, b2, b3, b4):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]

    random.shuffle(deck)

    num_tied = num_won = num_lost = 0
    

    player_one = Player(c1, c2)
    player_two = Player(c3, c4)

    for card in deck:
        if (card.value == player_one.card_one.value and card.suit == player_one.card_one.suit):
            deck.remove(card)
        elif (card.value == player_one.card_two.value and card.suit == player_one.card_two.suit):
            deck.remove(card)
        elif (card.value == player_two.card_one.value and card.suit == player_two.card_one.suit):
            deck.remove(card)
        elif (card.value == player_two.card_two.value and card.suit == player_two.card_two.suit):
            deck.remove(card)
        elif(card.value == b1.value and card.suit == b1.suit):
            deck.remove(card)
        elif(card.value == b2.value and card.suit == b2.suit):
            deck.remove(card)
        elif(card.value == b3.value and card.suit == b3.suit):
            deck.remove(card)
        elif(card.value == b4.value and card.suit == b4.suit):
            deck.remove(card)

    for x in range(vs_sample):

        nums = list(range(0, len(deck)))
        random.shuffle(nums)
        combination = []
        for x in range(7):
            combination.append(deck[nums[x]])

        board = Board(b1,b2,b3,b4,combination[0])

        pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]
        pool_two = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two.card_one, player_two.card_two]

        result = check_winner(best_hand(pool), best_hand(pool_two))


        if result == 0:
            num_tied += 1
        elif result == 1:
            num_won += 1
        else:
            num_lost += 1


    total = num_won + num_lost + num_tied
    equity = num_won/total + 0.5 * num_tied/total
    return equity

def calculate_equity_river(c1, c2, b1, b2, b3, b4, b5):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]

    random.shuffle(deck)
    num_tied = num_won = num_lost = 0
    

    player_one = Player(c1, c2)

    for card in deck:
        if (card.value == player_one.card_one.value and card.suit == player_one.card_one.suit):
            deck.remove(card)
        elif (card.value == player_one.card_two.value and card.suit == player_one.card_two.suit):
            deck.remove(card)
        elif(card.value == b1.value and card.suit == b1.suit):
            deck.remove(card)
        elif(card.value == b2.value and card.suit == b2.suit):
            deck.remove(card)
        elif(card.value == b3.value and card.suit == b3.suit):
            deck.remove(card)
        elif(card.value == b4.value and card.suit == b4.suit):
            deck.remove(card)
        elif(card.value == b5.value and card.suit == b5.suit):
            deck.remove(card)

    for x in range(sample_size):

        nums = list(range(0, len(deck)))
        random.shuffle(nums)
        combination = []
        for x in range(2):
            combination.append(deck[nums[x]])

        player_two = Player(combination[0], combination[1])

        board = Board(b1,b2,b3,b4,b5)

        pool = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one.card_one, player_one.card_two]
        pool_two = [board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two.card_one, player_two.card_two]

        result = check_winner(best_hand(pool), best_hand(pool_two))

       

        if result == 0:
            num_tied += 1
        elif result == 1:
            num_won += 1
        else:
            num_lost += 1


    total = num_won + num_lost + num_tied
    equity = num_won/total + 0.5 * num_tied/total
    return equity
