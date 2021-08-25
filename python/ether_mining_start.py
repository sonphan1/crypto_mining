from pywinauto import Desktop
import os
import subprocess
import sys

def get_max_phoenix_version(directory=os.getcwd()):

    print('listing directorys in', directory)
    dir_path_list = os.listdir(directory)
    # https://stackoverflow.com/questions/3416401/removing-elements-from-a-list-containing-specific-characters
    phoenix_lists = [path for path in dir_path_list if "PhoenixMiner" in path]

    max_phoenix_version = max(phoenix_lists)
    sys.path += [max_phoenix_version+'PhoenixMiner.exe']
    return max_phoenix_version


def main():
    # https://stackoverflow.com/questions/57217688/returning-all-desktop-windows-with-pywinauto
    file = 'start_miner - Shortcut'
    windows = Desktop(backend="uia").windows()
    cur_dir = os.getcwd()
    if 'python' in cur_dir:
        cur_dir = cur_dir.replace('python','')
    print('cur_dir', cur_dir)
    sys.path += [cur_dir]

    miner_version = get_max_phoenix_version(directory=cur_dir)

    if file in [w.window_text() for w in windows]:
        print('its already active silly boi')
    else:
        # https://stackoverflow.com/questions/204017/how-do-i-execute-a-program-from-python-os-system-fails-due-to-spaces-in-path
        # C:/Users/Lance-PC/Desktop/github/crypto_mining/PhoenixMiner_5.7b_Windows/PhoenixMiner_5.7b_Windows/start_miner.bat
        # filepath = 'C:/Users/Lance-PC/Desktop/github/crypto_mining/PhoenixMiner_5.7b_Windows/start_miner.bat'
        filepath = os.path.join(cur_dir, miner_version, file)
        print("not active, starting {}".format(filepath))
        os.startfile(filepath)

    return True


if __name__ == '__main__':
    main()
