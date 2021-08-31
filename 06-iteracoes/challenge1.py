import random

ramdom_number = random.randint(1, 5)
tries = 0
pick = 0

while pick != ramdom_number:
    tries +=1
    pick = input('Guess a number between 1 and 5')
    if pick.isnumeric() == False:
        continue
    pick = int(pick)

print(f'You guessed it in {tries} tries!')
