from random import randint 
tries = 0

print "Howdy, what's your name?", 
name = raw_input()

print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
print "Your guess?",
guess = int(raw_input())

answer = randint(1, 100)
tries = 1
