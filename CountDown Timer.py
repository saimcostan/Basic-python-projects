import time

#taking input from user about how long they want to set the count down for
this_time=int(input("Enter the time you want to count down in seconds: "))

#using a loop to run from the time given till zero
for x in range(this_time,0,-1):
    #separating seconds, minutes and hours to display
    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    #using "02" for proper 0 padding if the number is a single digit to make it seem like a digital clock
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")
