# Task 1: Hangman Game - Python Mini Project

import random
import hangmanstages

    
def Hangman():
    print("Welcome To Hangman Game\nGuess the Number between 1-100")
    
    while True:
        secret_no = random.randint(1, 100)
        lives = 6
        flag = True
        
        while flag:
            try:
                guess_no = int(input("Guess the Number: "))
            except ValueError:
                print("Enter a valid number")
                continue
    
            if guess_no == secret_no:
                print(guess_no, "You win!")
                play_again = input("Do you want to play again? y/n: ")
                if play_again.lower() == "y":
                    break 
                else:
                    flag = False
                    print("GAME OVER")
                    return
                    
            elif guess_no > secret_no:
                print("Too high!")
            else:
                print("Too low!")
                
            lives -= 1
            print(hangmanstages.stages[6 - lives])
            
            if lives == 0:
                print("YOU LOSE! The correct number was", secret_no)
                # Display the final stage
                print(hangmanstages.stages[6])
                play_again = input("Do you want to play again? y/n: ")
                if play_again.lower() == "y":
                    break 
    
                else:
                    flag = False
                    print("GAME OVER")
                    return

Hangman()
    