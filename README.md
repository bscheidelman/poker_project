# Project Title: Heads-Up Poker AI

# Description:
This GitHub project is a comprehensive implementation of a Heads-Up Poker AI system, complete with three distinct AI bots, an equity calculator, and a performance evaluation tool. Whether you're looking to improve your poker game or explore the world of algorithmic decision making in gaming, this project has you covered.

# Key Components:

## Bots:

### Categorization Bot: 
This bot employs a categorization-based approach to evaluate poker hands and make decisions at different stages of the game (preflop, flop, turn, and river). It maintains a range of potential hands and adapts its strategy based on calculated equities and opponent actions. This bot currently beats the Intermediate Bot by an average of 4.78 BB per hand.
### Intermediate Bot: 
An intermediate-level poker bot that uses equity calculations to make decisions. It adjusts its strategy according to the current pot size, cost to call, and the strength of its hand.
## Simple Bot: 
A basic poker bot that follows a straightforward strategy. It evaluates its hand's equity and makes simple decisions based on predefined thresholds.
## Equity Calculator:
The equity calculator module provides functions for calculating the equity (winning probability) of a hand at different stages of the game (preflop, flop, turn, and river). It's a fundamental tool for the bots to make informed decisions.
## Performance Calculator:
The performance calculator tool allows you to evaluate how these poker bots perform against each other. It simulates poker games between the bots, records results, and provides insights into their relative strengths and weaknesses.
## Upcoming Features for Categorization Bot:
### Dynamic Bet Sizing: 
The bot will dynamically adjust its bet sizing based on the board texture. Expect larger bets on wet (highly coordinated) boards and smaller bets on dry (lowly coordinated) boards for improved strategic play.
### Range Adjustment: 
The bot will intelligently remove hands from its potential range that include cards in it's hand, enhancing its decision-making process by considering your opponent's possible holdings.
### Live Range Display: 
Get real-time insights into the predicted possibility of each hand in the bot's range. This feature will help you understand the bot's thought process and adapt your own strategy accordingly.
