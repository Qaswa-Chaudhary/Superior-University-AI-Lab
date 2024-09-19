# Task 2: FizzBuzz Game - Python OOP Mini Project

class FizzBuzz:
    def __init__(self):
        print("~~~ Welcome to the FIZZBUZZ Game! ~~~")
    
    def number(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return num  # Return the number if it's neither divisible by 3 nor 5
        
game = FizzBuzz()

while True:
    player = input("Enter a number to play FizzBuzz or type 'exit' to quit: ")
    if player.lower() == "exit":
        print("Thanks for playing FizzBuzz!")
        break
    else:
        try:
            player = int(player)
            result = game.number(player)
            print(result)
        except ValueError:
            print("Invalid input, please enter a valid number or 'exit' to quit.")

