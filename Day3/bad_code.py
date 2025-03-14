import numpy as np
import random

random.seed(42)
options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

cards = [f'{'rank':options}, of {'suit':suits}' for options in options for suits in suits]

random.shuffle(all)
handout = {f'{i+1}': [] for i in range(4)}


for _ in range(5):
    for player in handout:
        card = all.pop()
        handout[player].append(card)


for player, hand in handout.items():
    print(f"{player}'s hand: {hand}") 