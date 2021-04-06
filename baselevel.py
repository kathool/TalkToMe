# import needed modules
import asyncio
import subprocess
import time
from os import path

# starts level
print("\nLoading...")


async def main(int_tries=3):
    tries = int_tries
    await asyncio.sleep(2)
    print('\nFinished!')
    await asyncio.sleep(2)
    # Put the questions here!
    # ends level
    await asyncio.sleep(1)
    print("\nYour free to go.\n\nYou won! Victory!\n\n\n")
    if path.exists("moddedlevel2.py"):
        subprocess.call("moddedlevel2.py", shell=True)
    if path.exists("level2.py"):
        subprocess.call("level2.py", shell=True)
    else:
        print("Thanks for playing!")
        time.sleep(1)
        quit()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())