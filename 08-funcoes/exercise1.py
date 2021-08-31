# def say_hello(name = 'World', gretting = None):
#     if gretting == None:
#         print(f'Hello {name}!')
#     else:
#         print(f'{gretting} {name}!')

# say_hello()
# say_hello('Python')
# say_hello(gretting='HIII')
# say_hello('Python', 'Howdy')

# print(type(None))

# def add_two_numbers(x, y):
#     return x + y

# add_two_numbers(4, 6)
# result = add_two_numbers(5, 7)
# print(result)

def create_deck():
  suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
  deck = []

  for  suit in suits:
    for rank in ranks:
      deck.append(f'{rank} of {suit}')

  return deck

my_deck = create_deck()
print(len(my_deck))