from random import randint 

name = raw_input("Howdy, what's your name? > ")

print("Hi %s, I'm thinking of a number between 1 and 100. Try to guess my number." % name)

number = randint(1, 100)

game = True

guessCount = 0

while game:
    try:
        guess = int(raw_input("Your guess? > "))
        if guess < 1 or guess > 100:
            print "That's out of range silly"
        else:
            guessCount += 1
            if guess > number:
                print("Your guess is too high, try again")
            elif guess < number:
                print("Your guess is too low, try again")
            else:
                game = False
                print "Good job! You found my guess in %i tries" % guessCount
    except ValueError:
        print "Oops!  You didn't enter a valid number."

