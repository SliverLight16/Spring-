import random

def guess(x):
    random_number = random.randint(-100,x)
    guess = -156
    while guess != random_number:
        guess = int(input(f'Guess a number betwen -100 {x}: '))
        print(guess)
        if guess < random_number:
            print('Sorry, too low')
        elif guess > random_number:
            print('Oops, too high')

    print(f'Congrats you have guessed the correct number: {random_number}')

guess(100)