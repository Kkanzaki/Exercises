import random

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

game = [rock,paper,scissors]
op = random.choice(game)
player = int(input("Type 0 for rock, 1 for paper or 2 for Scissors"))

if player == 0:
  print(rock)
elif player == 1:
  print(paper)
else:
  print(scissors)

print('Computer choose')
print(op)

if player == 0 and op == rock:
  print("It\'s a draw")
elif player == 1 and op == paper:
  print("It\'s a draw")
elif player == 2 and op == scissors:
  print("It\'s a draw")
elif player == 0 and op == scissors:
  print('You win!!!')
elif player == 1 and op == rock:
  print('You win!!!')
elif player == 2 and op == paper:
  print('You win!!!')
elif player == 0 and op == paper:
  print("You lose")
elif player == 1 and op == scissors:
  print("You lose")
elif player == 2 and op == rock:
  print("You lose")
