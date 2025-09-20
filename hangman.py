import random

def hangman():
    # Predefined list of words
    words = ["python", "hangman", "computer", "science", "programming"]
    
    # Pick a random word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)  # display with underscores
    guessed_letters = []
    attempts = 6  # maximum wrong guesses
    
    print("🎮 Welcome to Hangman!")
    print("You have 6 chances to guess the word.")
    print(" ".join(guessed_word))
    
    # Game loop
    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabet letter.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try another letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.")
            # Reveal guessed letters
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! You have {attempts} attempts left.")
        
        print("Word: " + " ".join(guessed_word))
        print("Guessed letters: " + ", ".join(guessed_letters))
    
    # End of game
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)


# Run the game
hangman()
