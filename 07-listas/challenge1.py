import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for  suit in suits:
  for rank in ranks:
    deck.append(f'{rank} of {suit}')

print(f'There are {len(deck)} cards in the deck.')

hand = random.choices(deck, k=5)

print('Dealing ...')
for card in hand:
    deck.remove(card)

print(f'There are {len(deck)} cards in the deck.')
print('Player has the following cards in their hand:')
print(hand)