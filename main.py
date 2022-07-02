# This is a Template for a easy Spammer
# This Template is by Lk-Programming
# But you can open use it if you want

# Imports, Remember to install the Package pyautogui (pip install pyautogui)
from time import sleep

import colorama
import pyautogui

# setting up Variables as text and message

text = str(input("Put text do you want to be spammed here: "))
print("")  # this for the design
count = int(input("Please put in a number how often you want it to be spammed: "))
print("")  # This is Also for design
send = str(input("Do you want to press enter wenn one message is send (True / False) : "))
lcount = 0
print("")  # This is Also for design
print(colorama.Back.RED + "You now have 10 seconds to click in the window you want to spam in!" + colorama.Back.RESET)
sleep(10)  # Your 10 seconds for switching window's

# sending mechanic

while lcount < count:
    lcount = lcount + 1
    pyautogui.typewrite(text)
    if send == "True":
        pyautogui.press("enter")

if send == "True":
    print(colorama.Back.RESET + "")  # This is Also for design
    if count == 1:
        print("Finished Spamming " + str(
            count) + " Message with " + colorama.Fore.LIGHTGREEN_EX + "actived" + colorama.Fore.RESET + " sending")
    else:
        print("Finished Spamming " + str(
            count) + " Messages with " + colorama.Fore.LIGHTGREEN_EX + "actived" + colorama.Fore.RESET + " sending")

else:
    print(colorama.Back.RESET + "")  # This is Also for design
    if count == 1:
        print("Finished Spamming " + str(
            count) + " Messages with " + colorama.Fore.RED + "deactivated" + colorama.Fore.RESET + " sending")
    else:
        print("Finished Spamming " + str(
            count) + " Messages with " + colorama.Fore.RED + "deactivated" + colorama.Fore.RESET + " sending")
