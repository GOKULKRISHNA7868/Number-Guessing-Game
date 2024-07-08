import random  # To generate a random number
import time  # To add pauses for better user experience

def intro():
    """Introduction function to ask for the player's name and explain the game."""
    print("May I ask you for your name?")
    name = input()  # asks for the name
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name  # returning the name to use later in the pick function

def pick(name, number):
    """Function to handle the guessing logic."""
    guessesTaken = 0  # Number of guesses the player has taken
    while guessesTaken < 6:  # Allow up to 6 guesses
        time.sleep(0.25)
        enter = input("Guess: ")  # prompts the user to enter their guess
        try:
            guess = int(enter)  # Convert the input to an integer

            if 1 <= guess <= 200:  # Check if the guess is in range
                guessesTaken += 1  # Increment the number of guesses taken
                if guess < number:
                    print("The guess of the number that you have entered is too low")
                elif guess > number:
                    print("The guess of the number that you have entered is too high")
                else:
                    break  # If the guess is correct, break out of the loop

                if guessesTaken < 6:
                    time.sleep(0.5)
                    print("Try Again!")
            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")

        except ValueError:
            print(f"I don't think that {enter} is a number. Sorry")

    if guess == number:
        print(f'Good job, {name}! You guessed my number in {guessesTaken} guesses!')
    else:
        print(f'Nope. The number I was thinking of was {number}')

def main():
    """Main function to control the flow of the game."""
    playagain = "yes"
    while playagain.lower() in ("yes", "y"):  # Allow the user to play again
        name = intro()  # Get the player's name
        number = random.randint(1, 200)  # Generate a random number between 1 and 200
        pick(name, number)  # Start the guessing game
        print("Do you want to play again?")
        playagain = input()

# Run the game
main()
