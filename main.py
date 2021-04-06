import asyncio
import subprocess
import time
from os import path

print("A Game By Nick Daggett - https://kathool.xyz/")

levels = '1'


async def main():
    await asyncio.sleep(1)
    print("\nPlease make sure to only say yes or no for yes or no questions to play correctly.")
    await asyncio.sleep(2)
    if path.exists("moddedlevel1.py"):
        subprocess.call("moddedlevel1.py", shell=True)
    if path.exists("level1.py"):
        subprocess.call("level1.py", shell=True)
    else:
        print("Couldn't find level 1! Quitting game...")
        time.sleep(1)
        quit()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
