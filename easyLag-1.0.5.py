# A stress testing tool for MC servers, lower TPS with just a crafting table.
# @noguilt on Github, more projects soon to come (hopefully)
import time
import pyautogui
from colorama import init, Fore, Back, Style

init()

# Start screen
print(Fore.YELLOW + "easyLag " + Style.RESET_ALL + "- a stress testing tool for MC servers")
print(Fore.BLUE + "---------------------------------" + Style.RESET_ALL)
print(Fore.CYAN + "Github: " + Style.RESET_ALL + "https://github.com/noguilt")
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
print(Fore.YELLOW + "Positions saved...\n" + Style.RESET_ALL)

# Asks user how long to run the process
while True:
    value = input("How long would you like to run the script (in seconds)? ")
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
		pyautogui.click(pos1, _pause = 0) #_pause = 0 added to bypass pyautogui delay
		pyautogui.click(pos2, _pause = 0)
		pyautogui.keyUp('shift')
