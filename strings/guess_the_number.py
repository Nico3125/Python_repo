# Guess the number game:
import random

if input("would you like to play a game?Type y for yes, n for no ") == 'y':
    play_game= True
while play_game==True:

    print("Welcome to the guess a number game!\n I'm thinking of a number between 1 and 100")
    dificulty = input("Choose a dificulty, type 'easy' or 'hard'")
    if dificulty == 'hard':
        attempts = 5
        print(f"you have {attempts} attempts remaining to guess the number")
    elif dificulty == 'easy':
        attempts = 10
        print(f' Your have {attempts} attempts remaining to guess the number.')
    else:
        print("Invalid input")
    number_to_be_guessed = random.randint(1, 100)
    print(f"pssst, the number is..{number_to_be_guessed}.")

    while attempts > 0:
        # print("Guess again")
        guess = int(input("Make a guess: "))
        if guess>100 and guess <1:
            print("This is not what I thought of..try a number between 1 and 100!")
        elif guess > number_to_be_guessed:
            print("Too high")
            print("Guess again")
            attempts -= 1
            print(f'You have {attempts} attempts left!')
        elif guess < number_to_be_guessed:
            print("Too low")
            print("Guess again")
            attempts -= 1
            print(f'You have {attempts} attempts left!')
        elif guess == number_to_be_guessed:
            attempts=0
            play_game = False
            print("YOu guessed!")

    if attempts == 0:
        print("Game Over")
        play_game = False
    play_again=input("would you like to play again? y or n ")
    if play_again:
        play_game= True
