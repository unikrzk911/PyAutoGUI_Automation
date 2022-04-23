# Import the relevant modules
import pyautogui
import time

# Give the python file some time before continuing
time.sleep(3)

# Mouse Functions
# Prints the resolution of your screen
print(pyautogui.size())
# Prints the current position of the mouse
print(pyautogui.position())
# Moves the mouse over time (3 seconds)
pyautogui.moveTo(100, 100, 3)
# Move the mouse relative to its current position
pyautogui.moveRel(100, 100, 3)

# Click
pyautogui.click(500, 500, 3, 3, button="left")
pyautogui.tripleClick()
pyautogui.doubleClick()
pyautogui.leftClick()
pyautogui.rightClick()

# Scrolls up 500
pyautogui.scroll(500)
# Scrolls down 500
pyautogui.scroll(-500)

# Mouse up and down
pyautogui.mouseUp(100, 100, button="left")
pyautogui.mouseDown(100, 100, button="left")

# Example of mouse up and down
pyautogui.mouseDown(300, 400, button="left")
pyautogui.moveTo(800, 400, 3)
pyautogui.mouseUp()
pyautogui.moveTo(1000, 400, 3)

# Keyboard functions
pyautogui.write("hello")
pyautogui.press("enter")
pyautogui.press("space")


# Screenshot in pyautogui
pyautogui.screenshot("screenshot.png")