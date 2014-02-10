from random import randint 

def game():
    name = raw_input("Howdy, what's your name?") 
    print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name

    answer = randint(1, 100)

    guess = 0
    tries = 1

    while guess != answer:
        guess = int(raw_input('Your guess?'))
        if guess < answer:
            print "Your guess is too low, try again."
            tries += 1
        elif guess > answer:
            print "Your guess is too high, try again."
            tries += 1
        else: print "Well done, %s! You found my number in %d tries." % (name, tries)

game()