import names
import time

gender = input("What gender? (m/f) ")
number = input("Number of names to generate ")
num1 = int(number)
curname = 0

while (curname != num1):
    curname = curname + 1
    time.sleep(1)
    print(names.get_full_name(gender=gender))

if (curname == num1):
    print(f"{number} name(s) have/has been generated")
time.sleep(10)    
