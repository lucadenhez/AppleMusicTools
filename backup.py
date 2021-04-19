from sys import exit
from colorama import Fore, init

init(True)

def write(f, song, artist, time):
    f.write("[Status] Song: " + song + " | Artist: " + artist + " | Length: "  + time + "\n")

def output(song, artist, time):
    print("[" + Fore.CYAN + "Status" + Fore.RESET + "] " + Fore.MAGENTA + "Song: " + song + Fore.GREEN + " | Artist: " + artist + Fore.BLUE + " | Length: "  + time)

def getInfo():
    print("\n[" + Fore.GREEN + "Start" + Fore.RESET + "] In order to start, open iTunes, then go to the 'Songs' tab, focus on a song, then press 'Ctrl/Cmd + a' then 'Ctrl/Cmd + c' and exit.")
    print("[" + Fore.MAGENTA + "Input" + Fore.RESET + "] Please paste your songs (Ctrl/Cmd + v) in this console and then press enter once or twice:\n\n")
    lines = []
    
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return lines

unparsed = getInfo()

try:
    with open('unparsed.txt', 'w') as f:
        for line in unparsed:
            f.write(line)
except:
    print("[" + Fore.RED + "ERROR" + Fore.RESET + "] Couldn't write to files. Is your file in a protected or root directory? Exiting...\n")
    exit()

with open('parsed.txt', 'w') as f:
    try:
        for i in range (len(unparsed)):
            info = unparsed[i].split("\t")
            
            if info[0] == "":
                info[0] = "N/A"
            if info[2] == "":
                info[2] = "N/A"
            if info[3] == "":
                info[3] = "N/A"

            output(info[0], info[2], info[3])
            write(f, info[0], info[2], info[3])
    except Exception as ex:
        print("[" + Fore.RED + "ERROR" + Fore.RESET + "] Unexpected error, exiting...\n")
        q = input("[" + Fore.MAGENTA + "Input" + Fore.RESET + "] Would you like to see the exception? (y/n) ")
        if q == 'y':
            print(f"\n{ex}")
        exit()

print("\n[" + Fore.MAGENTA + "Done" + Fore.RESET + "] Found " + Fore.RED + str(i) + Fore.RESET + " songs! 😀 | Saved to the text file parsed.txt\n")
