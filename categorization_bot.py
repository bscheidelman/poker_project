from equity_calculator import calculate_equity_preflop, calculate_equity_flop, calculate_equity_turn, calculate_equity_river, calculate_equity_preflop_vs, calculate_equity_flop_vs, calculate_equity_turn_vs
import itertools, random
from bases import Card, Player, Board, best_hand, check_winner


class categorization_bot:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
        self.potential_range = {}


    def update_board_flop(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        for hand in list(self.potential_range):
            if (hand[0].value == self.b1.value and hand[0].suit == self.b1.suit) or (hand[0].value == self.b2.value and hand[0].suit == self.b2.suit) or (hand[0].value == self.b3.value and hand[0].suit == self.b3.suit) or (hand[1].value == self.b1.value and hand[1].suit == self.b1.suit) or (hand[1].value == self.b2.value and hand[1].suit == self.b2.suit) or (hand[1].value == self.b3.value and hand[1].suit == self.b3.suit):
                del self.potential_range[hand]


    def update_board_turn(self, b4):
        self.b4 = b4
        for hand in list(self.potential_range):
            if (hand[0].value == self.b4.value and hand[0].suit == self.b4.suit) or (hand[1].value == self.b4.value and hand[1].suit == self.b4.suit):
                del self.potential_range[hand]

    def update_board_river(self, b5):
        self.b5 = b5
        for hand in list(self.potential_range):
            if (hand[0].value == self.b5.value and hand[0].suit == self.b5.suit) or (hand[1].value == self.b5.value and hand[1].suit == self.b5.suit):
                del self.potential_range[hand]

    def pre_flop_rank_range(self):
        for hand in self.potential_range:
            self.potential_range[hand][1] = calculate_equity_preflop_vs(self.c1, self.c2, hand[0], hand[1])

    def flop_rank_range(self): 
        for hand in self.potential_range:
            self.potential_range[hand][1] = calculate_equity_flop_vs(self.c1, self.c2, hand[0], hand[1], self.b1, self.b2, self.b3)

    def turn_rank_range(self):
        for hand in self.potential_range:
            self.potential_range[hand][1] = calculate_equity_turn_vs(self.c1, self.c2, hand[0], hand[1], self.b1, self.b2, self.b3, self.b4)

    def river_rank_range(self):
        for hand in self.potential_range:
            p1_pool = [self.c1, self.c2, self.b1, self.b2, self.b3, self.b4, self.b5]
            p2_pool = [hand[0], hand[1], self.b1, self.b2, self.b3, self.b4, self.b5]
            result = check_winner(best_hand(p1_pool), best_hand(p2_pool))
            if result == 1:
                self.potential_range[hand][1] = 1
            elif result == 2:
                self.potential_range[hand][1] = 0
            else:
                self.potential_range[hand][1] = 0.5

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
        self.pre_flop_rank_range()

    def update_action(self, action, raise_amount, pot_size):
        if action == "Raise":
            for hand in self.potential_range:
                self.potential_range[hand][0] = self.potential_range[hand][0] * (1 - self.potential_range[hand][1]) * (1 + (raise_amount/pot_size))
        elif action == "Check":
            for hand in self.potential_range:
                self.potential_range[hand][0] = self.potential_range[hand][0] * self.potential_range[hand][1]
        elif action == "Call":
            for hand in self.potential_range:
                self.potential_range[hand][0] = self.potential_range[hand][0] * (1 - self.potential_range[hand][1]) * (1 + (raise_amount/pot_size))


    def calculate_pot_value(self, equity, pot_size, cost_size):
        if cost_size > 0:
            return ((pot_size + cost_size)/cost_size) * equity
        return 999

    def decision_engine(self, raise_amount, pot_size):
        if raise_amount > 0:
            total = count = 0
            for hand in self.potential_range:
                count += self.potential_range[hand][0]
                total += self.potential_range[hand][0] * self.calculate_pot_value(self.potential_range[hand][1], pot_size, raise_amount)

            if total/count < 1:
                return -1
            pot_size = pot_size + raise_amount


        total = count = 0
        for hand in self.potential_range:
            total += self.potential_range[hand][0] * self.potential_range[hand][1]
            count += self.potential_range[hand][0]

        avg_equity = total/count
        raise_percent = 100 * (avg_equity*avg_equity)

        if raise_percent < random.randint(1,73):
            return .5 * pot_size
        return 0
