from equity_calculator import calculate_equity_preflop, calculate_equity_flop, calculate_equity_turn, calculate_equity_river
from bases import Card, Player, Board, best_hand, check_winner
import itertools, random


def calculate_pot_value(equity, pot_size, cost_size):
    if cost_size > 0:
        return (pot_size/cost_size) * equity
    return 999


def intermediate_bot_preflop(c1,c2, pot_size, cost_size):
    equity = calculate_equity_preflop(c1,c2)
    if calculate_pot_value(equity, pot_size, cost_size) < 1:
        return -1
    elif 100 * equity < random.randint(1,101):
        return 0
    return .5 * (cost_size + pot_size)


def intermediate_bot_flop(c1,c2, b1,b2,b3,pot_size, cost_size):
    equity = calculate_equity_flop(c1,c2,b1,b2,b3)
    if calculate_pot_value(equity, pot_size, cost_size) < 1:
        return -1
    elif 100 * equity < random.randint(1,101):
        return 0
    return .5 * (cost_size + pot_size)


def intermediate_bot_turn(c1,c2, b1,b2,b3,b4,pot_size, cost_size):
    equity = calculate_equity_turn(c1,c2,b1,b2,b3,b4)
    if calculate_pot_value(equity, pot_size, cost_size) < 1:
        return -1
    elif 100 * equity < random.randint(1,101):
        return 0
    return .5 * (cost_size + pot_size)

def intermediate_bot_river(c1,c2,b1,b2,b3,b4,b5, pot_size, cost_size):
    equity = calculate_equity_river(c1,c2,b1,b2,b3,b4,b5)
    if calculate_pot_value(equity, pot_size, cost_size) < 1:
        return -1
    elif 100 * equity < random.randint(1,101):
        return 0
    return .5 * (cost_size + pot_size)