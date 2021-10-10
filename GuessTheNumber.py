number = 42

guess = int(input("Guess the secret number between 1 and 50: "))

if guess == number:
    print("Congrats! You have guessed the meaning of life! The secret number is 42!")
else:
    print("Better luck next time! The secret number is not: " + str(guess) + "!")