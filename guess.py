# this is a guess the number game.
import random

guessesTaken = 0

print('Hello! what is your name?')
myName = raw_input()

number = random.randint(1, 20)

print('well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')
    guess = raw_input()
    guess = int(guess)

    guessesTaken = guessesTaken +1
    print(" %i is guessestaken" % guessesTaken)


    if guess < number:
        print('your guess is too low.')

    if guess > number:
            print('your guess is too high.')

    if guess == number:
            break


if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' +myName + '! you guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number =str(number)
    print('Nope. The number I was thinking of was ' +number)
              
