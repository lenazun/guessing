from random import randint 

bestScore = 100

def safenumber(x):
    try:
        x = int(x)
        return x
    except ValueError:
        return "Error!"   


def guessing():
    global bestScore
    print("I'm thinking of a number between 1 and 100. Try to guess my number.")

    number = randint(1, 100)

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
                if bestScore > guessCount:
                    print "That is a new record score!"
                    bestScore = guessCount
        
def main():
    global bestScore 
    bestScore = 100
    name = raw_input("Howdy, what's your name? > ")
    print("Hi %s!" % name)

    guessing()



    play_again = raw_input("Do you want to play again? Y or N >")
    
    if play_again == "Y" or play_again == "y":
        while play_again == "Y" or play_again == "y":
            guessing()
            play_again = raw_input("Do you want to play again? Y or N >")
    elif play_again == "N" or play_again =="n":
        print "OK, good bye"
    else:
        print "I don't understand"

main()

  
# g = ri() 
# try:
#   x = int(g)
# except ValueError:
#   kjkllkjlkj

# hfghgfhgfhfg