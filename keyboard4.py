print("Задание", 4)
from keyboard_folder import keyboard

key_count = []

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key_count.append(event.name)
        print(f"фиксация: {event.name}")
        if event.name == 'esc':
            break
with open("key_logs.txt", "w", encoding='utf-8') as f:
    for key in key_count:
        f.write(f"{key}n")
print(f"кол-во нажатий: {len(key_count)}")
