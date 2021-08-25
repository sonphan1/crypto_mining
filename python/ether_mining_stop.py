
from pywinauto import Desktop
import os

def main():
    # https://stackoverflow.com/questions/57217688/returning-all-desktop-windows-with-pywinauto
    windows = Desktop(backend="uia").windows()
    file = 'start_miner - Shortcut'

    if file in [w.window_text() for w in windows]:
        print('its active, stop it')
        os.system("taskkill /im cmd.exe")

    else:
        pass
    return True


if __name__ == '__main__':
    main()
