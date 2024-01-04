# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92

[-->] Script for Managing your Instagram Account Remotely


IAM: Instagram Account Manager


******************************|IMPORTANT|*******************************
* User's data (such as username password) will not be stored or saved !*
* Will be used only for some functions of the script.                  *
************************************************************************
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! IAM requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use IAM ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        exit(0)
    import platform
    from os import system
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ['sys', 'time', 'os', 'platform', 'rich', 'instagrapi', 'requests', 'json', 'instaloader', 'tkinter', 'colorama']
    with console.status('[bold dark_orange]Loading module...') as status:
        for mod in mods:
            sleep(0.8)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]okay')
    import instagrapi
    import instaloader
    import instagram_private_api
    import instapy
    import json
    import webbrowser
    import datetime
    import requests as re
    import os
    from colorama import init, Fore
    from tkinter import *
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in IAM have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Error ! Cannot install the required modules !")
                sleep(1)
                print("[*] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall script")
                print("[2] Exit")
                opt=int(input(f"[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[*] Acceptable numbers: [1/2]")
                    sleep(1)
                    print("[1] Uninstall script")
                    print("[2] Exit")
                    opt=int(input(f"[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))
                        return None
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(fpath('IAM'))
                    print("[✓] Files and dependencies uninstalled successfully !")
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    exit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip3 install -r requirements.txt")

loader=instaloader.Instaloader()
client=instagrapi.Client()

init(autoreset=True)
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW

sleep(0.8)
console.clear()
console.print(f"[bold dark_green][✓] Successfully loaded modules.")
sleep(1.1)
console.clear()

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def banner() -> str:
    return f"""{green}
    ██╗░█████╗░███╗░░░███╗
    ██║██╔══██╗████╗░████║
    ██║███████║██╔████╔██║
    ██║██╔══██║██║╚██╔╝██║
    ██║██║░░██║██║░╚═╝░██║
    ╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
    """

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

def Get_Hpk(url:str) -> str:
    return client.highlight_pk_from_url(url)

def Get_Spk(url:str) -> str:
    return client.story_pk_from_url(url)

def valUser(user):
    return re.get(f"https://www.instagram.com/{user}/", allow_redirects=False).status_code != 200

def Except(ex:str):
    print(f"{red}[!] Error !")
    sleep(1)
    print(f"{yellow}[*] Error message ==> {ex}")
    sleep(2)
    print(f"{yellow}[1] Return to menu")
    print(f"{yellow}[2] Exit")
    num=int(input(f"{yellow}[::] Number (from the above ones) >>> "))
    while num < 1 or num > 2:
        print(f"{red}[!] Invalid number !")
        sleep(1)
        print(f"{green}[*] Acceptable numbers: [1/2]")
        sleep(1)
        print(f"{yellow}[1] Return to menu")
        print(f"{yellow}[2] Exit")
        num=int(input(f"{yellow}[::] Number (from the above ones) >>> "))
    if num == 1:
        clear()
        main()
    else:
        print(f"{yellow}[+] Exiting...")
        sleep(1)
        print(f"{yellow}[+] See you next time 👋")
        sleep(1)
        exit(0)

def checkOpt(opt,data):
    if data == "username":
        print(f"{red}[!] Invalid length !")
        sleep(1)
        print(f"{green}[*] Acceptable length: less than or equal to 30 characters")
    elif data == "id":
        print(f"{red}[!] Invalid length !")
        sleep(1)
        print(f"{green}[*] Acceptable length: greater than 3")
    elif data == "path":
        print(f"{green}[*] Path must contain: / or \\ ")
    else:
        print(f"{red}[!] Invalid number !")

def valOpt(opt:int,x:int,y:int):
    return opt < x or opt > y

def CheckVal() -> str:
    print(f"{red}[!] User not found !")
    sleep(1)
    print(f"{yellow}[1] Try with another username")
    print(f"{yellow}[2] Return to menu")
    print(f"{yellow}[3] Exit")
    opt=int(input(f"{yellow}[::] Number (from the above ones) >>> "))
    while valOpt(opt,1,3):
        checkOpt(opt, 'other')
        sleep(1)
        print(f"{yellow}[1] Try with another username")
        print(f"{yellow}[2] Return to menu")
        print(f"{yellow}[3] Exit")
        opt=int(input(f"{yellow}[::] Number (from the above ones) >>> "))
    if opt == 1:
        username=input(f"{yellow}[::] Username >>> ")
        while checkUser(username):
            checkOpt(opt, 'username')
        sleep(1)
        username=input(f"{yellow}[::] Username >>> ")
        return username
    elif opt == 2:
        clear()
        main()
    else:
        print(f"{yellow}[+] Thank you for using IAM 😁")
        sleep(0.8)
        print(f"{yellow}[+] See you next time 👋")
        sleep(0.8)
        exit(0)
    return False
    
ANS = ['yes', 'no']
NULL = ['', ' ']

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(fpath('IAM'))
    return f"{green}[✓] Files and dependencies uninstalled successfully !"

def Next() -> int:
    sleep(1)
    print(f"{yellow}[1] Return to menu")
    print(f"{yellow}[2] Exit")
    opt=int(input(f"{yellow}[::] Number (from the above ones) >>> "))
    while valOpt(opt,1,2):
        print(f"{red}[!] Invalid number !")
        sleep(1)
        print(f"{green}[*] Acceptable numbers: [1/2]")
        sleep(1)
        opt=int(input(f"{yellow}[::] Number (from the above ones) >>> "))
    return opt

def Class():
    main() if Next() == 1 else Exiting()

def Exiting():
    print(f"{yellow}[+] Exiting...")
    sleep(1)
    print(f"{yellow}[+] See you next time 👋")
    sleep(1)
    exit(0)
    
def checkCount(num: int) -> bool:
    return num < 1
    
def checkTag(tag: str) -> bool:
    return "#" not in tag or tag in NULL

def checkPath(path: str) -> bool:
    return path in NULL or "/" not in path or "\\" not in path

def AvActs() -> str:
    return f"""{yellow}
    1) Publish post(s)
    2) Change profile pic
    3) Upload story with pic
    4) Publish IGTV video
    5) Follow user(s)
    6) Unfollow user(s)
    """

def ScriptInfo():
    with open('IAM/config.json') as config:
        conf = json.load(config)
    f = f"{conf['name']}.py"
    fp = fpath(f) is None
    fsize = os.stat(fpath(f).st_size if fp else 0)
    print(f"{yellow}[+] Author ==> {conf['author']}")
    print(f"{yellow}[+] Github ==> @{conf['author']}")
    print(f"{yellow}[+] License ==> {conf['lice']}")
    print(f"{yellow}[+] Script's name ==> {conf['name']}")
    print(f"{yellow}[+] Script's version ==> {conf['version']}")
    print(f"{yellow}[+] Programming language(s) used ==> {conf['lang']}")
    print(f"{yellow}[+] Natural language ==> {conf['language']}")
    print(f"{yellow}[+] File size ==> {fsize} bytes")
    print(f"{yellow}[+] File path ==> {fpath(f)}")
    print(f"{yellow}[+] Number of lines ==> {conf['lines']}")
    print(f"{yellow}[+] API(s) used ==> {conf['api']}")
    print(f"{yellow}|======|GITHUB REPO INFO|======|")
    print(f"{yellow}[+] Stars ==> {conf['stars']}")
    print(f"{yellow}[+] Forks ==> {conf['forks']}")
    print(f"{yellow}[+] Open issues ==> {conf['issues']}")
    print(f"{yellow}[+] Closed issues ==> {conf['clissues']}")
    print(f"{yellow}[+] Open pull requests ==> {conf['prs']}")
    print(f"{yellow}[+] Closed pull requests ==> {conf['clprs']}")
    print(f"{yellow}[+] Discussions ==> {conf['discs']}")


def checkUser(username: str) -> bool:
    return username in NULL or len(username) > 30

def GetID(username: str) -> int:
    return loader.check_profile_id(username)

def checkID(id: int) -> bool:
    return id == None or len(id) < 3

TABLE = [
    [
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://new92.github.io/[/]"
    ],
    [
        "[b white]Github[/]: [i light_green]@new92[/]",
        "[green]https://github.com/new92[/]"
    ],
    [
        "[b white]Leetcode[/]: [i light_green]@new92[/]",
        "[green]https://leetcode.com/new92[/]"
    ],
    [
        "[b white]PyPI[/]: [i light_green]@new92[/]",
        "[green]https://pypi.org/user/new92[/]"
    ]
]

console = Console()
table = Table(show_footer=False)
centered = Align.center(table)

TaggedUsers=[]
Location=[]
Locations=[]
REC=[]
LOCATIONS=[]
LINKS=[]
IDS=[]
HASHTAGS=[]
FUFERS=[]
FUFING=[]
LTAGS=[]
LBU=[]
MSGIDS=[]
FILEIDS=[]
PHOTOIDS=[]
VIDEOIDS=[]
LBL=[]
BLOCKU=[]
REPLS=[]
STIDS=[]
STBTGS=[]
GTST=[]
HASHVID=[]
LOCLIKE=[]
random = None
sktp = None
count = 0


def main():
    print(banner())
    print(f"\n")
    print(f"{yellow}[+] IAM: Instagram Account Manager")
    print(f"\n")
    print(f"{yellow}[+] Python script for Managing your Instagram Account Remotely")
    print(f"\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print(f"\n")
    print(f"{yellow}[1] Display profile ID")
    print(f"{yellow}[2] Display security information")
    print(f"{yellow}[3] Display account info")
    print(f"{yellow}[4] Display pending follow requests")
    print(f"{yellow}[5] Display followers")
    print(f"{yellow}[6] Display the users you Follow")
    print(f"\n")
    print(f"{yellow}[7] Download my highlights")
    print(f"{yellow}[8] Download anonymous stories of other users")
    print(f"{yellow}[9] Download my saved posts")
    print(f"{yellow}[10] Download posts from my feed")
    print(f"\n")
    print(f"{yellow}[11] Publish post(s)")
    print(f"{yellow}[12] Enable/Disable notifications")
    print(f"{yellow}[13] Change profile pic")
    print(f"{yellow}[14] Upload story with pic")
    print(f"{yellow}[15] Publish IGTV video")
    print(f"\n")
    print(f"{yellow}[16] Follow user(s)")
    print(f"{yellow}[17] Unfollow user(s)")
    print(f"{yellow}[18] Accept follow request(s)")
    print(f"{yellow}[19] Reject follow request(s)")
    print(f"{yellow}[20] Follow user's followers")
    print(f"{yellow}[21] Follow user's following")
    print(f"\n")
    print(f"{yellow}[22] Send DM (Direct Message)")
    print(f"{yellow}[23] Send file")
    print(f"{yellow}[24] Send photo")
    print(f"{yellow}[25] Send video")
    print(f"\n")
    print(f"{yellow}[26] Like the posts from hashtag(s)")
    print(f"{yellow}[27] Like the posts from user(s)")
    print(f"{yellow}[28] Like the posts from location(s)")
    print(f"{yellow}[29] Like the posts from feed")
    print(f"\n")
    print(f"{yellow}[30] Comment by user")
    print(f"{yellow}[31] Set default reply to comments")
    print(f"{yellow}[32] Comment {red}<== CURRENTLY UNAVAILABLE")
    print(f"\n")
    print(f"{yellow}[33] Block User(s)")
    print(f"{yellow}[34] Get username from user ID")
    print(f"{yellow}[35] Get a list of all users you have blocked")
    print(f"\n")
    print(f"{yellow}[36] Create highlight(s)")
    print(f"{yellow}[37] Delete highlight(s)")
    print(f"{yellow}[38] Change the cover of highlight(s)")
    print(f"{yellow}[39] Display the highlights of user(s)")
    print(f"{yellow}[40] Retrieve information from highlight(s)")
    print(f"\n")
    print(f"{yellow}[41] Delete story")
    print(f"{yellow}[42] Get story viewers")
    print(f"{yellow}[43] Get stories by hashtags")
    print(f"{yellow}[44] Get stories by users")
    print(f"{yellow}[45] Retrieve information of a story")
    print(f"\n")
    print(f"{yellow}[46] Change country")
    print(f"{yellow}[47] Change bio")
    print(f"{yellow}[48] Gather information for a user")
    print(f"{yellow}[49] Get information about posts where user is tagged")
    print(f"{yellow}[50] Reset password")
    print(f"\n")
    print(f"{yellow}[51] Edit profile")
    print(f"{yellow}[52] Like/Unlike (post(s), reel(s), igtv(s) etc.)")
    print(f"{yellow}[53] Delete (post(s), reel(s), igtv(s) etc.)")
    print(f"{yellow}[54] Save/Unsave (post(s), reel(s), igtv(s) etc.)")
    print(f"\n")
    print(f"{yellow}[55] Set a specific time (from the current day) to execute an action")
    print(f"\n")
    print(f"{yellow}[56] Hide stories from a specific user")
    print(f"\n")
    print(f"{yellow}[57] Uninstall script")
    print(f"\n")
    print(f"{yellow}[999] Show script's info")
    print(f"\n")
    print(f"{yellow}[0] Exit")
    print(f"\n")
    option=int(input(f"{yellow}[::] Please enter a number (from the above ones): "))
    while valOpt(option,1,57) and opt != 999:
        checkOpt(option, "other")
        sleep(2)
        print(f"{yellow}[1] Display profile ID")
        print(f"{yellow}[2] Display security information")
        print(f"{yellow}[3] Display account info")
        print(f"{yellow}[4] Display pending follow requests")
        print(f"{yellow}[5] Display followers")
        print(f"{yellow}[6] Display the users you Follow")
        print(f"\n")
        print(f"{yellow}[7] Download my highlights")
        print(f"{yellow}[8] Download anonymous stories of other users")
        print(f"{yellow}[9] Download my saved posts")
        print(f"{yellow}[10] Download posts from my feed")
        print(f"\n")
        print(f"{yellow}[11] Publish post(s)")
        print(f"{yellow}[12] Enable/Disable notifications")
        print(f"{yellow}[13] Change profile pic")
        print(f"{yellow}[14] Upload story with pic")
        print(f"{yellow}[15] Publish IGTV video")
        print(f"\n")
        print(f"{yellow}[16] Follow user(s)")
        print(f"{yellow}[17] Unfollow user(s)")
        print(f"{yellow}[18] Accept follow request(s)")
        print(f"{yellow}[19] Reject follow request(s)")
        print(f"{yellow}[20] Follow user's followers")
        print(f"{yellow}[21] Follow user's following")
        print(f"\n")
        print(f"{yellow}[22] Send DM (Direct Message)")
        print(f"{yellow}[23] Send file")
        print(f"{yellow}[24] Send photo")
        print(f"{yellow}[25] Send video")
        print(f"\n")
        print(f"{yellow}[26] Like the posts from hashtag(s)")
        print(f"{yellow}[27] Like the posts from user(s)")
        print(f"{yellow}[28] Like the posts from location(s)")
        print(f"{yellow}[29] Like the posts from feed")
        print(f"\n")
        print(f"{yellow}[30] Comment by user")
        print(f"{yellow}[31] Set default reply to comments")
        print(f"{yellow}[32] Comment {red}<== CURRENTLY UNAVAILABLE")
        print(f"\n")
        print(f"{yellow}[33] Block User(s)")
        print(f"{yellow}[34] Get username from user ID")
        print(f"{yellow}[35] Get a list of all users you have blocked")
        print(f"\n")
        print(f"{yellow}[36] Create highlight(s)")
        print(f"{yellow}[37] Delete highlight(s)")
        print(f"{yellow}[38] Change the cover of highlight(s)")
        print(f"{yellow}[39] Display the highlights of user(s)")
        print(f"{yellow}[40] Retrieve information from highlight(s)")
        print(f"\n")
        print(f"{yellow}[41] Delete story")
        print(f"{yellow}[42] Get story viewers")
        print(f"{yellow}[43] Get stories by hashtags")
        print(f"{yellow}[44] Get stories by users")
        print(f"{yellow}[45] Retrieve information of a story")
        print(f"\n")
        print(f"{yellow}[46] Change country")
        print(f"{yellow}[47] Change bio")
        print(f"{yellow}[48] Gather information for a user")
        print(f"{yellow}[49] Get information about posts where user is tagged")
        print(f"{yellow}[50] Reset password")
        print(f"\n")
        print(f"{yellow}[51] Edit profile")
        print(f"{yellow}[52] Like/Unlike (post(s), reel(s), igtv(s) etc.)")
        print(f"{yellow}[53] Delete (post(s), reel(s), igtv(s) etc.)")
        print(f"{yellow}[54] Save/Unsave (post(s), reel(s), igtv(s) etc.)")
        print(f"\n")
        print(f"{yellow}[55] Set a specific time (from the current day) to execute an action")
        print(f"\n")
        print(f"{yellow}[56] Hide stories from a specific user")
        print(f"\n")
        print(f"{yellow}[57] Uninstall script")
        print(f"\n")
        print(f"{yellow}[999] Show script's info")
        print(f"\n")
        print(f"{yellow}[0] Exit") 
        print(f"\n")
        option=int(input(f"{yellow}[::] Please enter again a number (from the above ones): "))
    if option != 0:
        clear()
        print(f"\n")
        print(f"|--------------------|LOGIN|--------------------|")
        print(f"\n")
        username=input(f"{yellow}[::] Please enter your username: ")
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=input(f"{yellow}[::] Please enter again your username: ")
        while valUser(username):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        global globalu
        globalu = username
        password=input(f"{yellow}[::] Please enter your password: ")
        while password in NULL:
            print(f"{red}[✕] This field can't be blank !")
            sleep(1)
            password=input(f"{yellow}[::] Please enter again your password: ")
        password = password.strip()
        try:
            loader.login(username,password)
            client.login(username,password,True)
            api = instagram_private_api.Client(username, password)
            bot = instapy.InstaPy(username, password)
        except Exception as ex:
            Except(ex)

    elif option == 999:
        clear()
        ScriptInfo()
    
    elif option == 0:
        clear()
        print(f"{yellow}[+] Thank you for using IAM 😁")
        sleep(2)
        print(f"{yellow}[+] See you next time 👋")
        sleep(1)
        exit(0)

    elif option == 1:
        clear()
        try:
            print(f"{yellow}[+] Your ID >>> {GetID(username)}")
        except Exception as ex:
            Except(ex)

    elif option == 2:
        clear()
        try:
            sec=client.account_security_info()
            print(f"{yellow}[+] Phone number confirmed >>> {sec['is_phone_confirmed']}")
            print(f"{yellow}[+] 2FA (2 factor authentication) enabled >>> {sec['is_two_factor_enabled']}")
            print(f"{yellow}[+] Time-based One-Time Passwords (TOTP) authentication enabled >>> {sec['is_totp_two_factor_enabled']}")
            print(f"{yellow}[+] Trusted notifications enabled >>> {sec['is_trusted_notifications_enabled']}")
            print(f"{yellow}[+] Eligible for Whatsapp 2 factor authentication >>> {sec['is_eligible_for_whatsapp_two_factor']}")
            print(f"{yellow}[+] Whatsapp 2FA >>> {sec['is_whatsapp_two_factor_enabled']}")
            print(f"{yellow}[+] Backup codes >>> {sec['backup_codes']}")
            print(f"{yellow}[+] Trusted devices >>> {sec['trusted_devices']}")
            print(f"{yellow}[+] Reachable email >>> {sec['has_reachable_email']}")
            print(f"{yellow}[+] Eligible for trusted notifications >>> {sec['eligible_for_trusted_notifications']}")
            print(f"{yellow}[+] Eligible for multiple TOTP >>> {sec['is_eligible_for_multiple_totp']}")
            print(f"{yellow}[+] TOTP seeds >>> {sec['totp_seeds']}")
            print(f"{yellow}[+] Can add additional TOTP seed >>> {sec['can_add_additional_totp_seed']}")
        except Exception as ex:
            Except(ex)

    elif option == 3:
        clear()
        try:
            print(f"{yellow}[+] Your account info >>> {client.account_info()}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 4:
        clear()
        try:
            print(api.friendships_pending())
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 5:
        clear()
        print(GetID(username))
        id=int(input(f"{yellow}[::] ID >>> "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
        try:
            print(client.user_followers(id))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 6:
        clear()
        print(GetID(username))
        id=int(input(f"{yellow}[::] ID >>> "))
        while checkID(id):
            checkOpt(id,"id")
            sleep(1)
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
        try:
            print(client.user_following(id))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 7:
        clear()
        print(GetID(username))
        id=int(input(f"{yellow}[::] ID >>> "))
        while checkID(id):
            checkOpt(id,"id")
            sleep(1)
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
        try:
            print(f"{yellow}[+] Fetching highlights...")
            sleep(1)
            highlights=loader.download_highlights(id)
            sleep(1)
            print(f"{green}[✓] Fetch complete.")
            sleep(0.7)
            print(f"{yellow}[+] Highlights saved at >>> {fpath(highlights)}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 8:
        clear()
        count=int(input(f"{yellow}[+] Number of accounts >>> "))
        while valOpt(count,1,999):
            checkOpt(count,'other')
            sleep(1)
            count=int(input(f"{yellow}[::] Number of accounts >>> "))
        for i in range(count):
            username=input(f"{yellow}[::] Username >>> ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Username >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input(f"{yellow}[::] ID >>> "))
            while checkID(id):
                checkOpt(id,"id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            IDS.append(id)
        try:
            print(f"{yellow}[+] Fetching stories...")
            sleep(1)
            loader.download_stories(IDS)
            sleep(1)
            print(f"{green}[✓] Fetch complete.")
            sleep(0.7)
            print(f"{yellow}[+] Stories saved at >>> {fpath(':stories')}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 9:
        clear()
        count=int(input(f"{yellow}[?] Number of saved posts to download >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[?] Number of saved posts to download >>> "))
        try:
            print(f"{yellow}[+] Fetching posts...")
            sleep(1)
            loader.download_saved_posts(count)
            sleep(1)
            print(f"{green}[✓] Fetch complete.")
            sleep(0.7)
            print(f"{yellow}[+] Saved posts at >>> {fpath(':saved')}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 10:
        clear()
        count=int(input(f"{yellow}[?] Number of posts to download >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[?] Number of posts to download >>> "))
        try:
            print(f"{yellow}[+] Fetching posts...")
            sleep(1)
            loader.download_feed_posts(count)
            sleep(1)
            print(f"{green}[✓] Fetch complete.")
            sleep(0.7)
            print(f"{yellow}[+] Feed posts at >>> {fpath(':feed')}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 11:
        clear()
        count=int(input(f"{yellow}[::] Number of posts to post >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Number of posts to post >>> "))
        default = 'Check out my new post !'
        for i in range(count):
            path=input(f"{yellow}[::] Path to photo >>> ")
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=input(f"{yellow}[::] Path to photo (to be uploaded) >>> ")
            sleep(2)
            print(f"{yellow}>>>CAPTION<<<")
            sleep(1)
            print(f"{yellow}[+] Default: {default}")
            sleep(2)
            print(f"{yellow}[*] Hit <Enter> to apply the default caption")
            sleep(2)
            caption=input(f"{yellow}[::] Caption >>> ")
            if caption == '':
                caption = default
            print(f"{yellow}>>>TAGS<<<")
            sleep(2)
            print(f"{yellow}[+] Default: {ANS[1]}")
            sleep(2)
            print(f"{yellow}[*] Hit <Enter> to apply the default option")
            sleep(2)
            print(f"{green}[*] Acceptable answers: {ANS}")
            sleep(2)
            tags=input(f"{yellow}[?] Tag users >>> ")
            while tags.lower() not in ANS or tags in NULL:
                if tags in NULL:
                    print(f"{red}[!] This field can't be empty !")
                else:
                    print(f"{red}[!] Invalid answer !")
                    sleep(1)
                    print(f"{green}[*] Acceptable answers: {ANS}")
                sleep(1)
                tags=input(f"{yellow}[?] Tag users >>> ")
            if tags.lower() == ANS[0]:
                print(f"{yellow}[+] Default: 1")
                sleep(2)
                print(f"{yellow}[*] Hit <Enter> to apply the default option")
                sleep(1)
                count=input(f"{yellow}[?] Number of users to tag >>> ")
                if count == '':
                    username=input(f"{yellow}[::] Username >>> ")
                    while checkUser(username):
                        checkOpt(username, "username")
                        sleep(1)
                        username=input(f"{yellow}[::] Username >>> ")
                    while valUser(username):
                        CheckVal()
                    username = username.lower().strip()
                else:
                    while checkCount(count):
                        checkOpt(count,"other")
                        sleep(1)
                        count=int(input(f"{yellow}[?] Number of users to tag >>> "))
                    for i in range(count):
                        utag=input(f"{yellow}[::] Username No{i+1} >>> ")
                        while checkUser(utag):
                            checkOpt(utag,"username")
                            sleep(1)
                            utag=input(f"{yellow}[::] Username No{i+1} >>> ")
                        while valUser(utag):
                            CheckVal()
                        utag = utag.strip().lower()
                        TaggedUsers.append(utag)
            print(f"{yellow}>>>LOCATION<<<")
            sleep(2)
            print(f"{yellow}[+] Default: {ANS[1]}")
            sleep(1)
            print(f"{yellow}[*] Hit <Enter> to apply the default option")
            sleep(2)
            print(f"{green}[*] Acceptable answers: {ANS}")
            sleep(1)
            loc=input(f"{yellow}[?] Include location(s) >>> ")
            if loc.lower() == ANS[0]:
                count=int(input(f"{yellow}[?] Number >>> "))
                while checkCount(count):
                    checkOpt(count,"other")
                    sleep(1)
                    count=int(input(f"{yellow}[?] Number >>> "))
                for i in range(count):
                    location=input(f"{yellow}[::]Location No{i+1}: ")
                    while location in NULL:
                        print(f"{red}[✕] This field can't be blank !")
                        sleep(1)
                        location=input(f"{yellow}[::] Location No{i+1}: ")
                    LOCATIONS.append(location)
                    print(f"{green}[✓] Location added !")
                try:
                    client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                    sleep(2)
                    print(f"{green}[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)
            if tags.lower() in ANS and loc.lower() in ANS:
                try:
                    client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                    sleep(2)
                    print(f"{green}[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif tags.lower() in ANS and loc.lower() in ANS:
                try:
                    client.photo_upload(path=path,caption=caption,tags=TaggedUsers)
                    sleep(2)
                    print(f"{green}[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif tags.lower() in ANS and loc.lower() in ANS:
                try:
                    client.photo_upload(path=path,caption=caption,location=LOCATIONS)
                    sleep(2)
                    print(f"{green}[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif tags.lower() in ANS and loc.lower() in ANS:
                try:
                    client.photo_upload(path=path,caption=caption)
                    sleep(2)
                    print(f"{green}[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 12:
        clear()
        EN = ["enable","disable"]
        print(f"{green}[*] Acceptable answers: {EN}")
        sleep(1)
        endis=input(f"{yellow}[?] ENTER >>> ")
        while endis.lower() not in EN or endis in NULL:
            if endis in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid input !")
            sleep(1)
            print(f"{green}[*] Acceptable answers: {EN}")
            sleep(1)
            endis=input(f"{yellow}[?] Notifications to enable >>> ")
        if endis.lower() == EN[0]:
            noti = ['posts', 'reels', 'stories', 'videos']
            print(f"{green}[*] Notifications available for: {noti}")
            sleep(2)
            action=input(f"{yellow}[?] Notifications to enable >>> ")
            while action.lower() not in noti or action in NULL:
                if action in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                else:
                    print(f"{red}[!] Invalid input !")
                sleep(1)
                print(f"{green}[*] Acceptable answers: {noti}")
                sleep(1)
                action=input(f"{yellow}[?] Please enter again the notifications to enable: ")
            if action.lower() == "posts":
                print(GetID(globalu))
                uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                try:
                    print(f"{green}[✓] Post notifications enabled !") if client.enable_posts_notifications(uid) else print(f"{red}[✕] Unable to enable post notifications !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif action.lower() == "reels":
                print(GetID(globalu))
                uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                try:
                    print(f"{green}[✓] Reels notifications enabled !") if client.enable_reels_notifications(uid) else print(f"{red}[✕] Unable to enable reels notifications !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif action.lower() == "stories":
                print(GetID(globalu))
                uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                while checkID(uid):
                    checkOpt(uid, 'id')
                    sleep(1)
                    uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                try:
                    print(f"{green}[✓] Stories notifications enabled !") if client.enable_stories_notifications(uid) else print(f"{yellow}[✕] Unable to enable stories notifications !")
                    Class()
                except Exception as ex:
                    Except(ex)

            else:
                print(GetID(globalu))
                uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                try:
                    print(f"{green}[✓] Stories video enabled !") if client.enable_video_notifications(uid) else print(f"{yellow}[✕] Unable to enable video notifications !")
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 13:
        clear()
        path=input(f"{yellow}[::] Path to pic >>> ")
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=input(f"{yellow}[::] Path to pic >>> ")
        try:
            client.account_change_picture(path)
            print(f"{green}[✓] Your profile pic changed !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 14:
        clear()
        path=input(f"{yellow}[::] Path to photo >>> ")
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=input(f"{yellow}[::] Path to photo >>> ")
        sleep(2)
        print(f"{green}[*] Acceptable answers: {ANS}")
        sleep(1)
        AddCaption=input(f"{yellow}[?] Add caption >>> ")
        while AddCaption.lower() not in ANS or AddCaption in NULL:
            if AddCaption in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid input !")
                sleep(1)
                print(f"{green}[*] Acceptable answers: {ANS}")
            sleep(1)
            AddCaption=input(f"{yellow}[?] Add caption >>> ")
        if AddCaption.lower() == ANS[0]:
            default = 'Check out my new story !'
            print(f"{yellow}[+] Default: {default}")
            sleep(1)
            print(f"{yellow}[*] Hit <Enter> to apply the default option")
            sleep(2)
            caption=input(f"{yellow}[::] Caption >>> ")
            while caption in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                caption=input(f"{yellow}[::] Caption >>> ")
            if caption == '':
                caption = default
            else:
                caption=input(f"{yellow}[::] Caption >>> ")
                while caption in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    caption=input(f"{yellow}[::] Caption >>> ")
        sleep(1)
        print(f"{green}[*] Acceptable answers: {ANS}")
        sleep(1)
        AddMention=input(f"{yellow}[?] Tag other users >>> ")
        while AddMention.lower() not in ANS or AddMention in NULL:
            if AddMention in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid input !")
            sleep(1)
            print(f"{green}[*] Acceptable answers: {ANS}")
            sleep(1)
            mention=input(f"{yellow}[?] Tag other users >>> ")
        if AddMention.lower() == ANS[0]:
            MENTIONS = []
            count=int(input(f"{yellow}[?] Number >>> "))
            while checkCount(count):
                checkOpt(count,"other")
                sleep(1)
                count=int(input(f"{yellow}[?] Number >>> "))
            for i in range(count):
                mention=input(f"{yellow}[::] Username No{i+1} >>> ")
                while checkUser(mention):
                    checkOpt(mention, "username")
                    sleep(1)
                    mention=input(f"{yellow}[::] Username No{i+1} >>> ")
                MENTIONS.append(mention.lower().strip())
        sleep(1)
        print(f"{green}[*] Acceptable answers: {ANS}")
        sleep(1)
        AddLoc=input(f"{yellow}[?] Add location >>> ")
        while AddLoc.lower() not in ANS or AddLoc in NULL:
            if AddLoc in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid input !")
            sleep(1)
            print(f"{green}[*] Acceptable answers: {ANS}")
            sleep(1)
            AddLoc=input(f"{yellow}[?] Add location >>> ")
        if AddLoc.lower() == ANS[0]:
            count=int(input(f"{yellow}[?] Number of locations >>> "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input(f"{yellow}[?] Number >>> "))
            for i in range(count):
                loc=input(f"{yellow}[::] Location No{i+1} >>> ")
                while loc == None:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    loc=input(f"{yellow}[::] Location No{i+1} >>> ")
                LOCATIONS.append(loc)
        sleep(1)
        print(f"{green}[*] Acceptable answers: {ANS}")
        sleep(1)
        AddLinks=input(f"{yellow}[?] Include url(s) >>> ")
        while AddLinks.lower() not in ANS or AddLinks in NULL:
            if AddLinks in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid input !")
            sleep(1)
            AddLinks=input(f"{yellow}[?] Include url(s) >>> ")
        if AddLinks.lower() == ANS[0]:
            count=int(input(f"{yellow}[?] Number >>> "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input(f"{yellow}[?] Number >>> "))
            for i in range(count):
                url=input(f"{yellow}[::] Url No{i+1} >>> ")
                while "/" not in url and ("https" not in url or "http" not in url) or url in NULL:
                    print(f"{red}[!] Invalid URL !")
                    sleep(1)
                    print(f"{green}[+] Acceptable URL format >>> https://example.com")
                    sleep(1)
                    url=input(f"{yellow}[::] Url No{i+1} >>> ")
                LINKS.append(url.lower().strip())
        sleep(1)
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(0.8)
        AddHash=input(f"{yellow}[?] Include hashtags >>> ")
        while AddHash.lower() not in ANS or AddHash in NULL:
            if AddHash in NULL:
                print(f"{yellow}[✕] This field can't be blank !")
            else:
                print(f"{yellow}[!] Invalid input !")
            sleep(1)
            AddHash=input(f"{yellow}[?] Include hashtags >>> ")
        if AddHash.lower() in ANS[0]:
            count=int(input(f"{yellow}[?] Number >>> "))
            while checkCount(count):
                checkOpt(count,"other")
                sleep(1)
                count=int(input(f"{yellow}[?] Number >>> "))
            for i in range(count):
                hashtag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
                while hashtag in NULL or "#" not in hashtag:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    hashtag=input(f"{yellow}[::] Please enter again the hashtag No{i+1}: ")
                HASHTAGS.append(hashtag)
        if AddCaption and AddMention and AddLoc and AddLinks and AddHash:
            try:
                client.photo_upload_to_story(path, caption, mentions=MENTIONS, locations=LOCATIONS, links=LINKS, hashtags=HASHTAGS)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)
        elif not AddCaption and not AddMention and not AddLoc and not AddLinks and not AddHash:
            try:
                client.photo_upload_to_story(path)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)
        elif not AddCaption and AddMention and AddLoc and AddLinks and AddHash:
            try:
                client.photo_upload_to_story(path, mentions=MENTIONS, locations=LOCATIONS, links=LINKS, hashtags=HASHTAGS)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption and not AddMention and AddLoc and AddLinks and AddHash:
            try:
                client.photo_upload_to_story(path, caption, locations=LOCATIONS, links=LINKS, hashtags=HASHTAGS)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption and AddMention and not AddLoc and AddLinks and AddHash:
            try:
                client.photo_upload_to_story(path, caption, mentions=MENTIONS, links=LINKS, hashtags=HASHTAGS)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption and AddMention and AddLoc and not AddLinks and AddHash:
            try:
                client.photo_upload_to_story(path, caption, mentions=MENTIONS, locations=LOCATIONS, hashtags=HASHTAGS)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption and AddMention and AddLoc and AddLinks and not AddHash:
            try:
                client.photo_upload_to_story(path, caption, mentions=MENTIONS, locations=LOCATIONS)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)
        elif not AddCaption and not AddMention and AddLoc and AddLinks and AddHash:
            try:
                client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption and not AddMention and not AddLoc and AddLinks and AddHash:
            try:
                client.photo_upload_to_story(path, caption, links=LINKS, hashtags=HASHTAGS)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 15:
        clear()
        hashtag = None
        location = None
        path=input(f"{yellow}[::] Path to video >>> ")
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=input(f"{yellow}[::] Path to video >>> ")
        sleep(0.5)
        print(f"{yellow}[+] Acceptable answers >>> {ANS}")
        sleep(0.8)
        incap=input(f"{yellow}[?] Include caption >>> ")
        while incap.lower() not in ANS or incap in NULL:
            if incap in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid input !")
            sleep(1)
            incap=input(f"{yellow}[?] Include caption >>> ")
        if incap.lower() == ANS[0]:
            default = 'Check out my new video !'
            sleep(1)
            print(f"{yellow}[+] Default: {default}")
            sleep(2)
            print(f"{yellow}[*] Hit <Enter> to apply the default caption")
            sleep(2)
            caption=input(f"{yellow}[::] Caption ")
            if caption == '':
                caption = default
        sleep(0.5)
        print(f"{yellow}[+] Acceptable answers: {ANS}")
        sleep(0.8)
        intag=input(f"{yellow}[::] Include hashtags >>> ")
        while intag.lower() not in ANS or intag in NULL:
            if intag in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid input !")
            sleep(1)
            intag=input(f"{yellow}[::] Include hashtags >>> ")
        if intag.lower() == ANS[0]:
            count=int(input(f"{yellow}[?] Number >>> "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input(f"{yellow}[?] Number >>> "))
            for i in range(count):
                hashtag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
                while checkTag(hashtag):
                    if hashtag in NULL:
                        print(f"{red}[✕] This field can't be blank !")
                    else:
                        print(f"{red}[!] Invalid hashtag !")
                    sleep(1)
                    hashtag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
                HASHVID.append(hashtag)
                sleep(1)
                print(f"{green}[✓] Hashtag added.")
        sleep(1)
        inloc=input(f"{yellow}[?] Include location(s) >>> ")
        while inloc.lower() not in ANS or inloc in NULL:
            if inloc in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid answer !")
            sleep(1)
            print(f"{green}[+] Acceptable answers: {ANS}")
            sleep(0.8)
            inloc=input(f"{yellow}[?] Include location(s) >>> ")
        if inloc in ANS[:9]:
            count=int(input(f"{yellow}[?] Number >>> "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input(f"{yellow}[?] Number >>> "))
            for i in range(count):
                location=input(f"{yellow}[::] Location No{i+1} >>> ")
                while location in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    location=input(f"{yellow}[::] Location No{i+1} >>> ")
        try:
            client.video_upload(path,caption,usertags=HASHVID,location=location)
            sleep(2)
            print(f"{green}[✓] Video uploaded.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 16:
        clear()
        count=int(input(f"{yellow}[::] Number of accounts to follow >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Number of accounts to follow >>> "))
        if count == 1:
            username=input(f"{yellow}[::] Username >>> ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Username >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            try:
                client.user_follow(id)
                sleep(2)
                print(f"{green}[✓] Followed {username}.")
                Class()
            except Exception as ex:
                print(f"{red}[✕] Unable to follow {username}")
                Except(ex)
        else:
            for i in range(count):
                username=input(f"{yellow}[::] Username No{i+1} >>> ")
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=input(f"{yellow}[::] Username No{i+1} >>> ")
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                sleep(0.5)
                print(GetID(username))
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                while checkID(id):
                    checkOpt(id, "id")
                    sleep(1)
                    id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                try:
                    client.user_follow(id)
                    sleep(2)
                    print(f"{green}[✓] Followed {username}.")
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 17:
        clear()
        count=int(input(f"{yellow}[::] Number of accounts to unfollow >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Number of accounts to unfollow >>> "))
        if count == 1: 
            username=input(f"{yellow}[::] Username >>> ")
            while checkUser(username):
                checkOpt(username, username)
                sleep(1)
                username=input(f"{yellow}[::] Username >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            sleep(0.5)
            print(GetID(username))
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            try:
                client.user_unfollow(id)
                sleep(1)
                print(f"{green}[✓] unfollowed {username}.")
            except Exception as ex:
                print(f"{red}[✕] Unable to unfollow {username}.")
        else:
            for i in range(count):
                username=input(f"{yellow}[::] Username No{i+1} >>> ")
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=input(f"{yellow}[::] Username No{i+1} >>> ")
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                try:
                    client.user_unfollow(uid)
                    sleep(2)
                    print(f"{green}[✓] unfollowed {username}.")
                except Exception as e:
                    print(f"{red}[✕] Unable to unfollow {username}.")
                    Except(ex)
        Class()

    elif option == 18:
        clear()
        count=int(input(f"{yellow}[::] Follow requests to accept (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Follow requests to accept (num) >>> "))
        try:
            bot.accept_follow_requests(count,3)
            print(f"{green}[✓] Follow requests accepted.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 19:
        clear()
        count=int(input(f"{yellow}[::] Follow requests to remove (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Follow requests to remove (num) >>> "))
        try:
            bot.remove_follow_requests(count,3)
            print(f"{green}[✓] Follow requests removed !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 20:
        clear()
        count=int(input(f"{yellow}[::] Users to follow (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Users to follow (num) >>> "))
        sleep(0.9)
        countu=int(input(f"{yellow}[?] Users to follow their followers (num) >>> "))
        while checkCount(countu):
            checkOpt(countu, "other")
            sleep(1)
            countu=int(input(f"{yellow}[?] Users to follow their followers (num) >>> "))
        for i in range(countu):
            username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            FUFERS.append(username)
            print(f"{green}[✓] User added.")
            sleep(0.5)
        try:
            print(f"{yellow}[+] Initiating following process...")
            sleep(0.5)
            bot.follow_user_followers(FUFERS,count)
            sleep(2)
            print(f"{green}[✓] Users followed.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 21:
        clear()
        username=input(f"{yellow}[::] Target username >>> ")
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=input("[::] Target username >>> ")
        while valUser(username):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        profile = loader.Profile.from_username(loader.context, username)
        L = [following.username for following in profile.get_followees()]
        for i in range(len(L)):
            print(GetID(L[i]))
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            try:
                client.user_follow(id)
                sleep(2)
                print(f"{green}[✓] Followed {L[i]}.")
            except Exception as ex:
                print(f"{red}[✕] Unable to follow {L[i]}")
            Class()

    elif option == 22:
        clear()
        count=int(input(f"{yellow}[::] Messages to send (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Messages (num) >>> "))
        for i in range(count):
            text=input(f"{yellow}[::] Text >>>  ")
            while text in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                text=input(f"{yellow}[::] Text >>>  ")
            sleep(0.5)
            count=int(input(f"{yellow}[::] Receivers (num) >>> "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input(f"{yellow}[::] Receivers (num) >>> "))
            for j in range(count):
                username=input(f"{yellow}[::] Username No{j+1} >>> ")
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=input(f"{yellow}[::] Username No{j+1} >>> ")
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                sleep(0.5)
                print(GetID(username))
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                while checkID(id):
                    checkOpt(id, "id")
                    sleep(1)
                    id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                MSGIDS.append(id)
                try:
                    client.direct_send(text,MSGIDS)
                    sleep(1)
                    print(f"{green}[✓] Message sent.")
                except Exception as ex:
                    print(f"{red}[✕] Unable to send message to {MSGIDS[j]}")
        Class()

    elif option == 23:
        clear()
        path=input(f"{yellow}[::] Path to file >>> ")
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=input(f"{yellow}[::] Path to file >>> ")
        sleep(0.8)
        count=int(input(f"{yellow}[::] Receivers (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Receivers (num) >>>  "))
        for i in range(count):
            username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            sleep(0.8)
            print(GetID(username))
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            FILEIDS.append(id)
            try:
                client.direct_send_file(path,FILEIDS)
                sleep(1.5)
                print(f"{green}[✓] File sent.")
            except Exception as ex:
                print(f"{red}[✕] Unable to send photo to {FILEIDS[i]}...")
                sleep(1)
        Class()

    elif option == 24:
        clear()
        path=input(f"{yellow}[::] Path to photo >>> ")
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=input(f"{yellow}[::] Path to photo >>> ")
        sleep(0.7)
        count=int(input(f"{yellow}[::] Receivers (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Receivers (num) >>> "))
        for i in range(count):
            username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            sleep(0.8)
            print(GetID(username))
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            PHOTOIDS.append(id)
            try:
                client.direct_send_photo(path, PHOTOIDS)
                sleep(2)
                print(f"{green}[✓] Photo sent.")
            except Exception as ex:
                print(f"{red}[✕] Unable to send photo to {PHOTOIDS[i]}...")
                sleep(1)
        Class()

    elif option == 25:
        clear()
        path=input(f"{yellow}[::] Path to video >>> ")
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=input(f"{yellow}[::] Path to video >>> ")
        sleep(0.7)
        count=int(input(f"{yellow}[::] Receivers (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Receivers (num) >>> "))
        for i in range(count):
            username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            sleep(0.8)
            print(GetID(username))
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            VIDEOIDS.append(id)
            try:
                client.direct_send_video(path,VIDEOIDS)
                sleep(2)
                print(f"{green}[✓] Video sent.")
            except Exception as ex:
                print(f"{red}[✕] Unable to send video to {VIDEOIDS[i]}...")
                sleep(1)
        Class()

    elif option == 26:
        clear()
        count=int(input(f"{yellow}[::] Hashtags (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Hashtags (num) >>> "))
        sleep(0.5)
        nump=int(input(f"{yellow}[::] Posts (num) >>> "))
        while checkCount(nump):
            checkOpt(nump, "other")
            sleep(1)
            nump=int(input(f"{yellow}[::] Posts (num) >>> "))
        for i in range(count):
            hashtag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
            while checkTag(hashtag):
                print(f"[!] Invalid hashtag !")
                sleep(1)
                if "#" not in hashtag:
                    print(f"{yellow}[+] Please include the   #   symbol")
                sleep(1)
                hashtag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
            LTAGS.append(hashtag)
            print(f"{green}[✓] Hashtag added.")
            sleep(0.5)
        sleep(0.6)
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(0.9)
        rtags=input(f"{yellow}[::] Like random hashtags >>> ")
        while rtags.lower() not in ANS or rtags in NULL:
            if rtags in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid answer !")
                sleep(0.9)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            rtags=input(f"{yellow}[::] Like random hashtags >>> ")
        random = rtags.lower() == ANS[0]
        try:
            bot.like_by_tags(LTAGS, random, count)
            sleep(2)
            print(f"{green}[✓] Posts liked.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 27:
        clear()
        countu=int(input(f"{yellow}[::] Accounts (num) >>> "))
        while checkCount(countu):
            checkOpt(countu, "other")
            sleep(1)
            countu=int(input(f"{yellow}[::] Accounts >>> "))
        sleep(0.9)
        count=int(input(f"{yellow}[::] Posts to like (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Posts to like >>> "))
        sleep(0.5)
        if countu == 1:
            username=input(f"{yellow}[::] Username >>> ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Username >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            LBU.append(username)
        else:
            for i in range(countu):
                username=input(f"{yellow}[::] Username No{i+1} >>> ")
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=input(f"{yellow}[::] Username No{i+1} >>> ")
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                LBU.append(username)
        try:
            bot.like_by_users(LBU, count)
            sleep(2)
            print(f"{green}[✓] Posts liked.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 28:
        clear()
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        rand=input(f"{yellow}[::] Like posts randomly >>> ")
        while rand.lower() not in ANS or rand in NULL:
            if rand in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid answer !")
                sleep(1)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            rand=input(f"{yellow}[::] Like posts randomly >>> ")
        random = rand.lower() == ANS[0]
        sleep(0.5)
        numloc=int(input(f"{yellow}[::] Locations (num) >>> "))
        while checkCount(numloc):
            checkOpt(numloc, "other")
            sleep(1)
            numloc=int(input(f"{yellow}[::] Locations >>> "))
        sleep(1)
        countp=int(input(f"{yellow}[::] Posts per loc (num) >>> "))
        while checkCount(countp):
            checkOpt(countp, "other")
            sleep(1)
            countp=int(input(f"{yellow}[::] Posts per loc >>> "))
        for i in range(numloc):
            location=input(f"{yellow}[::] Location No{i+1} >>> ")
            while location in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                location=input(f"{yellow}[::] Location No{i+1} >>> ")
            LOCLIKE.append(location)
        try:
            bot.like_by_locations(LOCLIKE, number=countp, randomize=random)
            sleep(2)
            print(f"{green}[✓] Posts liked.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 29:
        clear()
        count=int(input(f"{yellow}[::] Posts to like (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Posts to like >>> "))
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        rand=input(f"{yellow}[::] Like randomly >>> ")
        while rand.lower() not in ANS or rand in NULL:
            if rand in NULL:
                print(f"{red}[!] This field can't be empty !")
            else:
                print(f"{red}[!] Invalid answer !")
                sleep(1)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            rand=input(f"{yellow}[::] Like randomly >>> ")
        rmize = rand.lower() == ANS[0]
        if count == 1:
            try:
                bot.like_by_feed(count, rmize)
                sleep(2)
                print(f"{green}[✓] Posts liked.")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(count):
                try:
                    bot.like_by_feed(count, rmize)
                    sleep(1)
                    print(f"{green}[✓] Posts liked.")
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 30:
        clear()
        amo=int(input(f"{yellow}[::] Posts to like (num) >>> "))
        while checkCount(amo):
            checkOpt(amo, "other")
            sleep(1)
            amo=int(input(f"{yellow}[::] Posts to like >>> "))
        sleep(0.7)
        username=input(f"{yellow}[::] Username >>> ")
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=input(f"{yellow}[::] Username >>> ")
        while valUser(username):
            if type(CheckVal()) == bool:
                    CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        sleep(0.6)
        print(GetID(username))
        id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            id=int(input(f"{yellow}[::] ID >>> "))
        try:
            bot.comment_user(id,amo)
            sleep(2)
            print(f"{green}[✓] Commented.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 31:
        clear()
        count=int(input(f"{yellow}[::] Replies (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Replies >>> "))
        for i in range(count):
            reply=input(f"{yellow}[::] Reply No{i+1} >>> ")
            while reply in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                reply=input(f"{yellow}[::] Reply No{i+1} >>> ")
            REPLS.append(reply)
        try:
            bot.set_comment_replies(REPLS)
            sleep(2)
            print(f"{green}[✓] Default replies applied.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 33:
        clear()
        count=int(input(f"{yellow}[::] Users to block (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Users to block >>> "))
        if count == 1:
            username=input(f"{yellow}[::] Username >>> ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Username >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            sleep(0.7)
            print(GetID(username))
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID >>> "))
            try:
                bot.block_users([id])
                sleep(1.5)
                print(f"{green}[✓] User blocked.")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(count):
                username=input(f"{yellow}[::] Username No{i+1} >>> ")
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=input(f"{yellow}[::] Username No{i+1} >>>  ")
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                sleep(0.7)
                print(GetID(username))
                uid = int(input(f"{yellow}[::] ID (as shown above) >>> "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid = int(input(f"{yellow}[::] ID >>> "))
                BLOCKU.append(uid)
            try:
                bot.block_users(BLOCKU)
                sleep(2)
                print(f"{green}[✓] Users blocked.")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 34:
        clear()
        uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
        while checkID(uid):
            checkOpt(uid, "id")
            sleep(1)
            uid=int(input(f"{yellow}[::] ID >>> "))
        try:
            print(f"{yellow}[+] Username >>> {client.username_from_user_id(uid)}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 35:
        clear()
        try:
            print(f"{yellow}[+] Blocked users ")
            print(f"\n")
            print(api.blocked_user_list())
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 36:
        clear()
        counti=int(input(f"{yellow}[::] Highlights (num) >>> "))
        while checkCount(counti):
            checkOpt(counti, "other")
            sleep(1)
            counti=int(input(f"{yellow}[::] Highlights >>> "))
        if counti == 1:
            title=input(f"{yellow}[::] Title >>> ")
            while title in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                title=input(f"{yellow}[::] Title >>> ")
            sleep(0.6)
            count=int(input(f"{yellow}[::] Stories to add (num) >>> "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input(f"{yellow}[::] Stories to add >>> "))
            for i in range(count):
                story_id=int(input(f"{yellow}[::] Story ID No{i+1} >>> "))
                while not story_id:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    story_id=int(input(f"{yellow}[::] Story ID No{i+1} >>> "))
                STIDS.append(story_id)
            try:
                client.highlight_create(title,STIDS)
                sleep(2)
                print(f"{green}[✓] Highlight created.")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(counti):
                title=input(f"{yellow}[::] Highlight title No{i+1} >>> ")
                while title in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    title=input(f"{yellow}[::] Highlight title No{i+1} >>> ")
                sleep(0.5)
                count=int(input(f"{yellow}[::] Stories to add (num) >>> "))
                while checkCount(count):
                    checkOpt(count, "other")
                    sleep(1)
                    count=int(input(f"{yellow}[::] Stories to add >>> "))
                for i in range(count):
                    story_id=int(input(f"{yellow}[::] Story ID No{i+1} >>> "))
                    while not story_id:
                        print(f"{red}[✕] This field can't be blank !")
                        sleep(1)
                        story_id=int(input(f"{yellow}[::] Story ID No{i+1} >>> "))
                    STIDS.append(story_id)
                try:
                    client.highlight_create(title,STIDS)
                    sleep(2)
                    print(f"{green}[✓] Highlight created.")
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 37:
        clear()
        count=int(input(f"{yellow}[::] Highlights to delete (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Highlights to delete >>> "))
        if count == 1:
            hid=int(input(f"{yellow}[::] Highlight ID >>> "))
            while not hid:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                hid=int(input(f"{yellow}[::] Highlight ID >>> "))
            try:
                api.highlight_delete(hid)
                sleep(2)
                print(f"{green}[✓] Highlight deleted.")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(count):
                hid=int(input(f"{yellow}[::] Highlight ID No{i+1} >>> "))
                while not hid:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    hid=int(input(f"{yellow}[::] Highlight ID No{i+1} >>> "))
                try:
                    api.highlight_delete(hid)
                    sleep(2)
                    print(f"{green}[✓] Highlight deleted.")
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 38:
        clear()
        count=int(input(f"{yellow}[::] Covers to change (num) >>> "))
        while checkCount(count, "other"):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Covers to change (num) >>> "))
        if count == 1:
            url=input(f"{yellow}[::] Highlight URL >>> ")
            while url in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                url=input(f"{yellow}[::] Highlight URL >>> ")
            sleep(0.9)
            print(Get_Hpk(url))
            pk=int(input(f"{yellow}[::] Highlight ID (as shown above) >>> "))
            while not pk:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                pk=int(input(f"{yellow}[::] Highlight ID >>> "))
            sleep(0.8)
            path=input(f"{yellow}[::] New cover path >>> ")
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=input(f"{yellow}[::] New cover path >>> ")
            try:
                client.highlight_change_cover(pk,path) 
                sleep(2)
                print(f"{green}[✓] Highlight cover changed.")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(count):
                url=input(f"{yellow}[::] Highlight URL >>> ")
                while url in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    url=input(f"{yellow}[::] Highlight URL >>> ")
                sleep(1)
                print(Get_Hpk(url))
                pk=int(input(f"{yellow}[::] Highlight ID (as shown above) >>> "))
                while not pk:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    pk=int(input(f"{yellow}[::] Highlight ID (as shown above) >>> "))
                sleep(0.8)
                path=input(f"{yellow}[::] New cover path >>> ")
                while checkPath(path):
                    checkOpt(path, "path")
                    sleep(1)
                    path=input(f"{yellow}[::] New cover path >>> ")
                try:
                    client.highlight_change_cover(pk,path) 
                    sleep(2)
                    print(f"{green}[✓] Highlight cover changed.")
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 39:
        clear()
        countu=int(input(f"{yellow}[::] Users (num) >>> "))
        while checkCount(countu):
            checkOpt(countu, "other")
            sleep(1)
            countu=int(input(f"{yellow}[::] Users (num) >>> "))
        if countu == 1:
            username=input(f"{yellow}[::] Please enter the username: ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Please enter the username: ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            sleep(0.8)
            print(GetID(username))
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            sleep(0.7)
            number=int(input(f"{yellow}[::] Highlights to print (num) >>> "))
            while checkCount(number):
                checkOpt(number, "count")
                sleep(1)
                number=int(input(f"{yellow}[::] Highlights to print >>> "))
            try:
                HL = client.user_highlights(id,number)
                for i in range(len(HL)):
                    print(f"{yellow}[+] Highlight >>> {L[i]}")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(countu):
                username=input(f"{yellow}[::] Username >>> ")
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=input(f"{yellow}[::] Username >>> ")
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                sleep(0.5)
                print(GetID(username))
                id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                while checkID(id):
                    checkOpt(id, "id")
                    sleep(1)
                    id=int(input(f"{yellow}[::] ID >>> "))
                sleep(0.5)
                number=int(input(f"{yellow}[::] Highlights to print (num) >>> "))
                while checkCount(number):
                    checkOpt(number, "count")
                    sleep(1)
                    number=int(input(f"{yellow}[::] Highlights to print >>> "))
                try:
                    HL = client.user_highlights(id,number)
                    for j in range(len(HL)):
                        print(f"{yellow}[+] Highlight >>> {HL[j]}")
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 40:
        clear()
        counti=int(input(f"{yellow}[::] Highlights (num) >>> "))
        while checkCount(counti):
            checkOpt(counti, "other")
            sleep(1)
            counti=int(input(f"{yellow}[::] Highlights (num) >>> "))
        if counti == 1:
            url=input(f"{yellow}[::] Highlight URL >>> ")
            while url in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                url=input(f"{yellow}[::] Highlight URL >>> ")
            sleep(1)
            print(Get_Hpk(url))
            pk=int(input(f"{yellow}[::] Highlight ID (as shown above) >>> "))
            while not pk:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                pk=int(input(f"{yellow}[::] Highlight ID >>> "))
            try:
                sleep(1)
                print(f"{green}[✓] Retrieved information.")
                sleep(0.7)
                print(client.highlight_info(pk))
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(counti):
                url=input(f"{yellow}[::] Highlight URL >>> ")
                while url in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                    sleep(1)
                    url=input(f"{yellow}[::] Highlight URL >>> ")
                sleep(0.8)
                print(Get_Hpk(url))
                pk=int(input(f"{yellow}[::] Highlight ID (as shown above) >>> "))
                while not pk:
                    print(f"[✕] This field can't be blank !")
                    sleep(1)
                    pk=int(input(f"{yellow}[::] Highlight ID >>> "))
                try:
                    sleep(1)
                    print(f"{green}[✓] Retrieved information.")
                    sleep(0.8)
                    print(client.highlight_info(pk))
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 41:
        clear()
        url=input(f"{yellow}[::] Story URL >>> ")
        while url in NULL:
            print(f"{red}[✕] This field can't be blank !")
            sleep(1)
            url=input(f"{yellow}[::] Story URL >>> ")
        sleep(1)
        print(Get_Spk(url))
        pk=int(input(f"{yellow}[::] Story ID (as shown above) >>> "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            pk=int(input(f"{yellow}[::] Story ID >>> "))
        try:
            dell = client.story_delete(pk)
            print(f"{green}[✓] Story deleted." if dell else f"{red}[✕] Unable to delete story.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 42:
        clear()
        url=input(f"{yellow}[::] Story URL >>> ")
        while url in NULL:
            print(f"{red}[✕] This field can't be blank !")
            sleep(1)
            url=input(f"{yellow}[::] Story URL >>> ")
        sleep(1)
        print(Get_Spk(url))
        pk=int(input(f"{yellow}[::] Story ID (as shown above) >>> "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            pk=int(input(f"{yellow}[::] Story ID >>> "))
        sleep(0.8)
        number=int(input(f"{yellow}[::] Viewers to print (num) >>> "))
        while checkCount(number):
            checkOpt(number, "count")
            sleep(1)
            number=int(input(f"{yellow}[::] Viewers to print (num) >>> "))
        try:
            L = client.story_viewers(pk,number)
            for i in range(len(L)):
                print(f"{yellow}[+] Viewer No{i+1} >>> {L[i]}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 43:
        clear()
        count=int(input(f"{yellow}[::] Hashtags (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Hashtags >>> "))
        for i in range(count):
            tag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
            while checkTag(tag):
                if not tag:
                    print(f"{red}[✕] This field can't be blank !")
                else:
                    print(f"{red}[!] Invalid hashtag !")
                sleep(1)
                tag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
            STBTGS.append(tag)
        try:
            sleep(1)
            print(f"{green}[✓] Action successful.")
            sleep(0.8)
            print(bot.story_by_tags(STBTGS))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 44:
        clear()
        count=int(input(f"{yellow}[::] Users (num) >>> "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input(f"{yellow}[::] Users >>> "))
        for i in range(count):
            username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=input(f"{yellow}[::] Username No{i+1} >>> ")
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            sleep(0.9)
            print(GetID(username))
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input(f"{yellow}[::] ID >>> "))
            GTST.append(id)
        try:
            sleep(1)
            print(f"{green}[✓] Action successful !")
            sleep(0.8)
            print(loader.get_stories(GTST))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 45:
        clear()
        url=input(f"{yellow}[::] Story URL >>> ")
        while url in NULL:
            print(f"{red}[✕] This field can't be blank !")
            sleep(1)
            url=input(f"{yellow}[::] Story URL >>> ")
        sleep(1)
        print(Get_Spk(url))
        pk=int(input(f"{yellow}[::] Story ID (as shown above) >>> "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            pk=int(input(f"{yellow}[::] Story ID >>> "))
        try:
            sleep(1)
            print(f"{green}[✓] Action successfull.")
            sleep(0.8)
            print(client.story_info_v1(pk))
        except Exception as ex:
            Except(ex)

    elif option == 46:
        clear()
        print(f"{yellow}[+] Country example: US, BR, CZ")
        sleep(1)
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        fcodes=input(f"{yellow}[::] Print full list >>> ")
        while fcodes.lower() not in ANS or fcodes in NULL:
            if fcodes in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid input !")
            sleep(1)
            fcodes=input(f"{yellow}[::] Print full list >>> ")
        if fcodes == ANS[0]:
            webbrowser.open("https://www.iban.com/country-codes")
        sleep(1)
        country=input(f"{yellow}[::] Country >>> ")
        while country in NULL or not country:
            print(f"{red}[✕] This field can't be blank !")
            sleep(1)
            country=input(f"{yellow}[::] Country >>> ")
        try:
            client.set_country(country)
            sleep(2)
            print(f"{green}[✓] Country applied.")
        except Exception as ex:
            Except(ex)

    elif option == 47:
        clear()
        bio=input(f"{yellow}[::] Bio >>> ")
        while bio in NULL or not bio:
            print(f"{red}[✕] This field can't be blank !")
            sleep(1)
            bio=input(f"{yellow}[::] Bio >>> ")
        try:
            client.account_set_biography(bio)
            sleep(2)
            print(f"{green}[✓] Bio changed.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 48:
        clear()
        """
        SAME METHOD AS POIROT
        """

    elif option == 49:
        clear()
        username=input(f"{yellow}[::] Username >>> ")
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=input(f"{yellow}[::] Username >>> ")
        while valUser(username):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        sleep(1)
        print(GetID(username))
        id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            id=int(input(f"{yellow}[::] ID >>> "))
        try:
            posts=client.usertag_medias_v1(id)
            sleep(2)
            print(f"{green}[✓] Action successful.")
            sleep(1)
            for i in range(len(posts)):
                print(posts[i])
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 50:
        clear()
        username=input(f"{yellow}[::] Username (your) >>> ")
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=input(f"{yellow}[::] Username (your) >>> ")
        while valUser(username):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        try:
            dictr = client.reset_password(username)
            sleep(2)
            print(f"{green}[✓] Password reset.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 51:
        clear()
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        set_first_name=input(f"{yellow}[::] Set first name >>> ")
        while set_first_name in NULL or set_first_name.lower() not in ANS:
            if set_first_name in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid answer !")
                sleep(1)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            set_first_name=input(f"{yellow}[::] Set first name >>> ")
        if set_first_name.lower() == ANS[0]:
            first_name=input(f"{yellow}[::] First name >>> ")
            while first_name in NULL or not first_name:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                first_name=input(f"{yellow}[::] First name >>> ")
        else:
            first_name = ''
        sleep(1)
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        set_bio=input(f"{yellow}[::] Set bio >>> ")
        while set_bio in NULL or set_bio.lower() not in ANS:
            if set_bio in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid answer !")
                sleep(1)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            set_bio=input(f"{yellow}[::] Set bio >>> ")
        if set_bio.lower() == ANS[0]:
            bio=input(f"{yellow}[::] Bio >>> ")
            while bio in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                bio=input(f"{yellow}[::] Bio >>> ")
        else:
            bio = ''
        sleep(1)
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        set_ex_url=input(f"{yellow}[::] Add external URL >>> ")
        while set_ex_url in NULL or set_ex_url.lower() not in ANS:
            if set_ex_url in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid answer !")
                sleep(1)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            set_ex_url=input(f"{yellow}[::] Add external URL >>> ")
        if set_ex_url.lower() == ANS[0]:
            url=input(f"{yellow}[::] URL >>> ")
            while url in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                url=input(f"{yellow}[::] URL >>> ")
        else:
            url = ''
        sleep(1)
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        set_email=input(f"{yellow}[::] Add email >>> ")
        while set_email in NULL or set_email.lower() not in ANS:
            if set_email in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid answer !")
                sleep(1)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            set_email=input(f"{yellow}[::] Add email >>> ")
        if set_email.lower() == ANS[0]:
            email=input(f"{yellow}[::] Email >>> ")
            while email in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                email=input(f"{yellow}[::] Email >>> ")
        else:
            email = ''
        sleep(1)
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        set_phone_number=input(f"{yellow}[::] Add phone >>> ")
        while set_phone_number in NULL or set_phone_number.lower() not in ANS:
            if set_phone_number in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid answer !")
                sleep(1)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            set_phone_number=input(f"{yellow}[::] Add phone >>> ")
        if set_phone_number == ANS[0]:
            phone_number=int(input(f"{yellow}[::] Phone >>> "))
            while not phone_number:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                phone_number=int(input(f"{yellow}[::] Phone >>> "))
        else:
            phone_number = 00000000
        sleep(1)
        print(f"{green}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        set_gender=input(f"{yellow}[::] Set a gender >>> ")
        while set_gender in NULL or set_gender.lower() not in ANS:
            if set_gender in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Invalid input !")
                sleep(1)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            set_gender=input(f"{yellow}[::] Set a gender >>> ")
        if set_gender == ANS[0]:
            gender=input(f"{yellow}[::] Gender >>> ")
            while gender in NULL:
                print(f"[✕] This field can't be blank !")
                sleep(1)
                gender=input(f"{yellow}[::] Gender >>> ")
        else:
            gender = ''
        try:
            api.edit_profile(first_name, bio, url, email, phone_number, gender)
            sleep(2)
            print(f"{green}[✓] Profile edited.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 52:
        clear()
        count=int(input(f"{yellow}[::] Posts to like/unlike (num) >>> "))
        while checkCount(count):
            checkOpt(count, "count")
            sleep(1)
            count=int(input(f"{yellow}[::] Posts to like/unlike (num) >>> "))
        browser = webdriver.Chrome()
        for i in range(count):
            url=input(f"{yellow}[::] Post url >>> ")
            while url in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                url=input(f"{yellow}[::] Post url >>> ")
            try:
                browser.get(url)
                like = browser.find_element_by_id("mount_0_0_Cs")
                like.click()
                sleep(2)
                print(f"{green}[✓] Post liked.")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 53:
        clear()
        count=int(input(f"{yellow}[::] Deletes (num) >>> "))
        while checkCount(count):
            checkOpt(count, "count")
            sleep(1)
            count=int(input(f"{yellow}[::] Deletes (num) >>> "))
        browser = webdriver.Chrome()
        for i in range(count):
            url=input(f"{yellow}[::] URL >>> ")
            while url in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                url=input(f"{yellow}[::] URL >>> ")
            try:
                browser.get(url)
                menu = browser.find_element_by_class_name("_ab6-")
                menu.click()
                delete = browser.find_element_by_class_name("_a9-- _a9-_")
                delete.click()
                sleep(2)
                print(f"{green}[✓] Element deleted.")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 54:
        count=int(input(f"{yellow}[::] Elements to save (num) >>> "))
        while checkCount(count):
            checkOpt(count, "count")
            sleep(1)
            count=int(input(f"{yellow}[::] Elements to save >>> "))
        browser = webdriver.Chrome()
        for i in range(count):
            url=input(f"{yellow}[::] URL >>> ")
            while url in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                url=input(f"{yellow}[::] URL >>> ")
            try:
                browser.get(url)
                save = browser.find_element_by_class_name("_abm0 _abm1")
                save.click()
                sleep(2)
                print(f"{green}[✓] Element saved.")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 55:
        clear()
        print(f"{green}[+] Acceptable time format >>> 15:06:10")
        sleep(1)
        tm=input(f"{yellow}[::] Time >>> ")
        while tm in NULL or ":" not in tm:
            if tm in NULL:
                print(f"{red}[✕] This field can't be blank !")
            else:
                print(f"{red}[!] Missing : from time.")
                sleep(1)
                print(f"{green}[+] Acceptable time format >>> 15:06:10")
            sleep(1)
            tm=input(f"{yellow}[::] Time >>> ")
        AvActs()
        cur_time = datetime.now()
        current_time = cur_time.now("%H:%M:%S")
        action=int(input(f"{yellow}[::] Num (from the above ones) >>> "))
        while valOpt(action, 1, 26):
            print(f"{red}[!] Invalid number !")
            sleep(1)
            print(f"{green}[+] Acceptable numbers >>> [1-26]")
            sleep(1)
            action=int(input(f"{yellow}[::] Num (from the above ones) >>> "))
        if action == 1:
            clear()
            count=int(input(f"{yellow}[::] Posts to make (num) >>> "))
            while checkCount(count):
                checkOpt(count, "count")
                sleep(1)
                count=int(input(f"{yellow}[::] Posts to make >>> "))
            sleep(0.5)
            for i in range(count):
                path=input(f"{yellow}[::] Path to photo >>> ")
                while checkPath(path):
                    checkOpt(path, "path")
                    sleep(1)
                    path=input(f"{yellow}[::] Path to photo >>> ")
                sleep(1.5)
                print(f"{yellow}>>>CAPTION<<<")
                sleep(0.5)
                default = 'Check out my new post !'
                print(f"{yellow}[+] Default: \"{default}\"")
                sleep(0.6)
                print(f"{yellow}[*] Hit <Enter> to apply the default caption.")
                sleep(0.7)
                cap = input(f"{yellow}[::] Caption >>> ")
                cap = default if cap == '' else cap
                print(f"{yellow}>>>TAGS<<<")
                sleep(0.5)
                print(f"{yellow}[+] Default: [No]")
                sleep(1)
                print(f"{yellow}[*] Hit <Enter> to apply the default option.")
                sleep(0.8)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                tags=input(f"{yellow}[::] Tag user(s) >>> ")
                while tags.lower() not in ANS or tags in NULL:
                    if tags in NULL:
                        print(f"{red}[✕] This field can't be blank !")
                    else:
                        print(f"{red}[!] Invalid answer !")
                        sleep(1)
                        print(f"{green}[+] Acceptable answers >>> {ANS}")
                    sleep(1)
                    tags=input(f"{yellow}[::] Tag user(s) >>> ")
                tags = tags == ANS[0]
                if tags:
                    print(f"{yellow}[+] Default: 1")
                    sleep(0.5)
                    print(f"{yellow}[*] Hit <Enter> to apply the default option.")
                    sleep(0.7)
                    count=int(input(f"{yellow}[::] Users to tag (num) >>> "))
                    while checkCount(count):
                        checkOpt(count, "count")
                        sleep(1)
                        count=int(input(f"{yellow}[::] Users to tag (num) >>> "))
                    sleep(0.8)
                    utag=input(f"{yellow}[::] Username >>> ")
                    while checkUser(username):
                        checkOpt(username, "username")
                        sleep(1)
                        utag=input(f"{yellow}[::] Username >>> ")
                    while valUser(utag):
                        if type(CheckVal()) == bool:
                            CheckVal()
                        else:
                            utag = CheckVal()
                    utag = utag.lower().strip()
                    TaggedUsers.append(utag)
                    for i in range(count):
                        utag=input(f"{yellow}[::] Username No{i+1} >>> ")
                        while checkUser(utag):
                            checkOpt(utag, "username")
                            sleep(1)
                            utag=input(f"{yellow}[::] Username No{i+1} >>> ")
                        while valUser(utag):
                            if type(CheckVal()) == bool:
                                CheckVal()
                            else:
                                utag = CheckVal()
                        utag = utag.strip().lower()
                        TaggedUsers.append(utag)
                sleep(0.7)
                print(f"{yellow}>>>LOCATION<<<")
                sleep(0.5)
                print(f"{yellow}[+] Default: [No]")
                sleep(0.5)
                print(f"{yellow}[*] Hit <Enter> to apply the default option.")
                sleep(0.7)
                print(f"{green}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                loc=input(f"{yellow}[::] Include location >>> ")
                while loc.lower() not in ANS or loc in NULL:
                    if loc in NULL:
                        print(f"{red}[✕] This field can't be blank !")
                    else:
                        print(f"[!] Invalid answer !")
                        sleep(1)
                        print(f"{green}[+] Acceptable answers >>> {ANS}")
                    sleep(1)
                    loc=input(f"{yellow}[::] Include location >>> ")
                loc = loc == ANS[0]
                if loc:
                    count=int(input(f"{yellow}[::] Number >>> "))
                    while checkCount(count):
                        checkOpt(count, "count")
                        sleep(1)
                        count=int(input(f"{yellow}[::] Number >>> "))
                    for i in range(count):
                        location=input(f"{yellow}[::] Location No{i+1} >>> ")
                        while location in NULL:
                            print(f"{red}[✕] This field can't be blank !")
                            sleep(1)
                            location=input(f"{yellow}[::] Location No{i+1} >>> ")
                        LOCATIONS.append(location)
                        print(f"{green}[✓] Location added.")
                    if current_time == tm:
                        try:
                            client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                            sleep(2)
                            print(f"{green}[✓] Photo uploaded.")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"{yellow}[+] Current time: {current_time}")
                        sleep(1)
                        print(f"{yellow}[+] Waiting for time: {tm}...")
                        Class()

                if tags and loc:
                    if current_time == tm:
                        try:
                            client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                            print(f"{green}[✓] Photo uploaded.")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"{yellow}[+] Current time: {current_time}")
                        sleep(1)
                        print(f"{yellow}[+] Waiting for time: {tm}...")
                        Class()
                elif tags and loc:
                    if current_time == tm:
                        try:
                            client.photo_upload(path=path,caption=caption,tags=TaggedUsers)
                            print(f"{green}[✓] Photo uploaded.")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"{yellow}[+] Current time: {current_time}")
                        sleep(1)
                        print(f"{yellow}[+] Waiting for time: {tm}...")
                        Class()
                elif not tags and loc:
                    if current_time == tm:
                        try:
                            client.photo_upload(path=path,caption=caption,location=LOCATIONS)
                            print(f"{green}[✓] Photo uploaded.")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"{yellow}[+] Current time: {current_time}")
                        sleep(1)
                        print(f"{yellow}[+] Waiting for time: {tm}...")
                        Class()
                elif not tags and not loc:
                    if current_time == tm:
                        try:
                            client.photo_upload(path=path,caption=caption)
                            print(f"{green}[✓] Photo uploaded.")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"{yellow}[+] Current time: {current_time}")
                        sleep(1)
                        print(f"{yellow}[+] Waiting for time: {tm}...")
                        Class()

        elif action == 2:
            clear()
            path=input(f"{yellow}[::] Path to pic >>> ")
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=input(f"{yellow}[::] Path to pic >>> ")
            try:
                client.account_change_picture(path)
                sleep(2)
                print(f"{green}[✓] Profile pic changed.")
                Class()
            except Exception as ex:
                Except(ex)

        elif action == 3:
            path=input(f"{yellow}[::] Path to photo >>> ")
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=input(f"{yellow}[::] Path to photo >>> ")
            sleep(0.5)
            print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            AddCaption=input(f"{yellow}[::] Add caption >>> ")
            while AddCaption.lower() not in ANS or AddCaption in NULL:
                if AddCaption in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                else:
                    print(f"{red}[!] Invalid answer !")
                    sleep(1)
                    print(f"{green}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                AddCaption=input(f"{yellow}[::] Add caption >>> ")
            caption = ''
            if AddCaption == ANS[0]:
                print(f"{yellow}[+] Default: \"{default}\"")
                sleep(1)
                print(f"{yellow}[*] Hit <Enter> to apply the default caption.")
                sleep(1)
                caption=input(f"{yellow}[::] Caption >>> ")
            caption = default if caption == NULL[0] else caption
            sleep(1)
            print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            AddMention=input(f"{yellow}[?] Add mention >>> ")
            while AddMention.lower() not in ANS or AddMention in NULL:
                if AddMention in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                else:
                    print(f"{red}[!] Invalid answer !")
                    sleep(1)
                    print(f"{green}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                AddMention=input(f"{yellow}[?] Add mention >>> ")
            if AddMention == ANS[0]:
                MENTIONS = []
                count=int(input(f"{yellow}[::] Number >>> "))
                while checkCount(count):
                    checkOpt(count, "count")
                    sleep(1)
                    count=int(input(f"{yellow}[::] Number >>> "))
                for i in range(count):
                    mention=input(f"{yellow}[::] Username No{i+1} >>> ")
                    while checkUser(mention):
                        checkOpt(mention, "username")
                        sleep(1)
                        mention=input(f"{yellow}[::] Username No{i+1} >>> ")
                    while valUser(mention):
                        if type(CheckVal()) == bool:
                            CheckVal()
                        else:
                            mention = CheckVal()
                    mention = mention.lower().strip()
                    MENTIONS.append(mention)
                    sleep(1)
                    print(f"{green}[✓] Mention added.")
            sleep(1)
            print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            AddLoc=input(f"{yellow}[::] Add location >>> ")
            while AddLoc.lower() not in ANS or AddLoc in NULL:
                if AddLoc in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                else:
                    print(f"{red}[!] Invalid answer !")
                    sleep(1)
                    print(f"{green}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                AddLoc=input(f"{yellow}[::] Add location >>> ")
            if AddLoc == ANS[0]:
                count=int(input(f"{yellow}[::] Number >>> "))
                while checkCount(count):
                    checkOpt(count, "count")
                    sleep(1)
                    count=int(input(f"{yellow}[::] Number >>> "))
                for i in range(count):
                    loc=input(f"{yellow}[::] Location No{i+1} >>> ")
                    while loc in NULL:
                        print(f"{yellow}[✕] This field can't be blank !")
                        sleep(1)
                        loc=input(f"{yellow}[::] Location No{i+1} >>> ")
                    LOCATIONS.append(loc)
                    sleep(1)
                    print(f"{green}[✓] Location added.")
            sleep(1)
            print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            AddLinks=input(f"{yellow}[::] Include urls >>> ")
            while AddLinks.lower() not in ANS or AddLinks in NULL:
                if AddLinks in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                else:
                    print(f"{red}[!] Invalid answer !")
                    sleep(1)
                    print(f"{green}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                AddLinks=input(f"{yellow}[::] Include urls >>> ")
            if AddLinks == ANS[0]:
                count=int(input(f"{yellow}[::] Number >>> "))
                while checkCount(count):
                    checkOpt(count, "other")
                    sleep(1)
                    count=int(input(f"{yellow}[::] Number >>> "))
                for i in range(count):
                    link=input(f"{yellow}[::] Url No{i+1} >>> ")
                    while link in NULL:
                        print(f"{red}[✕] This field can't be blank !")
                        sleep(1)
                        link=input(f"{yellow}[::] Url No{i+1} >>> ")
                    LINKS.append(link)
                    sleep(1)
                    print(f"{green}[✓] URL added.")
            sleep(1)
            print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            AddHash=input(f"{yellow}[::] Include hashtags >>> ")
            while AddHash.lower() not in ANS or AddHash in NULL:
                if AddHash in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                else:
                    print(f"{red}[!] Invalid answer !")
                    sleep(1)
                    print(f"{green}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                AddHash=input(f"{yellow}[::] Include hashtags >>> ")
            if AddHash == ANS[0]:
                count=int(input(f"{yellow}[::] Number >>> "))
                while checkCount(count):
                    checkOpt(count, "count")
                    sleep(1)
                    count=int(input(f"{yellow}[::] Number >>> "))
                for i in range(count):
                    hashtag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
                    while hashtag in NULL or "#" not in hashtag:
                        if hashtag in NULL:
                            print(f"{red}[✕] This field can't be blank !")
                        else:
                            print(f"{red}[!] Hashtag must include: #")
                        sleep(1)
                        hashtag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
                    HASHTAGS.append(hashtag)
                    sleep(1)
                    print(f"{green}[✓] Hashtag added.")
            while current_time != tm:
                print(f"{yellow}[+] Current time: {current_time}")
                sleep(1)
                print(f"{yellow}[+] Waiting for time: {tm}...")
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                sleep(2)
                print(f"{green}[✓] Story uploaded.")
                Class()
            except Exception as ex:
                Except(ex)

        elif action == 4:
            hashtag = location = ''
            path=input(f"{yellow}[::] Path to video >>> ")
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=input(f"{yellow}[::] Path to video >>> ")
            sleep(0.7)
            print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            incap=input(f"{yellow}[::] Include caption >>> ")
            while incap.lower() not in ANS or incap in NULL:
                if incap in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                else:
                    print(f"{red}[!] Invalid answer !")
                    sleep(1)
                    print(f"{green}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                incap=input(f"{yellow}[::] Include caption >>> ")
            caption = ''
            if incap.lower() == ANS[0]:
                default = 'Check out my new video !'
                sleep(1)
                print(f"{yellow}[+] Default: \"{default}\"")
                sleep(1)
                print(f"{yellow}[*] Hit <Enter> to apply the default caption.")
                sleep(0.8)
                caption=input(f"{yellow}[::] Caption >>> ")
                if caption == '':
                    caption = default
            sleep(1)
            print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            intag=input(f"{yellow}[::] Include hashtags >>> ")
            while intag.lower() not in ANS or intag in NULL:
                if intag in NULL:
                    print(f"{red}[✕] This field can't be blank !")
                else:
                    print(f"{red}[!] Invalid answer !")
                    sleep(1)
                    print(f"{green}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                intag=input(f"{yellow}[::] Include hashtags >>> ")
            if intag.lower() == ANS[0]:
                count=int(input(f"{yellow}[::] Number >>> "))
                while checkCount(count):
                    checkOpt(count, "count")
                    sleep(1)
                    count=int(input(f"{yellow}[::] Number >>> "))
                for i in range(count):
                    hashtag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
                    while checkTag(hashtag):
                        if hashtag in NULL:
                            print(f"{red}[✕] This field can't be blank !")
                        else:
                            print(f"{red}[!] Invalid hashtag !")
                            sleep(0.5)
                            print(f"{green}[+] Acceptable hashtag format >>> #random")
                        sleep(1)
                        hashtag=input(f"{yellow}[::] Hashtag No{i+1} >>> ")
                    HASHVID.append(hashtag)
                    sleep(1)
                    print(f"{green}[✓] Hashtag added.")
            sleep(1)
            print(f"{green}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            inloc=input(f"{yellow}[::] Include location(s) >>> ")
            while inloc.lower() not in ANS or inloc in NULL:
                print(f"{red}[✕] This field can't be blank !")
                sleep(1)
                inloc=input(f"{yellow}[::] Include location(s) >>> ")
            location = ''
            if inloc == ANS[0]:
                count=int(input(f"{yellow}[::] Number >>> "))
                while checkCount(count):
                    checkOpt(count, "other")
                    sleep(1)
                    count=int(input(f"{yellow}[::] Number >>> "))
                for i in range(count):
                    location=input(f"{yellow}[::] Location No{i+1} >>> ")
                    while location in NULL:
                        print(f"{red}[✕] This field can't be blank !")
                        sleep(1)
                        location=input(f"{yellow}[::] Location No{i+1} >>> ")
            if current_time == tm:
                try:
                    client.video_upload(path,caption,usertags=HASHVID,location=location)
                    sleep(1.5)
                    print(f"{green}[✓] Video uploaded.")
                    Class()
                except Exception as ex:
                    Except(ex)
            else:
                print(f"{yellow}[+] Current time: {current_time}")
                sleep(1)
                print(f"{yellow}[+] Waiting for time: {tm}...")
                Class()

        elif action == 5:
            count=int(input(f"{yellow}[::] Number >>> "))
            while checkCount(count):
                checkOpt(count, "count")
                sleep(1)
                count=int(input(f"{yellow}[::] Number >>> "))
            if count == 1:
                username=input(f"{yellow}[::] Please enter the username: ")
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=input(f"{yellow}[::] Please enter the username: ")
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                sleep(0.8)
                print(GetID(username))
                uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                if current_time == tm:
                    try:
                        client.user_follow(uid)
                        sleep(2)
                        print(f"{green}[✓] Followed {username}.")
                        Class()
                    except Exception as ex:
                        Exception(ex)
                else:
                    print(f"{yellow}[+] Current time: {current_time}")
                    sleep(1)
                    print(f"{yellow}[+] Waiting for time: {tm}...")
                    Class()
            else:
                for i in range(count):
                    username=input(f"{yellow}[::] Username No{i+1} >>> ")
                    while checkUser(username):
                        checkOpt(username, "username")
                        sleep(1)
                        username=input(f"{yellow}[::] Username No{i+1} >>> ")
                    while valUser(username):
                        if type(CheckVal()) == bool:
                            CheckVal()
                        else:
                            username = CheckVal()
                    username = username.lower().strip()
                    sleep(0.8)
                    print(GetID(username))
                    uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                    while checkID(uid):
                        checkOpt(uid, "id")
                        sleep(1)
                        uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                    if current_time == tm:
                        try:
                            client.user_follow(id)
                            sleep(2)
                            print(f"{green}[✓] Followed {username}.")
                            Class()
                        except Exception as ex:
                            Exception(ex)
                    else:
                        print(f"{yellow}[+] Current time: {current_time}")
                        sleep(1)
                        print(f"{yellow}[+] Waiting for time: {tm}...")
                        Class()
     
        elif action == 6:
            if current_time == tm:
                count=int(input(f"{yellow}[::] Number >>> "))
                while checkCount(count):
                    checkOpt(count, "other")
                    sleep(1)
                    count=int(input(f"{yellow}[::] Number >>> "))
                if count == 1: 
                    username=input(f"{yellow}[::] Username >>> ")
                    while checkUser(username):
                        checkOpt(username, "username")
                        sleep(1)
                        username=input(f"{yellow}[::] Username >>> ")
                    while valUser(username):
                        if type(CheckVal()) == bool:
                            CheckVal()
                        else:
                            username = CheckVal()
                    username = username.lower().strip()
                    sleep(1)
                    print(GetID(username))
                    uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                    while checkID(uid):
                        checkOpt(uid, "id")
                        sleep(1)
                        uid=int(input(f"{yellow}[::] ID (as shown above) >>> "))
                    try:
                        client.user_unfollow(uid)
                        sleep(2)
                        print(f"{green}[✓] Unfollowed {username}.")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    for i in range(count):
                        username=input(f"{yellow}[::] Username No{i+1} >>> ")
                        while checkUser(username):
                            checkOpt(username, "username")
                            sleep(1)
                            username=input(f"{yellow}[::] Username No{i+1} >>> ")
                        while valUser(username):
                            if type(CheckVal()) == bool:
                                CheckVal()
                            else:
                                username = CheckVal()
                        username = username.lower().strip()
                        try:
                            client.user_unfollow(uid)
                            sleep(2)
                            print(f"{green}[✓] Unfollowed {username}.")
                        except Exception as e:
                            Except(ex)
                    Class()
            else:
                print(f"{yellow}[+] Current time: {current_time}")
                sleep(0.8)
                print(f"{yellow}[+] Waiting for time: {tm}...")
                sleep(0.8)
                Class()

    elif option == 56:
        clear()
        user=input(f"{yellow}[::] Username >>> ")
        while checkUser(user):
            checkOpt(user, "username")
            sleep(1)
            user=input(f"{yellow}[::] Username >>> ")
        while valUser(user):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                user = CheckVal()
        user = user.lower().strip()
        sleep(1)
        print(GetID(user))
        id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            id=int(input(f"{yellow}[::] ID (as shown above) >>> "))
        try:
            api.block_friend_reel(id)
            sleep(2)
            print(f"{green}[✓] User: {user} blocked from watching your stories.")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 57:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{yellow}[+] Thank you for choosing IAM 😀😁")
        sleep(2)
        print(f"{yellow}[+] Hope you enjoyed it 🤗")
        sleep(1)
        print(f"{yellow}[+] Found a bug ? Report it here ==> https://github.com/new92/IAM/issues/new/choose")
        sleep(3)
        print(f"{yellow}[+] Until we meet again 🫡")
        sleep(1)
        exit(0)

if __name__ == '__main__':
    main()
