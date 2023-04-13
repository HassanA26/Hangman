import random
import string
won = 0
losses = 0
def game():
    global won
    global losses

    attempts = 8
    words = ["python", "java", "swift", "javascript"]
    secret_word = random.choice(words)
    hidden_word = list("-" * len(secret_word))
    letters_in_word = set(secret_word)
    already_guessed = set()
    while attempts > 0:
        print(f"\n{''.join(hidden_word)}")
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("Please, input a single letter.")
            continue

        if not guess.islower() or guess not in string.ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        if guess in already_guessed:
            print("You've already guessed this letter.")

        else:
            already_guessed.add(guess)

            if guess in letters_in_word:
                for i in range(len(secret_word)):

                    if secret_word[i] == guess:
                        hidden_word[i] = secret_word[i]

                if set(hidden_word) == letters_in_word:
                    print("\n" + ''.join(hidden_word))
                    print(f"You guessed the word {secret_word}!\nYou survived!")
                    won += 1
                    break

            else:
                print("That letter doesn't appear in the word.")
                attempts -= 1
                print(f"{attempts} attempts")

    if attempts == 0:
        print("\nYou lost!")
        losses += 1


def main_menu():
    print(f"H A N G M A N")

    while True:
        choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if choice == "play":
            game()
        elif choice == "results":
            print(f"You won: {won} times\nYou lost: {losses} times")
        elif choice == "exit":
            break
        else:
            print("Invalid choice. Please choose 'play', 'results', or 'exit'.")


main_menu()