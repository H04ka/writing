print("Задание", 1)
from keyboard_folder import keyboard

while True:
    if keyboard.is_pressed('Enter'):
        chisla = (132, 301)
        print(f"Любимые числа: {chisla}")
        keyboard.wait('Enter', suppress=True)



