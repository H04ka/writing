print("Задание", 6)
from keyboard_folder import keyboard
counter = 0
def fun():
    global counter
    if keyboard.is_pressed('i'):
        counter += 1
    if keyboard.is_pressed('d'):
        counter -= 1
    if keyboard.is_pressed('q'):
        print(f"счётчик: {counter}")
keyboard.add_hotkey('i', fun)
keyboard.add_hotkey('d', fun)
keyboard.add_hotkey('q', fun)
keyboard.wait('esc')
        