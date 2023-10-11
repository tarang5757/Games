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

lives = 6


word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
]
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append("_")
print(display)

guess = input("guess a letter: ").lower()

hangman = 0
while True:
    count = 0
    for position in range(word_length):
        letter = chosen_word[position]

        for element in chosen_word:
          if letter == guess:
            display[position] = letter
            count += 1

    print(display)    

    if count == 0:
      lives -= 1
      hangman += 1
      print(stages[hangman])
      
      

    if lives <= 0:
      break


    if ''.join(display) == chosen_word:
        break        
    guess = input("guess a letter").lower()
            
if lives == 0:
  print('You lost the game')
  print("the word was:", chosen_word)

else: 
  print("You got it!!! The word was:", chosen_word)