import subprocess
import time
from os import path

if path.exists("main.py"):
    subprocess.call("main.py", shell=True)
else:
    print("Couldn't find game! Quitting launcher...")
    time.sleep(1)
    quit()
