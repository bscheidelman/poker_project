from equity_calculator import calculate_equity_preflop, calculate_equity_flop, calculate_equity_turn, calculate_equity_river, calculate_equity_preflop_vs
from bases import Card, Player, Board, best_hand, check_winner
import itertools, random

#IN PROGRESS

class categorization_bot:
    def __init__(self, c1, c2, p1_bet, p2_bet):
        self.c1 = c1
        self.c2 = c2
        self.p1_bet = p1_bet
        self.p2_bet = p2_bet
        self.potential_range = {}

    def pre_flop_rank_range(self):
        for hand in self.potential_range:
            self.potential_range[hand][1] = calculate_equity_preflop_vs(self.c1, self.c2, hand[0], hand[1])

    def make_range(self):
        for x in range(2,15):
            for y in range(2,15):
                if x != y:
                    card_one_spades = Card( "Spades", x)
                    card_one_hearts = Card( "Hearts", x)
                    card_one_clubs = Card( "Clubs", x)
                    card_one_diamonds = Card( "Diamonds", x)
                    card_two_spades = Card("Spades", y)
                    card_two_hearts = Card( "Hearts", y)
                    card_two_clubs = Card( "Clubs", y)
                    card_two_diamonds = Card( "Diamonds", y)
                    self.potential_range[card_one_spades, card_two_spades] = [1, .5]
                    self.potential_range[card_one_spades, card_two_hearts] = [1, .5]
                    self.potential_range[card_one_spades, card_two_clubs] = [1, .5]
                    self.potential_range[card_one_spades, card_two_diamonds] = [1, .5]
                    self.potential_range[card_one_clubs, card_two_spades] = [1, .5]
                    self.potential_range[card_one_clubs, card_two_hearts] = [1, .5]
                    self.potential_range[card_one_clubs, card_two_clubs] = [1, .5]
                    self.potential_range[card_one_clubs, card_two_diamonds] = [1, .5]
                    self.potential_range[card_one_hearts, card_two_spades] = [1, .5]
                    self.potential_range[card_one_hearts, card_two_hearts] = [1, .5]
                    self.potential_range[card_one_hearts, card_two_clubs] = [1, .5]
                    self.potential_range[card_one_hearts, card_two_diamonds] = [1, .5]
                    self.potential_range[card_one_diamonds, card_two_spades] = [1, .5]
                    self.potential_range[card_one_diamonds, card_two_hearts] = [1, .5]
                    self.potential_range[card_one_diamonds, card_two_clubs] = [1, .5]
                    self.potential_range[card_one_diamonds, card_two_diamonds] = [1, .5]
                else:
                    card_one_spades = Card( "Spades", x)
                    card_one_hearts = Card( "Hearts", x)
                    card_one_clubs = Card( "Clubs", x)
                    card_one_diamonds = Card( "Diamonds", x)
                    self.potential_range[card_one_spades, card_one_hearts] = [1, .5]
                    self.potential_range[card_one_spades, card_one_clubs] = [1, .5]
                    self.potential_range[card_one_spades, card_one_diamonds] = [1, .5]
                    self.potential_range[card_one_clubs, card_one_hearts] = [1, .5]
                    self.potential_range[card_one_clubs, card_one_diamonds] = [1, .5]
                    self.potential_range[card_one_diamonds, card_one_hearts] = [1, .5]




    def pre_flop_action(self, action, raise_amount, pot_size):
        if action == "Raise":
            for hand in self.potential_range:
                self.potential_range[hand][0] = self.potential_range[hand][0] * (1 - self.potential_range[hand][1]) * (1 + (raise_amount/pot_size))
        elif action == "Check":
            for hand in self.potential_range:
                self.potential_range[hand][0] = self.potential_range[hand][0] * self.potential_range[hand][1]
        elif action == "Call":
            for hand in self.potential_range:
                self.potential_range[hand][0] = self.potential_range[hand][0] * (1 - self.potential_range[hand][1]) * (1 + (raise_amount/pot_size))


    def calculate_pot_value(equity, pot_size, cost_size):
        if cost_size > 0:
            print("pot_value:",  ((pot_size + cost_size)/cost_size) * equity)
            return ((pot_size + cost_size)/cost_size) * equity
        return 999

    def pre_flop_decision(self, action, raise_amount, pot_size):
        self.p1_bet = self.p1_bet + raise_amount
        pre_flop_action(action, raise_amount, self.p1_bet + self.p1_bet)

        if action == "Raise":
            total = count = 0
            for hand in self.potential_range:
                count += self.potential_range[hand][0]
                total += self.potential_range[hand][0] * calculate_pot_value(self.potential_range[hand][1], pot_size, raise_amount)

            if total/count < 1:
                return -1
            pot_size = pot_size + raise_amount


        total = count = 0
        for hand in self.potential_range:
            total += self.potential_range[0] * self.potential_range[1]
            count += self.potential_range[0]

        avg_equity = total/count
        raise_percent = 100 * (avg_equity*avg_equity)

        if raise_percent < random.randint(1,73):
            return .5 * pot_size
        return 0
