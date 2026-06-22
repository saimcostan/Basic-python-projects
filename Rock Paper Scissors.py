import random

WinCount=0
LoseCount=0
DrawCount=0
MatchCount=0
while True:
    while True:
        #take input from user for their choice and checking if its valid
        UserChoice=input("rock, paper or scissors? Enter 'r' or 'p' or 's': ").lower()
        if UserChoice=="r":
            print("you chose 🪨")
            break
        elif UserChoice=="p":
            print("you chose 📄")
            break
        elif UserChoice=="s":
            print("you chose ✂️")
            break
        else:
            print("Error! invalid input")
    
    #selecting computer choice
    Num=random.randint(1,3)
    
    
    if Num==1:
        CompChoice="r"
        print("Computer chose 🪨")
    elif Num==2:
        CompChoice="p"
        print("Computer chose 📄")
    else:
        CompChoice="s"
        print("Computer chose ✂️")

    #printing results based on different combinations
    if UserChoice=="r" and  CompChoice=="p":
        print("you lose")
        LoseCount+=1
    elif UserChoice=="p" and  CompChoice=="s":
        print("you lose")
        LoseCount+=1
    elif UserChoice=="s" and  CompChoice=="r":
        print("you lose")
        LoseCount+=1
    elif UserChoice=="p" and  CompChoice=="r":
        print("you won")
        WinCount+=1
    elif UserChoice=="s" and  CompChoice=="p":
        print("you won")
        WinCount+=1
    elif UserChoice=="r" and  CompChoice=="s":
        print("you won")
        WinCount+=1
    else:
        print("Its a draw")
        DrawCount+=1
    MatchCount+=1

    if WinCount==2:
        print("you are the overall winner")
        break
    elif LoseCount==2:
        print("Computer is the overall winner")
        break
    

    #asking user if they want to continue
    
    Continue=input("Continue? (y/n): ").lower()
    if Continue=="n":
        break

print(f"Number of times you won: {WinCount}")
print(f"Number of times you lost: {LoseCount}")
print(f"Number of times the match was a draw: {DrawCount}")
    

