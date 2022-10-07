"""
Author: new92
Github: @new92
[-->] Program for Managing your Instagram Account Remotely
IAM: Instagram Account Manager
User's data (such as username password) will not be stored or saved ! 
Will be used only for some functions of the program.
"""

#Imports

try:
    import platform
    import sys
    from time import sleep
    from os import system



    import instagrapi
    import instaloader
    import instapy
    import instabot
    import instagram_private_api
    import webbrowser
    import requests as re
    import json as js
    import os
    import art
    import keyboard as kb



    from art import tprint
    from datetime import datetime
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from tkinter import *



except ImportError as imp:
    print("[!] WARNING: Not all modules used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring Warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        system("sudo pip3 install -r requirements.txt")
        pass
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
        pass
    elif sys.platform == 'win32':
        system("python -m pip install requirements.txt")
        pass

#Displaying Logo

tprint("IAM", font="tarty1")

#Defs

def Get_Hpk(link):
    pk = client.highlight_pk_from_url(link)
    return pk

def Get_Spk(link):
    pk = client.story_pk_from_url(link)
    return pk

def Av_Acts():
    actions = """
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
    return actions

def ProgInfo():
    __version__ = "1.0"
    __author__ = "new92"
    __license__ = "MIT"
    __name__ = "IAM"
    __contributors__ = None
    __programmedwith__ = "Python"
    __language__ = "English - en"
    print("[+] Version ==> "+str(__version__))
    print("[+] Author ==> "+str(__author__))
    print("[+] License ==> "+str(__license__))
    print("[+] Program's name ==> "+str(__name__))
    print("[+] Contributors ==> "+str(__contributors__)+" so far... :)")
    print("[+] Programmed with ==> "+str(__programmedwith__))
    print("[+] Language ==> "+str(__language__))

#Lists

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

#Main Program

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
print("[99] Show program info and exit")
print("\n")
print("[0] Exit") 
print("\n")
option=int(input("[::] Choose an option: "))
while option < 0 or option > 55 and option != 99 or option == None:
    print("[!] Invalid option !")
    sleep(2)
    option=int(input("[::] Please enter again: "))
loader=instaloader.Instaloader()
client=instagrapi.Client()
bot = instabot.Bot()
if option != 99:
    print("\n")
    print("|--------------------|LOGIN|--------------------|")
    print("\n")
    username=str(input("[::] Please enter your username: "))
    while username == None or len(username) > 30:
        print("[!] Sorry invalid username !")
        sleep(2)
        username=str(input("[::] Please enter again your username: "))

    if username.islower() == False:
        username = username.lower()
        username = username.strip()
        pass
    else:
        username = username.strip()
        pass
    password=input("[::] Please enter your password: ")
    while password == None:
        print("[!] Sorry, invalid password !")
        sleep(2)
        password=input("[::] Please enter again your password: ")
    password = password.strip()
    try:
        loginl = loader.login(username,password)
        loginc = client.login(username,password,True)
        logini = instapy.InstaPy(username,password)
        api = instagram_private_api.Client(username,password)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)
else:
    pass

if option == 0:
    print("[+] Exiting...")
    exit(0)

elif option == 99:
    ProgInfo()
    exit(0)

elif option == 1:
    try:
        id=loader.check_profile_id(username)
        print("[+] Your ID: ")
        print("\n")
        sleep(1)
        print(id)
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 2:
    try:
        sec_info=client.account_security_info()
        print("[+] Your security information: ")
        print("\n")
        sleep(1)
        print(sec_info)
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 3:
    try:
        AccInfo=client.account_info()
        print("[+] Your account information: ")
        print("\n")
        sleep(1)
        print(AccInfo)
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 4:
    try:
        req_sts = api.friendships_pending()
        sleep(1)
        print(req_sts)
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 5:
    prof_id=loader.check_profile_id(username)
    id=int(input("[::] Please enter your id as shown above: "))
    while id == None:
        print("[!] Invalid ID !")
        sleep(1)
        id=int(input("[::] Please enter again your ID as shown above: "))
    try:
        followers=client.user_followers(id)
        sleep(3)
        print("[!] Request successful !")
        print(followers)
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 6:
    uid=loader.check_profile_id(username)
    id=int(input("[::] Please enter your id (as shown above): "))
    while id == None or len(id) < 3:
        print("[!] Invalid ID !")
        sleep(1)
        id1=input("[::] Please enter again your id (as shown above): ")
    try:
        following=client.user_following(id)
        sleep(3)
        print("[!] Request successful !")
        print(following)
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 7:
    uid = loader.check_profile_id(username)
    id=int(input("[::] Please enter your id as shown above: "))
    while id == None or len(id) < 3:
        print("[!] Invalid ID !")
        sleep(1)
        id=int(input("[::] Please enter again your id as shown above: "))
    try:
        highlights=loader.download_highlights(id)
        sleep(3)
        print("[+] Highlights have been saved in a file in the current folder with the name --> "+str(username))
        sleep(3)
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 8:
    count=int(input("[+] Number of accounts (to get their stories): "))
    while count == None or count <= 0:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please enter the number of accounts (to get their stories): "))
    for i in range(count):
        username=str(input("[::] Please enter the username: "))
        while username == None or len(username) > 30:
            print("[!] Invalid Username !")
            sleep(1)
            username=input("[::] Please enter again the username: ")
        user_id=loader.check_profile_id(username)
        id=int(input("[::] Please enter the ID as shown above: "))
        while id == None or len(id) < 3:
            print("[!] Invalid ID !")
            sleep(1)
            usid=int(input("[::] Please enter again the ID as shown above: "))
        IDS.append(user_id)
    try:
        stories=loader.download_stories(IDS)
        sleep(3)
        print("\n [+] A folder in the current folder has been created with the name --> :stories   containing the stories of the given users")
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 9:
    count=int(input("[?] How many of your saved posts do you want to download ?: "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[?] How many of your saved posts do you want to download ?: "))
    try:
        saved_posts=loader.download_saved_posts(count)
        print("\n [+] A folder in the current directory has been created with the name --> :saved   containing "+str(count)+" posts of your saved posts")
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 10:
    count=int(input("[?] How many posts do you want to download ? "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[?] How many posts do you want to download ? "))
    try:
        posts=loader.download_feed_posts(count)
        print("[+] Feed Posts have been saved in a file in the current folder with the name --> :feed")
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 11:
    count=int(input("[::] Please enter the number of posts to post: "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please enter again the number of posts to post: "))
    for i in range(count):
        path=input("[::] Please enter the path of the file which contains the photo to be uploaded: ")
        while (path == None) or ("/" not in path):
            print("[!] Invalid Path !")
            sleep(1)
            path=input("[::] Please enter again the path of the file which contains the photo to be uploaded: ")
        sleep(2)
        print(">>>CAPTION<<<")
        sleep(1)
        print("[+] Default: Check out my new post !")
        sleep(2)
        print("[+] Hit <Enter> for the default option to be applied")
        sleep(2)
        caption=str(input("[::] Please enter the caption: "))
        if caption == None:
            caption = "New Post !"
        print(">>>TAGS<<<")
        sleep(2)
        print("[+] Default: [no]")
        sleep(2)
        print("[+] Hit <Space> and <Enter> to Apply the Default Option")
        sleep(2)
        tags=input("[?] Do you want to include other users to your post by tagging them ? [yes/no] ")
        while (tags != "yes" and tags != "YES" and tags != "no" and tags != "NO") or (tags == None):
            print("[!] Invalid Input !")
            sleep(1)
            tags=input("[?] Do you want to include other users to your post by tagging them ? [yes/no] ")
        if tags == "yes" or tags == "YES":
            print("[+] Default: 1")
            sleep(2)
            print("[+] Hit <Space> and <Enter> to Apply the Default Option")
            count=int(input("[?] How many users do you want to include ? "))
            while count <= 0 or count == None:
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[?] How many users do you want to tag ? "))
            utag=input("[::] Please enter the username: ")
            while utag == None or len(utag) > 30:
                print("[!] Invalid username !")
                sleep(1)
                utag=input("[::] Please enter again the username: ")
            utag = utag.strip()
            utag = utag.lower()
            TaggedUsers.append(utag)
            for i in range(1,count+1):
                utag=input("[::] Please enter the username No{}: ".format(i))
                while utag == None or len(utag) > 30:
                    print("[!] Invalid username !")
                    sleep(1)
                    utag=input("[::] Please enter again the username No{}: ".format(i))
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
        print("[+] Hit <Enter> to Apply the Default Option")
        sleep(2)
        loc=input("[?] Do you want to include location(s) ? [yes/no] ")
        while (loc != "yes" and loc != "YES" and loc != "no" and loc != "NO") or (loc == None):
            print("[!] Invalid Input !")
            sleep(1)
            loc=input("[?] Do you want to include location(s) ? [yes/no] ")
        if loc == "Y" or loc == "y":
            count=int(input("[?] How many ? "))
            while count <= 0 or count == None:
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[?] How many locations do you want to include ? "))
            for i in range(1,count+1):
               location1=input("[::] Please enter location No"+str(i)+": ")
               LOCATIONS.append(location1)
               print("[!] Location Added Successfully !")
            try:
                client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                sleep(2)
                print("[!] Photo Uploaded Successfully !")
                exit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)
        else:
            print("[OK]")
            pass
        if (tags == "yes" or tags == "YES") and (loc == "yes" or loc == "YES"):
            try:
                client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                print("[!] Photo Uploaded Successfully !")
                exit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)
        elif (tags == "yes" or tags == "YES") and (loc == "no" or loc == "NO"):
            try:
                client.photo_upload(path=path,caption=caption,tags=TaggedUsers)
                print("[!] Photo Uploaded Successfully !")
                exit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)
        elif (tags == "no" or tags == "NO") and (loc == "yes" or loc == "YES"):
            try:
                client.photo_upload(path=path,caption=caption,location=LOCATIONS)
                print("[!] Photo Uploaded Successfully !")
                exit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)
        elif (tags == "no" or tags == "NO" and loc == "no" or loc == "NO"):
            try:
                client.photo_upload(path=path,caption=caption)
                print("[!] Photo Uploaded Successfully !")
                exit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)

elif option == 12:
    username=str(input("[::] Please enter your username: "))
    while username == None or len(username) > 30:
        print("[!] Invalid username !")
        sleep(2)
        username=str(input("[::] Please enter again the username: "))
        username=username.lower()
        username=username.strip()
    endis=input("[?] Do you want to enable or disable your notifications ? [enable/disable] ")
    while (endis != "enable" and endis != "ENABLE" and endis != "disable" and endis != "DISABLE") or (endis == None):
        print("[!] Invalid option !")
        sleep(1)
        endis=input("[?] Do you want to enable or disable your notifications ? [enable/disable] ")
    if endis == "enable" or endis == "ENABLE":
        username=str(input("[::] Please enter your username: "))
        while username == None or len(username) > 30:
            print("[!] Invalid username !")
            sleep(1)
            username=str(input("[::] Please enter again your username: "))
        username=username.lower()
        username=username.strip()
        print("[+] Notifications available for: [posts/reels/stories/videos]")
        sleep(2)
        action=input("[?] Which notifications do you want to enable ?")
        while (action != "posts" and action != "POSTS" and action != "reels" and action != "REELS" and action != "stories" and action != "STORIES" and action != "videos" and action != "VIDEOS") or (action == None):
            print("[!] Invalid Notification !")
            sleep(1)
            print("[+] Notifications available for: [posts/reels/stories/videos]")
            sleep(2)
            action=input("[?] Please enter again the notifications to enable: ")
        if action == "posts" or action == "POSTS":
            username=input("[::] Please enter your username: ")
            while username == None or len(username) > 30:
                print("[!] Invalid Username !")
                sleep(1)
                username=input("[::] Please enter again your username: ")
            username_id = loader.check_profile_id(user)
            uid=int(input("[::] Please enter the ID as shown above: "))
            while uid == None or uid <= 0:
                print("[!] Invalid ID !")
                sleep(1)
                uid=int(input("[::] Please enter again the ID as shown above: "))
            try:
                client.enable_posts_notifications(uid)
                sleep(3)
                print("[!] Posts Notifications for user {} Enabled !".format(username))
                exit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)
        elif action == "reels" or action == "REELS":
            username=input("[::] Please enter your username: ")
            while username == None or len(username) > 30:
                    print("[!] Invalid Username !")
                    sleep(1)
                    username=input("[::] Please enter again your username: ")
            username_id = loader.check_profile_id(username)
            uid=int(input("[::] Please enter the ID as shown above: "))
            while uid == None or uid <= 0:
                print("[!] Invalid ID !")
                sleep(1)
                uid=int(input("[::] Please enter again the ID as shown above: "))
            try:
                client.enable_reels_notifications(uid)
                sleep(3)
                print("[!] Reels Notifications for user {} Enabled !".format(username))
                exit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)
        elif action == "stories" or action == "STORIES":
            username=str(input("[::] Please enter your username: "))
            while username == None or len(username) > 30:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again your username: "))
            username_id = loader.check_profile_id(username)
            uid=int(input("[::] Please enter the ID as shown above: "))
            while uid == None:
                    print("[!] Invalid ID !")
                    sleep(1)
                    uid=int(input("[::] Please enter again the ID as shown above: "))
            try:
                client.enable_stories_notifications(uid)
                print("[!] Stories Notifications for user {} Enabled !".format(username))
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)
        else:
            username=str(input("[::] Please enter the username: "))
            while username == None or len(username) > 30:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            username_id = loader.check_profile_id(username)
            uid0=int(input("[::] Please enter the ID as shown above: "))
            while uid == None or uid <= 0:
                print("[!] Invalid ID !")
                sleep(1)
                uid=int(input("[::] Please enter again the ID as shown above: "))
            try:
                client.enable_videos_notifications(uid)
                sleep(3)
                print("[!] Videos Notifications for user {} Enabled !".format(username))
                exit(0)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)

elif option == 13:
    path=input("[::] Please enter the full path of the folder which contains your new profile pic: ")
    while (path == None) or ("/" not in path):
        print("[!] Invalid Path !")
        sleep(1)
        path=input("[::] Please enter again the full path of the folder which contains your new profile pic: ")
    try:
        client.account_change_picture(path)
        sleep(3)
        print("[!] Your profile picture changed successfully !")
        exit(0)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 14:
    path=input("[::] Please enter the path of the file which contains the photo to be uploaded: ")
    while (path == None) or ("/" not in path):
        print("[!] Invalid Path !")
        sleep(1)
        path=input("[::] Please enter again the path of the file which contains the photo to be uploaded: ")
    AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
    while (AddCaption != "yes" and AddCaption != "YES" and AddCaption != "no" and AddCaption != "NO") or (AddCaption == None):
        print("[!] Invalid Input !")
        sleep(1)
        AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
    if AddCaption == "yes" or AddCaption =="YES":
        print("[+] Default: Check out my new story !")
        sleep(2)
        print("[+] Hit <Enter> for the default option to be applied")
        sleep(2)
        caption=str(input("[::] Please enter the caption: "))
        if caption == None:
            caption = "Check out my new story !"
            pass
        else:
            caption=str(input("[::] Please enter a caption to include to the story: "))
            while caption == None:
                print("[!] Invalid Caption !")
                sleep(1)
                caption=str(input("[::] Please enter again a caption to include to the story: "))
    else:
        print("[OK]")
        sleep(1)
        pass
    AddMention=str(input("[?] Do you want to add mention ? [yes/no] "))
    while (AddMention != "yes" and AddMention != "YES" and AddMention != "no" and AddMention != "NO") or (AddMention == None):
        print("[!] Invalid Mention !")
        sleep(1)
        mention=str(input("[?] Do you want to mention user(s) ? [yes/no] "))
    if AddMention == "yes" or AddMention == "YES":
        MENTIONS = []
        count=int(input("[?] How many ? "))
        while count <= 0 or count == None:
            print("[!] Invalid Input !")
            sleep(1)
            count=int(input("[?] How many ? "))
        for i in range(1,count+1):
            mention=str(input("[::] Please enter the username No{}: ".format(i)))
            while mention == None or len(mention) > 30:
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
    while (AddLoc != "yes" and AddLoc != "YES" and AddLoc != "no" and AddLoc != "NO") or (AddLoc == None):
        print("[!] Invalid Input !")
        sleep(1)
        AddLoc=str(input("[?] Do you want to add location ? [yes/no] "))
    if AddLoc == "yes" or AddLoc == "YES":
        count=int(input("[?] How many locations do you want to add ? "))
        while count <= 0 or count == None :
            print("[!] Invalid Number !")
            sleep(1)
            count=int(input("[?] How many locations do you want to add ? "))
        for i in range(1,count+1):
            loc=str(input("[::] Please enter location No{}: ".format(i)))
            while loc == None:
                print("[!] Invalid Location !")
                sleep(1)
                loc=str(input("[::] Please enter again location No{}: ".format(i)))
            LOCATIONS.append(loc)
            sleep(1)
            print("[!] Location added successfully !")
    else:
        print("[OK]")
        sleep(1)
        pass
    AddLinks=str(input("[?] Do you want to include links ? [yes/no] "))
    while (AddLinks != "yes" and AddLinks != "YES" and AddLinks != "no" and AddLinks != "NO") or (AddLinks == None):
        print("[!] Invalid Input !")
        sleep(1)
        AddLinks=str(input("[?] Do you want to include links ? [yes/no] "))
    if AddLinks == "yes" or AddLinks == "YES":
        count=int(input("[?] How many ? "))
        while count <= 0 or count == None:
            print("[!] Invalid Number !")
            sleep(1)
            count=int(input("[?] How many links do you want to include ? "))
        for i in range(1,count+1):
            link=str(input("[::] Please enter the link No{}: ".format(i)))
            while (link == None) or ("//" not in link):
                print("[!] Invalid Link !")
                sleep(1)
                link=str(input("[::] Please enter again the link No{}: ".format(i)))
            LINKS.append(link)
            sleep(1)
            print("[!] Link added successfully !")
    else:
        print("[OK]")
        sleep(1)
        pass
    AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
    while (AddHash != "yes" and AddHash != "YES" and AddHash != "no" and AddHash != "NO") or (AddHash == None):
        print("[!] Invalid Input !")
        sleep(1)
        AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
    if AddHash == "yes" or AddHash == "YES":
        count=int(input("[?] How many ? "))
        while  count <= 0 or count == None :
            print("[!] Invalid Number !")
            sleep(1)
            count=int(input("[?] How many hashtags do you want to include ? "))
        for i in range(1,count+1):
            hashtag=str(input("[::] Please enter the hashtag No{}: ".format(i)))
            while (hashtag == None) or ("#" not in hashtag):
                print("[!] Invalid Hashtag !")
                sleep(1)
                hashtag=str(input("[::] Please enter again the hashtag No{}: ".format(i)))
            HASHTAGS.append(hashtag)
            sleep(1)
            print("[!] Hashtag added successfully !")
    else:
        print("[OK]")
        sleep(1)
        pass
    if AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
        try:
            client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
        try:
            client.photo_upload_to_story(path,caption,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks != None and AddHash != None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,links=LINKS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash != None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash != None:
        try:
            client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
        try:
            client.photo_upload_to_story(path,caption,links=LINKS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,mentions=MENTIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,locations=LOCATIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
        try:
            client.photo_upload_to_story(path,links=LINKS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
        try:
            client.photo_upload_to_story(path,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=AddLinks)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
        try:
            client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
        try:
            client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
        try:
            client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
        try:
            client.photo_upload_to_story(path,caption,locations=LOCATIONS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc != None and AddLinks != None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS,locations=LOCATIONS,links=LINKS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks != None and AddHash != None:
        try:
            client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS,links=LINKS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention != None and AddLoc == None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,mentions=MENTIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention == None and AddLoc != None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,locations=LOCATIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks != None and AddHash == None:
        try:
            client.photo_upload_to_story(path,caption,links=LINKS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption != None and AddMention == None and AddLoc == None and AddLinks == None and AddHash != None:
        try:
            client.photo_upload_to_story(path,caption,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention != None and AddLoc != None and AddLinks == None and AddHash == None:
        try:
            client.photo_upload_to_story(path,mentions=MENTIONS,locations=LOCATIONS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks != None and AddHash == None:
        try:
            client.photo_upload_to_story(path,mentions=MENTIONS,links=LINKS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention != None and AddLoc == None and AddLinks == None and AddHash != None:
        try:
            client.photo_upload_to_story(path,mentions=MENTIONS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks != None and AddHash == None:
        try:
            client.photo_upload_to_story(path,locations=LOCATIONS,links=LINKS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention == None and AddLoc != None and AddLinks == None and AddHash != None:
        try:
            client.photo_upload_to_story(path,locations=LOCATIONS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    elif AddCaption == None and AddMention == None and AddLoc == None and AddLinks != None and AddHash != None:
        try:
            client.photo_upload_to_story(path,links=LINKS,hashtags=HASHTAGS)
            sleep(5)
            print("[!] Story uploaded successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)

elif option == 15:
    caption = None
    hashtag = None
    location = None
    path=input("[::] Please enter the path of the folder which contains the video: ")
    while (path == None) or ("/" not in path):
        print("[!] Invalid Path !")
        sleep(1)
        path=input("[::] Please enter again the path of the folder which contains the video: ")
    incap=str(input("[?] Do you want to include caption ? [yes/no] "))
    while (incap != "yes" and incap != "YES" and incap != "no" and incap != "NO") or (incap == None):
        print("[!] Invalid Input !")
        sleep(1)
        incap=str(input("[?] Do you want to include caption ? [yes/no] "))
    if incap == "yes" or incap == "YES":
        sleep(1)
        print("[+] Default Caption: Check out my new video !")
        sleep(2)
        print("[+] To apply the default caption hit: <Enter>")
        sleep(2)
        caption=str(input("[::] Please enter the caption: "))
        if caption == None:
            caption = "Check out my new video !"
            pass
        else:
            pass
    intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
    while (intag != "yes" and intag != "YES" and intag != "no" and intag != "NO") or (intag == None):
        print("[!] Invalid Input !")
        sleep(1)
        intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
    if intag == "yes" or intag == "YES":
        count=int(input("[?] How many ? "))
        while count <= 0 or count == None:
            print("[!] Invalid Number !")
            sleep(1)
            count=int(input("[?] How many hashtags to include ? "))
        for i in range(1,count+1):
            hashtag=str(input("[::] Please enter the hashtag No{} : ".format(i)))
            while (hashtag == None) or ("#" not in hashtag):
                print("[!] Invalid Hashtag !")
                sleep(2)
                print("[+] You have to include #")
                sleep(2)
                hashtag=str(input("[::] Please enter again hashtag No{} : ".format(i)))
            HASHVID.append(hashtag)
            sleep(1)
            print("[!] Hashtag added successfully !")
    else:
        print("[OK]")
        sleep(1)
        pass
    inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
    while (incloc != "yes" and inloc != "YES" and inloc != "no" and inloc != "NO") or (inloc == None):
        print("[!] Invalid Location !")
        sleep(1)
        inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
    if inloc == "yes" or inloc == "YES":
        count=int(input("[?] How many ? "))
        while count <= 0 or count == None:
            print("[!] Invalid Number !")
            sleep(1)
            count=int(input("[?] How many locations to include ? "))
        for i in range(1,count+1):
            location=str(input("[::] Please enter location No{} : ".format(i)))
            while location == None:
                print("[!] Invalid Location !")
                sleep(1)
                location=str(input("[::] Please enter again location No{} : ".format(i)))
    else:
        print("[OK]")
        sleep(1)
        pass
    try:
        client.video_upload(path,caption,usertags=HASHVID,location=location)
        sleep(5)
        print("[!] Video uploaded successfully !")
        exit(0)
    except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)

elif option == 16:
    count=int(input("[?] How many accounts do you want to follow ? "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[?] How many accounts do you want to follow ? "))
    if count == 1:
        username=str(input("[::] Please enter the username: "))
        while username == None or len(username) > 30:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        username.lower()
        username.strip()
        user_id = loader.check_profile_id(username)
        uid=int(input("[::] Please enter the user's ID as shown above: "))
        while uid == None or uid <= 0:
            print("[!] Invalid ID")
            sleep(1)
            uid=int(input("[::] Please enter again the user's ID as shown above: "))
        try:
            client.user_follow(uid)
            sleep(3)
            print("[!] Successfully followed {} !".format(username))
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    else:
        for i in range(1,count+1):
            username=str(input("[::] Please enter the username No{} :".format(i)))
            while username == None or len(username) > 30:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again username No{} : ".format(i)))
            username.lower()
            username.strip()
            uid=loader.check_profile_id(username)
            id=int(input("[::] Please enter the user's ID as shown above: "))
            while id == None or len(id) < 3:
                print("[!] Invalid ID !")
                sleep(1)
                uid=int(input("[::] Please enter again the user's ID as shown above: "))
            try:
                client.user_follow(id)
                sleep(3)
                print("[!] Successfully followed {} !".format(username))
            except Exception as ex:
                print("[!] Can't follow {} !".format(username))

elif option == 17:
    count=int(input("[?] How many accounts do you want to unfollow ? "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[?] How many accounts do you want to unfollow ? "))
    if count == 1: 
        username=str(input("[::] Please enter the username: "))
        while username == None or len(username) > 30:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        username.lower()
        username.strip()
        user_id = loader.check_profile_id(username)
        uid=int(input("[::] Please enter the user's ID as shown above: "))
        while uid == None or uid <= None:
            print("[!] Invalid ID !")
            sleep(1)
            uid=int(input("[::] Please enter again the user's ID as shown above: "))
        try:
            client.user_unfollow(uid)
            sleep(3)
            print("[!] Successfully unfollowed {} !".format(username))
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    else:
        for i in range(count):
            username=str(input("[::] Please enter the username: "))
            while username == None or len(username) > 30:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            username.lower()
            username.strip()
            try:
                client.user_unfollow(uid)
                sleep(3)
                print("[!] Successfully unfollowed {} !".format(username))
            except Exception as e:
                print("[!] Can't unfollow {} !".format(username))
                pass

elif option == 18:
    count=int(input("[::] Please enter the number of the follow requests to accept: "))
    while count == None or count <= 0:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please enter again the number of the follow requests to accept: "))
    try:
        logini.accept_follow_requests(count,3)
        sleep(7)
        print("[!] Follow Requests Accepted !")
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 19:
    count=int(input("[::] Please enter the number of the follow requests to remove: "))
    while count == None or count <= 0:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please enter again the number of the follow requests to remove: "))
    try:
        logini.remove_follow_requests(count,3)
        sleep(7)
        print("[!] Follow Requests Removed !")
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 20:
    count=int(input("[::] Please enter the amount of users to follow:  "))
    while count == None:
        print("[!] Invalid Number !")
        sleep(2)
        count=int(input("[::] Please enter again the amount of users to follow: "))
    countu=int(input("[?] From how many users do you want to follow their followers ? "))
    while countu <= 0 or countu == None:
        print("[!] Invalid Number !")
        sleep(1)
        countu=int(input("[?] From how many users do you want to follow their followers ? "))
    for i in range(countu):
        username=str(input("[::] Please enter the username of the user (to follow their followers): "))
        while username == None or len(username) > 30:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        FUFERS.append(username)
    try:
        logini.follow_user_followers(FUFERS,count)
        sleep(7)
        print("[!] Successfully Followed Users !")
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 21:
    count=int(input("[::] Please enter the amount of users to follow: "))
    while count == None:
        print("[!] Invalid Number !")
        sleep(2)
        count=int(input("[::] Please enter again the amount of users to follow: "))
    countu=int(input("[?] From how many users do you want to follow their followings ? "))
    while countu <= 0 or countu == None:
        print("[!] Invalid Number !")
        sleep(1)
        countu=int(input("[?] From how many users do you want to follow their followings ? "))
    for i in range(countu):
        username=str(input("[::] Please enter the username of the user: "))
        while username == None or len(username) > 30:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        FUFING.append(username)
    browser = webdriver.Firefox()
    for i in range(len(FUFING)):
        browser.get("https://www.instagram.com/{}/following/".format(username))
        for j in range(count):
            try:
                follow = browser.find_element_by_class_name("_acan _acap _acas")
                follow.click()
                print("[+] User followed !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)

elif option == 22:
    count=int(input("[?] How many messages do you want to send ? "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[?] How many messages do you want to send ? "))
    for i in range(1,count+1):
        text=str(input("[::] Please enter the text to send: "))
        while text == None:
            print("[!] Invalid Text !")
            sleep(1)
            text=str(input("[::] Please enter again the text to send: "))
        count=int(input("[?] In how many users do you want to send it ? "))
        while count <= 0 or count == None:
            print("[!] Invalid Number !")
            sleep(1)
            count=int(input("[?] In how many users do you want to send it ? "))
        for i in range(1,count+1):
            username=str(input("[::] Please enter the username No{} : ".format(i)))
            while username == None or len(username) > 30:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again the username No{} : ".format(i)))
            loader.check_profile_id(username)
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while id == None or len(id) < 3:
                print("[!] Invalid ID !")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            MSGIDS.append(id)
            try:
                client.direct_send(text,MSGIDS)
                sleep(1)
                print("[!] Message Sent Successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)

elif option == 23:
    path=str(input("[::] Please enter the path of the folder which contains the file: "))
    while (path == None) or ("/" not in path):
        print("[!] Invalid Path !")
        sleep(1)
        path=str(input("[::] Please enter again the path of the folder which contains the file: "))
    count=int(input("[?] In how many users do you want to send it ? "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[?] In how many users do you want to send it ? "))
    for i in range(1,count+1):
        username=str(input("[::] Please enter the username No{} : ".format(i)))
        while username == None or len(username) > 30:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username No{} : ".format(i)))
        loader.check_profile_id(username)
        id=int(input("[::] Please enter the ID of the user as shown above: "))
        while id == None or len(id) < 3:
            print("[!] Invalid ID !")
            sleep(1)
            id=int(input("[::] Please enter again the ID of the user as shown above: "))
        FILEIDS.append(id)
        try:
            client.direct_send_file(path,FILEIDS)
            sleep(2)
            print("[!] File Sent Successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)

elif option == 24:
    path=input("[::] Please enter the path of the folder which contains the photo: ")
    while (path == None) or ("/" not in path):
        print("[!] Invalid Path !")
        sleep(1)
        path=input("[::] Please enter again the path of the folder which contains the photo: ")
    count=int(input("[?] In how many users do you want to send it ? "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[?] In how many users do you want to send it ? "))
    for i in range(1,count+1):
        username=str(input("[::] Please enter the username No{} : ".format(i)))
        while username == None or len(username) > 30:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username No{} : ".format(i)))
        loader.check_profile_id(username)
        id=int(input("[::] Please enter the ID of the user as shown above: "))
        while id == None or len(id) < 3:
            print("[!] Invalid ID !")
            sleep(1)
            id=int(input("[::] Please enter again the ID of the user as shown above: "))
        PHOTOIDS.append(id)
        try:
            client.direct_send_photo(path,PHOTOIDS)
            sleep(2)
            print("[!] Photo Sent Successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)

elif option == 25:
    path=input("[::] Please enter the path of the folder which contains the video: ")
    while (path == None) or ("/" not in path):
        print("[!] Invalid Path !")
        sleep(1)
        path=input("[::] Please enter again the path of the folder which contains the video: ")
    count=int(input("[?] In how many users do you want to send it ? "))
    while count == None or count <= 0:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[?] In how many users do you want to send it ? "))
    for i in range(1,count+1):
        username=str(input("[::] Please enter the username No{} : ".format(i)))
        while username == None:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username No{} : ".format(i)))
        loader.check_profile_id(username)
        id=int(input("[::] Please enter the ID of the user as shown above: "))
        while id == None or len(id) < 3:
            print("[!] Invalid ID !")
            sleep(1)
            id=int(input("[::] Please enter again the ID of the user as shown above: "))
        VIDEOIDS.append(id)
        try:
            client.direct_send_video(path,VIDEOIDS)
            sleep(2)
            print("[!] Video Sent Successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)

elif option == 26:
    count=int(input("[::] Please enter the number of hashtags to like their posts: "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please enter again the number of hashtags to like their posts: "))
    nump=int(input("[::] Please enter the number of the posts to like: "))
    while nump <= 0 or nump == None:
        print("[!] Invalid Number !")
        sleep(1)
        nump=int(input("[::] Please enter again the number of the posts to like: "))
    for i in range(1,count+1):
        hashtag=str(input("[::] Please enter the hashtag No{} : ".format(i)))
        while (hashtag == None) or ("#" not in hashtag):
            print("[!] Invalid Hashtag !")
            sleep(1)
            hashtag=str(input("[::] Please enter again the hashtag No{} : ".format(i)))
        LTAGS.append(hashtag)
        print("[!] Hashtag Added Successfully !")
    rtags=str(input("[?] Do you want to like random tags ? [yes/no] "))
    while (rtags != "yes" and rtags != "YES" and rtags != "no" and rtags != "NO") or (rtags == None):
        print("[!] Invalid Input !")
        sleep(1)
        rtags=input("[?] Do you want to like random hashtags ? [yes/no] ")
    if rtags == "yes" or rtags == "YES":
        random = True
    else:
        random = False
    try:
        logini.like_by_tags(LTAGS,random,count)
        sleep(3)
        print("[!] Posts Liked !")
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 27:
    countu=int(input("[::] Please enter the number of accounts to like their posts: "))
    while countu <= 0 or countu == None:
        print("[!] Invalid Number !")
        sleep(1)
        countu=int(input("[::] Please enter again the number of accounts to like their posts: "))
    count=int(input("[::] Please enter the number of posts to like: "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please enter again the number of posts to like: "))
    if countu == 1:
        username=str(input("[::] Please enter the username: "))
        while username == None or len(username) > 30:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        LBU.append(username)
        try:
            logini.like_by_users(LBU,count)
            sleep(5)
            print("[!] Posts Liked Successfully !")
        except Exception as ex:
            print("[!] Error")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    else:
        for i in range(1,countu+1):
            username=str(input("[::] Please enter the username No{} : ".format(i)))
            while username == None or len(username) > 30:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again the username No{} : ".format(i)))
            LBU.append(username)
        try:
            logini.like_by_users(LBU,count)
            sleep(5)
            print("[!] Posts Liked Successfully !")
        except Exception as ex:
            print("[!] Error")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)

elif option == 28:
    rand=str(input("[?] Do you want to like the posts with random order ? [yes/no] "))
    while (rand != "yes" and rand != "YES" and rand != "no" and rand != "NO") or (rand == None):
        print("[!] Invalid Input !")
        sleep(1)
        rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
    if rand == "yes" or rand == "YES":
        random = True
        print("[OK]")
        pass
    else:
        random = False
        print("[OK]")
        pass
    numloc=int(input("[::] Please enter the number of locations to like their posts: "))
    while numloc <= 0 or numloc == None:
            print("[!] Invalid Number !")
            sleep(1)
            numloc=int(input("[::] Please enter again the number of locations to like their posts: "))
    sleep(2)
    countp=int(input("[?] How many posts to like for each location ? "))
    while countp <= 0 or countp == None:
        print("[!] Invalid Number !")
        sleep(1)
        countp=int(input("[?] How many posts to like for each location ? "))
    for i in range(1,numloc+1):
        location=str(input("[::] Please enter location No{} : ".format(i)))
        while location == None:
            print("[!] Invalid Location !")
            sleep(1)
            location=str(input("[::] Please enter again location No{} : ".format(i)))
        LOCLIKE.append(location)
    try:
        logini.like_by_locations(LOCLIKE,amount=countp,randomize=random)
        sleep(5)
        print("[!] Posts Liked !")
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 29:
    print("Getting in option 29")
    count=int(input("[+] Please enter the amount of posts to like: "))
    while count <= 0 or count == None:
        print("[!] Invalid Amount !")
        sleep(1)
        count=int(input("[::] Please enter again the amount of posts to like: "))
    if count == 1:
        rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
        while (rand != "yes" and rand != "YES" and rand != "no" and rand != "NO") or (rand == None):
            print("[!] Invalid Input !")
            sleep(1)
            rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
        if rand == "yes" or rand == "YES":
            rmize = True
            print("[OK]")
            pass
        else:
            rmize = False
            print("[OK]")
            pass
        try:
            logini.like_by_feed(count,rmize)
            sleep(5)
            print("[!] Posts Liked !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    else:
        rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
        while (rand != "yes" and rand != "YES" and rand != "no" and rand != "NO") or (rand == None):
            print("[!] Invalid Input !")
            sleep(1)
            rand=str(input("[?] Do you want to like them with random order ? [yes/no] "))
        if rand == "yes" or rand == "YES":
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
                print("[!] Posts Liked !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)

elif option == 30:
    amo=int(input("[::] Please enter the amount of posts to like: "))
    while amo <= 0 or amo == None:
        print("[!] Invalid Amount !")
        sleep(1)
        amo=int(input("[::] Please enter again the amount of posts to like: "))
    username=str(input("[::] Please enter the username: "))
    while username == None:
        print("[!] Invalid Username !")
        sleep(1)
        username=str(input("[::] Please enter again the username: "))
    uid = loader.check_profile_id(username)
    id=int(input("[::] Please enter user's ID as shown above: "))
    while id == None or len(id) < 3:
        print("[!] Invalid ID !")
        sleep(1)
        id=int(input("[::] Please enter again user's ID as shown above: "))
    bot.comment_user(id,amo)
elif option == 31:
    count=int(input("[::] Please enter the amount of replies to save: "))
    while count <= 0 or count == None:
        print("[!] Invalid Amount !")
        sleep(1)
        count=int(input("[::] Please enter again the amount of replies to save: "))
    for i in range(1,count+1):
        reply=str(input("[::] Please enter the reply No"+str(i)+" : "))
        while reply == None:
            print("[!] Invalid Reply !")
            sleep(1)
            reply=str(input("[::] Please enter again the reply No"+str(i)+" : "))
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
        exit(0)

elif option == 32:
    com=str(input("[::] Please enter your comment: "))
    while com == None:
        print("[!] Invalid Comment !")
        sleep(1)
        com=str(input("[::] Please enter again your comment: "))
    url="https://www.instagram.com"
    webbrowser.open(url)
    print("[+] Please find the post to comment and wait...")
    found=str(input("[::] If found enter [yes]: "))
    while (found != "yes" and found != "YES") or found == None:
        print("[!] Invalid Input !")
        sleep(1)
        found=str(input("[::] If found enter [yes]: "))
    if found == "yes" or found == "YES":
        browser=webdriver.Firefox()
        link=input("[::] Please enter the link for the post: ")
        while link == None or "https" not in link or "//" not in link or "instagram" not in link or "www" not in link or ".com" not in link:
            print("[!] Invalid Link !")
            sleep(1)
            link=input("[::] Please enter again the link for the post: ")
        browser.get(link)
        try:
            comment_label = browser.find_element_by_class_name("_ablz _aaoc")
            comment_label.send_keys(com)
            publish = browser.find_element_by_class_name("_aacl _aaco _aacw _adda _aad0 _aad6 _aade")
            publish.click()
            sleep(4)
            print("[!] Comment uploaded successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)

elif option == 33:
    count=int(input("[::] Please enter the number of users to block: "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please enter again the number of users to block: "))
    if count == 1:
        username=str(input("[::] Please enter the username: "))
        while username == None:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
            uid = loader.check_profile_id(username)
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while id == None or len(id) < 3:
                print("[!] Invalid ID !")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            BLOCKU.append(id)
            try:
                bot.block_users(BLOCKU)
                sleep(3)
                print("[!] User blocked successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)
    else:
        for i in range(1,count+1):
            username=str(input("[::] Please enter the username No"+str(i)+" : "))
            while username == None:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again the username No"+str(i)+" : "))
            uid = loader.check_profile_id(username)
            id = int(input("[::] Please enter the ID of the user as shown above: "))
            while id == None or len(id) < 3:
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
            exit(0)

elif option == 34:
    id=int(input("[::] Please enter the ID of the user: "))
    while id == None or len(id) < 3:
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
        exit(0)

elif option == 35:
    try:
        blocked_users = api.blocked_user_list()
        print("[+] Blocked Users: ")
        print("\n")
        print(blocked_users)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 36:
    counti=int(input("[::] How many highlights do you want to create ? "))
    while counti <= 0 or counti == None:
        print("[!] Invalid Amount !")
        sleep(1)
        counti=int(input("[::] How many highlights do you want to create ? "))
    if counti == 1:
        title=str(input("[::] Please enter the title of the highlight: "))
        while title == None:
            print("[!] Invalid Title")
            sleep(1)
            title=str(input("[::] Please enter again the title of the highlight: "))
        count=int(input("[::] Please enter the number of stories to add in the highlight: "))
        while count <= 0 or count == None:
            print("[!] Invalid Number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of stories to add in the highlight: "))
        for i in range(1,count+1):
            story_id = int(input("[::] Please enter the story ID No"+str(i)+" : "))
            while story_id == None or story_id <= 0:
                print("[!] Invalid ID !")
                sleep(1)
                story_id = int(input("[::] Please enter again the story ID No"+str(i)+" : "))
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
            exit(0)
    else:
        for i in range(counti):
            title=str(input("[::] Please enter the title of the highlight: "))
            while title == None:
                print("[!] Invalid Title")
                sleep(1)
                title=str(input("[::] Please enter again the title of the highlight: "))
            count=int(input("[::] Please enter the number of stories to add in the highlight: "))
            while count <= 0 or count == None:
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[::] Please enter again the number of stories to add in the highlight: "))
            for i in range(1,count+1):
                story_id = int(input("[::] Please enter the story ID No"+str(i)+" : "))
                while story_id == None or story_id <= 0:
                    print("[!] Invalid ID !")
                    sleep(1)
                    story_id = int(input("[::] Please enter again the story ID No"+str(i)+" : "))
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
                exit(0)

elif option == 37:
    count=int(input("[::] How many highlights do you want to delete ? "))
    while count <= 0 or count == None:
        print("[!] Invalid Amount !")
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
            exit(0)
    else:
        for i in range(count):
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
                exit(0)

elif option == 38:
    count=int(input("[::] How many covers of highlights do you want to change ? "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] How many covers of highlights do you want to change ? "))
    if count == 1:
        url=input("[::] Please enter the url for the highlight: ")
        while url == None or ("https" not in url or "//" not in url or "instagram" not in url or ".com" not in url):
            print("[!] Invalid Link !")
            sleep(1)
            url=input("[::] Please enter again the url for the highlight: ")
        Get_HP(url)
        pk=int(input("[::] Please enter the highlight id as shown above: "))
        while pk == None or pk <= 0:
            print("[!] Invalid ID !")
            sleep(1)
            pk=int(input("[::] Please enter again the highlight id as shown above: "))
        path=input("[::] Please enter the path of the cover for the highlight: ")
        while path == None or "/" not in path:
            print("[!] Invalid path !")
            sleep(1)
            print("[!] Path must contain /")
            sleep(2)
            path=input("[::] Please enter again the path of the cover for the highlight: ")
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
            exit(0)
    else:
        for i in range(count):
            url=input("[::] Please enter the url for the highlight: ")
            while url == None or ("https" not in url or "//" not in url or "instagram" not in url or ".com" not in url):
                print("[!] Invalid Link !")
                sleep(1)
                url=input("[::] Please enter again the url for the highlight: ")
            Get_HP(url)
            pk=int(input("[::] Please enter the highlight id as shown above: "))
            while pk == None or pk <= 0:
                print("[!] Invalid ID !")
                sleep(1)
                pk=int(input("[::] Please enter again the highlight id as shown above: "))
            path=input("[::] Please enter the path of the cover for the highlight: ")
            while path == None or "/" not in path:
                print("[!] Invalid path !")
                sleep(1)
                print("[!] Path must contain /")
                sleep(2)
                path=input("[::] Please enter again the path of the cover for the highlight: ")
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
                exit(0)

elif option == 39:
    countu=int(input("[::] From how many users you want to display their highlights ? "))
    while countu <= 0 or countu == None:
        print("[!] Invalid Number !")
        sleep(1)
        countu=int(input("[::] From how many users you want to display their highlights ? "))
    if countu == 1:
        username=str(input("[::] Please enter the username: "))
        while username == None:
            print("[!] Invalid Username !")
            sleep(1)
            username=str(input("[::] Please enter again the username: "))
        uid = loader.check_profile_id(username)
        id=int(input("[::] Please enter the ID of the user as shown above: "))
        while id == None or len(id) < 3:
            print("[!] Invalid ID !")
            sleep(1)
            id=int(input("[::] Please enter again the ID of the user as shown above: "))
        amount=int(input("[::] How many highlights do you want to display ? "))
        while amount <= 0 or amount == None:
            print("[!] Invalid Amount !")
            sleep(1)
            amount=int(input("[::] How many highlights do you want to display ? "))
        try:
            client.user_highlights(id,amount)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    else:
        for i in range(countu):
            username=str(input("[::] Please enter the username: "))
            while username == None:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            uid = loader.check_profile_id(username)
            id=int(input("[::] Please enter the ID of the user as shown above: "))
            while id == None or len(id) < 3:
                print("[!] Invalid ID !")
                sleep(1)
                id=int(input("[::] Please enter again the ID of the user as shown above: "))
            amount=int(input("[::] How many highlights do you want to display ? "))
            while amount <= 0 or amount == None:
                print("[!] Invalid Amount !")
                sleep(1)
                amount=int(input("[::] How many highlights do you want to display ? "))
            try:
                client.user_highlights(id,amount)
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)

elif option == 40:
    counti=int(input("[::] From how many highlights do you want to retrieve information ? "))
    while counti <= 0 or counti == None:
        print("[!] Invalid Number !")
        sleep(1)
        counti=int(input("[::] From how many highlights do you want to retrieve information ? "))
    if counti == 1:
        url=input("[::] Please enter the url for the highlight: ")
        while url == None or ("https" not in url or "//" not in url or "instagram" not in url or ".com" not in url):
            print("[!] Invalid Link !")
            sleep(1)
            url=input("[::] Please enter again the url for the highlight: ")
        Get_Hpk(url)
        pk=int(input("[::] Please enter the highlight id as shown above: "))
        while pk == None or pk <= 0:
            print("[!] Invalid ID !")
            sleep(1)
            pk=int(input("[::] Please enter again the highlight id as shown above: "))
        try:
            client.highlight_info(pk)
            sleep(3)
            print("[!] Information Retrieved Successfully !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)
    else:
        for i in range(counti):
            url=input("[::] Please enter the url for the highlight: ")
            while url == None or ("https" not in url or "//" not in url or "instagram" not in url or ".com" not in url):
                print("[!] Invalid Link !")
                sleep(1)
                url=input("[::] Please enter again the url for the highlight: ")
            Get_Hpk(url)
            pk=int(input("[::] Please enter the highlight id as shown above: "))
            while pk == None or pk <= 0:
                print("[!] Invalid ID !")
                sleep(1)
                pk=int(input("[::] Please enter again the highlight id as shown above: "))
            try:
                client.highlight_info(pk)
                sleep(3)
                print("[!] Information Retrieved Successfully !")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                exit(0)

elif option == 41:
    url=input("[::] Please enter the url of the story: ")
    while url == None or ("https" not in url or "//" not in url or "instagram" not in url or ".com" not in url):
        print("[!] Invalid url !")
        sleep(1)
        url=input("[::] Please enter again the url of the story: ")
    Get_Spk(url)
    pk=int(input("[::] Please enter the story ID as shown above: "))
    while id == None or len(id) < 3:
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
        exit(0)

elif option == 42:
    url=input("[::] Please enter the url of the story: ")
    while url == None or ("https" not in url or "//" not in url or "instagram" not in url or ".com" not in url):
        print("[!] Invalid url !")
        sleep(1)
        url=input("[::] Please enter again the url of the story: ")
    Get_Spk(url)
    pk=int(input("[::] Please enter the story ID as shown above: "))
    while id == None or len(id) < 3:
        print("[!] Invalid ID !")
        sleep(1)
        pk=int(input("[::] Please enter again the story ID as shown above: "))
    amount=int(input("[::] Please enter the amount of viewers to display: "))
    while amount <= 0 or amount == None:
        print("[!] Invalid Amount !")
        sleep(1)
        amount=int(input("[::] Please enter again the amount of viewers to display: "))
    try:
        client.story_viewers(pk,amount)
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 43:
    count=int(input("[::] Please specify the number of hashtags: "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please specify again the number of hashtags: "))
    for i in range(1,count+1):
        tag=input("[::] Please enter the hashtag No"+str(i)+" : ")
        while tag == None:
            print("[!] Invalid Hashtag !")
            sleep(1)
            tag=input("[::] Please enter again the hashtag No"+str(i)+" : ")
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
        exit(0)

elif option == 44:
    count=int(input("[::] Please specify the number of users: "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please specify again the number of users: "))
    for i in range(1,count+1):
        username=input("[::] Please enter the username No"+str(i)+" : ")
        while username == None:
            print("[!] Invalid Username !")
            sleep(1)
            username=input("[::] Please enter again the username No"+str(i)+" : ")
        uid = loader.check_profile_id(username)
        id=int(input("[::] Please enter the ID as shown above: "))
        while id == None or len(id) < 3:
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
        exit(0)

elif option == 45:
    url=input("[::] Please enter the url of the story: ")
    while url == None or ("https" not in url or "//" not in url or "instagram" not in url or ".com" not in url):
        print("[!] Invalid url !")
        sleep(1)
        url=input("[::] Please enter again the url of the story: ")
    Get_Spk(url)
    pk=int(input("[::] Please enter the story ID as shown above: "))
    while id == None or len(id) < 3:
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
        exit(0)

elif option == 46:
    print("[+] Countries example: US, BR, CZ")
    sleep(1)
    fcodes=str(input("[?] Do you want to display full list of country codes ? [yes/no] "))
    while (fcodes != "yes" and fcodes != "YES" and fcodes != "no" and fcodes != "NO") or fcodes == None:
        print("[!] Invalid Input !")
        sleep(1)
        fcodes=str(input("[?] Do you want to display full list of country codes ? [yes/no] "))
    if fcodes == "yes" or fcodes == "YES":
       webbrowser.open("https://www.iban.com/country-codes")
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
           exit(0)
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
            exit(0)

elif option == 47:
    bio=str(input("[::] Please enter the bio to set: "))
    while bio == None:
        print("[!] Invalid Bio !")
        sleep(1)
        bio=str(input("[::] Please enter again the bio to set: "))
    try:
        client.account_set_biography(bio)
        sleep(3)
        print("[!] Bio set successful !")
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 48:
    username=str(input("[::] Please enter your username: "))
    while username == None:
        print("[!] Invalid Username !")
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
        exit(0)

elif option == 49:
    username=str(input("[::] Please enter the username: "))
    while username == None:
        print("[!] Invalid Username !")
        sleep(1)
        username=str(input("[::] Please enter again the username: "))
    uid = loader.check_profile_id(username)
    id=int(input("[::] Please enter the ID as shown above: "))
    while id == None or len(id) < 3:
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
        exit(0)

elif option == 50:
    username=str(input("[::] Please enter your username: "))
    while username == None:
        print("[!] Invalid Username !")
        sleep(1)
        username=str(input("[::] Please enter again your username: "))
    try:
        client.reset_password(username)
        sleep(3)
        print("[!] Password reset successful !")
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 51:
    set_first_name=str(input("[?] Do you want to set a first name ? [yes/no] "))
    while (set_first_name != "yes" and set_first_name != "YES" and set_first_name != "no" and set_first_name != "NO") or set_first_name == None:
        print("[!] Invalid Input !")
        sleep(1)
        set_first_name=str(input("[?] Do you want to set a first name ? [yes/no] "))
    if set_first_name == "yes" or set_first_name == "YES":
        first_name=str(input("[::] Please enter your first name: "))
        while first_name == None:
            print("[!] Invalid first name !")
            sleep(1)
            first_name=str(input("[::] Please enter again your first name: "))
    else:
        pass
    set_bio=str(input("[?] Do you want to set a bio ? [yes/no] "))
    while (set_bio != "yes" and set_bio != "YES" and set_bio != "no" and set_bio != "NO") or set_bio == None:
        print("[!] Invalid Input !")
        sleep(1)
        set_bio=str(input("[?] Do you want to set a bio ? [yes/no] "))
    if set_bio == "yes" or set_bio == "YES":
        bio=str(input("[::] Please enter the bio: "))
        while bio == None:
            print("[!] Invalid Bio !")
            sleep(1)
            bio=str(input("[::] Please enter again the bio: "))
    else:
        pass
    set_ex_url=str(input("[?] Do you want to set an external url ? [yes/no] "))
    while (set_ex_url != "yes" and set_ex_url != "YES" and set_ex_url != "no" and set_ex_url != "NO") or set_ex_url == None:
        print("[!] Invalid Input !")
        sleep(1)
        set_ex_url=str(input("[?] Do you want to set an external url ? [yes/no] "))
    if set_ex_url == "yes" or set_ex_url == "YES":
        url=input("[::] Please enter the url: ")
        while url == None or "/" not in url or "//" not in url:
            print("[!] Invalid Url !")
            sleep(1)
            url=input("[::] Please enter again the url: ")
    else:
        pass
    set_email=str(input("[?] Do you want to set an email ? [yes/no] "))
    while (set_email != "yes" and set_email != "YES" and set_email != "no" and set_email != "NO") or set_email == None:
        print("[!] Invalid Input !")
        sleep(1)
        set_email=str(input("[?] Do you want to set an email ? [yes/no] "))
    if set_email == "yes" or set_email == "YES":
        email=str(input("[::] Please enter the email: "))
        while email == None:
            print("[!] Invalid Email !")
            sleep(1)
            email=str(input("[::] Please enter the email: "))
    else:
        pass
    set_phone_number=str(input("[?] Do you want to set a phone number ? [yes/no] "))
    while (set_phone_number != "yes" and set_phone_number != "YES" and set_phone_number != "no" and set_phone_number != "NO") or set_phone_number == None:
        print("[!] Invalid Input !")
        sleep(1)
        set_phone_number=str(input("[?] Do you want to set a phone number ? [yes/no] "))
    if set_phone_num == "yes" or set_phone_num == "YES":
        phone_number=int(input("[::] Please enter the phone number: "))
        while phone_number == None:
            print("[!] Invalid Phone Number !")
            sleep(1)
            phone_number=int(input("[::] Please enter the phone number: "))
    else:
        pass
    set_gender=str(input("[?] Do you want to enter a gender ? [yes/no] "))
    while (set_gender != "yes" and set_gender != "YES" and set_gender != "no" and set_gender != "NO") or set_gender == None:
        print("[!] Invalid Input !")
        sleep(1)
        set_gender=str(input("[?] Do you want to enter a gender ? [yes/no] "))
    if set_gender == "yes" or set_gender == "YES":
        gender=str(input("[::] Please enter the gender: "))
        while gender == None:
            print("[!] Invalid Gender !")
            sleep(1)
            gender=str(input("[::] Please enter again the gender: "))
    else:
        pass    
    try:
        api.edit_profile(first_name,bio,url,email,phone_number,gender)
        sleep(5)
        print("[!] Profile edit successful !")
    except Exception as ex:
        print("[!] Error !")
        sleep(1)
        print(ex)
        sleep(2)
        print("[+] Exiting...")
        exit(0)

elif option == 52:
    count=int(input("[::] How many posts do you want to like/unlike ? "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] How many posts do you want to like/unlike ? "))
    browser = webdriver.Chrome()
    for i in range(count):
        url=input("[::] Please enter the url of the post: ")
        while url == None or ("https" not in url and "instagram" not in url and "//" not in url and ".com" not in url and "/" not in url):
            print("[!] Invalid Url !")
            sleep(1)
            url=input("[::] Please enter again the url of the post: ")
        try:
            browser.get(url)
            like = browser.find_element_by_id("mount_0_0_Cs")
            like.click()
            print("[!] Liked !")
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)

elif option == 53:
    count=int(input("[::] Please enter the number of deletes to make: "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please enter again the number of deletes to make: "))
    browser = webdriver.Firefox()
    for i in range(count):
        url=input("[::] Please enter the url of the post, igtv, reel etc. : ")
        while url == None or ("https" not in url and "instagram" not in url and "//" not in url and ".com" not in url and "/" not in url):
            print("[!] Invalid Url !")
            sleep(1)
            url=input("[::] Please enter again the url of the post, igtv, reel etc. : ")
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
            exit(0)

elif option == 54:
    count=int(input("[::] Please enter the number of the posts to save: "))
    while count <= 0 or count == None:
        print("[!] Invalid Number !")
        sleep(1)
        count=int(input("[::] Please enter again the number of the posts to save: "))
    browser = webdriver.Firefox()
    for i in range(count):
        url=input("[::] Please enter the url of the post, igtv, reel etc. : ")
        while url == None or ("https" not in url and "instagram" not in url and "//" not in url and ".com" not in url and "/" not in url):
            print("[!] Invalid Url !")
            sleep(1)
            url=input("[::] Please enter again the url of the post, igtv, reel etc. : ")
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
            exit(0)

elif option == 55:
    __time__=str(input("[::] Please enter the time (example: 15:06:10): "))
    while __time__ == None or ":" not in __time__:
        print("[!] Invalid time !")
        sleep(1)
        __time__=str(input("[::] Please enter again the time (example: 15:06:10): "))
    Av_Acts()
    cur_time = datetime.now()
    current_time = cur_time.now("%H:%M:%S")
    action=int(input("[::] Please enter the number of the action: "))
    while action < 1 or action > 26 or action == None:
        print("[!] Invalid Number !")
        sleep(1)
        action=int(input("[::] Please enter the number of the action: "))

    if action == 1:
        count=int(input("[::] Please enter the number of posts to post: "))
        while count <= 0 or count == None:
            print("[!] Invalid Number !")
            sleep(1)
            count=int(input("[::] Please enter again the number of posts to post: "))
        for i in range(count):
            path=input("[::] Please enter the path of the file which contains the photo to be uploaded: ")
            while (path == None) or ("/" not in path):
                print("[!] Invalid Path !")
                sleep(1)
                path=input("[::] Please enter again the path of the file which contains the photo to be uploaded: ")
            sleep(2)
            print(">>>CAPTION<<<")
            sleep(1)
            print("[+] Default: Check out my new post !")
            sleep(2)
            print("[+] Hit <Enter> for the default option to be applied")
            sleep(2)
            caption=str(input("[::] Please enter the caption: "))
            if caption == None:
                caption = "New Post !"
            print(">>>TAGS<<<")
            sleep(2)
            print("[+] Default: [no]")
            sleep(2)
            print("[+] Hit <Space> and <Enter> to Apply the Default Option")
            sleep(2)
            tags=input("[?] Do you want to include other users to your post by tagging them ? [yes/no] ")
            while (tags != "yes" and tags != "YES" and tags != "no" and tags != "NO") or (tags == None):
                print("[!] Invalid Input !")
                sleep(1)
                tags=input("[?] Do you want to include other users to your post by tagging them ? [yes/no] ")
            if tags == "yes" or tags == "YES":
                print("[+] Default: 1")
                sleep(2)
                print("[+] Hit <Space> and <Enter> to Apply the Default Option")
                count=int(input("[?] How many users do you want to include ? "))
                while count <= 0 or count == None:
                    print("[!] Invalid Number !")
                    sleep(1)
                    count=int(input("[?] How many users do you want to tag ? "))
                utag=input("[::] Please enter the username: ")
                while utag == None or len(utag) > 30:
                    print("[!] Invalid username !")
                    sleep(1)
                    utag=input("[::] Please enter again the username: ")
                utag = utag.strip()
                utag = utag.lower()
                TaggedUsers.append(utag)
                for i in range(1,count+1):
                    utag=input("[::] Please enter the username No{}: ".format(i))
                    while utag == None or len(utag) > 30:
                        print("[!] Invalid username !")
                        sleep(1)
                        utag=input("[::] Please enter again the username No{}: ".format(i))
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
            print("[+] Hit <Enter> to Apply the Default Option")
            sleep(2)
            loc=input("[?] Do you want to include location(s) ? [yes/no] ")
            while (loc != "yes" and loc != "YES" and loc != "no" and loc != "NO") or (loc == None):
                print("[!] Invalid Input !")
                sleep(1)
                loc=input("[?] Do you want to include location(s) ? [yes/no] ")
            if loc == "Y" or loc == "y":
                count=int(input("[?] How many ? "))
                while count <= 0 or count == None:
                    print("[!] Invalid Number !")
                    sleep(1)
                    count=int(input("[?] How many locations do you want to include ? "))
                for i in range(1,count+1):
                   location1=input("[::] Please enter location No"+str(i)+": ")
                   LOCATIONS.append(location1)
                   print("[!] Location Added Successfully !")
                if current_time == __time__:
                    try:
                        client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                        sleep(2)
                        print("[!] Photo Uploaded Successfully !")
                        exit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        exit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            else:
                print("[OK]")
                pass
            if (tags == "yes" or tags == "YES") and (loc == "yes" or loc == "YES"):
                if current_time == __time__:
                    try:
                        client.photo_upload(path=path,caption=caption,usertags=TaggedUsers,location=LOCATIONS)
                        print("[!] Photo Uploaded Successfully !")
                        exit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        exit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif (tags == "yes" or tags == "YES") and (loc == "no" or loc == "NO"):
                if current_time == __time__:
                    try:
                        client.photo_upload(path=path,caption=caption,tags=TaggedUsers)
                        print("[!] Photo Uploaded Successfully !")
                        exit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        exit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif (tags == "no" or tags == "NO") and (loc == "yes" or loc == "YES"):
                if current_time == __time__:
                    try:
                        client.photo_upload(path=path,caption=caption,location=LOCATIONS)
                        print("[!] Photo Uploaded Successfully !")
                        exit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        exit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass
            elif (tags == "no" or tags == "NO" and loc == "no" or loc == "NO"):
                if current_time == __time__:
                    try:
                        client.photo_upload(path=path,caption=caption)
                        print("[!] Photo Uploaded Successfully !")
                        exit(0)
                    except Exception as ex:
                        print("[!] Error !")
                        sleep(1)
                        print(ex)
                        sleep(2)
                        print("[+] Exiting...")
                        exit(0)
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass

    elif action == 2:
        path=input("[::] Please enter the full path of the folder which contains your new profile pic: ")
        while (path == None) or ("/" not in path):
            print("[!] Invalid Path !")
            sleep(1)
            path=input("[::] Please enter again the full path of the folder which contains your new profile pic: ")
        try:
            client.account_change_picture(path)
            sleep(3)
            print("[!] Your profile picture changed successfully !")
            exit(0)
        except Exception as ex:
            print("[!] Error !")
            sleep(1)
            print(ex)
            sleep(2)
            print("[+] Exiting...")
            exit(0)

    elif action == 3:
        path=input("[::] Please enter the path of the file which contains the photo to be uploaded: ")
        while (path == None) or ("/" not in path):
            print("[!] Invalid Path !")
            sleep(1)
            path=input("[::] Please enter again the path of the file which contains the photo to be uploaded: ")
        AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
        while (AddCaption != "yes" and AddCaption != "YES" and AddCaption != "no" and AddCaption != "NO") or (AddCaption == None):
            print("[!] Invalid Input !")
            sleep(1)
            AddCaption=str(input("[?] Do you want to add caption ? [yes/no] "))
        if AddCaption == "yes" or AddCaption =="YES":
            print("[+] Default: Check out my new story !")
            sleep(2)
            print("[+] Hit <Enter> for the default option to be applied")
            sleep(2)
            caption=str(input("[::] Please enter the caption: "))
            if caption == None:
                caption = "Check out my new story !"
                pass
            else:
                caption=str(input("[::] Please enter a caption to include to the story: "))
                while caption == None:
                    print("[!] Invalid Caption !")
                    sleep(1)
                    caption=str(input("[::] Please enter again a caption to include to the story: "))
        else:
            print("[OK]")
            sleep(1)
            pass
        AddMention=str(input("[?] Do you want to add mention ? [yes/no] "))
        while (AddMention != "yes" and AddMention != "YES" and AddMention != "no" and AddMention != "NO") or (AddMention == None):
            print("[!] Invalid Mention !")
            sleep(1)
            mention=str(input("[?] Do you want to mention user(s) ? [yes/no] "))
        if AddMention == "yes" or AddMention == "YES":
            MENTIONS = []
            count=int(input("[?] How many ? "))
            while count <= 0 or count == None:
                print("[!] Invalid Input !")
                sleep(1)
                count=int(input("[?] How many ? "))
            for i in range(1,count+1):
                mention=str(input("[::] Please enter the username No{}: ".format(i)))
                while mention == None or len(mention) > 30:
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
        while (AddLoc != "yes" and AddLoc != "YES" and AddLoc != "no" and AddLoc != "NO") or (AddLoc == None):
            print("[!] Invalid Input !")
            sleep(1)
            AddLoc=str(input("[?] Do you want to add location ? [yes/no] "))
        if AddLoc == "yes" or AddLoc == "YES":
            count=int(input("[?] How many locations do you want to add ? "))
            while count <= 0 or count == None :
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[?] How many locations do you want to add ? "))
            for i in range(1,count+1):
                loc=str(input("[::] Please enter location No{}: ".format(i)))
                while loc == None:
                    print("[!] Invalid Location !")
                    sleep(1)
                    loc=str(input("[::] Please enter again location No{}: ".format(i)))
                LOCATIONS.append(loc)
                sleep(1)
                print("[!] Location added successfully !")
        else:
            print("[OK]")
            sleep(1)
            pass
        AddLinks=str(input("[?] Do you want to include links ? [yes/no] "))
        while (AddLinks != "yes" and AddLinks != "YES" and AddLinks != "no" and AddLinks != "NO") or (AddLinks == None):
            print("[!] Invalid Input !")
            sleep(1)
            AddLinks=str(input("[?] Do you want to include links ? [yes/no] "))
        if AddLinks == "yes" or AddLinks == "YES":
            count=int(input("[?] How many ? "))
            while count <= 0 or count == None:
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[?] How many links do you want to include ? "))
            for i in range(1,count+1):
                link=str(input("[::] Please enter the link No{}: ".format(i)))
                while (link == None) or ("//" not in link):
                    print("[!] Invalid Link !")
                    sleep(1)
                    link=str(input("[::] Please enter again the link No{}: ".format(i)))
                LINKS.append(link)
                sleep(1)
                print("[!] Link added successfully !")
        else:
            print("[OK]")
            sleep(1)
            pass
        AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
        while (AddHash != "yes" and AddHash != "YES" and AddHash != "no" and AddHash != "NO") or (AddHash == None):
            print("[!] Invalid Input !")
            sleep(1)
            AddHash=str(input("[?] Do you want to include hashtags ? [yes/no] "))
        if AddHash == "yes" or AddHash == "YES":
            count=int(input("[?] How many ? "))
            while  count <= 0 or count == None :
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[?] How many hashtags do you want to include ? "))
            for i in range(1,count+1):
                hashtag=str(input("[::] Please enter the hashtag No{}: ".format(i)))
                while (hashtag == None) or ("#" not in hashtag):
                    print("[!] Invalid Hashtag !")
                    sleep(1)
                    hashtag=str(input("[::] Please enter again the hashtag No{}: ".format(i)))
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
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
                    exit(0)
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
            else:
                print("[+] Current time: "+str(current_time))
                sleep(1)
                print("[+] Waiting for the time: "+str(__time__))
                pass

    elif action == 4:
        caption = None
        hashtag = None
        location = None
        path=input("[::] Please enter the path of the folder which contains the video: ")
        while (path == None) or ("/" not in path):
            print("[!] Invalid Path !")
            sleep(1)
            path=input("[::] Please enter again the path of the folder which contains the video: ")
        incap=str(input("[?] Do you want to include caption ? [yes/no] "))
        while (incap != "yes" and incap != "YES" and incap != "no" and incap != "NO") or (incap == None):
            print("[!] Invalid Input !")
            sleep(1)
            incap=str(input("[?] Do you want to include caption ? [yes/no] "))
        if incap == "yes" or incap == "YES":
            sleep(1)
            print("[+] Default Caption: Check out my new video !")
            sleep(2)
            print("[+] To apply the default caption hit: <Enter>")
            sleep(2)
            caption=str(input("[::] Please enter the caption: "))
            if caption == None:
                caption = "Check out my new video !"
                pass
            else:
                pass
        intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
        while (intag != "yes" and intag != "YES" and intag != "no" and intag != "NO") or (intag == None):
            print("[!] Invalid Input !")
            sleep(1)
            intag=str(input("[?] Do you want to include hashtag(s) ? [yes/no] "))
        if intag == "yes" or intag == "YES":
            count=int(input("[?] How many ? "))
            while count <= 0 or count == None:
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[?] How many hashtags to include ? "))
            for i in range(1,count+1):
                hashtag=str(input("[::] Please enter the hashtag No{} : ".format(i)))
                while (hashtag == None) or ("#" not in hashtag):
                    print("[!] Invalid Hashtag !")
                    sleep(2)
                    print("[+] You have to include #")
                    sleep(2)
                    hashtag=str(input("[::] Please enter again hashtag No{} : ".format(i)))
                HASHVID.append(hashtag)
                sleep(1)
                print("[!] Hashtag added successfully !")
        else:
            print("[OK]")
            sleep(1)
            pass
        inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
        while (incloc != "yes" and inloc != "YES" and inloc != "no" and inloc != "NO") or (inloc == None):
            print("[!] Invalid Location !")
            sleep(1)
            inloc=str(input("[?] Do you want to include location(s) ? [yes/no] "))
        if inloc == "yes" or inloc == "YES":
            count=int(input("[?] How many ? "))
            while count <= 0 or count == None:
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[?] How many locations to include ? "))
            for i in range(1,count+1):
                location=str(input("[::] Please enter location No{} : ".format(i)))
                while location == None:
                    print("[!] Invalid Location !")
                    sleep(1)
                    location=str(input("[::] Please enter again location No{} : ".format(i)))
        else:
            print("[OK]")
            sleep(1)
            pass
        if cucurrent_time == __time__:
            try:
                client.video_upload(path,caption,usertags=HASHVID,location=location)
                sleep(5)
                print("[!] Video uploaded successfully !")
                exit(0)
            except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
        else:
            print("[+] Current time: "+str(current_time))
            sleep(1)
            print("[+] Waiting for the time: "+str(__time__))
            pass

    elif action == 5:
        count=int(input("[?] How many accounts do you want to follow ? "))
        while count <= 0 or count == None:
            print("[!] Invalid Number !")
            sleep(1)
            count=int(input("[?] How many accounts do you want to follow ? "))
        if count == 1:
            username=str(input("[::] Please enter the username: "))
            while username == None or len(username) > 30:
                print("[!] Invalid Username !")
                sleep(1)
                username=str(input("[::] Please enter again the username: "))
            username.lower()
            username.strip()
            user_id = loader.check_profile_id(username)
            uid=int(input("[::] Please enter the user's ID as shown above: "))
            while uid == None or uid <= 0:
                print("[!] Invalid ID")
                sleep(1)
                uid=int(input("[::] Please enter again the user's ID as shown above: "))
            if current_time == __time__:
                try:
                    client.user_follow(uid)
                    sleep(3)
                    print("[!] Successfully followed {} !".format(username))
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
            else:
                print("[+] Current time: "+str(current_time))
                sleep(1)
                print("[+] Waiting for the time: "+str(__time__))
                pass
        else:
            for i in range(1,count+1):
                username=str(input("[::] Please enter the username No{} :".format(i)))
                while username == None or len(username) > 30:
                    print("[!] Invalid Username !")
                    sleep(1)
                    username=str(input("[::] Please enter again username No{} : ".format(i)))
                username.lower()
                username.strip()
                uid=loader.check_profile_id(username)
                id=int(input("[::] Please enter the user's ID as shown above: "))
                while id == None or len(id) < 3:
                    print("[!] Invalid ID !")
                    sleep(1)
                    uid=int(input("[::] Please enter again the user's ID as shown above: "))
                if current_time == __time__:
                    try:
                        client.user_follow(id)
                        sleep(3)
                        print("[!] Successfully followed {} !".format(username))
                    except Exception as ex:
                        print("[!] Can't follow {} !".format(username))
                        pass
                else:
                    print("[+] Current time: "+str(current_time))
                    sleep(1)
                    print("[+] Waiting for the time: "+str(__time__))
                    pass

    elif action == 6:
        if current_time == __time__:
            count=int(input("[?] How many accounts do you want to unfollow ? "))
            while count <= 0 or count == None:
                print("[!] Invalid Number !")
                sleep(1)
                count=int(input("[?] How many accounts do you want to unfollow ? "))
            if count == 1: 
                username=str(input("[::] Please enter the username: "))
                while username == None or len(username) > 30:
                    print("[!] Invalid Username !")
                    sleep(1)
                    username=str(input("[::] Please enter again the username: "))
                username.lower()
                username.strip()
                user_id = loader.check_profile_id(username)
                uid=int(input("[::] Please enter the user's ID as shown above: "))
                while uid == None or uid <= None:
                    print("[!] Invalid ID !")
                    sleep(1)
                    uid=int(input("[::] Please enter again the user's ID as shown above: "))
                try:
                    client.user_unfollow(uid)
                    sleep(3)
                    print("[!] Successfully unfollowed {} !".format(username))
                except Exception as ex:
                    print("[!] Error !")
                    sleep(1)
                    print(ex)
                    sleep(2)
                    print("[+] Exiting...")
                    exit(0)
            else:
                for i in range(count):
                    username=str(input("[::] Please enter the username: "))
                    while username == None or len(username) > 30:
                        print("[!] Invalid Username !")
                        sleep(1)
                        username=str(input("[::] Please enter again the username: "))
                    username.lower()
                    username.strip()
                    try:
                        client.user_unfollow(uid)
                        sleep(3)
                        print("[!] Successfully unfollowed {} !".format(username))
                    except Exception as e:
                        print("[!] Can't unfollow {} !".format(username))
                        pass
        else:
            print("[+] Current time: "+str(current_time))
            sleep(1)
            print("[+] Waiting for the time: "+str(__time__))
            sleep(1)
            pass