import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['morthos','erevan','miguel','wellby','amafrey','rowan','daisuke','kurai','kalista','sarkai','kayzwk','layla','tarthus','cariel']
game_ends = False
lives = 6
word = random.choice(word_list)

display = []
for letter in word:
    display += "_"
print(f"{' '.join(display)}")

while game_ends == False:
    guess = input('Diga uma letra\n').lower()

    for position in range (len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            game_ends = True
            print("You lose.")

    print(f"{' '.join(display)}")
    if "_" not in display:
            game_ends = True
            print("You win.")