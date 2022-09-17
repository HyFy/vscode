import os
import sys

## this is code to execute
program = "python"
print("Process calling...")
arguments = ["called_Process.py"]

## we call the called_Ptocess.py script
os.execvp(program, (program, ) + tuple(arguments))
print("Good Bye!!")
