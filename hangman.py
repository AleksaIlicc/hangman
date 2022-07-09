import random

clear = "\n" * 100
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
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
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
]
display = []
lives = 6
chosen_word = random.choice(word_list)
chosen_word_lenght = len(chosen_word)

for underscore in range(chosen_word_lenght):
    display.append('_')

end_of_game = len(display)

print(logo)


while(end_of_game > 0):
    end_of_game = 0
    guess = input("Guess a letter: ").lower()

    print(clear)

    if guess in display:
        print(f"You've already guessed a letter {guess}")

    lives_check = 0
    cntr = 0
    for letter in chosen_word:
        if letter == guess:
            display[cntr] = letter
            lives_check += 1
        cntr += 1

    print(f"{''.join(display)}") #_ _ _ _


    if lives_check == 0:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    print(stages[lives]) #art

    counter = 0
    for underscore in display:
        if display[counter] == "_":
            end_of_game += 1
        counter += 1
    if end_of_game == 0:
        print("You win!")
    if lives == 0:
        end_of_game = 0
        print("You lose. ")
