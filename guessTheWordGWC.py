import time

word = ("computer")

correct = word
clue = word[0] + word[(len(word)-1):(len(word))]
letter_guess = []
word_guess = []
store_letter = []
count = 0
limit = 13

print('Welcome to Guess the Word')
time.sleep(1)
print('You have 5 attempts at guessing letters in a word')
time.sleep(1)
print('Let\'s begin!')
print('\n')

while count < limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in word:
        print('yes!')
        store_letter += letter_guess
        count += 1

    if letter_guess not in word:
        print('no!')
        count += 1

print('\n')
print('You have guessed',len(store_letter),'letters correctly.')
print('Current letters gussed correctly: ', store_letter)

word_guess = input("What word did you guess?")
if word_guess == correct:
    print('You did it!!')
    exit()

elif word_guess != correct:
    print('Wrong! The answer was,', word)
    exit()

print('\n')
input('Press Enter to leave the program')

print('\n')
input('Press Enter to leave the program')
