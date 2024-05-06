
import random

def welcome_message():
    print("Welcome to Save Your Boat Game!")
    print("In this game, you need to guess the word by writing one letter at a time.")
    print("You have 5 lives. If you guess the word right, you'll save your boat and win.")
    print("But be careful, if you run out of lives, your boat will drown and you'll lose.")
    print("Let's start!")

def choose_word():
    words = ["python", "programming", "challenge", "game", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def play_game():
    word = choose_word()
    guessed_letters = []
    lives = 5

    print("The word has", len(word), "letters.")
    print(display_word(word, guessed_letters))

    while lives > 0:
        guess = input("Guess a letter: ").lower()

        if guess == "exit":
            print("Thanks for playing!")
            return

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            lives -= 1
            print("Oops! That letter is not in the word. You have", lives, "lives remaining.")
            if lives == 1:
                print("Hint: The word starts with", word[0])
            if lives == 0:
                print("Sorry, you've run out of lives. Your boat has drowned!")
                print("The word was:", word)
                return
        else:
            print("Good job! You guessed a letter.")
            word_display = display_word(word, guessed_letters)
            print(word_display)
            if "_" not in word_display:
                print("Congratulations! You've saved your boat!")
                return
            print("Game over!")



def main():
    welcome_message()
    
    play = input("Do you want to play the game? (yes/no): ").lower()
    
    if play == "yes":
        play_game()
    else:
        print("Okay, maybe next time!")

if __name__ == "__main__":
    main()
