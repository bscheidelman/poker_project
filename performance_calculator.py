from bases import Card, Player, Board, best_hand, check_winner
from equity_bot import equity_bot_preflop, equity_bot_flop, equity_bot_turn, equity_bot_river, random_bot
import itertools, random

def play_hand(leads):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]
    random.shuffle(deck)

    player_one = Player(deck[0], deck[1])
    player_two = Player(deck[2], deck[3])
    c1 = deck[0]
    c2 = deck[1]


    if leads % 2 == 0:
        player_one_bet = 1
        player_two_bet = 2

        p1_decision = equity_bot_preflop(c1,c2)
        while (player_one_bet != player_two_bet):

            if p1_decision >= 0:
                player_one_bet = player_two_bet + p1_decision

            else:
                return -1 * player_one_bet

            p2_decision = random_bot()
            if p2_decision >= 0:
                player_two_bet = player_one_bet + p2_decision
            else:
                return player_two_bet

        board = Board(deck[4], deck[5], deck[6], deck[7], deck[8])

        #Flop
        p1_decision = equity_bot_flop(c1,c2, board.flop_one, board.flop_two, board.flop_three)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + p1_decision
        p2_decision = random_bot()
        if p2_decision >= 0:
            player_two_bet = player_one_bet + p2_decision
        else:
            return player_two_bet

        while (player_one_bet != player_two_bet):
            if p1_decision > 0:
                player_one_bet = player_two_bet + p1_decision
            elif p1_decision == 0:
                player_one_bet = player_two_bet
                break
            else:
                return -player_one_bet
            p2_decision = random_bot()
            if p2_decision >= 0:
                player_two_bet = player_one_bet + p2_decision
            else:
                return player_two_bet
        #Turn
        p1_decision = equity_bot_turn(c1,c2, board.flop_one, board.flop_two, board.flop_three, board.turn)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + p1_decision
        p2_decision = random_bot()
        if p2_decision >= 0:
            player_two_bet = player_one_bet + p2_decision
        else:
            return player_two_bet

        while (player_one_bet != player_two_bet):
            if p1_decision > 0:
                player_one_bet = player_two_bet + p1_decision
            elif p1_decision == 0:
                player_one_bet == player_two_bet
                break
            else:
                return -player_one_bet
            p2_decision = random_bot()
            if p2_decision >= 0:
                player_two_bet = player_one_bet + p2_decision
            else:
                return player_two_bet
       
        #River
        p1_decision = equity_bot_river(c1,c2, board.flop_one, board.flop_two, board.flop_three, board.turn, board.river)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + p1_decision
        p2_decision = random_bot()
        if p2_decision >= 0:
            player_two_bet = player_one_bet + p2_decision
        else:
            return player_two_bet

        while (player_one_bet != player_two_bet):
            if p1_decision > 0:
                player_one_bet = player_two_bet + p1_decision
            elif p1_decision == 0:
                player_one_bet = player_two_bet
                break
            else:
                return -1 * player_one_bet
            p2_decision = random_bot()
            if p2_decision >= 0:
                player_two_bet = player_one_bet + p2_decision
            else:
                return player_two_bet

        bh_1 = best_hand([player_one.card_one,player_one.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        bh_2 = best_hand([player_two.card_one,player_two.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        result = check_winner( bh_1, bh_2)
        if result == 1:
            return player_two_bet
        elif result == 2:
            return -1 * player_one_bet
        else:
            return 0

    else:
        player_one_bet = 2
        player_two_bet = 1

        p1_decision = equity_bot_preflop(c1,c2)
        while (player_one_bet != player_two_bet):
            p2_decision = random_bot()
            if p2_decision > 0:
                player_two_bet = player_one_bet + p2_decision
            elif p2_decision == 0:
                player_two_bet = player_two_bet
                break
            else:
                return player_two_bet
            if p1_decision >= 0:
                player_one_bet = player_two_bet + p1_decision
            else:
                return -1 * player_one_bet



        board = Board(deck[4], deck[5], deck[6], deck[7], deck[8])

        #Flop
        p2_decision = random_bot()
        if p2_decision >= 0:
            player_two_bet = player_one_bet + p2_decision

        p1_decision = equity_bot_flop(c1,c2, board.flop_one, board.flop_two, board.flop_three)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + p1_decision
        else:
            return -player_one_bet
        


        while (player_one_bet != player_two_bet):
            p2_decision = random_bot()
            if p2_decision > 0:
                player_two_bet = player_one_bet + p2_decision
            elif p2_decision == 0:
                player_two_bet = player_two_bet
                break
            else:
                return player_two_bet
            if p1_decision >= 0:
                player_one_bet = player_two_bet + p1_decision
            else:
                return -player_one_bet

        #Turn
        p2_decision = random_bot()
        if p2_decision >= 0:
            player_two_bet = player_one_bet + p2_decision

        p1_decision = equity_bot_turn(c1,c2, board.flop_one, board.flop_two, board.flop_three, board.turn)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + p1_decision
        else:
            return -player_one_bet


        while (player_one_bet != player_two_bet):
            p2_decision = random_bot()
            if p2_decision > 0:
                player_two_bet = player_one_bet + p2_decision
            elif p2_decision == 0:
                player_two_bet = player_two_bet
                break
            else:
                return player_two_bet
            if p1_decision >= 0:
                player_one_bet = player_two_bet + p1_decision
            else:
                return -player_one_bet
       
        #River
        p1_decision = equity_bot_river(c1,c2, board.flop_one, board.flop_two, board.flop_three, board.turn, board.river)

        p2_decision = random_bot()
        if p2_decision >= 0:
            player_two_bet = player_one_bet + p2_decision
        if p1_decision >= 0:
            player_one_bet = player_two_bet + p1_decision
        else:
            return -player_one_bet

        while (player_one_bet != player_two_bet):
            p2_decision = random_bot()
            if p2_decision > 0:
                player_two_bet = player_one_bet + p2_decision
            elif p2_decision == 0:
                player_two_bet = player_two_bet
                break
            else:
                return player_two_bet
            if p1_decision >= 0:
                player_one_bet = player_two_bet + p1_decision
            else:
                return -1 * player_one_bet


        bh_1 = best_hand([player_one.card_one,player_one.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        bh_2 = best_hand([player_two.card_one,player_two.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        result = check_winner( bh_1, bh_2)

        if result == 1:
            return player_two_bet
        elif result == 2:
            return -1 * player_one_bet
        else:
            return 0





       

def hand_avg(num_hands):
    total = 0
    for x in range(num_hands):
        total += play_hand(x)
        print("Hand", x, "result:", total)
        

    print("average return per hand:", total/num_hands)

hand_avg(15)
