import pyautogui
import time


def liker(num):
    time.sleep(5)
    for i in range(num):
        pyautogui.moveTo(420, 402)
        time.sleep(1)
        pyautogui.doubleClick()
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)


def unliker(num):
    time.sleep(5)
    for i in range(num):
        liked_cord = pyautogui.locateCenterOnScreen('liked.png')
        pyautogui.leftClick(liked_cord)
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)


print("Open the account whose video you want to like in web browser with the video open\n")
while True:
    print('What do you want to do?')
    print('1. Like videos')
    print('2. Unlike videos')
    print('3. Exit')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        n = int(input('How many videos you want to like?'))
        liker(n)
        exit()
    elif choice == 2:
        n = int(input('How many videos you want to unlike?'))
        unliker(n)
        exit()
    elif choice == 3:
        exit()
    else:
        print('\nInvalid choice.')
        continue


