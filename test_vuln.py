import os

def vulnerable_function():
    os.system('ls')

def unused_function():
    pass

vulnerable_function()
