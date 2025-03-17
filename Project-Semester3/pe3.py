import random


random_number = random.randint(10, 20)


while True:
    guess = int(input("Guess the number (between 10 and 20): "))
    
    if guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Try again!")
