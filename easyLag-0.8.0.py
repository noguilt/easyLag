# A simple python script that just shift clicks between recipes over and over.
# @linux-stack on Github, more projects soon to come (hopefully)
import time
import pyautogui
from colorama import init, Fore, Back, Style

init()

# Start screen
print(Fore.YELLOW + "easyLag " + Style.RESET_ALL + "- probably the easiest way to lag some Minecraft servers with friends")
print(Fore.BLUE + "---------------------------------" + Style.RESET_ALL)
print(Fore.CYAN + "Github: " + Style.RESET_ALL + "https://github.com/linux-stack/")
print(Fore.BLUE + "---------------------------------" + Style.RESET_ALL)
print("Mouse position will be recorded twice. Make sure your mouse is over the recipes")
print("before pressing enter")
input("When you're ready, press Enter to continue...\n")

# Grabbing mouse position
pos1 = pyautogui.position()
print(pos1)
print(Fore.YELLOW + "Next position in 5 seconds\n" + Style.RESET_ALL)

time.sleep(5)

pos2 = pyautogui.position()
print(pos2)

# Asks user how long to run the process
while True:
    value = input("\nHow long would you like to run the script (in seconds)? ")
    try:
        val = int(value)
        if val < 0:
            print("Sorry, input must be a positive number\n")
            continue
        break
    except ValueError:
        print("That's not a number\n")     

print(Fore.YELLOW + "\nProcess will start soon, make sure you have the Minecraft window selected\n" + Style.RESET_ALL)
time.sleep(5)

# Process started
print(Fore.GREEN + "Started" + Style.RESET_ALL)
t_end = time.time() + int(value)
while time.time() < t_end:
		pyautogui.keyDown('shift')
		pyautogui.click(pos1)
		pyautogui.click(pos2)
		pyautogui.keyUp('shift')
