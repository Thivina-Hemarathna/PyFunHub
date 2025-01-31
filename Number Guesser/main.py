import art
import random

VALUE=random.randint(1,100)
tries=0

def initial():
    print(art.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking about a number between 1 and 100.")

def play():
    global tries
    while tries!=0:
        print(f"You have {tries} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))

        if guess > VALUE:
            print("Too high.")
            print("Guess again.")
            tries-=1
            play()
        elif guess < VALUE:
            print("Too low.")
            print("Guess again.")
            tries -= 1
            play()
        else:
            print(f"You got it! The answer was {VALUE}")
            tries=0

initial()
difficulty= input("Choose a difficulty 'easy' or 'hard': ")

if difficulty=="easy":
    tries=10
else:
    tries=5
    
play()