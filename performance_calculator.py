from bases import Card, Player, Board, best_hand, check_winner
from equity_bot import equity_bot_preflop, equity_bot_flop, equity_bot_turn, equity_bot_river, random_bot
from intermediate_bot import intermediate_bot_flop, intermediate_bot_preflop, intermediate_bot_river, intermediate_bot_turn
import itertools, random

def play_hand(leads):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]
    random.shuffle(deck)

    player_one = Player(deck[0], deck[1])
    player_two = Player(deck[2], deck[3])
    c1 = deck[0]
    c2 = deck[1]
    c3 = deck[2]
    c4 = deck[3]

    print(c1.value, c1.suit, c2.value, c2.suit)
    print(c3.value, c3.suit, c4.value, c4.suit)

    cap = 100

    if leads % 2 == 0:
        player_one_bet = 1
        player_two_bet = 2

        p1_decision = equity_bot_preflop(c1,c2)
        while (player_one_bet != player_two_bet):
            print(player_one_bet, player_two_bet)

            if p1_decision >= 0:
                player_one_bet = player_two_bet + min(p1_decision, cap)
                print("Player one raises: ", min(p1_decision, cap))

            else:
                return -1 * player_one_bet

            p2_decision = intermediate_bot_preflop(c3,c4, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
            if p2_decision >= 0:
                player_two_bet = player_one_bet + min(p2_decision, cap) 
                print("Player two raises: ", min(p2_decision, cap))
            else:
                return player_two_bet

        board = Board(deck[4], deck[5], deck[6], deck[7], deck[8])
        print(board.flop_one.value,board.flop_two.value, board.flop_three.value, board.turn.value, board.river.value)
        #Flop
        p1_decision = equity_bot_flop(c1,c2, board.flop_one, board.flop_two, board.flop_three)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + min(p1_decision, cap)
            print("Player one raises: ", min(p1_decision, cap))
        p2_decision = intermediate_bot_flop(c3,c4,board.flop_one, board.flop_two, board.flop_three, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
        if p2_decision >= 0:
            player_two_bet = player_one_bet + min(p2_decision, cap) 
            print("Player two raises: ", min(p2_decision, cap))
        else:
            return player_two_bet

        while (player_one_bet != player_two_bet):
            print(player_one_bet, player_two_bet)
            if p1_decision > 0:
                player_one_bet = player_two_bet + min(p1_decision, cap)
                print("Player one raises: ", min(p1_decision, cap))
            elif p1_decision == 0:
                player_one_bet = player_two_bet
                print("Player one checks")
                break
            else:
                return -player_one_bet
            p2_decision = intermediate_bot_flop(c3,c4,board.flop_one, board.flop_two, board.flop_three, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
            if p2_decision >= 0:
                player_two_bet = player_one_bet + min(p2_decision, cap) 
                print("Player two raises: ", min(p2_decision, cap))
            else:
                return player_two_bet
        #Turn
        p1_decision = equity_bot_turn(c1,c2, board.flop_one, board.flop_two, board.flop_three, board.turn)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + min(p1_decision, cap)
            print("Player one raises: ", min(p1_decision, cap))
        p2_decision = intermediate_bot_turn(c3,c4,board.flop_one, board.flop_two, board.flop_three, board.turn, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
        if p2_decision >= 0:
            player_two_bet = player_one_bet + min(p2_decision, cap) 
            print("Player two raises: ", min(p2_decision, cap))
        else:
            return player_two_bet

        while (player_one_bet != player_two_bet):
            print(player_one_bet, player_two_bet)
            if p1_decision > 0:
                player_one_bet = player_two_bet + min(p1_decision, cap)
                print("Player one raises: ", min(p1_decision, cap))
            elif p1_decision == 0:
                player_one_bet == player_two_bet
                print("Player one checks")
                break
            else:
                return -player_one_bet
            p2_decision = intermediate_bot_turn(c3,c4,board.flop_one, board.flop_two, board.flop_three, board.turn, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
            if p2_decision >= 0:
                player_two_bet = player_one_bet + min(p2_decision, cap) 
                print("Player two raises: ", min(p2_decision, cap))
            else:
                return player_two_bet
       
        #River
        p1_decision = equity_bot_river(c1,c2, board.flop_one, board.flop_two, board.flop_three, board.turn, board.river)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + min(p1_decision, cap)
            print("Player one raises: ", min(p1_decision, cap))
        p2_decision = intermediate_bot_river(c3,c4,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
        if p2_decision >= 0:
            player_two_bet = player_one_bet + min(p2_decision, cap) 
            print("Player two raises: ", min(p2_decision, cap))
        else:
            return player_two_bet

        while (player_one_bet != player_two_bet):
            print(player_one_bet, player_two_bet)
            if p1_decision > 0:
                player_one_bet = player_two_bet + min(p1_decision, cap)
                print("Player one raises: ", min(p1_decision, cap))
            elif p1_decision == 0:
                player_one_bet = player_two_bet
                print("Player one checks")
                break
            else:
                return -1 * player_one_bet
            p2_decision = intermediate_bot_river(c3,c4,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
            if p2_decision >= 0:
                player_two_bet = player_one_bet + min(p2_decision, cap) 
                print("Player two raises: ", min(p2_decision, cap))

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
            p2_decision = intermediate_bot_preflop(c3,c4, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
            if p2_decision > 0:
                player_two_bet = player_one_bet + min(p2_decision, cap) 
                print("Player two raises: ", min(p2_decision, cap))
            elif p2_decision == 0:
                player_two_bet = player_two_bet
                break
            else:
                return player_two_bet
            if p1_decision >= 0:
                player_one_bet = player_two_bet + min(p1_decision, cap)
                print("Player one raises: ", min(p1_decision, cap))
            else:
                return -1 * player_one_bet



        board = Board(deck[4], deck[5], deck[6], deck[7], deck[8])
        print(board.flop_one.value,board.flop_two.value, board.flop_three.value, board.turn.value, board.river.value)

        #Flop
        p2_decision = intermediate_bot_flop(c3,c4,board.flop_one, board.flop_two, board.flop_three, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
        if p2_decision >= 0:
            player_two_bet = player_one_bet + min(p2_decision, cap) 
            print("Player two raises: ", min(p2_decision, cap))

        p1_decision = equity_bot_flop(c1,c2, board.flop_one, board.flop_two, board.flop_three)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + min(p1_decision, cap)
            print("Player one raises: ", min(p1_decision, cap))
        else:
            return -player_one_bet
        


        while (player_one_bet != player_two_bet):
            p2_decision = intermediate_bot_flop(c3,c4,board.flop_one, board.flop_two, board.flop_three, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
            if p2_decision > 0:
                player_two_bet = player_one_bet + min(p2_decision, cap) 
                print("Player two raises: ", min(p2_decision, cap))
            elif p2_decision == 0:
                player_two_bet = player_two_bet
                break
            else:
                return player_two_bet
            if p1_decision >= 0:
                player_one_bet = player_two_bet + min(p1_decision, cap)
                print("Player one raises: ", min(p1_decision, cap))
            else:
                return -player_one_bet

        #Turn
        p2_decision = intermediate_bot_turn(c3,c4,board.flop_one, board.flop_two, board.flop_three, board.turn, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
        if p2_decision >= 0:
            player_two_bet = player_one_bet + min(p2_decision, cap) 
            print("Player two raises: ", min(p2_decision, cap))

        p1_decision = equity_bot_turn(c1,c2, board.flop_one, board.flop_two, board.flop_three, board.turn)
        if p1_decision >= 0:
            player_one_bet = player_two_bet + min(p1_decision, cap)
        else:
            return -player_one_bet


        while (player_one_bet != player_two_bet):
            p2_decision = intermediate_bot_turn(c3,c4,board.flop_one, board.flop_two, board.flop_three, board.turn, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
            if p2_decision > 0:
                player_two_bet = player_one_bet + min(p2_decision, cap) 
                print("Player two raises: ", min(p2_decision, cap))
            elif p2_decision == 0:
                player_two_bet = player_two_bet
                break
            else:
                return player_two_bet
            if p1_decision >= 0:
                player_one_bet = player_two_bet + min(p1_decision, cap)
                print("Player one raises: ", min(p1_decision, cap))
            else:
                return -player_one_bet
       
        #River
        p1_decision = equity_bot_river(c1,c2, board.flop_one, board.flop_two, board.flop_three, board.turn, board.river)

        p2_decision = intermediate_bot_river(c3,c4,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
        if p2_decision >= 0:
            player_two_bet = player_one_bet + min(p2_decision, cap) 
            print("Player two raises: ", min(p2_decision, cap))
        if p1_decision >= 0:
            player_one_bet = player_two_bet + min(p1_decision, cap)
            print("Player one raises: ", min(p1_decision, cap))
        else:
            return -player_one_bet

        while (player_one_bet != player_two_bet):
            p2_decision = intermediate_bot_river(c3,c4,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_two_bet + player_one_bet, player_one_bet- player_two_bet)
            if p2_decision > 0:
                player_two_bet = player_one_bet + min(p2_decision, cap) 
                print("Player two raises: ", min(p2_decision, cap))

            elif p2_decision == 0:
                player_two_bet = player_two_bet
                break
            else:
                return player_two_bet
            if p1_decision >= 0:
                player_one_bet = player_two_bet + min(p1_decision, cap)
                print("Player one raises: ", min(p1_decision, cap))
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
    p1_stack = 200
    p2_stack = 200
    for x in range(num_hands):
        result = play_hand(x)
        print("Hand", x, "result:", result)
        total += result
        

    print("average return per hand:", total/num_hands)

hand_avg(100)
