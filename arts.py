import random

end_of_game = False

word_list = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = []

for _in in range(word_length):
    display += "_"
while not_end_of_game:
    guess = input("Guess a letter:").lower()
    if guess in display:
        print(f"You have already guessed{guess}")

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
if guess not in chosen_word:
    print(f"You guessed{guess} , that is not in the word . You loosed a life .")
    lives -= 1
    if lives == 0:
        not_end_of_game = True
        print("You Loose")
print(f"{''.join(display)}")
if "_" not in display:
    not_end_of_game = true
    print("You Win")
