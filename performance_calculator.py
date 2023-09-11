from bases import Card, Player, Board, best_hand, check_winner
from simple_bot import simple_bot_preflop, simple_bot_flop, simple_bot_turn, simple_bot_river, random_bot
from intermediate_bot import intermediate_bot_flop, intermediate_bot_preflop, intermediate_bot_river, intermediate_bot_turn
from categorization_bot import categorization_bot
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

    board = Board(deck[4], deck[5], deck[6], deck[7], deck[8])

    chips = 100
    small_blind = 0.5
    big_blind = 1
    player_one_bet = 0
    player_two_bet = 0

    if (leads % 2 == 0):
        player_one_bet = small_blind
        player_two_bet = big_blind
        run_once = True
        while player_one_bet != player_two_bet:
            p1_decison = simple_bot_preflop(player_one.card_one, player_one.card_two)
            if p1_decison > 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            elif p1_decison == 0:
                player_one_bet = player_two_bet
                if run_once == False:
                    break
            else:
                return -player_one_bet
            p2_decison = intermediate_bot_preflop(player_two.card_one, player_two.card_two, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison >= 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                print("Player Two raises by", p2_decison)
            else:
                return player_two_bet
            run_once = False


        print("Flop!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value)

        run_once = True
        while run_once == True or player_one_bet != player_two_bet:
            p1_decison = simple_bot_flop(player_one.card_one, player_one.card_two,board.flop_one, board.flop_two, board.flop_three)
            if p1_decison > 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            elif p1_decison == 0:
                player_one_bet = player_two_bet
                if run_once == False:
                    break
            else:
                return -player_one_bet
            p2_decison = intermediate_bot_flop(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three,player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison >= 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                print("Player Two raises by", p2_decison)
            else:
                return player_two_bet
            run_once = False


        print("Turn!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value, board.turn.value)

        run_once = True
        while run_once == True or player_one_bet != player_two_bet:
            p1_decison = simple_bot_turn(player_one.card_one, player_one.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn)
            if p1_decison > 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            elif p1_decison == 0:
                player_one_bet = player_two_bet
                if run_once == False:
                    break
            else:
                return -player_one_bet
            p2_decison = intermediate_bot_turn(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, board.turn, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison >= 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                print("Player Two raises by", p2_decison)
            else:
                return player_two_bet
            run_once = False

        print("River!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value, board.turn.value, board.river.value)

        run_once = True
        while run_once == True or player_one_bet != player_two_bet:
            p1_decison = simple_bot_river(player_one.card_one, player_one.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river)
            if p1_decison > 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            elif p1_decison == 0:
                player_one_bet = player_two_bet
                if run_once == False:
                    break
            else:
                return -player_one_bet
            p2_decison = intermediate_bot_river(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison >= 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                print("Player Two raises by", p2_decison)
            else:
                return player_two_bet
            run_once = False

        bh_1 = best_hand([player_one.card_one,player_one.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        bh_2 = best_hand([player_two.card_one,player_two.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        result = check_winner( bh_1, bh_2)

        if result == 1:
            return player_two_bet
        elif result == 2:
            return -1 * player_one_bet
        return 0
    else:
        player_one_bet = big_blind
        player_two_bet = small_blind
        run_once = True
        while player_one_bet != player_two_bet:
            p2_decison = intermediate_bot_preflop(player_two.card_one, player_two.card_two, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison > 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                print("Player Two raises by", p2_decison)
            elif p2_decison == 0:
                player_two_bet = player_one_bet
                if run_once == False:
                    break
            else:
                return player_two_bet
            p1_decison = simple_bot_preflop(player_one.card_one, player_one.card_two)
            if p1_decison >= 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            else:
                return -1 * player_one_bet
            run_once = False


        print("Flop!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value)

        run_once = True
        while run_once == True or player_one_bet != player_two_bet:
            p2_decison = intermediate_bot_flop(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison > 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                print("Player Two raises by", p2_decison)
            elif p2_decison == 0:
                player_two_bet = player_one_bet
                if run_once == False:
                    break
            else:
                return player_two_bet
            p1_decison = simple_bot_flop(player_one.card_one, player_one.card_two,board.flop_one, board.flop_two, board.flop_three)
            if p1_decison >= 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            else:
                return -1 * player_one_bet
            run_once = False

        print("Turn!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value, board.turn.value)

        run_once = True
        while run_once == True or player_one_bet != player_two_bet:
            p2_decison = intermediate_bot_turn(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, board.turn, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison > 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                print("Player Two raises by", p2_decison)
            elif p2_decison == 0:
                player_two_bet = player_one_bet
                if run_once == False:
                    break
            else:
                return player_two_bet
            p1_decison = simple_bot_turn(player_one.card_one, player_one.card_two , board.flop_one, board.flop_two, board.flop_three, board.turn)
            if p1_decison >= 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            else:
                return -1 * player_one_bet
            run_once = False


        print("River!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value, board.turn.value, board.river.value)

        run_once = True
        while run_once == True or player_one_bet != player_two_bet:
            p2_decison = intermediate_bot_river(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison > 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                print("Player Two raises by", p2_decison)
            elif p2_decison == 0:
                player_two_bet = player_one_bet
                if run_once == False:
                    break
            else:
                return player_two_bet
            p1_decison = simple_bot_river(player_one.card_one, player_one.card_two , board.flop_one, board.flop_two, board.flop_three, board.turn, board.river)
            if p1_decison >= 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            else:
                return -1 * player_one_bet
            run_once = False

        bh_1 = best_hand([player_one.card_one,player_one.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        bh_2 = best_hand([player_two.card_one,player_two.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        result = check_winner( bh_1, bh_2)

        if result == 1:
            return player_two_bet
        elif result == 2:
            return -1 * player_one_bet
        return 0




def play_hand_vs(leads):
    suit_li = ["Diamonds", "Hearts", "Spades", "Clubs"]
    deck = [Card(suit, value) for value in range(2, 15) for suit in suit_li]
    random.shuffle(deck)

    
    player_one = Player(deck[0], deck[1])
    player_two = Player(deck[2], deck[3])
    c1 = deck[0]
    c2 = deck[1]
    c3 = deck[2]
    c4 = deck[3]
    cat_bot = categorization_bot(player_one.card_one, player_one.card_two)
    cat_bot.make_range()

    print(c1.value, c1.suit, c2.value, c2.suit)
    print(c3.value, c3.suit, c4.value, c4.suit)

    board = Board(deck[4], deck[5], deck[6], deck[7], deck[8])

    chips = 100
    small_blind = 0.5
    big_blind = 1
    player_one_bet = 0
    player_two_bet = 0

    if (leads % 2 == 0):
        player_one_bet = small_blind
        player_two_bet = big_blind
        run_once = True
        cat_bot.pre_flop_rank_range()
        while player_one_bet != player_two_bet:
            p1_decison = cat_bot.decision_engine(player_two_bet -player_one_bet, player_two_bet + player_one_bet)
            if p1_decison > 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            elif p1_decison == 0:   
                player_one_bet = player_two_bet
                if run_once == False:
                    break
            else:
                return -player_one_bet
            p2_decison = intermediate_bot_preflop(player_two.card_one, player_two.card_two, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison >= 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                if p2_decison > 0:
                    cat_bot.update_action("Raise", p2_decison, player_one_bet + player_two_bet)
                elif p1_decison > 0:
                    cat_bot.update_action("Call", p1_decison, player_one_bet + player_two_bet)
                else:
                    cat_bot.update_action("Check", p1_decison, player_one_bet + player_two_bet)

                print("Player Two raises by", p2_decison)
            else:
                return player_two_bet
            run_once = False


        print("Flop!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value)
        cat_bot.update_board_flop(board.flop_one, board.flop_two, board.flop_three)

        run_once = True
        cat_bot.flop_rank_range()
        while run_once == True or player_one_bet != player_two_bet:
            p1_decison = cat_bot.decision_engine(player_two_bet -player_one_bet, player_two_bet + player_one_bet)
            if p1_decison > 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            elif p1_decison == 0:
                player_one_bet = player_two_bet
                if run_once == False:
                    break
            else:
                return -player_one_bet
            p2_decison = intermediate_bot_flop(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three,player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison >= 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                if p2_decison > 0:
                    cat_bot.update_action("Raise", p2_decison, player_one_bet + player_two_bet)
                elif p1_decison > 0:
                    cat_bot.update_action("Call", p1_decison, player_one_bet + player_two_bet)
                else:
                    cat_bot.update_action("Check", p1_decison, player_one_bet + player_two_bet)
                print("Player Two raises by", p2_decison)
            else:
                return player_two_bet
            run_once = False


        print("Turn!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value, board.turn.value)
        cat_bot.update_board_turn(board.turn)

        run_once = True
        cat_bot.turn_rank_range()
        while run_once == True or player_one_bet != player_two_bet:
            p1_decison = p1_decison = cat_bot.decision_engine(player_two_bet -player_one_bet, player_two_bet + player_one_bet)
            if p1_decison > 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            elif p1_decison == 0:
                player_one_bet = player_two_bet
                if run_once == False:
                    break
            else:
                return -player_one_bet
            p2_decison = intermediate_bot_turn(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, board.turn, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison >= 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                if p2_decison > 0:
                    cat_bot.update_action("Raise", p2_decison, player_one_bet + player_two_bet)
                elif p1_decison > 0:
                    cat_bot.update_action("Call", p1_decison, player_one_bet + player_two_bet)
                else:
                    cat_bot.update_action("Check", p1_decison, player_one_bet + player_two_bet)
                print("Player Two raises by", p2_decison)
            else:
                return player_two_bet
            run_once = False

        print("River!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value, board.turn.value, board.river.value)
        cat_bot.update_board_river(board.river)

        run_once = True
        cat_bot.river_rank_range()
        while run_once == True or player_one_bet != player_two_bet:
            p1_decison = p1_decison = cat_bot.decision_engine(player_two_bet -player_one_bet, player_two_bet + player_one_bet)
            if p1_decison > 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            elif p1_decison == 0:
                player_one_bet = player_two_bet
                if run_once == False:
                    break
            else:
                return -player_one_bet
            p2_decison = intermediate_bot_river(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison >= 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                if p2_decison > 0:
                    cat_bot.update_action("Raise", p2_decison, player_one_bet + player_two_bet)
                elif p1_decison > 0:
                    cat_bot.update_action("Call", p1_decison, player_one_bet + player_two_bet)
                else:
                    cat_bot.update_action("Check", p1_decison, player_one_bet + player_two_bet)
                print("Player Two raises by", p2_decison)
            else:
                return player_two_bet
            run_once = False

        bh_1 = best_hand([player_one.card_one,player_one.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        bh_2 = best_hand([player_two.card_one,player_two.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        result = check_winner( bh_1, bh_2)

        if result == 1:
            return player_two_bet
        elif result == 2:
            return -1 * player_one_bet
        return 0
    else:
        player_one_bet = big_blind
        player_two_bet = small_blind
        run_once = True
        cat_bot.pre_flop_rank_range()
        while player_one_bet != player_two_bet:
            p1_decison = 1
            p2_decison = intermediate_bot_preflop(player_two.card_one, player_two.card_two, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison > 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                if p2_decison > 0:
                    cat_bot.update_action("Raise", p2_decison, player_one_bet + player_two_bet)
                print("Player Two raises by", p2_decison)
            elif p2_decison == 0:
                player_two_bet = player_one_bet
                if p1_decison > 0:
                    cat_bot.update_action("Call", p1_decison, player_one_bet + player_two_bet)
                else:
                    cat_bot.update_action("Check", p1_decison, player_one_bet + player_two_bet)
                if run_once == False:
                    break
            else:
                return player_two_bet
            p1_decison = p1_decison = cat_bot.decision_engine(player_two_bet -player_one_bet, player_two_bet + player_one_bet)
            if p1_decison >= 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            else:
                return -1 * player_one_bet
            run_once = False


        print("Flop!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value)
        cat_bot.update_board_flop(board.flop_one, board.flop_two, board.flop_three)

        run_once = True
        cat_bot.flop_rank_range()
        while run_once == True or player_one_bet != player_two_bet:
            p1_decison = 0
            p2_decison = intermediate_bot_flop(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison > 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                if p2_decison > 0:
                    cat_bot.update_action("Raise", p2_decison, player_one_bet + player_two_bet)
                print("Player Two raises by", p2_decison)
            elif p2_decison == 0:
                player_two_bet = player_one_bet
                if p1_decison > 0:
                    cat_bot.update_action("Call", p1_decison, player_one_bet + player_two_bet)
                else:
                    cat_bot.update_action("Check", p1_decison, player_one_bet + player_two_bet)
                if run_once == False:
                    break
            else:
                return player_two_bet
            p1_decison = p1_decison = cat_bot.decision_engine(player_two_bet -player_one_bet, player_two_bet + player_one_bet)
            if p1_decison >= 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            else:
                return -1 * player_one_bet
            run_once = False

        print("Turn!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value, board.turn.value)
        cat_bot.update_board_turn(board.turn)

        run_once = True
        cat_bot.turn_rank_range()
        while run_once == True or player_one_bet != player_two_bet:
            p1_decison = 0
            p2_decison = intermediate_bot_turn(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, board.turn, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison > 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                if p2_decison > 0:
                    cat_bot.update_action("Raise", p2_decison, player_one_bet + player_two_bet)
                print("Player Two raises by", p2_decison)
            elif p2_decison == 0:
                player_two_bet = player_one_bet
                if p1_decison > 0:
                    cat_bot.update_action("Call", p1_decison, player_one_bet + player_two_bet)
                else:
                    cat_bot.update_action("Check", p1_decison, player_one_bet + player_two_bet)
                if run_once == False:
                    break
            else:
                return player_two_bet
            p1_decison = p1_decison = cat_bot.decision_engine(player_two_bet - player_one_bet, player_two_bet + player_one_bet)
            if p1_decison >= 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            else:
                return -1 * player_one_bet
            run_once = False


        print("River!")
        print(board.flop_one.value, board.flop_two.value, board.flop_three.value, board.turn.value, board.river.value)
        cat_bot.update_board_river(board.river)

        run_once = True
        cat_bot.river_rank_range()
        while run_once == True or player_one_bet != player_two_bet:
            p1_decison = 0
            p2_decison = intermediate_bot_river(player_two.card_one, player_two.card_two, board.flop_one, board.flop_two, board.flop_three, board.turn, board.river, player_one_bet + player_two_bet, player_one_bet - player_two_bet)
            if p2_decison > 0:
                player_two_bet = min(player_one_bet + p2_decison,chips)
                if p2_decison > 0:
                    cat_bot.update_action("Raise", p2_decison, player_one_bet + player_two_bet)
                print("Player Two raises by", p2_decison)
            elif p2_decison == 0:
                player_two_bet = player_one_bet
                if p1_decison > 0:
                    cat_bot.update_action("Call", p1_decison, player_one_bet + player_two_bet)
                else:
                    cat_bot.update_action("Check", p1_decison, player_one_bet + player_two_bet)
                if run_once == False:
                    break
            else:
                return player_two_bet
            p1_decison = p1_decison = cat_bot.decision_engine(player_two_bet -player_one_bet, player_two_bet + player_one_bet)
            if p1_decison >= 0:
                player_one_bet = min(player_two_bet + p1_decison,chips)
                print("Player One raises by", p1_decison)
            else:
                return -1 * player_one_bet
            run_once = False

        bh_1 = best_hand([player_one.card_one,player_one.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        bh_2 = best_hand([player_two.card_one,player_two.card_two,board.flop_one, board.flop_two, board.flop_three, board.turn, board.river])
        result = check_winner( bh_1, bh_2)

        if result == 1:
            return player_two_bet
        elif result == 2:
            return -1 * player_one_bet
        return 0


def hand_avg(num_hands):
    total = 0
    for x in range(num_hands):
        result = play_hand_vs(x)
        print("Hand", x, "result:", result)
        total += result
        print("average return per hand:", total/x)
