import random

def number_guessing_game():
    print("      Welcome to Guess the Number    ")
   
    print("I am thinking of a number between 1 and 100.")
    print("Try to guess it!")
    print("only put numbers otherwise the code wont work")
    secret = random.randint(1, 100)
    attempts = 0
    guessed = False

    guesses = [] 

    while not guessed:
        guess = int(input("Enter your guess: "))
        attempts += 1
        guesses.append(guess)

        print("Your guesses so far:", guesses)

        if guess < secret:
            print("Too low, try again.")
        elif guess > secret:
            print("Too high, try again.")
        else:
            
            print("You got it!")
            print("The number was:", secret)
            print("Number of attempts:", attempts)
            print("Your guesses were:", guesses)
            print("Nice job!")
            guessed = True

number_guessing_game()
