import pyautogui
import time


def liker(num):
    time.sleep(5)
    for i in range(num):
        pyautogui.moveTo(420, 402)
        time.sleep(1)
        pyautogui.doubleClick()
        time.sleep(1)
        pyautogui.moveTo(782, 418)
        time.sleep(1)
        pyautogui.leftClick()


print("Open the account whose video you want to like in web browser with the video open")
while True:
    confirmation = input('\nOpened yet?(Y/N):')
    if confirmation == 'y' or confirmation == 'Y':
        videos_to_like = int(input("How many videos you want to like?:"))
        liker(videos_to_like)
        break
    else:
        print('\nNote: Open the profile in the browser')
        continue
