import random
#ask the user to enter a range from which they want to guess the number
while True:
    lowest=int(input("Enter the lowest number to guess from: "))
    highest=int(input("Enter the highest number to guess from: "))
    if highest<lowest:
        print("Enter a valid range")
    else:
        break

#choosing the number to guess
target=random.randint(lowest,highest)

#informing the user about the number of attempts available
AttemptsRemaining=10
print(f"You have {AttemptsRemaining} attempts")
Attempts=0

#taking guesses until attempts are finished or the number is guessed correctly
while True:
    choice=int(input("Enter you guess: "))
    Attempts=Attempts+1
    AttemptsRemaining=AttemptsRemaining-1
    #checking if guess is larger or smaller or same
    if choice>target:
        print("Too high! try again")
    elif choice<target:
        print("Too low! try again")
    else:
        print(f"Congrats! you guessed it in {Attempts} attempts")
        break

    #informing user about attempts remaining or ending the game if no attempts left
    if AttemptsRemaining>0:
        print(f"You have {AttemptsRemaining} guesses left")
    else:
        print("You have no guesses remaining, Better luck next time")
        break