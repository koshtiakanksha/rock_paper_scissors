rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

guess = input("What do you want to select, rock, paper or scissors\n ").lower()
if guess == "rock":
    print(rock)
elif guess == "paper":
    print(paper)
else:
    print(scissors)

computer = random.randint(1, 3)
if computer == 1:
    print(rock)
elif computer == 2:
    print(paper)
else:
    print(scissors)

if guess == "rock" and computer == 3:
    print("You win")
elif guess == "paper" and computer == 1:
    print("You win")
elif guess == "scissors" and computer == 2:
    print("You win")
elif guess == "rock" and computer == 1:
    print("It's a draw")
elif guess == "paper" and computer == 2:
    print("It's a draw")
elif guess == "scissors" and computer == 3:
    print("It's a draw")
else:
    print("You loose")

