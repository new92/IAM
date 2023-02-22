"""
Author: new92
Github: @new92
[-->] Script for Managing your Instagram Account Remotely
IAM: Instagram Account Manager


******************************|IMPORTANT|*******************************
* User's data (such as username password) will not be stored or saved !*
* Will be used only for some functions of the program.                 *
************************************************************************
"""



try:
    import sys
    import platform
    from os import system
    from time import sleep
    import instagrapi
    import instaloader
    import instabot
    import requests as re
    import os
    from tkinter import *
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
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
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip3 install -r requirements.txt")

loader=instaloader.Instaloader()
client=instagrapi.Client()
bot=instabot.Bot()

def banner() -> str:
    """
    Returns the script's banner
    """
    return """
██╗░█████╗░███╗░░░███╗
██║██╔══██╗████╗░████║
██║███████║██╔████╔██║
██║██╔══██║██║╚██╔╝██║
██║██║░░██║██║░╚═╝░██║
╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
"""

def Except(ex:str):
    """
    Used for exceptions
    """
    print("[!] Error !")
    sleep(1)
    print(f"[=] Error message -> {ex}")
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
            print("[+] Acceptable numbers: [1/2]")
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

def cls():
    """
    Clears the terminal
    """
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")

def Get_Hpk(url:str) -> str:
    return client.highlight_pk_from_url(url)

def Get_Spk(url:str) -> str:
    return client.story_pk_from_url(url)

def valUser(user):
    """
    Checks the validation of the username using the requests module
    """
    return re.get(f"https://www.instagram.com/{user}/").status_code == 404 or re.get(f"https://www.instagram.com/{user}/").status_code == 400

def checkOpt(opt,data):
    """
    data must be a string or an integer
    """
    if data == "username":
        if opt == None:
            print("[!] This field can't be empty !")
        elif type(opt) != str:
            print("[!] Username must be a string !")
        else:
            print("[!] Invalid length !")
            sleep(1)
            print("[+] Acceptable length: less than or equal to 30 characters")
    elif data == "id":
        if opt == None:
            print("[!] This field can't be empty !")
        elif type(opt) != int:
            print("[!] ID must be an integer !")
        else:
            print("[!] Invalid length !")
            sleep(1)
            print("[+] Acceptable length: greater than 3")
    elif data == "path":
        if opt == None:
            print("[!] This field can't be empty !")
        elif type(opt) != str:
            print("[!] Path must be a string !")
        else:
            print("[!] Path must contain: / or \ ")
    else:
        if opt == None:
            print("[!] This field can't be empty !")
        elif type(opt) != int:
            print("[!] This input must be an integer !")
        else:
            print("[!] Invalid number !")

def valOpt(opt:int,x:int,y:int):
    """
    Checks the validation of the number of an option
    """
    return opt < x or opt > y or opt == None or type(opt) != int
    
def Class():
    if Next() == 1:
        main()
    else:
        Exiting()

def Exiting():
    """
    Exits the script
    """
    print("[+] Exiting...")
    sleep(1)
    print("[+] See you next time 👋")
    sleep(1)
    quit(0)
    
def Next() -> int:
    print("[1] Return to menu")
    print("[2] Exit")
    opt=int(input("[::] Please enter a number (from the above ones): "))
    while valOpt(opt,1,2):
        if opt == None:
            print("[!] This field can't be blank !")
        elif type(opt) != int:
            print("[!] You must enter an integer !")
        else:
            print("[!] Invalid number !")
            sleep(1)
            print("[+] Acceptable numbers: [1/2]")
        sleep(1)
        opt=int(input("[::] Please enter a number (from the above ones): "))
    return opt
    
def checkCount(num:int) -> bool:
    """
    Returns true if num is invalid
    """
    return num == None or num < 1 or type(num) != int
    
def checkPath(path):
    return path == None or "/" not in path or "\\" not in path

def Av_Acts() -> str:
    """
    Returns the available options
    """
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

def ProgInfo():
    ___version__ = "1.2"
    __author__ = "new92"
    __license__ = "MIT"
    ___name__ = "IAM"
    __lines__ = 4365
    __programmedwith__ = "Python"
    __language__ = "en-US"
    stars = 8
    forks = stars // 2
    print("[+] Author ==> "+str(__author__))
    print("[+] Github ==> @"+str(__author__))
    print("[+] License ==> "+str(__license__))
    print("[+] Script's name ==> "+str(___name__))
    print("[+] Version ==> "+str(___version__))
    print("[+] Programmed with ==> "+str(__programmedwith__))
    print("[+] Natural language ==> "+str(__language__))
    print("[+] Number of lines ==> "+str(__lines__))
    print("[+] Number of stars on the github repo ==> "+str(stars))
    print("[+] Number of forks on the github repo ==> "+str(forks))

def checkUser(username:str) -> bool:
    """
    Checks the username's validation
    """
    return username == None or len(username) > 30

def GetID(username:str) -> int:
    """
    Returns the Instagram ID of the username
    """
    return loader.check_profile_id(username)

def checkID(id:int) -> bool:
    """
    Checks the validation of the ID
    """
    return id == None or len(id) < 3 or type(id) != int


