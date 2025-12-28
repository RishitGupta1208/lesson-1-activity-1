import random
while True:
    user_action=input("enter your choice(rock,paper,scissors,paper)")
    possible_action=["rock","paper","scissors"]
    computer_action=random.choice(possible_action)
    print(f"\n you chose {user_action} computer chose {computer_action}")
    if user_action==computer_action:
        print("you both chose the same,it's a tie")
    elif user_action=='rock':
        if computer_action=='scissors':
            print("rock smashes scissors,you win")
        else:
            print("paper cover rock like a black hole,you lose")
    elif user_action=='scissors':
        if computer_action=='paper':
            print("scissors cuts paper,you win")
        else:
            print("rock smashes sicissors,you lose")
    elif user_action=='paper':
        if computer_action=='rock':
            print("paper cover rock like a black hole,you win")
        else:
            print("scissors cuts paper,you lose")
    play_again=input("want to play again (y/n):")
    if play_again!='y':
        break