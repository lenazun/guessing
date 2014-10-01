from random import randint 

def getScore():
    """ Gets the best score stored in a text file """
    file = open('bestScore.txt', 'r')
    bestScore = file.read()
    file.close()
    return bestScore

def setScore(newScore, name):
    """ Writes the new best score and name to a file once the game is over """
    file = open('bestScore.txt', 'w')
    file.write(str(newScore) + " guesses, by ")
    file.write(name)
    file.close()

def safenumber(x):
    """Validates that the number entered is an integer"""
    try:
        x = int(x)
        return x
    except ValueError:
        return "Error!"   

def guessing(name):
    """Sets a random number and asks the user to guess, giving feedback"""
    
    print("I'm thinking of a number between 1 and 100. Try to guess my number.")

    number = randint(1, 100)
    #print number

    game = True

    guessCount = 0

    while game:
        
        guess = safenumber(raw_input("Your guess? > "))

        if guess == "Error!":
            print "Oops that's not a valid entry."
        elif guess < 1 or guess > 100:
            print "That's out of range silly"
        else:
            guessCount += 1
            if guess > number:
                print("Your guess is too high, try again")
            elif guess < number:
                print("Your guess is too low, try again")
            else:
                game = False
                print "Good job! You found my guess in %i tries." % guessCount
                if getScore() > guessCount:
                    print "That is a new record score!"
                    setScore(guessCount, name) 
        

def main():
    """Greets the user, gets the name, once it runs the game asks if user wants to play again"""

    print "The current record is: " + getScore()

    name = raw_input("Howdy, what's your name? > ")
    print("Hi %s!" % name)

    guessing(name)

    play_again = raw_input("Do you want to play again? Y or N >")
    
    if play_again == "Y" or play_again == "y":
        while play_again == "Y" or play_again == "y":
            guessing(name)
            play_again = raw_input("Do you want to play again? Y or N >")
    elif play_again == "N" or play_again =="n":
        print "OK, good bye"
    else:
        print "I don't understand"


main()