ANS = ["yes","YES","Yes","y","Y","YeS","yEs","YEs","yES","no","NO","No","n","N","nO"]

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
    print("\n")
    print("[+] IAM: Instagram Account Manager")
    print("\n")
    print("[+] Program for Managing your Instagram Account Remotely")
    print("\n")
    print("[+] Github: @new92")
    print("\n")
    print("[1] Display your profile ID")
    print("[2] Display your security information")
    print("[3] Display your account info")
    print("[4] Display your pending follow requests")
    print("[5] Display your followers")
    print("[6] Display the users you follow")
    print("\n")
    print("[7] Download your highlights")
    print("[8] Download anonymously stories of other users")
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
    print("[999] Show program info and exit")
    print("\n")
    print("[0] Exit") 
    print("\n")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while valOpt(opt,1,56) and opt != 999:
        if option == None:
            print("[!] This field can't be blank !")
        elif type(option) != int:
            print("[!] You must enter an integer in the current input !")
        else:
            print("[+] Invalid number !")
            sleep(1)
            print("[+] Acceptable numbers: [1 to 56 /999/0]")
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
        print("[999] Show program info and exit")
        print("\n")
        print("[0] Exit")
        option=int(input("[::] Please enter again a number (from the above ones): "))
    if option != 0:
        cls()
        print("\n")
        print("|--------------------|LOGIN|--------------------|")
        print("\n")
        username=str(input("[::] Please enter your username: "))
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        while valUser(username):
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            opt=int(input("[::] Please enter a number (from the above ones): "))
            while valOpt(opt,1,3):
                checkOpt(opt, "other")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                opt=int(input("[::] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input("[::] Please enter the username: "))
                while checkUser(username):
                    checkOpt(opt,"username")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            elif opt == 2:
                main()
            else:
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        if not username.islower():
            username = username.lower()
        username = username.strip()
        password=str(input("[::] Please enter your password: "))
        while password == None or type(password) !=str:
            if password == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Password must be a string !")
            sleep(1)
            password=input("[::] Please enter again your password: ")
        password = password.strip()
        try:
            loginl = loader.login(username,password)
            loginc = client.login(username,password,True)
            logini = instapy.InstaPy(username,password)
            api = instagram_private_api.Client(username,password)
        except Exception as ex:
            Except()

    elif option == 999:
        cls()
        ProgInfo()
    
    if option == 0:
        cls()
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

    elif option == 1:
        cls()
        try:
            print("[+] Your ID: "+str(GetID(username)))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 2:
        cls()
        try:
            sec=client.account_security_info()
            print("[+] Is phone confirmed ? "+str(sec["is_phone_confirmed"]))
            print("[+] Is 2 factor authentication enabled ? "+str(sec["is_two_factor_enabled"]))
            print("[+] Is Time-based One-Time Passwords (TOTP) 2 factor authentication enabled ? "+str(sec["is_totp_two_factor_enabled"]))
            print("[+] Is trusted notifications enabled ? "+str(sec["is_trusted_notifications_enabled"]))
            print("[+] Is eligible for Whatsapp 2 factor authentication ? "+str(sec["is_eligible_for_whatsapp_two_factor"]))
            print("[+] Is Whatsapp 2 factor authentication enabled ? "+str(sec["is_whatsapp_two_factor_enabled"]))
            print("[+] Backup codes: "+str(sec["backup_codes"]))
            print("[+] Trusted devices: "+str(sec["trusted_devices"]))
            print("[+] Has reachable email ? "+str(sec["has_reachable_email"]))
            print("[+] Is eligible for trusted notifications ? "+str(sec["eligible_for_trusted_notifications"]))
            print("[+] Is eligible for multiple TOTP ? "+str(sec["is_eligible_for_multiple_totp"]))
            print("[+] TOTP seeds: "+str(sec["totp_seeds"]))
            print("[+] Can add additional TOTP seed ? "+str(sec["can_add_additional_totp_seed"]))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 3:
        cls()
        try:
            print("[+] Your account information: "+str(client.account_info()))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 4:
        cls()
        try:
            print(api.friendships_pending())
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 5:
        cls()
        print(GetID(username))
        id=int(input("[::] Please enter your id as shown above: "))
        while checkID(id):
            checkOpt(id,"id")
            sleep(1)
            id=int(input("[::] Please enter again your ID as shown above: "))
        try:
            print(client.user_followers(id))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 6:
        cls()
        print(GetID(username))
        id=int(input("[::] Please enter your id (as shown above): "))
        while checkID(id):
            checkOpt(id,"id")
            sleep(1)
            id1=input("[::] Please enter again your id (as shown above): ")
        try:
            print(client.user_following(id))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 7:
        cls()
        print(GetID(username))
        id=int(input("[::] Please enter your id as shown above: "))
        while checkID(id):
            checkOpt(id,"id")
            sleep(1)
            id=int(input("[::] Please enter again your id as shown above: "))
        try:
            highlights=loader.download_highlights(id)
            sleep(1)
            print("[+] Highlights folder path: "+str(os.path.abspath(username)))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 8:
        cls()
        count=int(input("[+] Number of accounts (to get their stories): "))
        while valOpt(count,1,999):
            checkOpt(count,"other")
            sleep(1)
            count=int(input("[::] Please enter again the number of accounts (to get their stories): "))
        for i in range(count):
            username=str(input("[::] Please enter the username: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            while valUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
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
            print("[+] Path to folder containing the stories: "+os.path.abspath(":stories"))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 9:
        cls()
        count=int(input("[?] How many of your saved posts do you want to download ? (enter a number) "))
        while checkCount(count):
            checkOpt(count,"other")
            sleep(1)
            count=int(input("[?] How many of your saved posts do you want to download ? (enter a number) "))
        try:
            loader.download_saved_posts(count)
            print("[+] Path to folder containing saved posts: "+os.path.abspath(":saved"))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 10:
        cls()
        count=int(input("[?] How many posts do you want to download ? (enter a number) "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[?] How many posts do you want to download ? "))
        try:
            loader.download_feed_posts(count)
            print("[+] Path to folder containing feed posts: "+os.path.abspath(":feed"))
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 11:
        cls()
        count=int(input("[::] Please enter the number of posts to post: "))
        while checkCount(count):
            checkOpt(count, "other")
            sleep(1)
            count=int(input("[::] Please enter again the number of posts to post: "))
        for i in range(count):
            path=str(input("[::] Please enter the path to the photo to be uploaded: "))
            while checkPath(path):
                checkOpt(path,"path")
                sleep(1)
                path=str(input("[::] Please enter again the path to the photo to be uploaded: "))
            sleep(2)
            print(">>>CAPTION<<<")
            sleep(1)
            print("[+] Default: Check out my new post !")
            sleep(2)
            print("[*] Hit <Tab> and <Enter> for the default option to be applied")
            sleep(2)
            caption=str(input("[::] Please enter the caption: "))
            if caption == "\t":
                caption = "Check out my new post !"
            print(">>>TAGS<<<")
            sleep(2)
            print("[+] Default: [no]")
            sleep(2)
            print("[*] Hit <Tab> and <Enter> to apply the default option")
            sleep(2)
            tags=str(input("[?] Do you want to include other users to your post by tagging them ? [yes/no] "))
            while tags not in ANS or tags == None:
                if tags == None:
                    print("[!] This field can't be empty !")
                else:
                    print("[!] Invalid input !")
                    sleep(1)
                    print("[+] Acceptable input: [yes/no]")
                sleep(1)
                tags=str(input("[?] Do you want to include other users to your post by tagging them ? [yes/no] "))
            if tags in ANS[:9]:
                print("[+] Default: 1")
                sleep(2)
                print("[+] Hit <Tab> and <Enter> to apply the default option")
                sleep(1)
                count=input("[?] How many users do you want to include ? ")
                if count == "\t":
                    username=str(input("[::] Please enter the username: "))
                    while checkUser(username):
                        checkOpt(username, "username")
                        sleep(1)
                        username=str(input("[::] Please enter again the username: "))
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
                            checkOpt(utag,"username")
                            sleep(1)
                            utag=str(input(f"[::] Please enter again the username No{i+1}: "))
                        utag = utag.strip()
                        utag = utag.lower()
                        TaggedUsers.append(utag)
            print(">>>LOCATION<<<")
            sleep(2)
            print("[+] Default: [no]")
            sleep(1)
            print("[+] Hit <Tab> and <Enter> to Apply the Default Option")
            sleep(2)
            loc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
            while loc not in ANS or loc == None or type(loc) != str:
                print("[!] Invalid location !")
                sleep(1)
                loc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
            if loc in ANS[:9]:
                count=int(input("[?] How many ? (enter a number) "))
                while checkCount(count):
                    checkOpt(count,"other")
                    sleep(1)
                    count=int(input("[?] How many locations do you want to include ? (enter a number) "))
                for i in range(count):
                    location=str(input(f"[::] Please enter location No{i+1}: "))
                    while location == None or type(location) != str:
                        print("[!] Invalid location !")
                        sleep(1)
                        location=str(input(f"[::] Please enter again location No{i+1}: "))
                    LOCATIONS.append(location)
                    print("[!] Location added successfully !")
                try:
                    client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                    sleep(2)
                    print("[!] Photo uploaded successfully !")
                    Class()
                except Exception as ex:
                    Except(ex)

            if tags in ANS[:9] and loc in ANS[:9]:
                try:
                    client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                    print("[!] Photo uploaded successfully !")
                    
                except Exception as ex:
                    Except(ex)

            elif tags in ANS[:9] and loc in ANS[9:]:
                try:
                    client.photo_upload(path=path,caption=caption,tags=TaggedUsers)
                    print("[!] Photo uploaded successfully !")
                    Class()
                except Exception as ex:
                    Except(ex)
            elif tags in ANS[9:] and loc in ANS[:9]:
                try:
                    client.photo_upload(path=path,caption=caption,location=LOCATIONS)
                    print("[!] Photo uploaded successfully !")
                    Class()
                except Exception as ex:
                    Except(ex)
            elif tags in ANS[9:] and loc in ANS[:9]:
                try:
                    client.photo_upload(path=path,caption=caption)
                    print("[!] Photo uploaded successfully !")
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 12:
        cls()
        username=str(input("[::] Please enter your username: "))
        while checkUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        while valUser(username):
            checkOpt(username, "username")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        username=username.lower()
        username=username.strip()
        EN = ["enable","ENABLE","disable","DISABLE"]
        endis=str(input("[?] Do you want to enable or disable your notifications ? [enable/disable] "))
        while endis not in EN or endis == None:
            print("[!] Invalid input !")
            sleep(1)
            endis=input("[?] Do you want to enable or disable your notifications ? [enable/disable] ")
        if endis in EN[:2]:
            username=str(input("[::] Please enter your username: "))
            while checkUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again your username: "))
            while valUser(username):
                checkOpt(username, "username")
                sleep(1)
                username=str(input("[::] Please enter again your username: "))
            username=username.lower()
            username=username.strip()
            print("[+] Notifications available for: [posts/reels/stories/videos]")
            sleep(2)
            action=str(input("[?] Which notifications do you want to enable ?"))
            while action not in ["posts","POSTS","reels","REELS","stories","STORIES","videos","VIDEOS"] or action == None:
                if action == None:
                    print("[!] This field can't be blank !")
                else:
                    print("[!] Invalid input !")
                sleep(1)
                print("[+] Acceptable answers: [posts/reels/stories/videos]")
                sleep(1)
                action=input("[?] Please enter again the notifications to enable: ")
            if action == "posts" or action == "POSTS":
                username=str(input("[::] Please enter your username: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                while valUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                print(GetID(username))
                uid=int(input("[::] Please enter the ID as shown above: "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input("[::] Please enter again the ID as shown above: "))
                try:
                    enabled = client.enable_posts_notifications(uid)
                    print("[+] Post notifications enabled: "+str(enabled))
                    Class()
                except Exception as ex:
                    Except(ex)
            elif action == "reels" or action == "REELS":
                username=str(input("[::] Please enter your username: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                while valUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                print(GetID(username))
                uid=int(input("[::] Please enter your ID as shown above: "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input("[::] Please enter again your ID as shown above: "))
                try:
                    enabled = client.enable_reels_notifications(uid)
                    print("[+] Reels notifications enabled: "+str(enabled))
                    Class()
                except Exception as ex:
                    Except(ex)
            elif action == "stories" or action == "STORIES":
                username=str(input("[::] Please enter your username: "))
                while checkUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                while valUser(username):
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                print(GetID(username))
                uid=int(input("[::] Please enter the ID as shown above: "))
                while checkID(uid):
                        print("[!] Invalid ID !")
                        sleep(1)
                        uid=int(input("[::] Please enter again the ID as shown above: "))
                try:
                    enabled = client.enable_stories_notifications(uid)
                    print("[+] Stories notifications enabled: "+str(enabled))
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
                    checkOpt(username, "username")
                    sleep(1)
                    username=str(input("[::] Please enter again your username: "))
                print(GetID(username))
                uid=int(input("[::] Please enter your ID as shown above: "))
                while checkID(uid):
                    checkOpt(uid, "id")
                    sleep(1)
                    uid=int(input("[::] Please enter again your ID as shown above: "))
                try:
                    enabled = client.enable_videos_notifications(uid)
                    print("[+] Video notifications enabled: "+str(enabled))
                    Class()
                except Exception as ex:
                    Except(ex)

    elif option == 13:
        cls()
        path=str(input("[::] Please enter the path of the photo for your new profile picture: "))
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=str(input("[::] Please enter again the path of the photo for your new profile picture: "))
        try:
            client.account_change_picture(path)
            print("[!] Your profile picture changed successfully !")
            Class()
        except Exception as ex:
            Except(ex)

    elif option == 14:
        cls()
        path=str(input("[::] Please enter the path to the photo to be uploaded: "))
        while checkPath(path):
            checkOpt(path, "path")
            sleep(1)
            path=str(input("[::] Please enter again the path to the photo to be uploaded: "))
        AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
        while AddCaption not in ANS or AddCaption == None:
            if AddCaption == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
        if AddCaption in ANS[:9]:
            print("[+] Default: Check out my new story !")
            sleep(1)
            print("[+] Hit <Tab> and <Enter> for the default option to be applied")
            sleep(2)
            caption=str(input("[::] Please enter the caption: "))
            if caption == "\t":
                caption = "Check out my new story !"
            else:
                caption=str(input("[::] Please enter a caption to include to your story: "))
                while caption == None or type(caption) != str:
                    print("[!] Invalid caption !")
                    sleep(1)
                    caption=str(input("[::] Please enter again a caption to include to your story: "))
        AddMention=str(input("[?] Do you want to add mention ? [yes/no] "))
        while AddMention not in ANS or AddMention == None:
            if AddMention == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            mention=str(input("[?] Do you want to mention other user(s) ? [yes/no] "))
        if AddMention in ANS[:9]:
            MENTIONS = []
            count=int(input("[?] How many ? (enter a number) "))
            while checkCount(count):
                checkOpt(count,"other")
                sleep(1)
                count=int(input("[?] How many ? (enter a number) "))
            for i in range(count):
                mention=str(input(f"[::] Please enter the username No{i+1}: "))
                while checkUser(mention):
                    checkOpt(mention, "username")
                    sleep(1)
                    mention=str(input(f"[::] Please enter again the username No{i+1}: "))
                while valUser(mention):
                    checkOpt(mention, "username")
                    sleep(1)
                    mention=str(input(f"[::] Please enter again the username No{i+1}: "))
                MENTIONS.append(mention)
        AddLoc=str(input("[?] Do you want to add location ? [yes/no] "))
        while AddLoc not in ANS or AddLoc == None:
            if AddLoc == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            AddLoc=str(input("[?] Do you want to add location ? [yes/no] "))
        if AddLoc in ANS[:9]:
            count=int(input("[?] How many locations do you want to add ? (enter a number) "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input("[?] How many locations do you want to add ? (enter a number) "))
            for i in range(count):
                loc=str(input(f"[::] Please enter location No{i+1}: "))
                while loc == None or type(loc) != str:
                    if loc == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Location must be a string !")
                    sleep(1)
                    loc=str(input(f"[::] Please enter again location No{i+1}: "))
                LOCATIONS.append(loc)
        AddLinks=str(input("[?] Do you want to include urls ? [yes/no] "))
        while AddLinks not in ANS or AddLinks == None:
            if AddLinks == None:
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
            sleep(1)
            AddLinks=str(input("[?] Do you want to include urls ? [yes/no] "))
        if AddLinks in ANS[:9]:
            count=int(input("[?] How many ? (enter a number) "))
            while checkCount(count):
                checkOpt(count, "other")
                sleep(1)
                count=int(input("[?] How many urls do you want to include ? (enter a number) "))
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
            count=int(input("[?] How many ? (enter a number) "))
            while checkCount(count):
                checkOpt(count,"other")
                sleep(1)
                count=int(input("[?] How many hashtags do you want to include ? "))
            for i in range(count):
                hashtag=str(input(f"[::] Please enter the hashtag No{i+1}: "))
                while hashtag == None or "#" not in hashtag or type(hashtag) != str:
                    if hashtag == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid hashtag !")
                    sleep(1)
                    hashtag=str(input(f"[::] Please enter again the hashtag No{i+1}: "))
                HASHTAGS.append(hashtag)
        if AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                print("[!] Story uploaded successfully !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path)
                print("[!] Story uploaded successfully !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                print("[!] Story uploaded successfully !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                print("[!] Story uploaded successfully !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,links=LINKS,hashtags=HASHTAGS)
                print("[!] Story uploaded successfully !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,hashtags=HASHTAGS)
                print("[!] Story uploaded successfully !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                print("[!] Story uploaded successfully !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                print("[!] Story uploaded successfully !")
                Class()
            except Exception as ex:
                Except(ex)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,links=LINKS,hashtags=HASHTAGS)
                print("[!] Story uploaded successfully !")
                Class()
            except Exception as ex:
                Except(ex)
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$]
        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,hashtags=HASHTAGS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,locations=LOCATIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,links=LINKS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,hashtags=HASHTAGS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=AddLinks)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,locations=LOCATIONS,hashtags=HASHTAGS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,locations=LOCATIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,caption,links=LINKS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,mentions=MENTIONS,hashtags=HASHTAGS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash == None:
            try:
                client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
            try:
                client.photo_upload_to_story(path,locations=LOCATIONS,hashtags=HASHTAGS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
            try:
                client.photo_upload_to_story(path,links=LINKS,hashtags=HASHTAGS)
                sleep(5)
                print("[!] Story uploaded successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 15:
        caption = None
        hashtag = None
        location = None
        path=str(input("[::] Please enter the path to the video: "))
        while path == None or "/" not in path or "\\" not in path:
            print("[!] Invalid path !")
            sleep(1)
            path=str(input("[::] Please enter again the to the video: "))
        incap=str(input("[?] Do you want to include caption ? [yes/no] "))
        while incap not in ANS and incap not in NANS or incap == None:
            print("[!] Invalid input !")
            sleep(1)
            incap=str(input("[?] Do you want to include caption ? [yes/no] "))
        if incap in ANS:
            sleep(1)
            print("[+] Default: Check out my new video !")
            sleep(2)
            print("[+] Hit <Tab> and <Enter> to apply the default option")
            sleep(2)
            caption=str(input("[::] Please enter the caption: "))
            if caption == "\t":
                caption = "Check out my new video !"
        intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
        while intag not in ANS and intag not in NANS or intag == None:
            print("[!] Invalid input !")
            sleep(1)
            intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
        if intag in ANS:
            count=int(input("[?] How many ? (enter a number) "))
            while count <= 0 or count == None:
                print("[!] Invalid number !")
                sleep(1)
                count=int(input("[?] How many hashtags to include ? (enter a number) "))
            for i in range(count):
                hashtag=str(input(f"[::] Please enter the hashtag No{i+1}: "))
                while hashtag == None or "#" not in hashtag:
                    print("[!] Invalid hashtag !")
                    sleep(2)
                    print("[+] Please include the    #    sign")
                    sleep(2)
                    hashtag=str(input(f"[::] Please enter again hashtag No{i+1}: "))
                HASHVID.append(hashtag)
                sleep(1)
                print("[!] Hashtag added successfully !")
        else:
            print("[OK]")
            sleep(1)
            pass
        inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
        while inloc not in ANS and inloc not in NANS or inloc == None:
            print("[!] Invalid location !")
            sleep(1)
            inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
        if inloc in ANS:
            count=int(input("[?] How many ? (enter a number) "))
            while count <= 0 or count == None:
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[?] How many locations to include ? (enter a number) "))
            for i in range(count):
                location=str(input(f"[::] Please enter location No{i+1} : "))
                while location == None:
                    print("[!] Invalid location !")
                    sleep(1)
                    location=str(input(f"[::] Please enter again location No{i+1} : "))
        else:
            print("[OK]")
            pass
        try:
            client.video_upload(path,caption,usertags=HASHVID,location=location)
            sleep(5)
            print("[!] Video uploaded successfully !")
            quit(0)
        except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 16:
        count=int(input("[?] How many accounts do you want to follow ? (enter a number) "))
        while count <= 0 or count == None:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[?] How many accounts do you want to follow ? (enter a number) "))
        if count == 1:
            username=str(input("[::] Please enter the username: "))
            while checkUser(username) == True:
                print("[!] Invalid username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            username.lower()
            username.strip()
            print(GetID(username))
            uid=int(input("[::] Please enter the user's ID as shown above: "))
            while checkID(uid):
                print("[!] Invalid ID !")
                sleep(1)
                uid=int(input("[::] Please enter again the user's ID as shown above: "))
            try:
                client.user_follow(uid)
                sleep(3)
                print(f"[!] Successfully followed {username} !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            for i in range(count):
                username=str(input(f"[::] Please enter the username No{i+1} :"))
                while checkUser(username) == True:
                    print("[!] Invalid username !")
                    sleep(1)
                    username=str(input(f"[::] Please enter again username No{i+1} : "))
                username.lower()
                username.strip()
                print(GetID(username))
                id=int(input("[::] Please enter the user's ID as shown above: "))
                while checkID(id):
                    print("[!] Invalid ID !")
                    sleep(1)
                    uid=int(input("[::] Please enter again the user's ID as shown above: "))
                try:
                    client.user_follow(id)
                    sleep(3)
                    print(f"[!] Successfully followed {username} !")
                except Exception as ex:
                    print(f"[!] Unable to follow {username} !")
                    sleep(2)
                    print("[+] Error: "+str(ex))

    elif option == 17:
        count=int(input("[?] How many accounts do you want to unfollow ? (enter a number) "))
        while count <= 0 or count == None:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[?] How many accounts do you want to unfollow ? (enter a number) "))
        if count == 1: 
            username=str(input("[::] Please enter the username: "))
            while checkUser(username) == True:
                print("[!] Invalid username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            username.lower()
            username.strip()
            print(GetID(username))
            uid=int(input("[::] Please enter the user's ID as shown above: "))
            while checkID(uid):
                print("[!] Invalid ID !")
                sleep(1)
                uid=int(input("[::] Please enter again the user's ID as shown above: "))
            try:
                client.user_unfollow(uid)
                sleep(3)
                print(f"[!] Successfully unfollowed {username} !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            for i in range(count):
                username=str(input(f"[::] Please enter username No{i+1}: "))
                while checkUser(username) == True:
                    print("[!] Invalid username !")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
                username.lower()
                username.strip()
                try:
                    client.user_unfollow(uid)
                    sleep(3)
                    print(f"[!] Successfully unfollowed {username} !")
                except Exception as e:
                    print(f"[!] Can't unfollow {username} !")
                    pass

    elif option == 18:
        count=int(input("[::] Please enter the number of the follow requests to accept: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of the follow requests to accept: "))
        try:
            logini.accept_follow_requests(count,3)
            print("[!] Follow requests accepted !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 19:
        count=int(input("[::] Please enter the number of the follow requests to remove: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of the follow requests to remove: "))
        try:
            logini.remove_follow_requests(count,3)
            print("[!] Follow requests removed !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 20:
        count=int(input("[::] Please enter the number of users to follow:  "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(2)
            count=int(input("[::] Please enter again the number of users to follow: "))
        countu=int(input("[?] From how many users do you want to follow their followers ? (enter a number) "))
        while countu <= 0 or countu == None:
            print("[!] Invalid number !")
            sleep(1)
            countu=int(input("[?] From how many users do you want to follow their followers ? "))
        for i in range(countu):
            username=str(input("[::] Please enter the username of the user (to follow their followers): "))
            while checkUser(username) == True:
                print("[!] Invalid username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            FUFERS.append(username)
        try:
            logini.follow_user_followers(FUFERS,count)
            print("[!] Successfully followed users !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 21:
        count=int(input("[::] Please enter the number of users to follow: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(2)
            count=int(input("[::] Please enter again the number of users to follow: "))
        countu=int(input("[?] From how many users do you want to follow their followings ? (enter a number) "))
        while countu == None or countu <= 0:
            print("[!] Invalid number !")
            sleep(1)
            countu=int(input("[?] From how many users do you want to follow their followings ? (enter a number) "))
        for i in range(countu):
            username=str(input("[::] Please enter the username: "))
            while checkUser(username) == True:
                print("[!] Invalid username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            FUFING.append(username)
        browser = webdriver.Firefox()
        for i in range(len(FUFING)):
            browser.get(f"https://www.instagram.com/{username}/following/")
            for j in range(count):
                try:
                    follow = browser.find_element_by_class_name("_acan _acap _acas")
                    follow.click()
                    print(f"[+] User >>> {username} -> followed !")
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)

    elif option == 22:
        count=int(input("[?] How many messages do you want to send ? (enter a number) "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[?] How many messages do you want to send ? (enter a number) "))
        for i in range(1,count+1):
            text=str(input("[::] Please enter the message to send >>>  "))
            while text == None:
                print("[!] Invalid message !")
                sleep(1)
                text=str(input("[::] Please enter again the text to send >>>  "))
            count=int(input("[?] In how many users do you want to send it ? (enter a number) "))
            while count == None or count <= 0:
                print("[!] Invalid number !")
                sleep(1)
                count=int(input("[?] In how many users do you want to send it ? (enter a number) "))
            for i in range(count):
                username=str(input(f"[::] Please enter the username No{i+1} : "))
                while checkUser(username) == True:
                    print("[!] Invalid username !")
                    sleep(1)
                    username=str(input(f"[::] Please enter again the username No{i+1} : "))
                print(GetID(username))
                id=int(input("[::] Please enter the ID of the user as shown above: "))
                while checkID(id):
                    print("[!] Invalid ID !")
                    sleep(1)
                    id=int(input("[::] Please enter again the ID of the user as shown above: "))
                MSGIDS.append(id)
                try:
                    client.direct_send(text,MSGIDS)
                    sleep(1)
                    print("[!] Message sent successfully !")
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)

    elif option == 23:
        path=str(input("[::] Please enter the path to the file: "))
        while path == None or "/" not in path or "\\" not in path:
            print("[!] Invalid path !")
            sleep(1)
            path=str(input("[::] Please enter again the path to the file: "))
        count=int(input("[?] In how many users do you want to send it ? (enter a number) "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[?] In how many users do you want to send it ? (enter a number) "))
        for i in range(count):
            username=str(input(f"[::] Please enter the username No{i+1}: "))
            while checkUser(username) == True:
                print("[!] Invalid username !")
                sleep(1)
                username=str(input(f"[::] Please enter again the username No{i+1} : "))
            print(GetID(username))
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while checkID(id):
                print("[!] Invalid ID !")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            FILEIDS.append(id)
            try:
                client.direct_send_file(path,FILEIDS)
                sleep(2)
                print("[!] File sent successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 24:
        path=str(input("[::] Please enter the path to the photo: "))
        while path == None or "/" not in path or "\\" not in path:
            print("[!] Invalid path !")
            sleep(1)
            path=str(input("[::] Please enter again the path to the photo: "))
        count=int(input("[?] In how many users do you want to send it ? (enter a number) "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[?] In how many users do you want to send it ? (enter a number) "))
        for i in range(count):
            username=str(input(f"[::] Please enter the username No{i+1} : "))
            while checkUser(username) == True:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input(f"[::] Please enter again the username No{i+1} : "))
            print(GetID(username))
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while checkID(id):
                print("[!] Invalid ID !")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            PHOTOIDS.append(id)
            try:
                client.direct_send_photo(path,PHOTOIDS)
                sleep(2)
                print("[!] Photo sent successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 25:
        path=str(input("[::] Please enter the path to the video: "))
        while path == None or "/" not in path or "\\" not in path:
            print("[!] Invalid path !")
            sleep(1)
            path=str(input("[::] Please enter again the path to the video: "))
        count=int(input("[?] In how many users do you want to send it ? (enter a number) "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[?] In how many users do you want to send it ? (enter a number) "))
        for i in range(count):
            username=str(input(f"[::] Please enter the username No{i+1} : "))
            while checkUser(username) == True:
                print("[!] Invalid username !")
                sleep(1)
                username=str(input(f"[::] Please enter again the username No{i+1} : "))
            print(GetID(username))
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while checkID(id):
                print("[!] Invalid ID !")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            VIDEOIDS.append(id)
            try:
                client.direct_send_video(path,VIDEOIDS)
                sleep(2)
                print("[!] Video sent successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 26:
        count=int(input("[::] Please enter the number of hashtags: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of hashtags: "))
        nump=int(input("[::] Please enter the number of the posts to like: "))
        while nump == None or nump <= 0:
            print("[!] Invalid number !")
            sleep(1)
            nump=int(input("[::] Please enter again the number of the posts to like: "))
        for i in range(count):
            hashtag=str(input(f"[::] Please enter the hashtag No{i+1} : "))
            while (hashtag == None) or ("#" not in hashtag):
                print("[!] Invalid Hashtag !")
                sleep(1)
                hashtag=str(input(f"[::] Please enter again the hashtag No{i+1} : "))
            LTAGS.append(hashtag)
            print("[!] Hashtag added successfully !")
        rtags=str(input("[?] Do you want to like random tags ? [yes/no] "))
        while rtags not in ANS and rtags not in NANS or rtags == None:
            print("[!] Invalid input !")
            sleep(1)
            rtags=input("[?] Do you want to like random hashtags ? [yes/no] ")
        if rtags in ANS:
            random = True
        else:
            random = False
        try:
            logini.like_by_tags(LTAGS,random,count)
            sleep(3)
            print("[!] Posts liked !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 27:
        countu=int(input("[::] Please enter the number of accounts: "))
        while countu == None or countu <= 0:
            print("[!] Invalid number !")
            sleep(1)
            countu=int(input("[::] Please enter again the number of accounts: "))
        count=int(input("[::] Please enter the number of posts to like: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of posts to like: "))
        if countu == 1:
            username=str(input("[::] Please enter the username: "))
            while checkUser(username) == True:
                print("[!] Invalid username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            LBU.append(username)
            try:
                logini.like_by_users(LBU,count)
                sleep(5)
                print("[!] Posts liked successfully !")
            except Exception as ex:
                print("[!] Error")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            for i in range(countu):
                username=str(input(f"[::] Please enter the username No{i+1} : "))
                while checkUser(username) == True:
                    print("[!] Invalid username !")
                    sleep(1)
                    username=str(input(f"[::] Please enter again the username No{i+1} : "))
                LBU.append(username)
            try:
                logini.like_by_users(LBU,count)
                sleep(5)
                print("[!] Posts liked successfully !")
            except Exception as ex:
                print("[!] Error")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 28:
        rand=str(input("[?] Do you want to like the posts with random order ? [yes/no] "))
        while rand not in ANS and rand not in NANS or rand == None:
            print("[!] Invalid input !")
            sleep(1)
            rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
        if rand in ANS:
            random = True
            print("[OK]")
            pass
        else:
            random = False
            print("[OK]")
            pass
        numloc=int(input("[::] Please enter the number of locations to like their posts: "))
        while numloc == None or numloc <= 0:
                print("[!] Invalid number !")
                sleep(1)
                numloc=int(input("[::] Please enter again the number of locations to like their posts: "))
        sleep(2)
        countp=int(input("[?] How many posts to like per location ? (enter a number) "))
        while countp == None or countp <= 0:
            print("[!] Invalid number !")
            sleep(1)
            countp=int(input("[?] How many posts to like per location ? (enter a number) "))
        for i in range(numloc):
            location=str(input(f"[::] Please enter location No{i+1} : "))
            while location == None:
                print("[!] Invalid location !")
                sleep(1)
                location=str(input(f"[::] Please enter again location No{i+1} : "))
            LOCLIKE.append(location)
        try:
            logini.like_by_locations(LOCLIKE,number=countp,randomize=random)
            sleep(5)
            print("[!] Posts liked !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 29:
        count=int(input("[+] Please enter the number of posts to like: "))
        while count <= 0 or count == None:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of posts to like: "))
        if count == 1:
            rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
            while rand not in ANS and rand not in NANS or rand == None:
                print("[!] Invalid input !")
                sleep(1)
                rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
            if rand in ANS:
                rmize = True
                print("[OK]")
            else:
                rmize = False
                print("[OK]")
            try:
                logini.like_by_feed(count,rmize)
                sleep(5)
                print("[!] Posts liked !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
            while rand not in ANS and rand not in NANS or rand == None:
                print("[!] Invalid input !")
                sleep(1)
                rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
            if rand in ANS:
                random = True
                print("[OK]")
                pass
            else:
                random = False
                print("[OK]")
                pass
            for i in range(count):
                try:
                    logini.like_by_feed(count,random)
                    sleep(5)
                    print("[!] Posts liked !")
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)

    elif option == 30:
        amo=int(input("[::] Please enter the number of posts to like: "))
        while amo == None or amo <= 0:
            print("[!] Invalid number !")
            sleep(1)
            amo=int(input("[::] Please enter again the number of posts to like: "))
        username=str(input("[::] Please enter the username: "))
        while checkUser(username) == True:
            print("[!] Invalid username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        print(GetID(username))
        id=int(input("[::] Please enter user's ID as shown above: "))
        while checkID(id):
            print("[!] Invalid ID !")
            sleep(1)
            id=int(input("[::] Please enter again user's ID as shown above: "))
        bot.comment_user(id,amo)
    elif option == 31:
        count=int(input("[::] Please enter the number of replies: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of replies to save: "))
        for i in range(count):
            reply=str(input(f"[::] Please enter the reply No{i+1}: "))
            while reply == None:
                print("[!] Invalid reply !")
                sleep(1)
                reply=str(input(f"[::] Please enter again the reply No{i+1}: "))
            REPLS.append(reply)
        try:
            logini.set_comment_replies(REPLS)
            sleep(3)
            print("[!] Default replies applied successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 32:
        print("[+] Default: \"Love it !\"\n")
        com=str(input("[::] Please enter your comment: "))
        while com == None:
            print("[!] Invalid comment !")
            sleep(1)
            com=str(input("[::] Please enter again your comment: "))
        url="https://www.instagram.com"
        webbrowser.open(url)
        print("[+] Please find the post to comment and wait...")
        found=str(input("[::] If found enter [yes]: "))
        while found not in ANS or found == None:
            print("[!] Invalid input !")
            sleep(1)
            found=str(input("[::] If found enter [yes]: "))
        if found in ANS:
            browser=webdriver.Firefox()
            link=input("[::] Please enter the url for the post: ")
            while link == None or "https" not in link or "//" not in link or "instagram" not in link or "www" not in link or ".com" not in link:
                print("[!] Invalid url !")
                sleep(1)
                link=input("[::] Please enter again the url for the post: ")
            browser.get(link)
            try:
                comment_label = browser.find_element_by_class_name("_ablz _aaoc")
                comment_label.send_keys(com)
                publish = browser.find_element_by_class_name("_aacl _aaco _aacw _adda _aad0 _aad6 _aade")
                publish.click()
                sleep(4)
                print("[!] Commented successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 33:
        count=int(input("[::] Please enter the number of users to block: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of users to block: "))
        if count == 1:
            username=str(input("[::] Please enter the username: "))
            while checkUser(username) == True:
                print("[!] Invalid username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
                print(GetID(username))
                id=int(input("[::] Please enter the ID of the user as shown above: "))
                while checkID(id):
                    print("[!] Invalid ID !")
                    sleep(1)
                    id=int(input("[::] Please enter again the ID of the user as shown above: "))
                BLOCKU.append(id)
                try:
                    bot.block_users(BLOCKU)
                    sleep(3)
                    print("[!] User blocked !")
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)
        else:
            for i in range(count):
                username=str(input(f"[::] Please enter the username No{i+1}: "))
                while checkUser(username) == True:
                    print("[!] Invalid Username !")
                    sleep(1)
                    username=str(input(f"[::] Please enter again the username No{i+1}: "))
                uid = loader.check_profile_id(username)
                id = int(input("[::] Please enter the ID of the user as shown above: "))
                while checkID(id):
                    print("[!] Invalid ID !")
                    sleep(1)
                    id = int(input("[::] Please enter again the ID of the user as shown above: "))
                BLOCKU.append(id)
            try:
                bot.block_users(BLOCKU)
                sleep(3)
                print("[!] Users blocked successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 34:
        id=int(input("[::] Please enter the ID of the user: "))
        while checkID(id):
            print("[!] Invalid ID !")
            sleep(1)
            id=int(input("[::] Please enter again the ID of the user: "))
        try:
            client.username_from_user_id(id)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 35:
        try:
            blocked_users = api.blocked_user_list()
            print("[+] Blocked users: ")
            print("\n")
            print(blocked_users)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 36:
        counti=int(input("[::] How many highlights do you want to create ? "))
        while counti == None or counti <= 0:
            print("[!] Invalid number !")
            sleep(1)
            counti=int(input("[::] How many highlights do you want to create ? "))
        if counti == 1:
            title=str(input("[::] Please enter the title of the highlight: "))
            while title == None:
                print("[!] Invalid title")
                sleep(1)
                title=str(input("[::] Please enter again the title of the highlight: "))
            count=int(input("[::] Please enter the number of stories to add in the highlight: "))
            while count == None or count <= 0:
                print("[!] Invalid number !")
                sleep(1)
                count=int(input("[::] Please enter again the number of stories to add in the highlight: "))
            for i in range(count):
                story_id = int(input(f"[::] Please enter the story ID No{i+1}: "))
                while story_id == None or story_id <= 0:
                    print("[!] Invalid ID !")
                    sleep(1)
                    story_id = int(input(f"[::] Please enter again the story ID No{i+1}: "))
                STIDS.append(story_id)
            try:
                client.highlight_create(title,STIDS)
                sleep(3)
                print("[!] Highlight created successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            for i in range(counti):
                title=str(input(f"[::] Please enter the title of the highlight No{i+1}: "))
                while title == None:
                    print("[!] Invalid title")
                    sleep(1)
                    title=str(input(f"[::] Please enter again the title of the highlight No{i+1}: "))
                count=int(input("[::] Please enter the number of stories to add in the highlight: "))
                while count == None or count <= 0:
                    print("[!] Invalid number !")
                    sleep(1)
                    count=int(input("[::] Please enter again the number of stories to add in the highlight: "))
                for i in range(count):
                    story_id = int(input(f"[::] Please enter the story ID No{i+1}: "))
                    while story_id == None or story_id <= 0:
                        print("[!] Invalid ID !")
                        sleep(1)
                        story_id = int(input(f"[::] Please enter again the story ID No{i+1}: "))
                    STIDS.append(story_id)
                try:
                    client.highlight_create(title,STIDS)
                    sleep(3)
                    print("[!] Highlight created successfully !")
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)

    elif option == 37:
        count=int(input("[::] How many highlights do you want to delete ? "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] How many highlights do you want to delete ? "))
        if count == 1:
            hid=int(input("[::] Please enter the highlight ID: "))
            while hid == None or hid <= 0:
                print("[!] Invalid ID !")
                sleep(1)
                hid=int(input("[::] Please enter again the highlight ID: "))
            try:
                api.highlight_delete(hid)
                sleep(3)
                print("[!] Highlight deleted successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            for i in range(count):
                hid=int(input(f"[::] Please enter the highlight ID No{i+1}: "))
                while hid == None or hid <= 0:
                    print("[!] Invalid ID !")
                    sleep(1)
                    hid=int(input(f"[::] Please enter again the highlight ID No{i+1}: "))
                try:
                    api.highlight_delete(hid)
                    sleep(3)
                    print("[!] Highlight deleted successfully !")
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)

    elif option == 38:
        count=int(input("[::] How many covers of highlights do you want to change ? "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] How many covers of highlights do you want to change ? "))
        if count == 1:
            url=str(input("[::] Please enter the url to the highlight: "))
            while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
                print("[!] Invalid url !")
                sleep(1)
                url=str(input("[::] Please enter again the url to the highlight: "))
            print(Get_Hpk(url))
            pk=int(input("[::] Please enter the highlight id as shown above: "))
            while pk == None or pk <= 0:
                print("[!] Invalid ID !")
                sleep(1)
                pk=int(input("[::] Please enter again the highlight id as shown above: "))
            path=str(input("[::] Please enter the path to the cover for the highlight: "))
            while path == None or "/" not in path or "\\" not in path:
                print("[!] Invalid path !")
                sleep(1)
                print("[!] Path must contain / or \\")
                sleep(2)
                path=str(input("[::] Please enter again the path of the cover for the highlight: "))
            try:
                client.highlight_change_cover(pk,path) 
                sleep(3)
                print("[!] Highlight cover changed successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            for i in range(count):
                url=str(input("[::] Please enter the url for the highlight: "))
                while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
                    print("[!] Invalid url !")
                    sleep(1)
                    url=str(input("[::] Please enter again the url for the highlight: "))
                print(Get_Hpk(url))
                pk=int(input("[::] Please enter the highlight id as shown above: "))
                while pk == None or pk <= 0:
                    print("[!] Invalid ID !")
                    sleep(1)
                    pk=int(input("[::] Please enter again the highlight id as shown above: "))
                path=str(input("[::] Please enter the path of the cover for the highlight: "))
                while path == None or "/" not in path or "\\" not in path:
                    print("[!] Invalid path !")
                    sleep(1)
                    print("[!] Path must contain / or \\")
                    sleep(2)
                    path=str(input("[::] Please enter again the path of the cover for the highlight: "))
                try:
                    client.highlight_change_cover(pk,path) 
                    sleep(3)
                    print("[!] Highlight cover changed successfully !")
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)

    elif option == 39:
        countu=int(input("[::] From how many users you want to display their highlights ? "))
        while countu <= 0 or countu == None:
            print("[!] Invalid Number !")
            sleep(1)
            countu=int(input("[::] From how many users you want to display their highlights ? "))
        if countu == 1:
            username=str(input("[::] Please enter the username: "))
            while checkUser(username) == True:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            uid = loader.check_profile_id(username)
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while checkID(id):
                print("[!] Invalid ID !")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            number=int(input("[::] How many highlights do you want to display ? "))
            while number == None or number <= 0:
                print("[!] Invalid number !")
                sleep(1)
                number=int(input("[::] How many highlights do you want to display ? "))
            try:
                client.user_highlights(id,number)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            for i in range(countu):
                username=str(input("[::] Please enter the username: "))
                while checkUser(username) == True:
                    print("[!] Invalid username !")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
                print(GetID(username))
                id=int(input("[::] Please enter the ID of the user as shown above: "))
                while checkID(id):
                    print("[!] Invalid ID !")
                    sleep(1)
                    id=int(input("[::] Please enter again the ID of the user as shown above: "))
                number=int(input("[::] How many highlights do you want to display ? "))
                while number == None or number <= 0:
                    print("[!] Invalid number !")
                    sleep(1)
                    number=int(input("[::] How many highlights do you want to display ? "))
                try:
                    client.user_highlights(id,number)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)

    elif option == 40:
        counti=int(input("[::] From how many highlights do you want to retrieve information ? "))
        while counti == None or counti <= 0:
            print("[!] Invalid number !")
            sleep(1)
            counti=int(input("[::] From how many highlights do you want to retrieve information ? "))
        if counti == 1:
            url=str(input("[::] Please enter the url for the highlight: "))
            while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
                print("[!] Invalid url !")
                sleep(1)
                url=str(input("[::] Please enter again the url for the highlight: "))
            Get_Hpk(url)
            pk=int(input("[::] Please enter the highlight id as shown above: "))
            while pk == None or pk <= 0:
                print("[!] Invalid ID !")
                sleep(1)
                pk=int(input("[::] Please enter again the highlight id as shown above: "))
            try:
                client.highlight_info(pk)
                sleep(3)
                print("[!] Information retrieved successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            for i in range(counti):
                url=str(input("[::] Please enter the url for the highlight: "))
                while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
                    print("[!] Invalid url !")
                    sleep(1)
                    url=str(input("[::] Please enter again the url for the highlight: "))
                print(Get_Hpk(url))
                pk=int(input("[::] Please enter the highlight id as shown above: "))
                while pk == None or pk <= 0:
                    print("[!] Invalid ID !")
                    sleep(1)
                    pk=int(input("[::] Please enter again the highlight id as shown above: "))
                try:
                    client.highlight_info(pk)
                    sleep(3)
                    print("[!] Information retrieved successfully !")
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)

    elif option == 41:
        url=str(input("[::] Please enter the url of the story: "))
        while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
            print("[!] Invalid url !")
            sleep(1)
            url=str(input("[::] Please enter again the url of the story: "))
        print(Get_Spk(url))
        pk=int(input("[::] Please enter the story ID as shown above: "))
        while checkID(id):
            print("[!] Invalid ID !")
            sleep(1)
            pk=int(input("[::] Please enter again the story ID as shown above: "))
        try:
            client.story_delete(pk)
            sleep(3)
            print("[!] Story deleted successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 42:
        url=str(input("[::] Please enter the url of the story: "))
        while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
            print("[!] Invalid url !")
            sleep(1)
            url=str(input("[::] Please enter again the url of the story: "))
        print(Get_Spk(url))
        pk=int(input("[::] Please enter the story ID as shown above: "))
        while checkID(id):
            print("[!] Invalid ID !")
            sleep(1)
            pk=int(input("[::] Please enter again the story ID as shown above: "))
        number=int(input("[::] Please enter the number of viewers to display: "))
        while number == None or number <= 0:
            print("[!] Invalid number !")
            sleep(1)
            number=int(input("[::] Please enter again the number of viewers to display: "))
        try:
            client.story_viewers(pk,number)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 43:
        count=int(input("[::] Please specify the number of hashtags: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please specify again the number of hashtags: "))
        for i in range(count):
            tag=input(f"[::] Please enter the hashtag No{i+1}: ")
            while tag == None:
                print("[!] Invalid hashtag !")
                sleep(1)
                tag=input(f"[::] Please enter again the hashtag No{i+1}: ")
            STBTGS.append(tag)
        try:
            logini.story_by_tags(STBTGS)
            sleep(3)
            print("[!] Request successful !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 44:
        count=int(input("[::] Please specify the number of users: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please specify again the number of users: "))
        for i in range(count):
            username=input(f"[::] Please enter the username No{i+1}: ")
            while checkUser(username) == True:
                print("[!] Invalid Username !")
                sleep(1)
                username=input(f"[::] Please enter again the username No{i+1}: ")
            print(GetID(username))
            id=int(input("[::] Please enter the ID as shown above: "))
            while checkID(id):
                print("[!] Invalid ID !")
                sleep(1)
                id=int(input("[::] Please enter again the ID as shown above: "))
            GTST.append(id)
        try:
            loader.get_stories(GTST)
            sleep(3)
            print("[!] Request successful !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 45:
        url=str(input("[::] Please enter the url of the story: "))
        while url == None or "https" not in url or "//" not in url or "instagram" not in url or ".com" not in url:
            print("[!] Invalid url !")
            sleep(1)
            url=str(input("[::] Please enter again the url of the story: "))
        print(Get_Spk(url))
        pk=int(input("[::] Please enter the story ID as shown above: "))
        while checkID(id):
            print("[!] Invalid ID !")
            sleep(1)
            pk=int(input("[::] Please enter again the story ID as shown above: "))
        try:
            client.story_info_v1(pk)
            sleep(3)
            print("[!] Request successful !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 46:
        print("[+] Countries example: US, BR, CZ")
        sleep(1)
        fcodes=str(input("[?] Do you want to display full list of country codes ? [yes/no] "))
        while fcodes not in ANS and fcodes not in NANS or fcodes == None:
            print("[!] Invalid input !")
            sleep(1)
            fcodes=str(input("[?] Do you want to display full list of country codes ? [yes/no] "))
        if fcodes in ANS:
            webbrowser.open("https://www.iban.com/country-codes")
            country=str(input("[::] Please enter the country: "))
            while country == None:
                print("[!] Invalid country !")
                sleep(1)
                country=str(input("[::] Please enter again the country: "))
            try:
                client.set_country(country)
                sleep(3)
                print("[!] Country applied successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            country_name=str(input("[::] Please enter the country: "))
            while country_name == None:
                print("[!] Invalid country !")
                sleep(1)
                country_name=str(input("[::] Please enter again the country: "))
                try:
                    client.set_country(country_name)
                    sleep(3)
                    print("[!] Country set successful !")
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    quit(0)

    elif option == 47:
        bio=str(input("[::] Please enter the text for the bio: "))
        while bio == None or type(bio) != str:
            if bio == None:
                print("[!] This input can't be empty !")
            else:
                print("[!] Invalid bio !")
            sleep(1)
            bio=str(input("[::] Please enter again the text for the bio: "))
        try:
            client.account_set_biography(bio)
            sleep(3)
            print("[!] Bio applied successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 48:
        username=str(input("[::] Please enter your username: "))
        while checkUser(username) == True:
            print("[!] Invalid username !")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        try:
            info = client.user_info_by_username_v1(username)
            sleep(3)
            print("[!] Information gathering successful !")
            sleep(2)
            print(info)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 49:
        username=str(input("[::] Please enter the username: "))
        while checkUser(username) == True:
            print("[!] Invalid username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        print(GetID(username))
        id=int(input("[::] Please enter the ID as shown above: "))
        while checkID(id):
            print("[!] Invalid ID !")
            sleep(1)
            id=int(input("[::] Please enter again the ID as shown above: "))
        try:
            posts = client.usertag_medias_v1(id)
            sleep(3)
            print("[+] Request successful !")
            sleep(1)
            print(posts)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 50:
        username=str(input("[::] Please enter your username: "))
        while checkUser(username) == True:
            print("[!] Invalid username !")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        try:
            client.reset_password(username)
            sleep(3)
            print("[!] Password reseted successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 51:
        set_first_name=str(input("[?] Do you want to set a first name ? [yes/no] "))
        while set_first_name == None or set_first_name not in ANS and set_first_name not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            set_first_name=str(input("[?] Do you want to set a first name ? [yes/no] "))
        if set_first_name in ANS:
            first_name=str(input("[::] Please enter your first name: "))
            while first_name == None:
                print("[!] Invalid first name !")
                sleep(1)
                first_name=str(input("[::] Please enter again your first name: "))
        else:
            pass
        set_bio=str(input("[?] Do you want to set a bio ? [yes/no] "))
        while set_bio == None or set_bio not in ANS and set_bio not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            set_bio=str(input("[?] Do you want to set a bio ? [yes/no] "))
        if set_bio in ANS:
            bio=str(input("[::] Please enter the bio: "))
            while bio == None:
                print("[!] Invalid Bio !")
                sleep(1)
                bio=str(input("[::] Please enter again the bio: "))
        else:
            pass
        set_ex_url=str(input("[?] Do you want to add an external url ? [yes/no] "))
        while set_ex_url == None or set_ex_url not in ANS and set_ex_url not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            set_ex_url=str(input("[?] Do you want to set an external url ? [yes/no] "))
        if set_ex_url in ANS:
            url=str(input("[::] Please enter the url: "))
            while url == None or "/" not in url or "//" not in url:
                print("[!] Invalid url !")
                sleep(1)
                url=str(input("[::] Please enter again the url: "))
        else:
            print("[OK]")
            pass
        set_email=str(input("[?] Do you want to add an email ? [yes/no] "))
        while set_email == None or set_email not in ANS and set_email not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            set_email=str(input("[?] Do you want to set an email ? [yes/no] "))
        if set_email in ANS:
            email=str(input("[::] Please enter the email address: "))
            while email == None or "@" not in email or "gmail" not in email or ".com" not in email:
                print("[!] Invalid email address!")
                sleep(1)
                email=str(input("[::] Please enter again the email address: "))
        else:
            pass
        set_phone_number=str(input("[?] Do you want to add a phone number ? [yes/no] "))
        while set_phone_number == None or set_phone_number not in ANS and set_phone_number not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            set_phone_number=str(input("[?] Do you want to set a phone number ? [yes/no] "))
        if set_phone_number in ANS:
            phone_number=int(input("[::] Please enter the phone number: "))
            while phone_number == None:
                print("[!] Invalid phone number !")
                sleep(1)
                phone_number=int(input("[::] Please enter the phone number: "))
        else:
            pass
        set_gender=str(input("[?] Do you want to set a gender ? [yes/no] "))
        while set_gender == None or set_gender not in ANS and set_gender not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            set_gender=str(input("[?] Do you want to set a gender ? [yes/no] "))
        if set_gender in ANS:
            gender=str(input("[::] Please enter the gender: "))
            while gender == None:
                print("[!] Invalid gender !")
                sleep(1)
                gender=str(input("[::] Please enter again the gender: "))
        else:
            pass    
        try:
            api.edit_profile(first_name,bio,url,email,phone_number,gender)
            sleep(5)
            print("[!] Profile edited successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            quit(0)

    elif option == 52:
        count=int(input("[::] How many posts do you want to like/unlike ? "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] How many posts do you want to like/unlike ? "))
        browser = webdriver.Chrome()
        for i in range(count):
            url=str(input("[::] Please enter the url of the post: "))
            while url == None or "https" not in url and "instagram" not in url and "//" not in url and ".com" not in url and "/" not in url:
                print("[!] Invalid url !")
                sleep(1)
                url=str(input("[::] Please enter again the url of the post: "))
            try:
                browser.get(url)
                like = browser.find_element_by_id("mount_0_0_Cs")
                like.click()
                print("[!] Posts liked !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 53:
        count=int(input("[::] Please enter the number of deletes to make: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of deletes to make: "))
        browser = webdriver.Chrome()
        for i in range(count):
            url=str(input("[::] Please enter the url of the post, igtv, reel etc. : "))
            while url == None or "https" not in url and "instagram" not in url and "//" not in url and ".com" not in url and "/" not in url:
                print("[!] Invalid url !")
                sleep(1)
                url=str(input("[::] Please enter again the url of the post, igtv, reel etc. : "))
            try:
                browser.get(url)
                menu = browser.find_element_by_class_name("_ab6-")
                menu.click()
                delete = browser.find_element_by_class_name("_a9-- _a9-_")
                delete.click()
                sleep(3)
                print("[!] Deleted successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 54:
        """

        Use xpath instead of browser.find_element_by_class_name()
        
        """
        count=int(input("[::] Please enter the number of the posts to save: "))
        while count == None or count <= 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of the posts to save: "))
        browser = webdriver.Chrome()
        for i in range(count):
            url=str(input("[::] Please enter the url of the post, igtv, reel etc. : "))
            while url == None or "https" not in url and "instagram" not in url and "//" not in url and ".com" not in url and "/" not in url:
                print("[!] Invalid url !")
                sleep(1)
                url=str(input("[::] Please enter again the url of the post, igtv, reel etc. : "))
            try:
                browser.get(url)
                save = browser.find_element_by_class_name("_abm0 _abm1")
                save.click()
                sleep(3)
                print("[!] Successfully saved !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

    elif option == 55:
        __time__=input("[::] Please enter the time (example: 15:06:10): ")
        while __time__ == None or ":" not in __time__:
            print("[!] Invalid time !")
            sleep(1)
            __time__=input("[::] Please enter again the time (example: 15:06:10): ")
        Av_Acts()
        cur_time = datetime.now()
        current_time = cur_time.now("%H:%M:%S")
        action=int(input("[::] Please enter the number of the action: "))
        while action < 1 or action > 26 or action == None:
            print("[!] Invalid number !")
            sleep(1)
            action=int(input("[::] Please enter the number of the action: "))

        if action == 1:
            count=int(input("[::] Please enter the number of posts to post: "))
            while count == None or count <= 0:
                print("[!] Invalid number !")
                sleep(1)
                count=int(input("[::] Please enter again the number of posts to post: "))
            for i in range(count):
                path=str(input("[::] Please enter the path to the photo: "))
                while path == None or "/" not in path and "\\" not in path:
                    print("[!] Invalid path !")
                    sleep(1)
                    path=str(input("[::] Please enter again the path to the photo: "))
                sleep(2)
                print(">>>CAPTION<<<")
                sleep(1)
                print("[+] Default: Check out my new post !")
                sleep(2)
                print("[+] Hit <Tab> and <Enter> to apply the default option")
                sleep(2)
                caption=str(input("[::] Please enter the caption: "))
                if caption == "\t":
                    caption = "Check out my new post !"
                print(">>>TAGS<<<")
                sleep(2)
                print("[+] Default: [no]")
                sleep(2)
                print("[+] Hit <Tab> and <Enter> to Apply the default option")
                sleep(2)
                tags=input("[?] Do you want to tag other users ? [yes/no] ")
                while tags not in ANS and tags not in NANS or tags == None:
                    print("[!] Invalid input !")
                    sleep(1)
                    tags=input("[?] Do you want to tag other users ? [yes/no] ")
                if tags == "\t":
                    tags = "no"
                if tags in ANS:
                    print("[+] Default: 1")
                    sleep(2)
                    print("[+] Hit <Tab> and <Enter> to Apply the Default Option")
                    count=int(input("[?] How many users do you want to include ? "))
                    while count == None or count <= 0:
                        print("[!] Invalid Number !")
                        sleep(1)
                        count=int(input("[?] How many users do you want to tag ? "))
                    utag=str(input("[::] Please enter the username: "))
                    while checkUser(username) == True(utag):
                        print("[!] Invalid username !")
                        sleep(1)
                        utag=str(input("[::] Please enter again the username: "))
                    utag = utag.strip()
                    utag = utag.lower()
                    TaggedUsers.append(utag)
                    for i in range(count):
                        utag=str(input(f"[::] Please enter the username No{i+1}: "))
                        while checkUser(username) == True(utag):
                            print("[!] Invalid username !")
                            sleep(1)
                            utag=str(input(f"[::] Please enter again the username No{i+1}: "))
                        utag = utag.strip()
                        utag = utag.lower()
                        TaggedUsers.append(utag)
                else:
                    print("[OK]")
                    pass
                print(">>>LOCATION<<<")
                sleep(2)
                print("[+] Default: [no]")
                sleep(1)
                print("[+] Hit <Tab> and <Enter> to apply the default option")
                sleep(2)
                loc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
                while loc not in ANS and loc not in NANS or loc == None:
                    print("[!] Invalid input !")
                    sleep(1)
                    loc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
                if loc == "\t":
                    loc = "no"
                if loc in ANS:
                    count=int(input("[?] How many ? "))
                    while count == None or count <= 0:
                        print("[!] Invalid number !")
                        sleep(1)
                        count=int(input("[?] How many locations do you want to include ? "))
                    for i in range(count):
                        location1=str(input(f"[::] Please enter location No{i+1}: "))
                        while location1 == None:
                            print("[!] Invalid location")
                            sleep(0.5)
                            location1=str(input(f"[::] Please enter again location No{i+1}: "))
                        LOCATIONS.append(location1)
                        print("[!] Location added successfully !")
                        if current_time == __time__:
                            try:
                                client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                                sleep(2)
                                print("[!] Photo uploaded successfully !")
                                quit(0)
                            except Exception as ex:
                                print("[!] Error !")
                                sleep(1)
                                print(ex)
                                sleep(2)
                                print("[+] Exiting...")
                                quit(0)
                    else:
                        print("[+] Current time: "+str(current_time))
                        sleep(1)
                        print("[+] Waiting for the time: "+str(__time__))
                        pass
                else:
                    print("[OK]")
                    pass
                if tags in ANS and loc in ANS:
                    if current_time == __time__:
                        try:
                            client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                            print("[!] Photo uploaded successfully !")
                            quit(0)
                        except Exception as ex:
                            print("[!] Error !")
                            sleep(1)
                            print(ex)
                            sleep(2)
                            print("[+] Exiting...")
                            quit(0)
                    else:
                        print("[+] Current time: "+str(current_time))
                        sleep(1)
                        print("[+] Waiting for the time: "+str(__time__))
                        pass
                elif tags in ANS and loc in NANS:
                    if current_time == __time__:
                        try:
                            client.photo_upload(path=path,caption=caption,tags=TaggedUsers)
                            print("[!] Photo uploaded successfully !")
                            quit(0)
                        except Exception as ex:
                            print("[!] Error !")
                            sleep(1)
                            print(ex)
                            sleep(2)
                            print("[+] Exiting...")
                            quit(0)
                    else:
                        print("[+] Current time: "+str(current_time))
                        sleep(1)
                        print("[+] Waiting for the time: "+str(__time__))
                        pass
                elif tags in NANS and loc in ANS:
                    if current_time == __time__:
                        try:
                            client.photo_upload(path=path,caption=caption,location=LOCATIONS)
                            print("[!] Photo uploaded successfully !")
                            quit(0)
                        except Exception as ex:
                            print("[!] Error !")
                            sleep(1)
                            print(ex)
                            sleep(2)
                            print("[+] Exiting...")
                            quit(0)
                    else:
                        print("[+] Current time: "+str(current_time))
                        sleep(1)
                        print("[+] Waiting for the time: "+str(__time__))
                        pass
                elif tags in NANS and loc in NANS:
                    if current_time == __time__:
                        try:
                            client.photo_upload(path=path,caption=caption)
                            print("[!] Photo uploaded successfully !")
                            quit(0)
                        except Exception as ex:
                            print("[!] Error !")
                            sleep(1)
                            print(ex)
                            sleep(2)
                            print("[+] Exiting...")
                            quit(0)
                    else:
                        print("[+] Current time: "+str(current_time))
                        sleep(1)
                        print("[+] Waiting for the time: "+str(__time__))
                        pass

        elif action == 2:
            path=str(input("[::] Please enter the path to the picture: "))
            while path == None or "/" not in path and "\\" not in path:
                print("[!] Invalid path !")
                sleep(1)
                path=str(input("[::] Please enter again the path to the picture: "))
            try:
                client.account_change_picture(path)
                sleep(3)
                print("[!] Your profile picture changed successfully !")
                quit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)

        elif action == 3:
            path=str(input("[::] Please enter the path to the photo: "))
            while path == None or "/" not in path and "\\" not in path:
                print("[!] Invalid path !")
                sleep(1)
                path=str(input("[::] Please enter again the path to the photo: "))
            AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
            while AddCaption not in ANS and AddCaption not in NANS or AddCaption == None:
                print("[!] Invalid input !")
                sleep(1)
                AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
            if AddCaption in ANS:
                print("[+] Default: Check out my new story !")
                sleep(2)
                print("[+] Hit <Tab> and <Enter> for the default option to be applied")
                sleep(2)
                caption=str(input("[::] Please enter the caption: "))
                if caption == "\t":
                    caption = "Check out my new story !"
                else:
                    caption=str(input("[::] Please enter a caption to include: "))
                    while caption == None:
                        print("[!] Invalid caption !")
                        sleep(1)
                        caption=str(input("[::] Please enter again a caption to include: "))
            else:
                print("[OK]")
                pass
            AddMention=str(input("[?] Do you want to add mention ? [yes/no] "))
            while AddMention not in ANS and AddMention not in NANS or AddMention == None:
                print("[!] Invalid input !")
                sleep(1)
                mention=str(input("[?] Do you want to mention user(s) ? [yes/no] "))
            if AddMention in ANS:
                MENTIONS = []
                count=int(input("[?] How many ? "))
                while count == None or count <= 0:
                    print("[!] Invalid number !")
                    sleep(1)
                    count=int(input("[?] How many users do you want to mention ? (enter a number) "))
                for i in range(count):
                    mention=str(input(f"[::] Please enter the username No{i+1}: "))
                    while checkUser(username) == True(mention) == False:
                        print("[!] Invalid Username !")
                        sleep(1)
                        mention=str(input("[::] Please enter again the username No{}: ".format(i)))
                    MENTIONS.append(mention)
                    sleep(1)
                    print("[!] Mention added successfully !")
            else:
                print("[OK]")
                sleep(1)
                pass
            AddLoc=str(input("[?] Do you want to add location ? [yes/no] "))
            while AddLoc not in ANS and AddLoc not in NANS or AddLoc == None:
                print("[!] Invalid input !")
                sleep(1)
                AddLoc=str(input("[?] Do you want to add location ? [yes/no] "))
            if AddLoc in ANS:
                count=int(input("[?] How many locations do you want to add ? "))
                while count == None or count <= 0:
                    print("[!] Invalid number !")
                    sleep(1)
                    count=int(input("[?] How many locations do you want to add ? "))
                for i in range(count):
                    loc=str(input(f"[::] Please enter location No{i+1}: "))
                    while loc == None:
                        print("[!] Invalid location !")
                        sleep(1)
                        loc=str(input(f"[::] Please enter again location No{i+1}: "))
                    LOCATIONS.append(loc)
                    sleep(1)
                    print("[!] Location added successfully !")
            else:
                print("[OK]")
                sleep(1)
                pass
            AddLinks=str(input("[?] Do you want to include links ? [yes/no] "))
            while AddLinks not in ANS and AddLinks not in NANS or AddLinks == None:
                print("[!] Invalid input !")
                sleep(1)
                AddLinks=str(input("[?] Do you want to include links ? [yes/no] "))
            if AddLinks in ANS:
                count=int(input("[?] How many ? (enter a number) "))
                while count == None or count <= 0:
                    print("[!] Invalid number !")
                    sleep(1)
                    count=int(input("[?] How many links do you want to include ? (enter a number) "))
                for i in range(count):
                    link=str(input(f"[::] Please enter the link No{i+1}: "))
                    while link == None or "/" not in link or "https" not in link:
                        print("[!] Invalid link !")
                        sleep(1)
                        link=str(input(f"[::] Please enter again the link No{i+1}: "))
                    LINKS.append(link)
                    sleep(1)
                    print("[!] Link added successfully !")
            else:
                print("[OK]")
                sleep(1)
                pass
            AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
            while AddHash not in ANS and AddHash not in NANS or AddHash == None:
                print("[!] Invalid input !")
                sleep(1)
                AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
            if AddHash in ANS:
                count=int(input("[?] How many ? (enter a number) "))
                while  count <= 0 or count == None :
                    print("[!] Invalid Number !")
                    sleep(1)
                    count=int(input("[?] How many hashtags do you want to include ? (enter a number) "))
                for i in range(count):
                    hashtag=str(input(f"[::] Please enter the hashtag No{i+1}: "))
                    while hashtag == None or "#" not in hashtag:
                        print("[!] Invalid hashtag !")
                        sleep(1)
                        hashtag=str(input(f"[::] Please enter again the hashtag No{i+1}: "))
                    HASHTAGS.append(hashtag)
                    sleep(1)
                    print("[!] Hashtag added successfully !")
            else:
                print("[OK]")
                sleep(1)
                pass
            if AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,links=LINKS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,locations=LOCATIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,links=LINKS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=AddLinks)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,locations=LOCATIONS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,mentions=MENTIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,locations=LOCATIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,links=LINKS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,mentions=MENTIONS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash == None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,locations=LOCATIONS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
                if current_time == __time__:
                    try:
                        client.photo_upload_to_story(path,links=LINKS,hashtags=HASHTAGS)
                        sleep(5)
                        print("[!] Story uploaded successfully !")
                        quit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass

        elif action == 4:
            caption = None
            hashtag = None
            location = None
            path=str(input("[::] Please enter the path to the video: "))
            while path == None or "/" not in path and "\\" not in path:
                print("[!] Invalid path !")
                sleep(1)
                path=str(input("[::] Please enter again the path to the video: "))
            incap=str(input("[?] Do you want to include caption ? [yes/no] "))
            while incap not in ANS and incap not in NANS or incap == None:
                print("[!] Invalid input !")
                sleep(1)
                incap=str(input("[?] Do you want to include caption ? [yes/no] "))
            if incap in ANS:
                sleep(1)
                print("[+] Default Caption: Check out my new video !")
                sleep(2)
                print("[+] Hit <Tab> and <Enter> to apply the default option")
                sleep(2)
                caption=str(input("[::] Please enter the caption: "))
                if caption == "\t":
                    caption = "Check out my new video !"
                else:
                    print("[OK]")
                    pass
            intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
            while intag not in ANS and intag not in NANS or intag == None:
                print("[!] Invalid input !")
                sleep(1)
                intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
            if intag in ANS:
                count=int(input("[?] How many ? (enter a number) "))
                while count == None or count <= 0:
                    print("[!] Invalid number !")
                    sleep(1)
                    count=int(input("[?] How many hashtags to include ? (enter a number) "))
                for i in range(count):
                    hashtag=str(input(f"[::] Please enter the hashtag No{i+1} : "))
                    while hashtag == None or "#" not in hashtag:
                        print("[!] Invalid hashtag !")
                        sleep(2)
                        print("[+] You have to include the   #   sign !")
                        sleep(2)
                        hashtag=str(input(f"[::] Please enter again hashtag No{i+1}: "))
                    HASHVID.append(hashtag)
                    sleep(1)
                    print("[!] Hashtag added successfully !")
            else:
                print("[OK]")
                sleep(1)
                pass
            inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
            while inloc not in ANS and inloc not in NANS or inloc == None:
                print("[!] Invalid location !")
                sleep(1)
                inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
            if inloc in ANS:
                count=int(input("[?] How many ? (enter a number) "))
                while count == None or count <= 0:
                    print("[!] Invalid number !")
                    sleep(1)
                    count=int(input("[?] How many locations to include ? (enter a number) "))
                for i in range(count):
                    location=str(input(f"[::] Please enter location No{i+1} : "))
                    while location == None:
                        print("[!] Invalid location !")
                        sleep(1)
                        location=str(input(f"[::] Please enter again location No{i+1}: "))
            else:
                print("[OK]")
                pass
            if current_time == __time__:
                try:
                    client.video_upload(path,caption,usertags=HASHVID,location=location)
                    sleep(5)
                    print("[!] Video uploaded successfully !")
                    quit(0)
                except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
            else:
                print("[+] Current time: "+str(current_time))
                sleep(1)
                print("[+] Waiting for the time: "+str(__time__))
                pass

        elif action == 5:
            count=int(input("[?] How many accounts do you want to follow ? (enter a number) "))
            while count == None or count <= 0:
                print("[!] Invalid number !")
                sleep(1)
                count=int(input("[?] How many accounts do you want to follow ? (enter a number) "))
            if count == 1:
                username=str(input("[::] Please enter the username: "))
                while checkUser(username) == True:
                    print("[!] Invalid username !")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
                username.lower()
                username.strip()
                print(GetID(username))
                uid=int(input("[::] Please enter the user's ID as shown above: "))
                while checkID(uid) == True:
                    print("[!] Invalid ID !")
                    sleep(1)
                    uid=int(input("[::] Please enter again the user's ID as shown above: "))
                if current_time == __time__:
                    try:
                        client.user_follow(uid)
                        sleep(3)
                        print(f"[!] Successfully followed {username} !")
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            else:
                for i in range(count):
                    username=str(input(f"[::] Please enter the username No{i+1}: "))
                    while checkUser(username) == True:
                        print("[!] Invalid username !")
                        sleep(1)
                        username=str(input(f"[::] Please enter again username No{i+1}: "))
                    username.lower()
                    username.strip()
                    print(GetID(username))
                    id=int(input("[::] Please enter the user's ID as shown above: "))
                    while checkID(id) == True:
                        print("[!] Invalid ID !")
                        sleep(1)
                        uid=int(input("[::] Please enter again the user's ID as shown above: "))
                    if current_time == __time__:
                        try:
                            client.user_follow(id)
                            sleep(3)
                            print(f"[!] Successfully followed {username} !")
                        except Exception as ex:
                            print(f"[!] Can't follow {username} !")
                            sleep(2)
                            print(f"[+] Reason -> {ex}")
                    else:
                        print("[+] Current time: "+str(current_time))
                        sleep(1)
                        print("[+] Waiting for the time: "+str(__time__))
                        pass

        elif action == 6:
            if current_time == __time__:
                count=int(input("[?] How many accounts do you want to unfollow ? (enter a number) "))
                while count == None or count <= 0:
                    print("[!] Invalid number !")
                    sleep(1)
                    count=int(input("[?] How many accounts do you want to unfollow ? (enter a number) "))
                if count == 1: 
                    username=str(input("[::] Please enter the username: "))
                    while checkUser(username) == True:
                        print("[!] Invalid username !")
                        sleep(1)
                        username=str(input("[::] Please enter again the username: "))
                    username.lower()
                    username.strip()
                    print(GetID(username))
                    uid=int(input("[::] Please enter the user's ID as shown above: "))
                    while checkID(uid) == True:
                        print("[!] Invalid ID !")
                        sleep(1)
                        uid=int(input("[::] Please enter again the user's ID as shown above: "))
                    try:
                        client.user_unfollow(uid)
                        sleep(3)
                        print(f"[!] Successfully unfollowed {username} !")
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        quit(0)
                else:
                    for i in range(count):
                        username=str(input(f"[::] Please enter the username No{i+1}: "))
                        while checkUser(username) == True:
                            print("[!] Invalid username !")
                            sleep(1)
                            username=str(input("[::] Please enter again the username: "))
                        username.lower()
                        username.strip()
                        try:
                            client.user_unfollow(uid)
                            sleep(3)
                            print(f"[!] Successfully unfollowed {username} !")
                        except Exception as e:
                            print(f"[!] Can't unfollow {username} !")
                            pass
            else:
                print("[+] Current time: "+str(current_time))
                sleep(1)
                print("[+] Waiting for the time: "+str(__time__))
                sleep(1)
                pass

    elif option == 56:
        user=str(input("[::] Please enter the username: "))
        while checkUser(user) == True:
            print("[!] Invalid username !")
            sleep(1)
            user=str(input("[::] Please enter again the username: "))
        print(GetID(user))
        id=int(input("[::] Please enter the user's ID as shown above: "))
        while checkID(id) == True:
            print("[!] Invalid ID !")
            sleep(1)
            id=int(input("[::] Please enter again the user's ID as shown above: "))
        try:
            api.block_friend_reel(id)
            sleep(3)
            print("[!] Successfully blocked user from watching your stories")
            quit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(3)
            print("[+] Exiting...")
            quit(0)
if __name__ == '__main__':
    main()
