import random
word_list=["apple","papaya"] 
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
chosen_word=random.choice(word_list)
guess= input("Guess a letter").lower()
lives=6
placeholder=""
i=len(chosen_word)
display=""
correct_letters=[]

for position in range(1,i+1):
    placeholder+="_"
    
print(placeholder)
gameover=False
while not gameover:
   
 for letter in chosen_word:

    if (letter==guess):
     display+=letter
     correct_letters.append(letter)
    elif letter not in correct_letters:
      display+=letter
    else:
     display+="_"
 guess=""
print(display)
if guess not in chosen_word:
  lives-=1
  if lives==0:
    gameover=True
    print("you lose")

if "_" not in display:
  gameover=True
  print("you win")

print(HANGMANPICS[lives])  
   
  




