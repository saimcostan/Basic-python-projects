#tuple of all the questions that the program will ask
Questions=("What is a temporary primary memory?",
           "What is the mass per unit volume?",
           "What is force per unit area?",
           "What is an example of an input device?")

#tuple of all the options given to the user
Options=(("A. ROM","B. RAM","C. SSD","D. HDD"),
         ("A. Area","B. Pressure","C. Density","D. Temperature"),
         ("A. Pressure","B. Volume","C. Mass","D. Weight"),
         ("A. Speaker","B. Printer","C. Monitor","D. Mouse"))

#tuple of all the answers to the given questions
Answers=("B","C","A","D")

# list of the guesses the user gives for each question
Guess=[]
QuestionNumber=0
Correct=0

#starting a loop for displaying questions
for Question in Questions:
    
    print(f"Q{QuestionNumber}.",Question)

    #starting a loop for displaying options
    for Option in Options[QuestionNumber]:
        print(Option)

    print()

    #Asking user input for their choice and adding it to the guess list
    UserGuess=input("Enter your answer (A,B,C,D): ").upper()

    Guess.append(UserGuess)

    #checking if the guess matches the answer
    if Answers[QuestionNumber]==UserGuess:
        print("CORRECT!")
        Correct+=1
    else:
        print("INCORRECT")
        print("The answer is",Answers[QuestionNumber])
    
    print()

    QuestionNumber+=1

#printing how many answers the user got correct       
print(f"You got {Correct} answers correct")

#printing a list of correct options
AnswerList="Answers="

for Answer in Answers:
    AnswerList=AnswerList+" "+Answer

print(AnswerList)

#printing a list of user guesses
GuessList="Your Guesses="

for YourGuess in Guess:
    GuessList=GuessList+" "+YourGuess

print(GuessList)

