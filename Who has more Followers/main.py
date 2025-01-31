import art
import game_data
import random

data=game_data.data
print(art.logo)
score=0
lose = False

selection_A=random.choice(data)
selection_B=random.choice(data)

def play(sel_A,sel_B):

    global score
    global lose
    print(f"Compare A: {sel_A['name']}, a {sel_A['description']}, from {sel_A['country']}.")
    print(art.vs)
    print(f"Compare B: {sel_B['name']}, a {sel_B['description']}, from {sel_B['country']}.")

    while not lose:

        choice=input("Who has more followers? Type 'A' or 'B': ")

        if choice=="A" and sel_A["follower_count"]>sel_B["follower_count"]:
            sel_A=sel_B
            sel_B=random.choice(data)
            score+=1
            print(f"You're right! Current score is: {score}")
            play(sel_A,sel_B)

        elif choice=="B" and sel_A["follower_count"]<sel_B["follower_count"]:
            sel_B=random.choice(data)
            score+=1
            print(f"You're right! Current score is: {score}")
            play(sel_A,sel_B)

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            lose=True


play(selection_A,selection_B)