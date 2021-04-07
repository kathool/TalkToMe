import asyncio
import subprocess
import time
import os
from os import path


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print("\nLoading...")


async def main(int_tries=3):
    tries = int_tries
    await asyncio.sleep(2)
    print('\nFinished!')
    await asyncio.sleep(2)
    cls()
    color = input('\n\nRed or Blue?\n\n')
    file = open("color.txt", "w")
    print('*writes that down*')
    file.write(color)
    await asyncio.sleep(1)
    cls()
    print('Go on...')
    name = input('What is your name?\n\n')
    file = open("name.txt", "w")
    print('*writes that down*')
    file.write(name)
    await asyncio.sleep(1)
    cls()
    print('Go on...')
    live = input('Where do you live?\n\n')
    file = open("live.txt", "w")
    print('*writes that down*')
    file.write(live)
    await asyncio.sleep(1)
    cls()
    print('Go on...')
    kill = input('Did you kill anyone?\n\n')
    while kill:
        if kill.startswith("y") or kill.startswith("Y") or kill.startswith("a") or kill.startswith("A"):
            print("Oh thanks for the quick answer, hope you like prison cause your gonna be there for a while.")
            await asyncio.sleep(2)
            quit()
        else:
            break
    file = open("kill.txt", "w")
    print('*writes that down*')
    file.write(kill)
    cls()
    await asyncio.sleep(1)
    print('Go on...')
    q = input('Where do you live?\n\n')
    file = open("live.txt")
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
    q = input('Did you kill anyone?\n\n')
    file = open("kill.txt")
    answer = file.read().replace("\n", " ")
    file.close()
    while q:
        if q in answer:
            print('Go on...')
            cls()
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
    q = input('What is your name\n\n')
    file = open("name.txt")
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
    q = input('Red or Blue?\n\n')
    file = open("color.txt")
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
    live = input('How old are you?\n\n')
    file = open("age.txt", "w")
    print('*writes that down*')
    file.write(live)
    await asyncio.sleep(1)
    cls()
    print('Go on...')
    q = input('Red or Blue?\n\n')
    file = open("color.txt")
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
    q = input('How old are you?\n\n')
    file = open("age.txt")
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
    q = input('Red or Blue?\n\n')
    file = open("color.txt")
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
    q = input('Did you kill someone?\n\n')
    file = open("kill.txt")
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
    q = input('Red or Blue?\n\n')
    file = open("color.txt")
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
    q = input('How old are you?\n\n')
    file = open("age.txt")
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
    q = input('Red or Blue?\n\n')
    file = open("color.txt")
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
    q = input('How old are you?\n\n')
    file = open("age.txt")
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
    q = input('Red or Blue?\n\n')
    file = open("color.txt")
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
    q = input('Did you kill someone?\n\n')
    file = open("kill.txt")
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
