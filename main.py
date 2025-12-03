import random

MAX_ATTEMPTS = 5
LOW = 1
HIGH = 30

def get_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            exit(0)
        if not value.isdigit():
            print("Please enter a valid number.")
            continue
        return int(value)

def play():
    secret = random.randint(LOW, HIGH)
    attempts = 0
    print(f"Guess a number between {LOW} and {HIGH}. \nYou have {MAX_ATTEMPTS} attempts. (type 'q' to quit)\n")

    while attempts < MAX_ATTEMPTS:
        guess = get_int(f"Attempt {attempts+1}: Your guess: ")
        attempts += 1

        if guess == secret:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
        elif guess < secret:
            print("Too low🙄.")
        else:
            print("Too high🙄.")

    else:
        print(f"Out of attempts. The number was {secret}.")

if __name__ == "__main__":
    while True:
        play()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing.")
            break
