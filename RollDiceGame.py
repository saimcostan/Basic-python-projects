import random
while True:
    #get input from user
    choice=input("Roll the dice?(y/n): ")
    if choice=="y":
        #if user says yes then generate two random numbers
        Ans1=str(random.randint(1,6))
        Ans2=str(random.randint(1,6))
        print("(",Ans1,",",Ans2,")")
    elif choice=="n":
        #end the game if user says no
        print("thanks for playing")
        break
    else:
        #ignore any other choices
        print("Invalid choice")

#end