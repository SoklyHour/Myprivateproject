import random
def hange_man():  

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

 word_list = ["ardvark", "baboon", "camel"]
 chosen_word = random.choice(word_list)
 word_length = len(chosen_word)

 print(f'Pssst, the solution is {chosen_word}.')
# uncomment this to see the chosen word ༼ つ ◕_◕ ༽つ

 display = []
 for _ in range(word_length):
    display += "_"

 end_of_game = False
 fault = 0
 while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in chosen_word: 
        fault +=1               
        print(stages[-fault])

    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You win.")
        break
    
    if fault == len(stages):
        print("You lose.")
        break

game_on = True
while game_on:
     hange_man()
     q1 = input("rematch? n/y: ")
     if q1 == "n":
        game_on= False
     elif q1=="y":
        game_on = True
