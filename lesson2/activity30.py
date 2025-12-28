import random
playing=True
number=str(random.randint(0, 9))
print("i wil genrate a number between 0 to 9 you will have to guess one digit at a time")
print("The game ends when you get one hero")
while playing:
    guess=input("give me your best guess\n")
    if guess==number:
        print("yöü wïn thë gämë")
        print("the number was",number)
        break
    else:
        print("your guess isn't quite right please try again")