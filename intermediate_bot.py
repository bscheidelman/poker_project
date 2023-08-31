from equity_calculator import calculate_equity_preflop, calculate_equity_flop, calculate_equity_turn, calculate_equity_river
from bases import Card, Player, Board, best_hand, check_winner
import itertools, random


def calculate_pot_value(equity, pot_size, cost_size):
    if cost_size > 0:
        print("pot_value:",  ((pot_size + cost_size)/cost_size) * equity)
        return ((pot_size + cost_size)/cost_size) * equity
    return 999

def raise_function(equity):
    #Equity squared as opposed to just Equity is used as to avoid over better with weak hands as this signfigantly lowers the chance of it betting with low equity.
    raise_percent = 100 * (equity*equity)
    print("raise percentage:", raise_percent * 1.33)
    #random.randint(1,73) is used as to design it to almost always raise around aces preflop. ~0.85 is aces equity vs blind hand preflop. 0.85 * 0.85 = 0.7225.
    return raise_percent < random.randint(1,73)


def intermediate_bot_preflop(c1,c2, pot_size, cost_size):
    equity = calculate_equity_preflop(c1,c2)
    if calculate_pot_value(equity, pot_size, cost_size) < 1:
        return -1
    elif raise_function(equity):
        return 0
    return .5 * (cost_size + pot_size)


def intermediate_bot_flop(c1,c2, b1,b2,b3,pot_size, cost_size):
    equity = calculate_equity_flop(c1,c2,b1,b2,b3)
    if calculate_pot_value(equity, pot_size, cost_size) < 1:
        return -1
    elif raise_function(equity):
        return 0
    return .5 * (cost_size + pot_size)


def intermediate_bot_turn(c1,c2, b1,b2,b3,b4,pot_size, cost_size):
    equity = calculate_equity_turn(c1,c2,b1,b2,b3,b4)
    if calculate_pot_value(equity, pot_size, cost_size) < 1:
        return -1
    elif raise_function(equity):
        return 0
    return .5 * (cost_size + pot_size)

def intermediate_bot_river(c1,c2,b1,b2,b3,b4,b5, pot_size, cost_size):
    equity = calculate_equity_river(c1,c2,b1,b2,b3,b4,b5)
    if calculate_pot_value(equity, pot_size, cost_size) < 1:
        return -1
    elif raise_function(equity):
        return 0
    return .5 * (cost_size + pot_size)
