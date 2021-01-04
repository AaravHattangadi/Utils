@echo off
echo This will now install all of the scripts in this folder
echo To not install a script, delete it from the folder
echo You have ten seconds to terminate

timeout /t 10

echo Installing

echo Copying clear.cmd

copy clear.cmd "C:\Users\%USERNAME%\Desktop\sys32"

echo clear.cmd has been copied!


echo Copying ls.cmd

copy ls.cmd "C:\Users\%USERNAME%\Desktop\sys32"

echo ls.cmd has been copied!

echo Install Completed!

pause
