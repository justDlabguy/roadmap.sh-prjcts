from random import randint

while True:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


    difficulty = [0,10,5,3]

    # Step 1: computer picks difficulty

    diff = int(input('''Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances):'''))

    if diff not in [1,2,3]:
        print("Invalid choice. Setting difficulty to Medium (5 chances).")
        diff = 2

    number = randint(1, 100)

    # Step 2: set fixed chances for now
    chances = difficulty[diff]
    print(f"great you have chosen")
    attempts = 0
    guess = None

    while attempts < chances:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}.")
        elif guess > number:
            print(f"Incorrect! The number is less than  {guess}.")


    if attempts == chances and guess != number:
        print(f"Sorry! You ran out of chances. The number was {number}.")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thank you for playing! Goodbye!")
        break