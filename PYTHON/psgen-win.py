import string
import secrets
import os
import sys

alphabet = string.ascii_letters + string.digits
i1 = input("How long should the password be? (number only) ")
i2 = input("Should I export your password to a text file? (y/n)")
bool1 = True if i2 == "y" else False


number = int(i1)
password = ''.join(secrets.choice(alphabet) for i in range(number))

if bool1 == True:
    f = open("yourPassword.txt", "a")
    f.write(f"Length: {number} , Password: {password}")
    f.close()
    print(password)
else:
    print(password)

os.system("pause")
sys.exit(0)
