import pyautogui
import time

text = input('Enter the message you want to spam: ')
num = int(input('How many messages you want to spam?: '))
while True:
    print('\nYou have 5 seconds you to move the cursor to the message window after confirming.')
    confirmation = input('Confirm (Y/N):')
    if confirmation == 'y' or confirmation == 'Y':
        time.sleep(5)
        for i in range(num):
            time.sleep(0.1)
            pyautogui.typewrite(text)
            time.sleep(0.1)
            pyautogui.press('enter')
        break
    else:
        continue
