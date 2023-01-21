import pyautogui
import pytesseract
import keyboard
import mouse
import matplotlib.pyplot as plt

# Set the shortcut key that will trigger the screenshot
shortcut_key = 'ctrl+shift+a'

pressed1 = False
pressed2 = False
pos1 = (0, 0)
pos2 = (0, 0)
shortcutPressed = False

def procedure():

    global pressed1 
    global pressed2
    global pos1
    global pos2

    if not pressed1 and not pressed2:
        pos1 = pyautogui.position()
        print("pos1: X: " + str(pos1[0]) + " Y: " + str(pos1[1]))
        pressed1 = True
    elif pressed1 and not pressed2:
        pos2 = pyautogui.position()
        print("pos2: X: " + str(pos2[0]) + " Y: " + str(pos2[1]))
        pressed2 = True


        
        left, top = min(pos1[0], pos2[0]), min(pos1[1], pos2[1])
        right, bottom = max(pos1[0], pos2[0]), max(pos1[1], pos2[1])
        width, height = right - left, bottom - top

# Take a screenshot of the selected area
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        # Extract the text from the screenshot using OCR
        text = pytesseract.image_to_string(screenshot)

        print(text)
        pressed1 = False
        pressed2 = False

# Start the main loop
while True:
    # Check if the shortcut key is pressed
    if keyboard.is_pressed(shortcut_key) and not shortcutPressed:
        # Wait for the user to drag on the screen to choose an area
        procedure()
        shortcutPressed = True
    elif not keyboard.is_pressed(shortcut_key) and shortcutPressed:
        shortcutPressed = False


