import random

word_list = ['lion', 'elephant', 'zebra', 'dog', 'cat', 'mouse', 'rabbit']
answer_word = random.choice(word_list).lower()

hidden_word = "_ " * len(answer_word)
hidden_word = hidden_word.strip()

number_of_failed_attempts = 6
incorrect_letters = []
correct_letters = []
hangman_pics = {
    1: '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    2: '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    3: '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    4: '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
    5: '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
    6: '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========='''}

while True:
    print('=======================================')
    print(f'Hidden word is {hidden_word}')

    picked_letter = input('Guess a letter: ').lower()

    if len(picked_letter) != 1 or not picked_letter.isalpha():
        print('Please enter a single letter.')
        continue

    if picked_letter in correct_letters or picked_letter in incorrect_letters:
        print('You already tried that letter, pick another one.')
        continue

    index_count = 0
    for i in answer_word:
        if i == picked_letter:
            hidden_word = (
                hidden_word[:index_count] +
                picked_letter +
                hidden_word[index_count + 1:])
        index_count += 2

    if hidden_word.count('_') == 0:
        print(answer_word)
        print('Congratulations, you win!')
        break

    if picked_letter in answer_word:
        correct_letters.append(picked_letter)
        print(f'Correct! The word contains the letter {picked_letter}!')
    else:
        incorrect_letters.append(picked_letter)
        print('Wrong!')
        print(incorrect_letters)
        print(hangman_pics[len(incorrect_letters)])

    if len(incorrect_letters) == number_of_failed_attempts:
        break

if len(incorrect_letters) == number_of_failed_attempts:
    print(f'Hanged! The word was: {answer_word}')
