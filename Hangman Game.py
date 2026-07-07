import random 

# list of 100 random animals
words = (
    "cat", "dog", "fish", "bird", "frog", "bear", "lion", "wolf", "deer", "duck",
    "cow", "pig", "hen", "fox", "owl", "bat", "bee", "ant", "rat", "fly",
    "horse", "sheep", "goat", "mule", "bull", "crab", "clam", "moth", "worm", "snail",
    "eagle", "shark", "whale", "tiger", "panda", "koala", "moose", "goose", "mouse", "swan",
    "robin", "finch", "crane", "heron", "stork", "raven", "crow", "dove", "parrot", "turkey",
    "monkey", "rabbit", "donkey", "lizard", "turtle", "oyster", "salmon", "shrimp", "pigeon", "magpie",
    "kitten", "puppy", "chick", "lamb", "calf", "piglet", "foal", "tadpole", "catfish", "starfish",
    "elephant", "giraffe", "penguin", "dolphin", "hamster", "sparrow", "lobster", "octopus", "squirrel", "peacock",
    "chicken", "buffalo", "gorilla", "leopard", "cheetah", "flamingo", "kangaroo", "hedgehog", "raccoon", "seagull",
    "goldfish", "bluebird", "reindeer", "chipmunk", "parakeet", "seahorse", "jellyfish", "caterpillar", "bumblebee", "dragonfly"
)

# Dictionary of all the images of hangman according to the number of wrong guesses
Hangman_Art={
            0:("       ",
               "       ",
               "       ",),

            1:("   o   ",
               "       ",
               "       "),

            2:("   o   ",
               "   |   ",
               "       "),

            3:("   o   ",
               "  /|   ",
               "       "),

            4:("   o   ",
               "  /|\\ ",
               "       "),

            5:("   o   ",
               "  /|\\ ",
               "  /    "),

            6:("   o   ",
               "  /|\\ ",
               "  / \\ "),}


# module to print the different stages of the hangman
def Display_Man(Wrong_Guesses):

    print("**************")
    for line in Hangman_Art[Wrong_Guesses]:
        print("  ",line)
    print("**************")

# module to print the hints
def Display_Hint(Hint):

    print(" ".join(Hint))

def main():
    # choosing a random animal name from the list
    Answer=random.choice(words)
    Hint=["_"]*len(Answer)

    # initiating wrong guesses and making a set of already guesses letters
    Wrong_Guesses=0
    Guessed_Letters=set()

    print("ANIMAL GUESSING GAME")

    while True:
        print()
        Display_Man(Wrong_Guesses)
        Display_Hint(Hint)
        print()
        # asking the user to enter their guess
        Guess=input("Enter a letter as your guess(a to z): ").lower()
        print()

        # Making sure guess is valid and not already entered
        if len(Guess)!=1 or not Guess.isalpha():
            print("**********")
            print("Invalid input")
            print("**********")
            continue
        
        if Guess in Guessed_Letters:
            print("**********")
            print(Guess,"is aleardy guessed")
            print("**********")
            continue
        
        # swapping the hint space with the letter if a letter is guessed correctly
        if Guess in Answer:
            for i in range(len(Answer)):
                if Answer[i]==Guess:
                    Hint[i]=Guess
        else:
            # incrementing wrong guesses to change the shape of the hangman
            Wrong_Guesses+=1

        Guessed_Letters.add(Guess)

        # if the word is completely guessed then anounce win
        if "_" not in Hint:
            Display_Man(Wrong_Guesses)
            print(Answer)
            print()
            print("YOU WIN!")
            print("**********")
            break
        # if hangman is completed then anounce lose
        elif Wrong_Guesses>=len(Hangman_Art)-1:
            Display_Man(Wrong_Guesses)
            print()
            print("You lost.")
            print("**********")
            print("Correct Answer:")
            print(Answer)
            break

# loop the game till the user wants to quit
while True:
    main()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("*******")
        print("  END")
        print("*******")
        break

    