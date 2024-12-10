print("Задание", 3)
from keyboard_folder import keyboard

lst = [1, 2, 3]

def hotkey_lst():
    lst.append(lst[-1]+ 1)
    print(f"список: {lst}")

keyboard.add_hotkey('p', hotkey_lst)
keyboard.wait('esc')
