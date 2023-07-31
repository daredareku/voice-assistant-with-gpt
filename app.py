import os

from gui import Application

from config import SETTINGS

import signal
import sys

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#устанавливаем переменные окружения из словаря SETTINGS
for key, value in SETTINGS.items():
    os.environ[key] = value

if __name__ == '__main__':
    try:
        while True:
            # Your program logic here...
            root = Application()
            root.mainloop()
            pass
    except KeyboardInterrupt:
        print('\nExiting program...')
        sys.exit(0)
    