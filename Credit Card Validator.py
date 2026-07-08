# asking user to input their credit card number
CardNum=input("Enter the credit card number to validate: ")

# Removing a ny dashes or white spaces from the credit card number
NewCardNum=""

for Char in CardNum:
    #adding only digits in a new string
    if Char!="-" and Char!=" ":
        NewCardNum=NewCardNum+Char


# Add all digits at odd places from right to left
OddSum=0
for Pos in reversed(range(len(NewCardNum))):
    #extracting digits and checking if they are in the odd place
    Char=NewCardNum[Pos]
    
    if (len(NewCardNum) - Pos) % 2 != 0:
        OddSum=OddSum+int(Char)
    
# Double every second digit and get their sum from right to left
# if result is a two digit number then add the two digits to get a single digit then add it in the sum

Second_Sum=0
Pos=len(NewCardNum)-2

while True:
    ThisNum=int(NewCardNum[Pos])
    Double= ThisNum * 2

    if Double >= 10:
        #extracting the two digits and adding them
        FirstNum=int(str(Double)[0])
        SecondNum=int(str(Double)[1])
        Double=0
        Double=FirstNum+SecondNum

    Second_Sum=Second_Sum+Double
    #decrementing by 2 places and checking if end has been reached
    Pos= Pos-2
    if Pos<0:
        break

#Adding up the two sums and if the answer is divisible by 10, the credit card is valid

Total=OddSum+Second_Sum

if Total%10==0:
    print("Your credit card is valid")
else:
    print("ERROR! credit card is invalid")



