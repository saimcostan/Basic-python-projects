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
for Question in Questions:
    
    print(f"Q{QuestionNumber}.",Question)


    for Option in Options[QuestionNumber]:
        print(Option)

    print()

    UserGuess=input("Enter your answer (A,B,C,D): ").upper()

    Guess.append(UserGuess)

    if Answers[QuestionNumber]==UserGuess:
        print("CORRECT!")
        Correct+=1
    else:
        print("INCORRECT")
        print("The answer is",Answers[QuestionNumber])
    
    print()

    QuestionNumber+=1
        
print(f"You got {Correct} answers correct")

AnswerList="Answers="

for Answer in Answers:
    AnswerList=AnswerList+" "+Answer

print(AnswerList)

GuessList="Your Guesses="

for YourGuess in Guess:
    GuessList=GuessList+" "+YourGuess

print(GuessList)

