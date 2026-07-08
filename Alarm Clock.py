# python alarm clock

import time
import datetime
import pygame


def Set_Alarm(AlarmTime):

    # printing the alarm time and placing the sound file in a variable
    print("Alarm set for",AlarmTime)
    sound_file="alarm sound.wav"

    while True:
        # printing current time each second until the alarm tiem is reached
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        # playing the sound file using pygame when the alarm time has been reached
        if current_time==AlarmTime:
            print("WAKE UP! 😫")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            # keep on repeating the alarm sound
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break

        time.sleep(1)

# getting user input about alarm time and calling Set_Alarm
def main():
    AlarmTime=input("Enter the alarm time (HH:MM:SS): ")
    Set_Alarm(AlarmTime)



if __name__=="__main__":
    main()
