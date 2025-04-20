# imports
from random import randint
from sys import exit

# generate a random number
computer_guess = randint(1,100)
chances = 0
print(computer_guess)

  # welcome message with rules
print("\n----- Welcome to the Number Guessing Game -----")
print("="*55)
print("\nI'm thinking of a number between 1 and 100")
print("You have multiple chances to guess the correct number.")


while True:
    
    # difficulty levels
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    # ask user to select difficulty
    try:
        difficulty = int(input("\nEnter your choice (1,2,3) : "))


        # check if user gives correct difficulty
        if difficulty == 1 or difficulty == 2 or difficulty == 3:

            # print message on based of user difficulty
            if difficulty == 1:
                print("Great you selected Easy difficulty.")
                chances = 10
            elif difficulty == 2:    
                print("Great you selected Medium difficulty.")
                chances = 5
            else:
                print("Great you selected Hard difficulty.")
                chances = 3

            # a loop that checks if user guess is under 100 and over 0                
            while True:

                # take user guess in try block to catch invalid value type
                try:    
                    # check if user has chances remaing
                    if chances > 0:

                    # ask the user to guess the number and convert it to an int
                        user_guess = int(input("Enter your guess: "))

                        # check if guess is between 1 and 100 
                        if user_guess >= 1 and user_guess <= 100:
                        
                            # now compare user guess with computer guess
                            if user_guess > computer_guess:
                                print("Incorrect! Number is less then" ,user_guess)                               
                                # reduce 1 chance on every wrong guess
                                chances -= 1
                            elif user_guess < computer_guess:
                                print("Incorrect! Number is greater then" ,user_guess)    
                                # reduce 1 chance on every wrong guess
                                chances -= 1

                            # if user guess matched with computer guess break the loop                            
                            else:
                                print("Correct! You won")
                                exit()
                        else:
                            print("Select a number between 1 to 100")
                    else:
                        print("No chances left")
                        break
                    
                # if user give invalid vlaue e.g str this except block will run        
                except ValueError:
                    print("invalid input")
                    print("Select a number between 1 to 100")

        # tell input is wrong and run loop again
        else:
            print("\nInvalid difficulty choice!")
            print("Choose between 1,2, or 3")
            
    except ValueError:
        print("\nInvalid value")
        print("Choose between 1,2, or 3")
        