"""
100 days of Python course
DAY 7
"""
# please ensure the art and words modules, supplied in this repository
# are in the same place where you run this one from
# they contain ASCII art and a word list and can be viewed in notepad

from replit import clear
import random
import words
import hangman_stages

# the word_list is from the imported module called hangman_words
chosen_word = random.choice(words.words)
word_len = len(chosen_word)

# the logo is in the imported module called hangman_art
print(hangman_stages.logo)

# this in range loop makes the underscores to show the blank "letters"
display = []  # empty list
for letter in range(word_len):
  display += "_"
print(display)  # prints dashes equal to number of letters

# boolean operation to see if game still in progress and a counter for lives
end_game = False  #when set to true loops end
lives = 0

# while loop keeps program active: it will stay active until boolean condition met
while not end_game:
  guess = input("Guess a letter: ").lower()

  clear() # Use the clear() function imported from replit to clear the output between guesses.

  if guess in display:
    print(f"You have already guess this letter {guess}")

  for position in range(word_len):
    letter = chosen_word[position]
    if letter in guess:
      display[position] = letter
  print(display)

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life!!")
    lives += 1
    if lives == 6:
      end_game = True
      print("you lose")

  if "_" not in display:
    end_game = True
    print("you win")

  print(hangman_stages.stages[lives])
