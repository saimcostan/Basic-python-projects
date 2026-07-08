# python alarm clock

import time
import datetime
import pygame


def Set_Alarm(AlarmTime):
    print("Alarm set for",AlarmTime)
    sound_file="alarm sound.wav"

    while True:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time==AlarmTime:
            print("WAKE UP! 😫")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break

        time.sleep(1)


def main():
    AlarmTime=input("Enter the alarm time (HH:MM:SS): ")
    Set_Alarm(AlarmTime)



if __name__=="__main__":
    main()
