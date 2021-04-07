# import needed modules
import asyncio
import subprocess
import time
from os import path

# clarifies what cls() does
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# starts level
print("\nLoading...")


async def main(int_tries=3):
    tries = int_tries
    await asyncio.sleep(2)
    print('\nFinished!')
    await asyncio.sleep(2)
    cls()
    # First-Time Question
    QUESTIONNAMEGOESHERE = input('\n\QUESTION GOES HERE\n\n')
    file = open("QUESTIONNAMEGOESHERE.txt", "w")
    print('*writes that down*')
    file.write(color)
    await asyncio.sleep(1)
    cls()
    print('Go on...')
    # Repeated Question
    q = input('QUESTION GOES HERE\n\n')
    file = open("QUESTIONNAMEGOESHERE.txt")
    answer = file.read().replace("\n", " ")
    file.close()
    while q:
        if q in answer:
            cls()
            print('Go on...')
            break
        else:
            print('You are not that great at lying...')
            if tries == 0:
                quit()
            else:
                tries = tries - 1
                print('You have ' + str(tries) + ' left!')
                break
    await asyncio.sleep(1)
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
