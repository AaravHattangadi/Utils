#NOT BEEN TESTED

import os

email = input("Your Email: ")

cmd = f"ssh-keygen -t ed25519 -C {email}"

os.system(cmd)