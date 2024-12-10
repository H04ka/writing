print("Задание", 2)
from keyboard_folder import keyboard

def hotkey():
    print("Hotkey ctrl+shift+a activated!")

keyboard.add_hotkey('ctrl+shift+a', hotkey)

keyboard.wait('esc')
