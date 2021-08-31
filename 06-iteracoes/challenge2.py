import random

value = random.randint(1, 10)
tries = 0
guess = 0

print('Guess a number between 1 and 10')
while guess != value:
    tries +=1
    guess = input('Enter guess #' + str(tries) + ': ')
    if guess.isnumeric() == False:
        print('Numbers only, please!')
        continue
    guess = int(guess)

    if guess > value:
        print('Your guess is too high, try again!')
    else:
        print('Your guess is too low, try again!')

else:
    print(f'You guessed it in {tries} tries!')
