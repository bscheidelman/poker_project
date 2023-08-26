from equity_calculator import calculate_equity_preflop, calculate_equity_flop, calculate_equity_turn, calculate_equity_river
import itertools, random

def simple_bot_preflop(c1, c2):
    equity =  calculate_equity_preflop(c1, c2)
    if equity > 0.5:
        return 2.5
    elif equity >= 0.4:
        return 0
    else:
        return -1


def simple_bot_flop(c1, c2, b1, b2, b3):
    equity =  calculate_equity_flop(c1, c2, b1, b2, b3)
    if equity > 0.5:
        return 5
    elif equity >= 0.3:
        return 0
    else:
        return -1

    
def simple_bot_turn(c1, c2, b1, b2, b3, b4):
    equity =  calculate_equity_turn(c1, c2, b1, b2, b3, b4)
    if equity > 0.5:
        return 8
    elif equity >= 0.3:
        return 0
    else:
        return -1


def simple_bot_river(c1, c2, b1, b2, b3, b4, b5):
    equity =  calculate_equity_river(c1, c2, b1, b2, b3, b4, b5)
    if equity > 0.5:
        return 13
    elif equity >= 0.3:
        return 0
    else:
        return -1

def random_bot():
    choice = random.randrange(1,4)
    if choice == 1:
        return 2.5
    if choice == 2:
        return 0
    if choice == 3:
        return 5
