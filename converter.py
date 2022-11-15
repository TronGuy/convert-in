'''
#Github: github.com/TronGuy
#License: GPLv3
'''
from os import system,path
from platform import system as platform
import signal,sys

def sigint_handler(signal,frame):
     system("clear")
     print('Kill program Covert-in...')
     sys.exit(0)

system("clear" or "cls")

def getsystem():
    return platform()

def converterInLinux():
    conversionList = []
    title = "|Choose a encoding to transform the MP4 or WEBM in MP3|"
    print("-"*len(title))
    print(title)
    print("-"*len(title))
    print(" \n\n----- [RECOMMEND] - DONT'T USE SPECIAL CHARACTERS OR SPACES IN FILES! -----\n\n")
    print("[1] - Bitrate Encoding(CBR)")
    print("[2] - Variable Bitrate Encoding(VBR)")
    answer = input('Choose: ').strip()
    if(answer == "1"):
        system("clear")
        print("[ENTER] - Press After the Choose of your files to Convert with CBR: ")
        while True:
            path = input("Path of the MP4 or WEBM: ")            
            if(path != ""):
                conversionList.append(path)
            else:
                for i in conversionList:
                    system("clear" or "cls")
                    print(f'File: {i}')
                    print("\n ----Don't use symbols or similar characters ----\n")
                    out = input("Name of the MP3 file: ").strip()
                    out = ''.join(out)
                    system(f"ffmpeg -i {i} -vn -acodec libmp3lame -ac 2 -ab 160k -ar 48000  '{out}'.mp3")
                    system("clear" or "cls")
                break


    if (answer == "2"):            
        system("clear")
        print("[ENTER] - Press After the choose of your MP4 Files to Convert with VBR: ")
        while True:
            path = input("Path of the MP4 or WEBM: ")            
            if(path != ""):
                conversionList.append(path)
            else:
                for i in conversionList:
                    system("clear" or "cls")
                    print(f'File: {i}')
                    print("\n ----Don't use symbols or similar characters ----\n")
                    out = input("Name of the MP3 File: ").strip()
                    out = ''.join(out)
                    system(f"ffmpeg -i {i} -vn -acodec libmp3lame -ac 2 -qscale:a 4 -ar 4  '{out}'.mp3")
                    system("clear" or "cls")
                

plataforma = getsystem()
if(plataforma == "Linux" or plataforma == "linux"):
    signal.signal(signal.SIGINT, sigint_handler)
    converterInLinux()

else:
    system("cls" or "clear")
    print("this script is only for GNU/linux for now. ")