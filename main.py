import random
while True:
    choice=input("Roll the dice?(y/n): ")
    if choice=="y":
        Ans1=str(random.randint(1,6))
        Ans2=str(random.randint(1,6))
        print("(",Ans1,",",Ans2,")")
    elif choice=="n":
        print("thanks for playing")
        break
    else:
        print("Invalid choice")