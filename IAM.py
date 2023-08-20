# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92

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
        quit(0)
    import platform
    from tqdm import tqdm
    total_mods = 11
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    from os import system
    import instagrapi
    import json
    import instaloader
    import requests as re
    import os
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
                print(f"[*] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall script")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2 or opt == None:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[*] Acceptable numbers: [1/2]")
                    sleep(1)
                    print("[1] Uninstall script")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
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
                    quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip3 install -r requirements.txt")

loader=instaloader.Instaloader()
client=instagrapi.Client()

print("[✓] Successfully loaded modules !")
sleep(1)

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def banner() -> str:
    return """
    ██╗░█████╗░███╗░░░███╗
    ██║██╔══██╗████╗░████║
    ██║███████║██╔████╔██║
    ██║██╔══██║██║╚██╔╝██║
    ██║██║░░██║██║░╚═╝░██║
    ╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
    """

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def Get_Hpk(url:str) -> str:
    return client.highlight_pk_from_url(url)

def Get_Spk(url:str) -> str:
    return client.story_pk_from_url(url)

def valUser(user):
    return re.get(f"https://www.instagram.com/{user}/").status_code != 200

def Except(ex:str):
    print("[!] Error !")
    sleep(1)
    print(f"[*] Error message ==> {ex}")
    sleep(2)
    print("[1] Return to menu")
    print("[2] Exit")
    num=int(input("[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 2 or num == None:
        if num == None:
            print("[!] This field can't be empty !")
        else:
            print("[!] Invalid number !")
            sleep(1)
            print("[*] Acceptable numbers: [1/2]")
        sleep(1)
        print("[1] Return to menu")
        print("[2] Exit")
        num=int(input("[::] Please enter a number (from the above ones): "))
    if num == 1:
        main()
    else:
        print("[+] Exiting...")
        sleep(1)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

def checkOpt(opt,data):
    if data == "username":
        if opt == None:
            print("[!] This field can't be empty !")
        else:
            print("[!] Invalid length !")
            sleep(1)
            print("[*] Acceptable length: less than or equal to 30 characters")
    elif data == "id":
        if opt == None:
            print("[!] This field can't be empty !")
        else:
            print("[!] Invalid length !")
            sleep(1)
            print("[*] Acceptable length: greater than 3")
    elif data == "path":
        if opt == None:
            print("[!] This field can't be empty !")
        else:
            print("[!] Path must contain: / or \ ")
    else:
        if opt == None:
            print("[!] This field can't be empty !")
        else:
            print("[!] Invalid number !")

def valOpt(opt:int,x:int,y:int):
    return opt < x or opt > y or opt == None

def CheckVal() -> str:
    print("[!] User not found !")
    sleep(1)
    print("[1] Try with another username")
    print("[2] Return to menu")
    print("[3] Exit")
    opt=int(input("[::] Please enter a number (from the above ones): "))
    while valOpt(opt,1,3):
        checkOpt(opt, 'other')
        sleep(1)
        print("[1] Try with another username")
        print("[2] Return to menu")
        print("[3] Exit")
        opt=int(input("[::] Please enter again a number (from the above ones): "))
    if opt == 1:
        username=str(input("[::] Please enter the username: "))
        while checkUser(username):
            checkOpt(opt, 'username')
        sleep(1)
        username=str(input("[::] Please enter again the username: "))
        return username
    elif opt == 2:
        main()
    else:
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)
    return False
    
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
    return "[✓] Files and dependencies uninstalled successfully !"

def Next() -> int:
    sleep(1)
    print("[1] Return to menu")
    print("[2] Exit")
    opt=int(input("[::] Please enter a number (from the above ones): "))
    while valOpt(opt,1,2):
        if opt == None:
            print("[!] This field can't be blank !")
        else:
            print("[!] Invalid number !")
            sleep(1)
            print("[*] Acceptable numbers: [1/2]")
        sleep(1)
        opt=int(input("[::] Please enter a number (from the above ones): "))
    return opt

def Class():
    main() if Next() == 1 else Exiting()

def Exiting():
    print("[+] Exiting...")
    sleep(1)
    print("[+] See you next time 👋")
    sleep(1)
    quit(0)
    
def checkCount(num: int) -> bool:
    return num == None or num < 1
    
def checkTag(tag: str) -> bool:
    return "#" in tag or tag == None or tag == ''

def checkPath(path: str) -> bool:
    return path == None or "/" not in path or "\\" not in path or path == ''

def Av_Acts() -> str:
    return """
    1) Publish post(s)
    2) Change profile pic
    3) Upload story with pic
    4) Publish IGTV video
    5) Follow user(s)
    6) Unfollow user(s)
    7) Accept follow request(s)
    8) Reject follow request(s)
    9) Follow user's followers
    10) Follow user's following
    11) Send DM (Direct Message)
    12) Send file
    13) Send photo
    14) Send video
    15) Like the posts from hashtag(s)
    16) Like the posts from user(s)
    17 Like the posts from location(s)
    18) Like the posts from feed
    19) Comment by user
    20) Set default reply to comments
    21) Do comment
    22) Block user(s)
    23) Delete story
    24) Like/Unlike (post(s), reel(s), igtv(s) etc.)
    25) Delete your (post(s), reel(s), igtv(s) etc.)
    26) Save/Unsave (post(s), reel(s), igtv(s) etc.)
    """

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    if os.path.exists(fpath(f)):
        fsize = os.stat(fpath(f)).st_size
    else:
        fsize = 0
    print(f"[+] Author ==> {conf['author']}")
    print(f"[+] Github ==> @{conf['author']}")
    print(f"[+] License ==> {conf['lice']}")
    print(f"[+] Script's name ==> {conf['name']}")
    print(f"[+] Script's version ==> {conf['version']}")
    print(f"[+] Programming language(s) used ==> {conf['lang']}")
    print(f"[+] Natural language ==> {conf['language']}")
    print(f"[+] File size ==> {fsize} bytes")
    print(f"[+] File path ==> {fpath(f)}")
    print(f"[+] Number of lines ==> {conf['lines']}")
    print(f"[+] API(s) used ==> {conf['api']}")
    print("|======|GITHUB REPO INFO|======|")
    print(f"[+] Stars ==> {conf['stars']}")
    print(f"[+] Forks ==> {conf['forks']}")
    print(f"[+] Open issues ==> {conf['issues']}")
    print(f"[+] Closed issues ==> {conf['clissues']}")
    print(f"[+] Open pull requests ==> {conf['prs']}")
    print(f"[+] Closed pull requests ==> {conf['clprs']}")
    print(f"[+] Discussions ==> {conf['discs']}")


def checkUser(username: str) -> bool:
    return username == None or len(username) > 30 or username == ''

def GetID(username: str) -> int:
    return loader.check_profile_id(username)

def checkID(id: int) -> bool:
    return id == None or len(id) < 3


ANS = ['yes','no']
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
    print("\n")
    print("[+] IAM: Instagram Account Manager")
    print("\n")
    print("[+] Script for Managing your Instagram Account Remotely")
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[1] Display your profile ID")
    print("[2] Display your security information")
    print("[3] Display your account info")
    print("[4] Display your pending follow requests")
    print("[5] Display your followers")
    print("[6] Display the users you Follow")
    print("\n")
    print("[7] Download your highlights")
    print("[8] Download anonymous stories of other users")
    print("[9] Download your saved posts")
    print("[10] Download posts from your feed")
    print("\n")
    print("[11] Publish post(s)")
    print("[12] Enable/Disable your notifications")
    print("[13] Change profile pic")
    print("[14] Upload story with pic")
    print("[15] Publish IGTV video")
    print("\n")
    print("[16] Follow user(s)")
    print("[17] Unfollow user(s)")
    print("[18] Accept follow request(s)")
    print("[19] Reject follow request(s)")
    print("[20] Follow user's followers")
    print("[21] Follow user's following")
    print("\n")
    print("[22] Send DM (Direct Message)")
    print("[23] Send file")
    print("[24] Send photo")
    print("[25] Send video")
    print("\n")
    print("[26] Like the posts from hashtag(s)")
    print("[27] Like the posts from user(s)")
    print("[28] Like the posts from location(s)")
    print("[29] Like the posts from feed")
    print("\n")
    print("[30] Comment by user")
    print("[31] Set default reply to comments")
    print("[32] Do comment")
    print("\n")
    print("[33] Block User(s)")
    print("[34] Get username from user ID")
    print("[35] Get a list of all users you have blocked")
    print("\n")
    print("[36] Create highlight(s)")
    print("[37] Delete highlight(s)")
    print("[38] Change the cover of highlight(s)")
    print("[39] Display the highlights of user(s)")
    print("[40] Retrieve information from highlight(s)")
    print("\n")
    print("[41] Delete story")
    print("[42] Get story viewers")
    print("[43] Get stories by hashtags")
    print("[44] Get stories by users")
    print("[45] Retrieve information of a story")
    print("\n")
    print("[46] Set country")
    print("[47] Set bio")
    print("[48] Gather information for a user (works better on public accounts)")
    print("[49] Get information about posts where user is tagged")
    print("[50] Reset your password")
    print("\n")
    print("[51] Edit profile")
    print("[52] Like/Unlike (post(s), reel(s), igtv(s) etc.)")
    print("[53] Delete your (post(s), reel(s), igtv(s) etc.)")
    print("[54] Save/Unsave (post(s), reel(s), igtv(s) etc.)")
    print("\n")
    print("[55] Set a specific time (from the current day) to execute an action")
    print("\n")
    print("[56] Hide your stories from a specific user")
    print("\n")
    print("[57] Uninstall script")
    print("\n")
    print("[999] Show program info and exit")
    print("\n")
    print("[0] Exit") 
    print("\n")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while valOpt(option,1,57) and opt != 999:
        checkOpt(option, "other")
        sleep(2)
        print("[1] Display your profile ID")
        print("[2] Display your security information")
        print("[3] Display your account info")
        print("[4] Display your pending follow requests")
        print("[5] Display your followers")
        print("[6] Display the users you Follow")
        print("\n")
        print("[7] Download your highlights")
        print("[8] Download anonymous stories of other users")
        print("[9] Download your saved posts")
        print("[10] Download posts from your feed")
        print("\n")
        print("[11] Publish post(s)")
        print("[12] Enable/Disable your notifications")
        print("[13] Change profile pic")
        print("[14] Upload story with pic")
        print("[15] Publish IGTV video")
        print("\n")
        print("[16] Follow user(s)")
        print("[17] Unfollow user(s)")
        print("[18] Accept follow request(s)")
        print("[19] Reject follow request(s)")
        print("[20] Follow user's followers")
        print("[21] Follow user's following")
        print("\n")
        print("[22] Send DM (Direct Message)")
        print("[23] Send file")
        print("[24] Send photo")
        print("[25] Send video")
        print("\n")
        print("[26] Like the posts from hashtag(s)")
        print("[27] Like the posts from user(s)")
        print("[28] Like the posts from location(s)")
        print("[29] Like the posts from feed")
        print("\n")
        print("[30] Comment by user")
        print("[31] Set default reply to comments")
        print("[32] Do comment")
        print("\n")
        print("[33] Block User(s)")
        print("[34] Get username from user ID")
        print("[35] Get a list of all users you have blocked")
        print("\n")
        print("[36] Create highlight(s)")
        print("[37] Delete highlight(s)")
        print("[38] Change the cover of highlight(s)")
        print("[39] Display the highlights of user(s)")
        print("[40] Retrieve information from highlight(s)")
        print("\n")
        print("[41] Delete story")
        print("[42] Get story viewers")
        print("[43] Get stories by hashtags")
        print("[44] Get stories by users")
        print("[45] Retrieve information of a story")
        print("\n")
        print("[46] Set country")
        print("[47] Set bio")
        print("[48] Gather information for a user (works better on public accounts)")
        print("[49] Get information about posts where user is tagged")
        print("[50] Reset your password")
        print("\n")
        print("[51] Edit profile")
        print("[52] Like/Unlike (post(s), reel(s), igtv(s) etc.)")
        print("[53] Delete your (post(s), reel(s), igtv(s) etc.)")
        print("[54] Save/Unsave (post(s), reel(s), igtv(s) etc.)")
        print("\n")
        print("[55] Set a specific time (from the current day) to execute an action")
        print("\n")
        print("[56] Hide your stories from a specific user")
        print("\n")
        print("[57] Uninstall script")
        print("\n")
        print("[999] Show program info and exit")
        print("\n")
        print("[0] Exit")
        option=int(input("[::] Please enter again a number (from the above ones): "))
    if option != 0:
        clear()
        print("\n")
        print("|--------------------|LOGIN|--------------------|")
        print("\n")
        username=str(input("[::] Please enter your username: "))
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        while valUser(username):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        password=str(input("[::] Please enter your password: "))
        while password == None or password == ''    :
            print("[!] This field can't be blank !")
            sleep(1)
            password=input("[::] Please enter again your password: ")
        password = password.strip()
        try:
            loginl = loader.login(username,password)
            loginc = client.login(username,password,True)
            logini = instapy.InstaPy(username,password)
            api = instagram_private_api.Client(username,password)
        except Exception as ex:
            Except(ex)

    elif option == 999:
        clear()
        ScriptInfo()
    
    if option == 0:
        clear()
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

    elif option == 1:
        clear()
        try:
            print(f"[+] Your ID: {GetID(username)}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 2:
        clear()
        try:
            sec=client.account_security_info()
            print(f"[+] Is phone confirmed ? {sec['is_phone_confirmed']}")
            print(f"[+] Is 2 factor authentication enabled ? {sec['is_two_factor_enabled']}")
            print(f"[+] Is Time-based One-Time Passwords (TOTP) 2 factor authentication enabled ? {sec['is_totp_two_factor_enabled']}")
            print(f"[+] Is trusted notifications enabled ? {sec['is_trusted_notifications_enabled']}")
            print(f"[+] Is eligible for Whatsapp 2 factor authentication ? {sec['is_eligible_for_whatsapp_two_factor']}")
            print(f"[+] Is Whatsapp 2 factor authentication enabled ? {sec['is_whatsapp_two_factor_enabled']}")
            print(f"[+] Backup codes: {sec['backup_codes']}")
            print(f"[+] Trusted devices: {sec['trusted_devices']}")
            print(f"[+] Has reachable email ? {sec['has_reachable_email']}")
            print(f"[+] Is eligible for trusted notifications ? {sec['eligible_for_trusted_notifications']}")
            print(f"[+] Is eligible for multiple TOTP ? {sec['is_eligible_for_multiple_totp']}")
            print(f"[+] TOTP seeds: {sec['totp_seeds']}")
            print(f"[+] Can add additional TOTP seed ? {sec['can_add_additional_totp_seed']}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 3:
        clear()
        try:
            print(f"[+] Your account information: {client.account_info()}")
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
        id=int(input("[::] Please enter your id as shown above: "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            id=int(input("[::] Please enter again your ID as shown above: "))
        try:
            print(client.user_followers(id))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 6:
        clear()
        print(GetID(username))
        id=int(input("[::] Please enter your id (as shown above): "))
        while checkID(id):
            checkOpt(id,"id")
            sleep(1)
            id=input("[::] Please enter again your id (as shown above): ")
        try:
            print(client.user_following(id))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 7:
        clear()
        print(GetID(username))
        id=int(input("[::] Please enter your id as shown above: "))
        while checkID(id):
            checkOpt(id,"id")
            sleep(1)
            id=int(input("[::] Please enter again your id as shown above: "))
        try:
            highlights=loader.download_highlights(id)
            sleep(1)
            print(f"[+] Highlights folder path: {fpath(highlights)}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 8:
        clear()
        count=int(input("[+] Number of accounts (to get their stories): "))
        while valOpt(count,1,999):
            checkOpt(count,'other')
            sleep(1)
            count=int(input("[::] Please enter again the number of accounts (to get their stories): "))
        for i in range(count):
            username=str(input("[::] Please enter the username: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input("[::] Please enter the ID as shown above: "))
            while checkID(id):
                checkOpt(id,"id")
                sleep(1)
                id=int(input("[::] Please enter again the ID as shown above: "))
            IDS.append(id)
        try:
            loader.download_stories(IDS)
            sleep(2)
            print(f"[+] Path to folder containing the stories: {fpath(':stories')}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 9:
        clear()
        count=int(input("[?] How many of your saved posts do you want to download ? "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[?] How many of your saved posts do you want to download ? "))
        try:
            loader.download_saved_posts(count)
            print(f"[+] Path to folder containing saved posts: {fpath(':saved')}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 10:
        clear()
        count=int(input("[?] How many posts do you want to download ? "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[?] How many posts do you want to download ? "))
        try:
            loader.download_feed_posts(count)
            print(f"[+] Path to folder containing feed posts: {fpath(':feed')}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 11:
        clear()
        count=int(input("[::] Please enter the number of posts to post: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of posts to post: "))
        for i in range(count):
            path=str(input("[::] Please enter the path to the photo to be uploaded: "))
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=str(input("[::] Please enter again the path to the photo to be uploaded: "))
            sleep(2)
            print(">>>CAPTION<<<")
            sleep(1)
            print("[+] Default: \"Check out my new post !\"")
            sleep(2)
            print("[*] Hit <Tab> and <Enter> to apply the default caption")
            sleep(2)
            caption=str(input("[::] Please enter the caption: "))
            if caption == "\t":
                caption = "Check out my new post !"
            print(">>>TAGS<<<")
            sleep(2)
            print("[+] Default: [No]")
            sleep(2)
            print("[*] Hit <Tab> and <Enter> to apply the default option")
            sleep(2)
            print("[*] Acceptable answers: [yes/no]")
            sleep(2)
            tags=str(input("[?] Do you want to include other users to your post by tagging them ? "))
            while tags.lower() not in ANS or tags == None or tags == '':
                if tags == None or tags == '':
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid answer !")
                    sleep(1)
                    print("[*] Acceptable answers: [yes/no]")
                sleep(1)
                tags=str(input("[?] Do you want to include other users to your post by tagging them ? "))
            if tags.lower() == ANS[0]:
                print("[+] Default: 1")
                sleep(2)
                print("[*] Please enter 'def' to apply the default option")
                sleep(1)
                count=input("[?] How many users do you want to include ? ")
                if count == 'def':
                    username=str(input("[::] Please enter the username: "))
                    while checkUser(username):
                        checkOpt(username, "username")
                        sleep(1)
                        username=str(input("[::] Please enter again the username: "))
                    while valUser(username):
                        CheckVal()
                    username = username.lower().strip()
                else:
                    while checkCount(count):
                        checkOpt(count,"other")
                        sleep(1)
                        count=int(input("[?] How many users do you want to tag ? "))
                    for i in range(count):
                        utag=str(input(f"[::] Please enter the username No{i+1}: "))
                        while checkUser(utag):
                            checkOpt(utag,"username")
                            sleep(1)
                            utag=str(input(f"[::] Please enter again the username No{i+1}: "))
                        while valUser(utag):
                            CheckVal()
                        utag = utag.strip().lower()
                        TaggedUsers.append(utag)
            print(">>>LOCATION<<<")
            sleep(2)
            print("[+] Default: [No]")
            sleep(1)
            print("[*] Please enter 'def' to apply the default option")
            sleep(2)
            print("[*] Acceptable answers: [yes/no]")
            sleep(1)
            loc=str(input("[?] Do you want to include location(s) ? "))
            while (loc.lower() not in ANS or loc == None or loc == '') and loc != 'def':
                if loc == None or loc == '':
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid location !")
                sleep(1)
                print("[*] Acceptable answers: [yes/no]")
                sleep(1)
                loc=str(input("[?] Do you want to include location(s) ? "))
            if loc.lower() == ANS[0]:
                count=int(input("[?] How many ? "))
                while checkCount(count):
                    checkOpt(count,"other")
                    sleep(1)
                    count=int(input("[?] How many locations do you want to include ? "))
                for i in range(count):
                    location=str(input(f"[::] Please enter location No{i+1}: "))
                    while location == None or location == '':
                        print("[!] This field can't be blank !")
                        sleep(1)
                        location=str(input(f"[::] Please enter again location No{i+1}: "))
                    LOCATIONS.append(location)
                    print("[✓] Location added !")
                try:
                    client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                    sleep(2)
                    print("[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)

            if tags.lower() in ANS and loc.lower() in ANS:
                try:
                    client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                    sleep(2)
                    print("[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif tags.lower() in ANS and loc.lower() in ANS:
                try:
                    client.photo_upload(path=path,caption=caption,tags=TaggedUsers)
                    sleep(2)
                    print("[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif tags.lower() in ANS and loc.lower() in ANS:
                try:
                    client.photo_upload(path=path,caption=caption,location=LOCATIONS)
                    sleep(2)
                    print("[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif tags.lower() in ANS and loc.lower() in ANS:
                try:
                    client.photo_upload(path=path,caption=caption)
                    sleep(2)
                    print("[✓] Photo uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 12:
        clear()
        username=str(input("[::] Please enter your username: "))
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        while valUser(username):
            CheckVal()
        username = username.lower().strip()
        EN = ["enable","disable"]
        print("[*] Acceptable answers: [enable/disable]")
        sleep(1)
        endis=str(input("[?] Do you want to enable or disable your notifications ? "))
        while endis.lower() not in EN or endis == None or endis == '':
            if endis == None or endis == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            print("[*] Acceptable answers: [enable/disable]")
            sleep(1)
            endis=input("[?] Do you want to enable or disable your notifications ? ")
        if endis.lower() == EN[0]:
            username=str(input("[::] Please enter your username: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again your username: "))
            while valUser(username):
                CheckVal()
            username = username.lower().strip()
            print("[*] Notifications available for: [posts/reels/stories/videos]")
            sleep(2)
            action=str(input("[?] Which notifications do you want to enable ?"))
            while action.lower() not in ["posts","reels","stories","videos"] or action == None or action == '':
                if action == None or action == '':
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                print("[*] Acceptable answers: [posts/reels/stories/videos]")
                sleep(1)
                action=input("[?] Please enter again the notifications to enable: ")
            if action.lower() == "posts":
                username=str(input("[::] Please enter your username: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                while valUser(username):
                    CheckVal()
                username = username.lower().strip()
                print(GetID(username))
                uid=int(input("[::] Please enter the ID as shown above: "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input("[::] Please enter again the ID as shown above: "))
                try:
                    enabled = client.enable_posts_notifications(uid)
                    if enabled:
                        print("[✓] Post notifications enabled !")
                    else:
                        print("[✕] Can't enable post notifications !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif action.lower() == "reels":
                username=str(input("[::] Please enter your username: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                while valUser(username):
                    CheckVal()
                username = username.lower().strip()
                print(GetID(username))
                uid=int(input("[::] Please enter your ID as shown above: "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input("[::] Please enter again your ID as shown above: "))
                try:
                    enabled = client.enable_reels_notifications(uid)
                    if enabled:
                        print("[✓] Reels notifications enabled !")
                    else:
                        print("[✕] Can't enable reels notifications !")
                    Class()
                except Exception as ex:
                    Except(ex)

            elif action.lower() == "stories":
                username=str(input("[::] Please enter your username: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                while valUser(username):
                    CheckVal()
                username = username.lower().strip()
                print(GetID(username))
                uid=int(input("[::] Please enter the ID as shown above: "))
                while checkID(uid):
                    print("[!] Invalid ID !")
                    sleep(1)
                    uid=int(input("[::] Please enter again the ID as shown above: "))
                try:
                    enabled = client.enable_stories_notifications(uid)
                    if enabled:
                        print("[✓] Stories notifications enabled !")
                    else:
                        print("[✕] Can't enable stories notifications !")
                    Class()
                except Exception as ex:
                    Except(ex)

            else:
                username=str(input("[::] Please enter your username: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                while valUser(username):
                    CheckVal()
                username = username.lower().strip()
                print(GetID(username))
                uid=int(input("[::] Please enter your ID as shown above: "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input("[::] Please enter again your ID as shown above: "))
                try:
                    enabled = client.enable_videos_notifications(uid)
                    print(f"[+] Video notifications enabled: {enabled}")
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 13:
        clear()
        path=str(input("[::] Please enter the path of the photo for your new profile picture: "))
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=str(input("[::] Please enter again the path of the photo for your new profile picture: "))
        try:
            client.account_change_picture(path)
            print("[✓] Your profile pic changed !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 14:
        clear()
        path=str(input("[::] Please enter the path to the photo to be uploaded: "))
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=str(input("[::] Please enter again the path to the photo to be uploaded: "))
        sleep(2)
        print("[*] Acceptable answers: [yes/no]")
        sleep(1)
        AddCaption=str(input("[?] Do you want to add caption ? "))
        while AddCaption.lower() not in ANS or AddCaption == None or AddCaption == '':
            if AddCaption == None or AddCaption == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
                sleep(1)
                print("[*] Acceptable answers: [yes/no]")
            sleep(1)
            AddCaption=str(input("[?] Do you want to add caption ? "))
        if AddCaption.lower() == ANS[0]:
            print("[+] Default: \"Check out my new story !\"")
            sleep(1)
            print("[*] Enter >>> 'def' for the default option to be applied")
            sleep(2)
            caption=str(input("[::] Please enter the caption: "))
            while caption == '' or caption == None or caption == ' ':
                print("[!] This field can't be blank !")
                sleep(1)
                caption=str(input("[::] Please enter again the caption: "))
            if caption == "def":
                caption = "Check out my new story !"
            else:
                caption=str(input("[::] Please enter a caption to include to your story: "))
                while caption == None or caption == '' or caption == ' ':
                    print("[!] This field can't be blank !")
                    sleep(1)
                    caption=str(input("[::] Please enter again a caption to include to your story: "))
        sleep(1)
        print("[*] Acceptable answers: [yes/no]")
        sleep(1)
        AddMention=str(input("[?] Do you want to add mention ? "))
        while AddMention.lower() not in ANS or AddMention == None or AddMention == '':
            if AddMention == None or AddMention == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            print("[*] Acceptable answers: [yes/no]")
            sleep(1)
            mention=str(input("[?] Do you want to mention other user(s) ? "))
        if AddMention.lower() == ANS[0]:
            MENTIONS = []
            count=int(input("[?] How many ? "))
            while checkCount(count):
                checkOpt(count,"other")
                sleep(1)
                count=int(input("[?] How many ? "))
            for i in range(count):
                mention=str(input(f"[::] Please enter the username No{i+1}: "))
                while checkUser(mention):
                    checkOpt(mention, "username")
                    sleep(1)
                    mention=str(input(f"[::] Please enter again the username No{i+1}: "))
                while valUser(mention):
                    checkVal()
                if not mention.islower():
                    mention = mention.lower().strip()
                MENTIONS.append(mention)
        sleep(1)
        print("[*] Acceptable answers: [yes/no]")
        sleep(1)
        AddLoc=str(input("[?] Do you want to add location ? "))
        while AddLoc.lower() not in ANS or AddLoc == None or AddLoc == '':
            if AddLoc == None or AddLoc == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            print("[*] Acceptable answers: [yes/no]")
            sleep(1)
            AddLoc=str(input("[?] Do you want to add location ? "))
        if AddLoc.lower() == ANS[0]:
            count=int(input("[?] How many locations do you want to add ? "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input("[?] How many locations do you want to add ? "))
            for i in range(count):
                loc=str(input(f"[::] Please enter location No{i+1}: "))
                while loc == None:
                    print("[!] This field can't be blank !")
                    sleep(1)
                    loc=str(input(f"[::] Please enter again location No{i+1}: "))
                LOCATIONS.append(loc)
        sleep(1)
        print("[*] Acceptable answers: [yes/no]")
        sleep(1)
        AddLinks=str(input("[?] Do you want to include urls ? "))
        while AddLinks.lower() not in ANS or AddLinks == None or AddLinks == '':
            if AddLinks == None or AddLinks == '':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            AddLinks=str(input("[?] Do you want to include urls ? "))
        if AddLinks.lower() == ANS[0]:
            count=int(input("[?] How many ? "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input("[?] How many urls do you want to include ? "))
            for i in range(count):
                url=str(input(f"[::] Please enter the url No{i+1}: "))
                while url == None or "/" not in url and ("https" not in url or "http" not in url):
                    print("[!] Invalid URL !")
                    sleep(1)
                    print("[+] Example of an acceptable URL: https://example.com")
                    sleep(1)
                    url=str(input(f"[::] Please enter again the url No{i+1}: "))
                while re.get(url).status_code == 404 or re.get(url).status_code == 400:
                    print(f"[+] The URL: {url} doesn't exist")
                    sleep(1)
                    url=str(input(f"[::] Please enter again the url No{i+1}: "))
                LINKS.append(url)
        AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
        while AddHash not in ANS or AddHash == None:
            if AddHash == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
        if AddHash in ANS[:9]:
            count=int(input("[?] How many ? "))
            while checkCount(count):
                checkOpt(count,"other")
                sleep(1)
                count=int(input("[?] How many hashtags do you want to include ? "))
            for i in range(count):
                hashtag=str(input(f"[::] Please enter the hashtag No{i+1}: "))
                while hashtag == None or "#" not in hashtag:
                    print("[!] This field can't be blank !")
                    sleep(1)
                    hashtag=str(input(f"[::] Please enter again the hashtag No{i+1}: "))
                HASHTAGS.append(hashtag)
        if AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,links=LINKS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,links=LINKS,hashtags=HASHTAGS)
                slee(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,locations=LOCATIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,links=LINKS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=AddLinks)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,locations=LOCATIONS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,locations=LOCATIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,links=LINKS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,locations=LOCATIONS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,links=LINKS,hashtags=HASHTAGS)
                sleep(2)
                print("[✓] Story uploaded !")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 15:
        clear()
        hashtag = None
        location = None
        path=str(input("[::] Please enter the path to the video: "))
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=str(input("[::] Please enter again the to the video: "))
        incap=str(input("[?] Do you want to include caption ? [yes/no] "))
        while incap not in ANS or incap == None:
            if incap == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            incap=str(input("[?] Do you want to include caption ? [yes/no] "))
        if incap in ANS[:9]:
            sleep(1)
            print("[+] Default: \"Check out my new video !\"")
            sleep(2)
            print("[*] Hit <Tab> and <Enter> to apply the default option")
            sleep(2)
            caption=str(input("[::] Please enter the caption: "))
            if caption == "\t":
                caption = "Check out my new video !"
        intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
        while intag not in ANS or intag == None:
            if intag == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
        if intag in ANS[:9]:
            count=int(input("[?] How many ? "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input("[?] How many hashtags to include ? "))
            for i in range(count):
                hashtag=str(input(f"[::] Please enter the hashtag No{i+1}: "))
                while checkTag(hashtag):
                    if hashtag == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid hashtag !")
                    sleep(1)
                    hashtag=str(input(f"[::] Please enter again hashtag No{i+1}: "))
                HASHVID.append(hashtag)
                sleep(1)
                print("[✓] Hashtag added !")
        inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
        while inloc not in ANS or inloc == None:
            if inloc == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid location !")
            sleep(1)
            inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
        if inloc in ANS[:9]:
            count=int(input("[?] How many ? "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input("[?] How many locations to include ? "))
            for i in range(count):
                location=str(input(f"[::] Please enter location No{i+1} : "))
                while location == None:
                    print("[!] This field can't be blank !")
                    sleep(1)
                    location=str(input(f"[::] Please enter again location No{i+1} : "))
        try:
            client.video_upload(path,caption,usertags=HASHVID,location=location)
            sleep(2)
            print("[✓] Video uploaded !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 16:
        clear()
        count=int(input("[?] How many accounts do you want to follow ? "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[?] How many accounts do you want to follow ? "))
        if count == 1:
            username=str(input("[::] Please enter the username: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input("[::] Please enter the user's ID as shown above: "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input("[::] Please enter again the user's ID as shown above: "))
            try:
                client.user_follow(id)
                sleep(2)
                print(f"[✓] Followed {username} !")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(count):
                username=str(input(f"[::] Please enter the username No{i+1} :"))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input(f"[::] Please enter again username No{i+1} : "))
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                print(GetID(username))
                id=int(input("[::] Please enter the user's ID as shown above: "))
                while checkID(id):
                    checkOpt(id, "id")
                    sleep(1)
                    id=int(input("[::] Please enter again the user's ID as shown above: "))
                try:
                    client.user_follow(id)
                    sleep(2)
                    print(f"[✓] Followed {username} !")
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 17:
        clear()
        count=int(input("[?] How many accounts do you want to unfollow ? "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[?] How many accounts do you want to unfollow ? "))
        if count == 1: 
            username=str(input("[::] Please enter the username: "))
            while checkUser(username):
                checkOpt(username, username)
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input("[::] Please enter the user's ID as shown above: "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input("[::] Please enter again the user's ID as shown above: "))
            try:
                client.user_unfollow(id)
                sleep(1)
                print(f"[✓] unfollowed {username} !")
                Class()
            except Exception as ex:
                print(f"[!] Can't unfollow {username} !")
        else:
            for i in range(count):
                username=str(input(f"[::] Please enter username No{i+1}: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                try:
                    client.user_unfollow(uid)
                    sleep(2)
                    print(f"[✓] unfollowed {username} !")
                except Exception as e:
                    print(f"[!] Can't unfollow {username} !")
            Class()

    elif option == 18:
        clear()
        count=int(input("[::] Please enter the number of the follow requests to accept: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of the follow requests to accept: "))
        try:
            logini.accept_follow_requests(count,3)
            print("[✓] Follow requests accepted !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 19:
        clear()
        count=int(input("[::] Please enter the number of the follow requests to remove: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of the follow requests to remove: "))
        try:
            logini.remove_follow_requests(count,3)
            print("[✓] Follow requests removed !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 20:
        clear()
        count=int(input("[::] Please enter the number of users to follow:  "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of users to follow: "))
        countu=int(input("[?] From how many users do you want to follow their followers ? "))
        while checkCount(countu):
            checkOpt(countu, "other")
            sleep(1)
            countu=int(input("[?] From how many users do you want to follow their followers ? "))
        for i in range(countu):
            username=str(input("[::] Please enter the username of the user (to follow their followers): "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            FUFERS.append(username)
        try:
            logini.follow_user_followers(FUFERS,count)
            sleep(2)
            print("[✓] Followed users !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 21:
        clear()
        username=str(input("[::] Please enter the first username: "))
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again the first username: "))
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
            id=int(input("[::] Please enter the user's ID as shown above: "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input("[::] Please enter again the user's ID as shown above: "))
            try:
                client.user_follow(id)
                sleep(2)
                print(f"[✓] Followed {L[i]} !")
            except Exception as ex:
                Except(ex)
            Class()

    elif option == 22:
        clear()
        count=int(input("[?] How many messages do you want to send ? "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[?] How many messages do you want to send ? "))
        for i in range(count):
            text=str(input("[::] Please enter the message to send >>>  "))
            while text == None:
                print("[!] This field can't be blank !")
                sleep(1)
                text=str(input("[::] Please enter again the text to send >>>  "))
            count=int(input("[?] In how many users do you want to send it ? "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input("[?] In how many users do you want to send it ? "))
            for j in range(count):
                username=str(input(f"[::] Please enter the username No{j+1} : "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input(f"[::] Please enter again the username No{j+1} : "))
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                print(GetID(username))
                id=int(input("[::] Please enter the ID of the user as shown above: "))
                while checkID(id):
                    checkOpt(id, "id")
                    sleep(1)
                    id=int(input("[::] Please enter again the ID of the user as shown above: "))
                MSGIDS.append(id)
                try:
                    client.direct_send(text,MSGIDS)
                    sleep(1)
                    print("[✓] Message sent !")
                except Exception as ex:
                    Except(ex)
        Class()

    elif option == 23:
        clear()
        path=str(input("[::] Please enter the path to the file: "))
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=str(input("[::] Please enter again the path to the file: "))
        count=int(input("[?] In how many users do you want to send it ? "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[?] In how many users do you want to send it ? "))
        for i in range(count):
            username=str(input(f"[::] Please enter the username No{i+1}: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input(f"[::] Please enter again the username No{i+1} : "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            FILEIDS.append(id)
            try:
                client.direct_send_file(path,FILEIDS)
                sleep(2)
                print("[✓] File sent !")
            except Exception as ex:
                Except(ex)
        Class()

    elif option == 24:
        clear()
        path=str(input("[::] Please enter the path to the photo: "))
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=str(input("[::] Please enter again the path to the photo: "))
        count=int(input("[?] In how many users do you want to send it ? "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[?] In how many users do you want to send it ? "))
        for i in range(count):
            username=str(input(f"[::] Please enter the username No{i+1} : "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input(f"[::] Please enter again the username No{i+1} : "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            PHOTOIDS.append(id)
            try:
                client.direct_send_photo(path,PHOTOIDS)
                sleep(2)
                print("[✓] Photo sent !")
            except Exception as ex:
                Except(ex)
        Class()

    elif option == 25:
        clear()
        path=str(input("[::] Please enter the path to the video: "))
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=str(input("[::] Please enter again the path to the video: "))
        count=int(input("[?] In how many users do you want to send it ? "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[?] In how many users do you want to send it ? "))
        for i in range(count):
            username=str(input(f"[::] Please enter the username No{i+1} : "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input(f"[::] Please enter again the username No{i+1} : "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            VIDEOIDS.append(id)
            try:
                client.direct_send_video(path,VIDEOIDS)
                sleep(2)
                print("[✓] Video sent !")
            except Exception as ex:
                Except(ex)
        Class()

    elif option == 26:
        clear()
        count=int(input("[::] Please enter the number of hashtags: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of hashtags: "))
        nump=int(input("[::] Please enter the number of the posts to like: "))
        while checkCount(nump):
            checkOpt(nump, "other")
            sleep(1)
            nump=int(input("[::] Please enter again the number of the posts to like: "))
        for i in range(count):
            hashtag=str(input(f"[::] Please enter the hashtag No{i+1} : "))
            while checkTag(hashtag):
                print("[!] Invalid hashtag !")
                sleep(1)
                if "#" not in hashtag:
                    print("[+] Please include the   #   symbol")
                sleep(1)
                hashtag=str(input(f"[::] Please enter again the hashtag No{i+1} : "))
            LTAGS.append(hashtag)
            print("[!] Hashtag added !")
        rtags=str(input("[?] Do you want to like random tags ? [yes/no] "))
        while rtags not in ANS or rtags == None:
            if rtags == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            rtags=input("[?] Do you want to like random hashtags ? [yes/no] ")
        if rtags in ANS[:9]:
            random = True
        else:
            random = False
        try:
            logini.like_by_tags(LTAGS,random,count)
            sleep(2)
            print("[✓] Posts liked !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 27:
        clear()
        countu=int(input("[::] Please enter the number of accounts: "))
        while checkCount(countu):
            checkOpt(countu, "other")
            sleep(1)
            countu=int(input("[::] Please enter again the number of accounts: "))
        count=int(input("[::] Please enter the number of posts to like: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of posts to like: "))
        if countu == 1:
            username=str(input("[::] Please enter the username: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            LBU.append(username)
            try:
                logini.like_by_users(LBU,count)
                sleep(2)
                print("[✓] Posts liked !")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(countu):
                username=str(input(f"[::] Please enter the username No{i+1} : "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input(f"[::] Please enter again the username No{i+1} : "))
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                LBU.append(username)
            try:
                logini.like_by_users(LBU,count)
                sleep(2)
                print("[✓] Posts liked !")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 28:
        clear()
        rand=str(input("[?] Do you want to like the posts with random order ? [yes/no] "))
        while rand not in ANS or rand == None:
            if rand == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
        if rand in ANS[:9]:
            random = True
        else:
            random = False
        numloc=int(input("[::] Please enter the number of locations to like their posts: "))
        while checkCount(numloc):
            checkOpt(numloc, "other")
            sleep(1)
            numloc=int(input("[::] Please enter again the number of locations to like their posts: "))
        sleep(1)
        countp=int(input("[?] How many posts to like per location ? "))
        while checkCount(countp):
            checkOpt(countp, "other")
            sleep(1)
            countp=int(input("[?] How many posts to like per location ? "))
        for i in range(numloc):
            location=str(input(f"[::] Please enter location No{i+1} : "))
            while location == None:
                print("[!] This field can't be empty !")
                sleep(1)
                location=str(input(f"[::] Please enter again location No{i+1} : "))
            LOCLIKE.append(location)
        try:
            logini.like_by_locations(LOCLIKE,number=countp,randomize=random)
            sleep(2)
            print("[✓] Posts liked !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 29:
        clear()
        count=int(input("[+] Please enter the number of posts to like: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of posts to like: "))
        if count == 1:
            rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
            while rand not in ANS or rand == None:
                if rand == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
            if rand in ANS[:9]:
                rmize = True
            else:
                rmize = False
            try:
                logini.like_by_feed(count,rmize)
                sleep(2)
                print("[✓] Posts liked !")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
            while rand not in ANS or rand == None:
                if rand == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
            if rand in ANS[:9]:
                random = True
            else:
                random = False
            for i in range(count):
                try:
                    logini.like_by_feed(count,random)
                    sleep(1)
                    print("[✓] Posts liked !")
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 30:
        clear()
        amo=int(input("[::] Please enter the number of posts to like: "))
        while checkCount(amo):
            checkOpt(amo, "other")
            sleep(1)
            amo=int(input("[::] Please enter again the number of posts to like: "))
        username=str(input("[::] Please enter the username: "))
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        while valUser(username):
            if type(CheckVal()) == bool:
                    CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        print(GetID(username))
        id=int(input("[::] Please enter user's ID as shown above: "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            id=int(input("[::] Please enter again user's ID as shown above: "))
        try:
            bot.comment_user(id,amo)
            sleep(2)
            print("[✓] Comment made !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 31:
        clear()
        count=int(input("[::] Please enter the number of replies: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of replies to save: "))
        for i in range(count):
            reply=str(input(f"[::] Please enter the reply No{i+1}: "))
            while reply == None:
                print("[!] This field can't be blank !")
                sleep(1)
                reply=str(input(f"[::] Please enter again the reply No{i+1}: "))
            REPLS.append(reply)
        try:
            logini.set_comment_replies(REPLS)
            sleep(2)
            print("[✓] Default replies applied !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 32:
        clear()
        print("[+] Default: \"Love it !\"")
        com=str(input("[::] Please enter your comment: "))
        while com == None:
            print("[!] This field can't be blank !")
            sleep(1)
            com=str(input("[::] Please enter again your comment: "))
        webbrowser.open("https://www.instagram.com")
        print("[+] Please find the post to comment and wait...")
        found=str(input("[::] If found enter [yes]: "))
        while found not in ANS[:9] or found == None:
            if found == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            found=str(input("[::] If found enter [yes]: "))
        if found in ANS[:9]:
            browser=webdriver.Firefox()
            link=str(input("[::] Please enter the url for the post: "))
            while link == None or "https" not in link or "//" not in link or "instagram" not in link or "www" not in link or ".com" not in link:
                print("[!] Invalid url !")
                sleep(1)
                link=str(input("[::] Please enter again the url for the post: "))
            browser.get(link)
            try:
                comment_label = browser.find_element_by_class_name("_ablz _aaoc")
                comment_label.send_keys(com)
                publish = browser.find_element_by_class_name("_aacl _aaco _aacw _adda _aad0 _aad6 _aade")
                publish.click()
                sleep(2)
                print("[✓] Comment made !")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 33:
        clear()
        count=int(input("[::] Please enter the number of users to block: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of users to block: "))
        if count == 1:
            username=str(input("[::] Please enter the username: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            BLOCKU.append(id)
            try:
                bot.block_users(BLOCKU)
                sleep(2)
                print("[✓] User blocked !")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(count):
                username=str(input(f"[::] Please enter the username No{i+1}: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input(f"[::] Please enter again the username No{i+1}: "))
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                print(GetID(username))
                id = int(input("[::] Please enter the ID of the user as shown above: "))
                while checkID(id):
                    checkOpt(id, "id")
                    sleep(1)
                    id = int(input("[::] Please enter again the ID of the user as shown above: "))
                BLOCKU.append(id)
            try:
                bot.block_users(BLOCKU)
                sleep(2)
                print("[✓] Users blocked !")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 34:
        clear()
        id=int(input("[::] Please enter the ID of the user: "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            id=int(input("[::] Please enter again the ID of the user: "))
        try:
            print("[+] Username: "+client.username_from_user_id(id))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 35:
        clear()
        try:
            print("[+] Blocked users: ")
            print("\n")
            print(api.blocked_user_list())
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 36:
        clear()
        counti=int(input("[::] How many highlights do you want to create ? "))
        while checkCount(counti):
            checkOpt(counti, "other")
            sleep(1)
            counti=int(input("[::] How many highlights do you want to create ? "))
        if counti == 1:
            title=str(input("[::] Please enter the title of the highlight: "))
            while title == None:
                print("[!] This field can't be blank !")
                sleep(1)
                title=str(input("[::] Please enter again the title of the highlight: "))
            count=int(input("[::] Please enter the number of stories to add in the highlight: "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input("[::] Please enter again the number of stories to add in the highlight: "))
            for i in range(count):
                story_id=int(input(f"[::] Please enter the story ID No{i+1}: "))
                while story_id == None:
                    print("[!] This field can't be blank !")
                    sleep(1)
                    story_id=int(input(f"[::] Please enter again the story ID No{i+1}: "))
                STIDS.append(story_id)
            try:
                client.highlight_create(title,STIDS)
                sleep(2)
                print("[✓] Highlight created !")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(counti):
                title=str(input(f"[::] Please enter the title of the highlight No{i+1}: "))
                while title == None:
                    print("[!] This field can't be blank !")
                    sleep(1)
                    title=str(input(f"[::] Please enter again the title of the highlight No{i+1}: "))
                count=int(input("[::] Please enter the number of stories to add in the highlight: "))
                while checkCount(count):
                    checkOpt(count, "other")
                    sleep(1)
                    count=int(input("[::] Please enter again the number of stories to add in the highlight: "))
                for i in range(count):
                    story_id=int(input(f"[::] Please enter the story ID No{i+1}: "))
                    while story_id == None:
                        print("[!] This field can't be blank !")
                        sleep(1)
                        story_id = int(input(f"[::] Please enter again the story ID No{i+1}: "))
                    STIDS.append(story_id)
                try:
                    client.highlight_create(title,STIDS)
                    sleep(2)
                    print("[✓] Highlight created !")
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 37:
        clear()
        count=int(input("[::] How many highlights do you want to delete ? "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] How many highlights do you want to delete ? "))
        if count == 1:
            hid=int(input("[::] Please enter the highlight ID: "))
            while hid == None:
                print("[!] This field can't be blank !")
                sleep(1)
                hid=int(input("[::] Please enter again the highlight ID: "))
            try:
                api.highlight_delete(hid)
                sleep(2)
                print("[✓] Highlight deleted !")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(count):
                hid=int(input(f"[::] Please enter the highlight ID No{i+1}: "))
                while hid == None:
                    print("[!] This field can't be blank !")
                    sleep(1)
                    hid=int(input(f"[::] Please enter again the highlight ID No{i+1}: "))
                try:
                    api.highlight_delete(hid)
                    sleep(2)
                    print("[!] Highlight deleted !")
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 38:
        clear()
        count=int(input("[::] How many covers of highlights do you want to change ? "))
        while checkCount(count, "other"):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] How many covers of highlights do you want to change ? "))
        if count == 1:
            url=str(input("[::] Please enter the url to the highlight: "))
            while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
                if url == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid url !")
                sleep(1)
                url=str(input("[::] Please enter again the url to the highlight: "))
            print(Get_Hpk(url))
            pk=int(input("[::] Please enter the highlight id as shown above: "))
            while pk == None:
                print("[!] This field can't be blank !")
                sleep(1)
                pk=int(input("[::] Please enter again the highlight id as shown above: "))
            path=str(input("[::] Please enter the path to the cover for the highlight: "))
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=str(input("[::] Please enter again the path of the cover for the highlight: "))
            try:
                client.highlight_change_cover(pk,path) 
                sleep(2)
                print("[✓] Highlight cover changed !")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(count):
                url=str(input("[::] Please enter the url for the highlight: "))
                while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
                    print("[!] This field can't be blank !")
                    sleep(1)
                    url=str(input("[::] Please enter again the url for the highlight: "))
                print(Get_Hpk(url))
                pk=int(input("[::] Please enter the highlight id as shown above: "))
                while pk == None:
                    print("[!] This field can't be blank !")
                    sleep(1)
                    pk=int(input("[::] Please enter again the highlight id as shown above: "))
                path=str(input("[::] Please enter the path of the cover for the highlight: "))
                while checkPath(path):
                    checkOpt(path, "path")
                    sleep(1)
                    path=str(input("[::] Please enter again the path of the cover for the highlight: "))
                try:
                    client.highlight_change_cover(pk,path) 
                    sleep(2)
                    print("[✓] Highlight cover changed !")
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 39:
        clear()
        countu=int(input("[::] From how many users you want to display their highlights ? "))
        while checkCount(countu):
            checkOpt(countu, "other")
            sleep(1)
            countu=int(input("[::] From how many users you want to display their highlights ? "))
        if countu == 1:
            username=str(input("[::] Please enter the username: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            number=int(input("[::] How many highlights do you want to display ? "))
            while checkCount(number):
                checkOpt(number, "count")
                sleep(1)
                number=int(input("[::] How many highlights do you want to display ? "))
            try:
                HL = client.user_highlights(id,number)
                for i in range(len(HL)):
                    print(f"[+] Highlight: {L[i]}")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(countu):
                username=str(input("[::] Please enter the username: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                print(GetID(username))
                id=int(input("[::] Please enter the ID of the user as shown above: "))
                while checkID(id):
                    checkOpt(id, "id")
                    sleep(1)
                    id=int(input("[::] Please enter again the ID of the user as shown above: "))
                number=int(input("[::] How many highlights do you want to display ? "))
                while checkCount(number):
                    checkOpt(number, "count")
                    sleep(1)
                    number=int(input("[::] How many highlights do you want to display ? "))
                try:
                    HL = client.user_highlights(id,number)
                    for j in range(len(HL)):
                        print(f"[+] Highlight: {HL[j]}")
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 40:
        clear()
        counti=int(input("[::] From how many highlights do you want to retrieve information ? "))
        while checkCount(counti):
            checkOpt(counti, "other")
            sleep(1)
            counti=int(input("[::] From how many highlights do you want to retrieve information ? "))
        if counti == 1:
            url=str(input("[::] Please enter the url for the highlight: "))
            while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
                print("[!] This field can't be blank !")
                sleep(1)
                url=str(input("[::] Please enter again the url for the highlight: "))
            print(Get_Hpk(url))
            pk=int(input("[::] Please enter the highlight id as shown above: "))
            while pk == None:
                if pk == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid ID !")
                sleep(1)
                pk=int(input("[::] Please enter again the highlight id as shown above: "))
            try:
                print(client.highlight_info(pk))
                sleep(2)
                print("[✓] retrieved information !")
                Class()
            except Exception as ex:
                Except(ex)
        else:
            for i in range(counti):
                url=str(input("[::] Please enter the url for the highlight: "))
                while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
                    if url == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid url !")
                    sleep(1)
                    url=str(input("[::] Please enter again the url for the highlight: "))
                print(Get_Hpk(url))
                pk=int(input("[::] Please enter the highlight id as shown above: "))
                while pk == None:
                    if pk == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid ID !")
                    sleep(1)
                    pk=int(input("[::] Please enter again the highlight id as shown above: "))
                try:
                    print(client.highlight_info(pk))
                    sleep(2)
                    print("[✓] retrieved information !")
                except Exception as ex:
                    Except(ex)
            Class()

    elif option == 41:
        clear()
        url=str(input("[::] Please enter the url of the story: "))
        while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
            print("[!] This field can't be blank !")
            sleep(1)
            url=str(input("[::] Please enter again the url of the story: "))
        print(Get_Spk(url))
        pk=int(input("[::] Please enter the story ID as shown above: "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            pk=int(input("[::] Please enter again the story ID as shown above: "))
        try:
            dels = client.story_delete(pk)
            if dels:
                print("[✓] Story deleted !")
            else:
                print("[!] Can't delete story !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 42:
        clear()
        url=str(input("[::] Please enter the url of the story: "))
        while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
            print("[!] This field can't be blank !")
            sleep(1)
            url=str(input("[::] Please enter again the url of the story: "))
        print(Get_Spk(url))
        pk=int(input("[::] Please enter the story ID as shown above: "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            pk=int(input("[::] Please enter again the story ID as shown above: "))
        number=int(input("[::] Please enter the number of viewers to display: "))
        while checkCount(number):
            checkOpt(number, "count")
            sleep(1)
            number=int(input("[::] Please enter again the number of viewers to display: "))
        try:
            L = client.story_viewers(pk,number)
            for i in range(len(L)):
                print(f"[+] Viewer No{i+1}: {L[i]}")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 43:
        clear()
        count=int(input("[::] Please specify the number of hashtags: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please specify again the number of hashtags: "))
        for i in range(count):
            tag=input(f"[::] Please enter the hashtag No{i+1} (include the  #  symbol): ")
            while checkTag(tag):
                if tag == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid hashtag !")
                sleep(1)
                tag=input(f"[::] Please enter again the hashtag No{i+1}: ")
            STBTGS.append(tag)
        try:
            print(logini.story_by_tags(STBTGS))
            sleep(2)
            print("[✓] Request successful !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 44:
        clear()
        count=int(input("[::] Please specify the number of users: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please specify again the number of users: "))
        for i in range(count):
            username=str(input(f"[::] Please enter the username No{i+1}: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input(f"[::] Please enter again the username No{i+1}: "))
            while valUser(username):
                if type(CheckVal()) == bool:
                    CheckVal()
                else:
                    username = CheckVal()
            username = username.lower().strip()
            print(GetID(username))
            id=int(input("[::] Please enter the ID as shown above: "))
            while checkID(id):
                checkOpt(id, "id")
                sleep(1)
                id=int(input("[::] Please enter again the ID as shown above: "))
            GTST.append(id)
        try:
            print(loader.get_stories(GTST))
            sleep(2)
            print("[✓] Request successful !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 45:
        clear()
        url=str(input("[::] Please enter the url of the story: "))
        while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
            print("[!] This field can't be blank !")
            sleep(1)
            url=str(input("[::] Please enter again the url of the story: "))
        print(Get_Spk(url))
        pk=int(input("[::] Please enter the story ID as shown above: "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            pk=int(input("[::] Please enter again the story ID as shown above: "))
        try:
            print(client.story_info_v1(pk))
            sleep(2)
            print("[✓] Request successful !")
        except Exception as ex:
            Except(ex)

    elif option == 46:
        clear()
        print("[+] Countries example: US, BR, CZ")
        sleep(1)
        fcodes=str(input("[?] Do you want to display full list of country codes ? [yes/no] "))
        while fcodes not in ANS or fcodes == None:
            if fcodes == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            fcodes=str(input("[?] Do you want to display full list of country codes ? [yes/no] "))
        if fcodes in ANS[:9]:
            webbrowser.open("https://www.iban.com/country-codes")
        country=str(input("[::] Please enter the country: "))
        while country == None:
            print("[!] This field can't be blank !")
            sleep(1)
            country=str(input("[::] Please enter again the country: "))
        try:
            client.set_country(country)
            sleep(2)
            print("[✓] Country applied !")
        except Exception as ex:
            Except(ex)

    elif option == 47:
        clear()
        bio=str(input("[::] Please enter the text for the bio: "))
        while bio == None:
            print("[!] This field can't be blank !")
            sleep(1)
            bio=str(input("[::] Please enter again the text for the bio: "))
        try:
            client.account_set_biography(bio)
            sleep(2)
            print("[✓] Bio applied !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 48:
        clear()
        username=str(input("[::] Please enter your username: "))
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        while valUser(username):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        try:
            info = client.user_info_by_username_v1(username)
            sleep(1)
            print("[✓] Information gathering successful !")
            sleep(2)
            print(info)
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 49:
        clear()
        username=str(input("[::] Please enter the username: "))
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        while valUser(username):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        print(GetID(username))
        id=int(input("[::] Please enter the ID as shown above: "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            id=int(input("[::] Please enter again the ID as shown above: "))
        try:
            posts=client.usertag_medias_v1(id)
            sleep(2)
            print("[✓] Request successful !")
            sleep(1)
            for i in range(len(posts)):
                print(posts[i])
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 50:
        clear()
        username=str(input("[::] Please enter your username: "))
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        while valUser(username):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                username = CheckVal()
        username = username.lower().strip()
        try:
            dictr = client.reset_password(username)
            sleep(2)
            print("[✓] Password reset successfull !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 51:
        clear()
        set_first_name=str(input("[?] Do you want to set a first name ? [yes/no] "))
        while set_first_name == None or set_first_name not in ANS:
            if set_first_name == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            set_first_name=str(input("[?] Do you want to set a first name ? [yes/no] "))
        if set_first_name in ANS[:9]:
            first_name=str(input("[::] Please enter your first name: "))
            while first_name == None:
                print("[!] This field can't be blank !")
                sleep(1)
                first_name=str(input("[::] Please enter again your first name: "))
        set_bio=str(input("[?] Do you want to set a bio ? [yes/no] "))
        while set_bio == None or set_bio not in ANS:
            if set_bio == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            set_bio=str(input("[?] Do you want to set a bio ? [yes/no] "))
        if set_bio in ANS[:9]:
            bio=str(input("[::] Please enter the bio: "))
            while bio == None:
                print("[!] This field can't be blank !")
                sleep(1)
                bio=str(input("[::] Please enter again the bio: "))
        set_ex_url=str(input("[?] Do you want to add an external url ? [yes/no] "))
        while set_ex_url == None or set_ex_url not in ANS:
            if set_ex_url == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            set_ex_url=str(input("[?] Do you want to set an external url ? [yes/no] "))
        if set_ex_url in ANS[:9]:
            url=str(input("[::] Please enter the url: "))
            while url == None or "/" not in url or "//" not in url:
                print("[!] This field can't be blank !")
                sleep(1)
                url=str(input("[::] Please enter again the url: "))
        set_email=str(input("[?] Do you want to add an email ? [yes/no] "))
        while set_email == None or set_email not in ANS:
            if set_email == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            set_email=str(input("[?] Do you want to set an email ? [yes/no] "))
        if set_email in ANS[:9]:
            email=str(input("[::] Please enter the email address: "))
            while email == None or "@" not in email or "gmail" not in email or ".com" not in email:
                if email == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid email address !")
                sleep(1)
                email=str(input("[::] Please enter again the email address: "))
        set_phone_number=str(input("[?] Do you want to add a phone number ? [yes/no] "))
        while set_phone_number == None or set_phone_number not in ANS:
            if set_phone_number == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            set_phone_number=str(input("[?] Do you want to set a phone number ? [yes/no] "))
        if set_phone_number in ANS[:9]:
            phone_number=int(input("[::] Please enter the phone number: "))
            while phone_number == None:
                print("[!] This field can't be blank !")
                sleep(1)
                phone_number=int(input("[::] Please enter again the phone number: "))
        set_gender=str(input("[?] Do you want to set a gender ? [yes/no] "))
        while set_gender == None or set_gender not in ANS:
            if set_gender == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            set_gender=str(input("[?] Do you want to set a gender ? [yes/no] "))
        if set_gender in ANS[:9]:
            gender=str(input("[::] Please enter the gender: "))
            while gender == None:
                print("[!] This field can't be blank !")
                sleep(1)
                gender=str(input("[::] Please enter again the gender: "))
        try:
            api.edit_profile(first_name,bio,url,email,phone_number,gender)
            sleep(2)
            print("[✓] Profile edited !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 52:
        clear()
        count=int(input("[::] How many posts do you want to like/unlike ? "))
        while checkCount(count):
            checkOpt(count, "count")
            sleep(1)
            count=int(input("[::] How many posts do you want to like/unlike ? "))
        browser = webdriver.Chrome()
        for i in range(count):
            url=str(input("[::] Please enter the url of the post: "))
            while url == None or "https" not in url and "instagram" not in url and "//" not in url and ".com" not in url and "/" not in url:
                print("[!] This field can't be blank !")
                sleep(1)
                url=str(input("[::] Please enter again the url of the post: "))
            try:
                browser.get(url)
                like = browser.find_element_by_id("mount_0_0_Cs")
                like.click()
                sleep(2)
                print("[✓] Posts liked !")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 53:
        clear()
        count=int(input("[::] Please enter the number of deletes to make: "))
        while checkCount(count):
            checkOpt(count, "count")
            sleep(1)
            count=int(input("[::] Please enter again the number of deletes to make: "))
        browser = webdriver.Chrome()
        for i in range(count):
            url=str(input("[::] Please enter the url of the post, igtv, reel etc. : "))
            while url == None or "https" not in url and "instagram" not in url and "//" not in url and ".com" not in url and "/" not in url:
                print("[!] This field can't be blank !")
                sleep(1)
                url=str(input("[::] Please enter again the url of the post, igtv, reel etc. : "))
            try:
                browser.get(url)
                menu = browser.find_element_by_class_name("_ab6-")
                menu.click()
                delete = browser.find_element_by_class_name("_a9-- _a9-_")
                delete.click()
                sleep(2)
                print("[✓] Deleted !")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 54:
        count=int(input("[::] Please enter the number of the posts, igtv, reels etc. to save: "))
        while checkCount(count):
            checkOpt(count, "count")
            sleep(1)
            count=int(input("[::] Please enter again the number of the posts to save: "))
        browser = webdriver.Chrome()
        for i in range(count):
            url=str(input("[::] Please enter the url of the post, igtv, reel etc. : "))
            while url == None or "https" not in url and "instagram" not in url and "//" not in url and ".com" not in url and "/" not in url:
                print("[!] This field can't be blank !")
                sleep(1)
                url=str(input("[::] Please enter again the url of the post, igtv, reel etc. : "))
            try:
                browser.get(url)
                save = browser.find_element_by_class_name("_abm0 _abm1")
                save.click()
                sleep(2)
                print("[✓] Saved !")
                Class()
            except Exception as ex:
                Except(ex)

    elif option == 55:
        clear()
        __time__=str(input("[::] Please enter the time (example: 15:06:10): "))
        while __time__ == None or ":" not in __time__:
            print("[!] This field can't be blank !")
            sleep(1)
            __time__=str(input("[::] Please enter again the time (example: 15:06:10): "))
        Av_Acts()
        cur_time = datetime.now()
        current_time = cur_time.now("%H:%M:%S")
        action=int(input("[::] Please enter the number of the action: "))
        while valOpt(action, 1, 26):
            if action == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid number !")
            sleep(1)
            action=int(input("[::] Please enter again the number of the action: "))
        if action == 1:
            count=int(input("[::] Please enter the number of posts to post: "))
            while checkCount(count):
                checkOpt(count, "count")
                sleep(1)
                count=int(input("[::] Please enter again the number of posts to post: "))
            for i in range(count):
                path=str(input("[::] Please enter the path to the photo: "))
                while checkPath(path):
                    checkOpt(path, "path")
                    sleep(1)
                    path=str(input("[::] Please enter again the path to the photo: "))
                sleep(2)
                print(">>>CAPTION<<<")
                sleep(1)
                print("[+] Default: \"Check out my new post !\"")
                sleep(2)
                print("[*] Hit <Tab> and <Enter> to apply the default option")
                sleep(2)
                caption=str(input("[::] Please enter the caption: "))
                if caption == "\t":
                    caption = "Check out my new post !"
                print(">>>TAGS<<<")
                sleep(2)
                print("[+] Default: [No]")
                sleep(2)
                print("[*] Hit <Tab> and <Enter> to apply the default option")
                sleep(2)
                tags=str(input("[?] Do you want to tag other users ? [yes/no] "))
                while tags not in ANS or tags == None:
                    if tags == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid input !")
                    sleep(1)
                    tags=str(input("[?] Do you want to tag other users ? [yes/no] "))
                if tags == "\t":
                    tags = "no"
                if tags in ANS[:9]:
                    print("[+] Default: 1")
                    sleep(2)
                    print("[*] Hit <Tab> and <Enter> to apply the default option")
                    count=int(input("[?] How many users do you want to include ? "))
                    while checkCount(count):
                        checkOpt(count, "count")
                        sleep(1)
                        count=int(input("[?] How many users do you want to tag ? "))
                    utag=str(input("[::] Please enter the username: "))
                    while checkUser(username):
                        checkOpt(username, "username")
                        sleep(1)
                        utag=str(input("[::] Please enter again the username: "))
                    while valUser(utag):
                        if type(CheckVal()) == bool:
                            CheckVal()
                        else:
                            utag = CheckVal()
                    utag = utag.lower().strip()
                    TaggedUsers.append(utag)
                    for i in range(count):
                        utag=str(input(f"[::] Please enter the username No{i+1}: "))
                        while checkUser(utag):
                            checkOpt(utag, "username")
                            sleep(1)
                            utag=str(input(f"[::] Please enter again the username No{i+1}: "))
                        while valUser(utag):
                            if type(CheckVal()) == bool:
                                CheckVal()
                            else:
                                utag = CheckVal()
                        utag = utag.strip().lower()
                        TaggedUsers.append(utag)
                print(">>>LOCATION<<<")
                sleep(2)
                print("[+] Default: [No]")
                sleep(1)
                print("[*] Hit <Tab> and <Enter> to apply the default option")
                sleep(2)
                loc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
                while loc not in ANS or loc == None:
                    if loc == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid input !")
                    sleep(1)
                    loc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
                if loc == "\t":
                    loc = "no"
                if loc in ANS[:9]:
                    count=int(input("[?] How many ? "))
                    while checkCount(count):
                        checkOpt(count, "count")
                        sleep(1)
                        count=int(input("[?] How many locations do you want to include ? "))
                    for i in range(count):
                        location1=str(input(f"[::] Please enter location No{i+1}: "))
                        while location1 == None:
                            print("[!] This field can't be blank !")
                            sleep(1)
                            location1=str(input(f"[::] Please enter again location No{i+1}: "))
                        LOCATIONS.append(location1)
                        print("[✓] Location added !")
                    if current_time == __time__:
                        try:
                            client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                            sleep(2)
                            print("[✓] Photo uploaded !")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"[+] Current time: {current_time}")
                        sleep(1)
                        print(f"[+] Waiting for time: {__time__}")
                        Class()

                if tags in ANS[:9] and loc in ANS[:9]:
                    if current_time == __time__:
                        try:
                            client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                            print("[✓] Photo uploaded !")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"[+] Current time: {current_time}")
                        sleep(1)
                        print(f"[+] Waiting for time: {__time__}")
                        Class()
                elif tags in ANS[:9] and loc in ANS[9:]:
                    if current_time == __time__:
                        try:
                            client.photo_upload(path=path,caption=caption,tags=TaggedUsers)
                            print("[✓] Photo uploaded !")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"[+] Current time: {current_time}")
                        sleep(1)
                        print(f"[+] Waiting for time: {__time__}")
                        Class()
                elif tags in ANS[9:] and loc in ANS[:9]:
                    if current_time == __time__:
                        try:
                            client.photo_upload(path=path,caption=caption,location=LOCATIONS)
                            print("[✓] Photo uploaded !")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"[+] Current time: {current_time}")
                        sleep(1)
                        print(f"[+] Waiting for time: {__time__}")
                        Class()
                elif tags in ANS[9:] and loc in ANS[9:]:
                    if current_time == __time__:
                        try:
                            client.photo_upload(path=path,caption=caption)
                            print("[✓] Photo uploaded !")
                            Class()
                        except Exception as ex:
                            Except(ex)
                    else:
                        print(f"[+] Current time: {current_time}")
                        sleep(1)
                        print(f"[+] Waiting for time: {__time__}")
                        Class()

        elif action == 2:
            path=str(input("[::] Please enter the path to the picture: "))
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=str(input("[::] Please enter again the path to the picture: "))
            try:
                client.account_change_picture(path)
                sleep(2)
                print("[✓] Profile picture changed !")
                Class()
            except Exception as ex:
                Except(ex)

        elif action == 3:
            path=str(input("[::] Please enter the path to the photo: "))
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=str(input("[::] Please enter again the path to the photo: "))
            AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
            while AddCaption not in ANS or AddCaption == None:
                if AddCaption == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
            if AddCaption in ANS[:9]:
                print("[+] Default: \"Check out my new story !\"")
                sleep(2)
                print("[*] Hit <Tab> and <Enter> for the default option to be applied")
                sleep(2)
                caption=str(input("[::] Please enter the caption: "))
                if caption == "\t":
                    caption = "Check out my new story !"
                else:
                    caption=str(input("[::] Please enter a caption to include: "))
                    while caption == None:
                        print("[!] This field can't be blank !")
                        sleep(1)
                        caption=str(input("[::] Please enter again a caption to include: "))
            AddMention=str(input("[?] Do you want to add mention ? [yes/no] "))
            while AddMention not in ANS or AddMention == None:
                if AddMention == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                mention=str(input("[?] Do you want to mention user(s) ? [yes/no] "))
            if AddMention in ANS[:9]:
                MENTIONS = []
                count=int(input("[?] How many ? "))
                while checkCount(count):
                    checkOpt(count, "count")
                    sleep(1)
                    count=int(input("[?] How many users do you want to mention ? "))
                for i in range(count):
                    mention=str(input(f"[::] Please enter the username No{i+1}: "))
                    while checkUser(mention):
                        checkOpt(mention, "username")
                        sleep(1)
                        mention=str(input(f"[::] Please enter again the username No{i+1}: "))
                    while valUser(mention):
                        if type(CheckVal()) == bool:
                            CheckVal()
                        else:
                            mention = CheckVal()
                    mention = mention.lower().strip()
                    MENTIONS.append(mention)
                    sleep(1)
                    print("[✓] Mention added !")
            AddLoc=str(input("[?] Do you want to add location ? [yes/no] "))
            while AddLoc not in ANS or AddLoc == None:
                if AddLoc == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                AddLoc=str(input("[?] Do you want to add location ? [yes/no] "))
            if AddLoc in ANS[:9]:
                count=int(input("[?] How many locations do you want to add ? "))
                while checkCount(count):
                    checkOpt(count, "count")
                    sleep(1)
                    count=int(input("[?] How many locations do you want to add ? "))
                for i in range(count):
                    loc=str(input(f"[::] Please enter location No{i+1}: "))
                    while loc == None:
                        print("[!] This field can't be blank !")
                        sleep(1)
                        loc=str(input(f"[::] Please enter again location No{i+1}: "))
                    LOCATIONS.append(loc)
                    sleep(1)
                    print("[✓] Location added !")
            AddLinks=str(input("[?] Do you want to include urls ? [yes/no] "))
            while AddLinks not in ANS or AddLinks == None:
                if AddLinks == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                AddLinks=str(input("[?] Do you want to include urls ? [yes/no] "))
            if AddLinks in ANS[:9]:
                count=int(input("[?] How many ? "))
                while checkCount(count):
                    checkOpt(count, "other")
                    sleep(1)
                    count=int(input("[?] How many urls do you want to include ? "))
                for i in range(count):
                    link=str(input(f"[::] Please enter the url No{i+1}: "))
                    while link == None or "/" not in link or "https" not in link:
                        print("[!] This field can't be blank !")
                        sleep(1)
                        link=str(input(f"[::] Please enter again the url No{i+1}: "))
                    LINKS.append(link)
                    sleep(1)
                    print("[✓] URL added !")
            AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
            while AddHash not in ANS or AddHash == None:
                if AddHash == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
            if AddHash in ANS[:9]:
                count=int(input("[?] How many ? "))
                while checkCount(count):
                    checkOpt(count, "count")
                    sleep(1)
                    count=int(input("[?] How many hashtags do you want to include ? "))
                for i in range(count):
                    hashtag=str(input(f"[::] Please enter the hashtag No{i+1}: "))
                    while hashtag == None or "#" not in hashtag:
                        print("[!] This field can't be blank !")
                        sleep(1)
                        hashtag=str(input(f"[::] Please enter again the hashtag No{i+1}: "))
                    HASHTAGS.append(hashtag)
                    sleep(1)
                    print("[✓] Hashtag added !")
            if AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,links=LINKS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for the time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,locations=LOCATIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for the time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,links=LINKS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=AddLinks)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,locations=LOCATIONS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                        sleep(2)
                        print("[!] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,locations=LOCATIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,links=LINKS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,locations=LOCATIONS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,links=LINKS,hashtags=HASHTAGS)
                        sleep(2)
                        print("[✓] Story uploaded !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()

        elif action == 4:
            hashtag = None
            location = None
            path=str(input("[::] Please enter the path to the video: "))
            while checkPath(path):
                checkOpt(path, "path")
                sleep(1)
                path=str(input("[::] Please enter again the path to the video: "))
            incap=str(input("[?] Do you want to include caption ? [yes/no] "))
            while incap not in ANS or incap == None:
                if incap == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                incap=str(input("[?] Do you want to include caption ? [yes/no] "))
            if incap in ANS[:9]:
                sleep(1)
                print("[+] Default: \"Check out my new video !\"")
                sleep(2)
                print("[*] Hit <Tab> and <Enter> to apply the default caption")
                sleep(2)
                caption=str(input("[::] Please enter the caption: "))
                if caption == "\t":
                    caption = "Check out my new video !"
            intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
            while intag not in ANS or intag == None:
                if intag == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
            if intag in ANS[:9]:
                count=int(input("[?] How many ? "))
                while checkCount(count):
                    checkOpt(count, "count")
                    sleep(1)
                    count=int(input("[?] How many hashtags to include ? "))
                for i in range(count):
                    hashtag=str(input(f"[::] Please enter the hashtag No{i+1} : "))
                    while checkTag(hashtag):
                        if hashtag == None:
                            print("[!] This field can't be blank !")
                        else:
                            print("[!] Invalid hashtag !")
                        sleep(2)
                        print("[+] You must include the: \"#\" symbol !")
                        sleep(2)
                        hashtag=str(input(f"[::] Please enter again hashtag No{i+1}: "))
                    HASHVID.append(hashtag)
                    sleep(1)
                    print("[✓] Hashtag added !")
            inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
            while inloc not in ANS or inloc == None:
                print("[!] This field can't be blank !")
                sleep(1)
                inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
            if inloc in ANS[:9]:
                count=int(input("[?] How many ? "))
                while checkCount(count):
                    checkOpt(count, "other")
                    sleep(1)
                    count=int(input("[?] How many locations to include ? "))
                for i in range(count):
                    location=str(input(f"[::] Please enter location No{i+1} : "))
                    while location == None:
                        print("[!] This field can't be blank !")
                        sleep(1)
                        location=str(input(f"[::] Please enter again location No{i+1}: "))
            if current_time == __time__:
                try:
                    client.video_upload(path,caption,usertags=HASHVID,location=location)
                    sleep(2)
                    print("[✓] Video uploaded !")
                    Class()
                except Exception as ex:
                    Except(ex)
            else:
                print(f"[+] Current time: {current_time}")
                sleep(1)
                print(f"[+] Waiting for time: {__time__}")
                Class()

        elif action == 5:
            count=int(input("[?] How many accounts do you want to follow ? "))
            while checkCount(count):
                checkOpt(count, "count")
                sleep(1)
                count=int(input("[?] How many accounts do you want to follow ? "))
            if count == 1:
                username=str(input("[::] Please enter the username: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
                while valUser(username):
                    if type(CheckVal()) == bool:
                        CheckVal()
                    else:
                        username = CheckVal()
                username = username.lower().strip()
                print(GetID(username))
                uid=int(input("[::] Please enter the user's ID as shown above: "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input("[::] Please enter again the user's ID as shown above: "))
                if current_time == __time__:
                    try:
                        client.user_follow(uid)
                        sleep(2)
                        print(f"[✓] Followed {username} !")
                        Class()
                    except Exception as ex:
                        Exception(ex)
                else:
                    print(f"[+] Current time: {current_time}")
                    sleep(1)
                    print(f"[+] Waiting for time: {__time__}")
                    Class()
            else:
                for i in range(count):
                    username=str(input(f"[::] Please enter the username No{i+1}: "))
                    while checkUser(username):
                        checkOpt(username, "username")
                        sleep(1)
                        username=str(input(f"[::] Please enter again username No{i+1}: "))
                    while valUser(username):
                        if type(CheckVal()) == bool:
                            CheckVal()
                        else:
                            username = CheckVal()
                    username = username.lower().strip()
                    print(GetID(username))
                    id=int(input("[::] Please enter the user's ID as shown above: "))
                    while checkID(id):
                        checkOpt(id, "id")
                        sleep(1)
                        uid=int(input("[::] Please enter again the user's ID as shown above: "))
                    if current_time == __time__:
                        try:
                            client.user_follow(id)
                            sleep(2)
                            print(f"[✓] Followed {username} !")
                            Class()
                        except Exception as ex:
                            Exception(ex)
                    else:
                        print(f"[+] Current time: {current_time}")
                        sleep(1)
                        print(f"[+] Waiting for time: {__time__}")
                        Class()
     
        elif action == 6:
            if current_time == __time__:
                count=int(input("[?] How many accounts do you want to unfollow ? "))
                while checkCount(count):
                    checkOpt(count, "other")
                    sleep(1)
                    count=int(input("[?] How many accounts do you want to unfollow ? "))
                if count == 1: 
                    username=str(input("[::] Please enter the username: "))
                    while checkUser(username):
                        checkOpt(username, "username")
                        sleep(1)
                        username=str(input("[::] Please enter again the username: "))
                    while valUser(username):
                        if type(CheckVal()) == bool:
                            CheckVal()
                        else:
                            username = CheckVal()
                    username = username.lower().strip()
                    print(GetID(username))
                    uid=int(input("[::] Please enter the user's ID as shown above: "))
                    while checkID(uid):
                        checkOpt(uid, "id")
                        sleep(1)
                        uid=int(input("[::] Please enter again the user's ID as shown above: "))
                    try:
                        client.user_unfollow(uid)
                        sleep(2)
                        print(f"[✓] Unfollowed {username} !")
                        Class()
                    except Exception as ex:
                        Except(ex)
                else:
                    for i in range(count):
                        username=str(input(f"[::] Please enter the username No{i+1}: "))
                        while checkUser(username):
                            checkOpt(usernmame, "username")
                            sleep(1)
                            username=str(input("[::] Please enter again the username: "))
                        while valUser(username):
                            if type(CheckVal()) == bool:
                                CheckVal()
                            else:
                                username = CheckVal()
                        username = username.lower().strip()
                        try:
                            client.user_unfollow(uid)
                            sleep(2)
                            print(f"[✓] Unfollowed {username} !")
                        except Exception as e:
                            Except(ex)
                    Class()
            else:
                print(f"[+] Current time: {current_time}")
                sleep(1)
                print(f"[+] Waiting for time: {__time__}")
                sleep(1)
                Class()

    elif option == 56:
        clear()
        user=str(input("[::] Please enter the username: "))
        while checkUser(user):
            checkOpt(user, "username")
            sleep(1)
            user=str(input("[::] Please enter again the username: "))
        while valUser(user):
            if type(CheckVal()) == bool:
                CheckVal()
            else:
                user = CheckVal()
        user = user.lower().strip()
        print(GetID(user))
        id=int(input("[::] Please enter the user's ID as shown above: "))
        while checkID(id):
            checkOpt(id, "id")
            sleep(1)
            id=int(input("[::] Please enter again the user's ID as shown above: "))
        try:
            api.block_friend_reel(id)
            sleep(2)
            print(f"[✓] User: {user} blocked from watching your stories")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 57:
        clear()
        print(Uninstall())
        sleep(2)
        print("[+] Thank you for choosing to use my script 😀😁")
        sleep(2)
        print("[+] Hope you enjoyed it 🤗")
        sleep(1)
        print("[+] If you have any suggestions or found a bug or need help feel free to contact me anytime, at this email address: new92github@gmail.com")
        sleep(3)
        print("[+] Until we meet again 🫡")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
