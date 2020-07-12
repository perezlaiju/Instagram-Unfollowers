import instaloader
import pickle
from threading import Thread

username="ur_username"#ur username
password="Ur_Passw0rd"#ur password
profile_name=username

Followers=[]
Following=[]

New_Followers=[]
New_Following=[]
Unfollowers=[]
Not_Following_Back=[]
Not_Following=[]

def read_files():
    #print("Reading Files....")
    global whitelist
    global xers
    global xing

    with open("whitefile", 'r') as f:
        whitelist = [line.rstrip('\n') for line in f]
    with open("Followers", 'r') as f:
        xers = [line.rstrip('\n') for line in f]
    with open("Following", 'r') as f:
        xing = [line.rstrip('\n') for line in f]

def get_ers():
    followers=profile.get_followers()
    for _ in followers:
        Followers.append(_.username)

def get_ing():
    followees=profile.get_followees()
    for _ in followees:
        Following.append(_.username)

def update_data():
    thread1=Thread(target=get_ers,args=())
    thread2=Thread(target=get_ing,args=())
    print("\nLoading Data....\n")
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

def update_files():
    with open("Following",'w') as f:
        for s in Following:
            f.write(s +'\n')
    with open("Followers",'w') as f:
        for s in Followers:
            f.write(s +'\n')
    print("\nFiles Updated.")

def analysis():
    print("Number of Followers : ",len(Followers))
    print("Number of Following : ",len(Following))

    for _ in xers:
        if(not(_ in Followers)):
            Unfollowers.append(_)
    for _ in Following:
        if(not(_ in xing)):
            New_Following.append(_)
        if(_ in whitelist):
            continue
        if(not(_ in Followers)):
            Not_Following_Back.append(_)
    for _ in Followers:
        if(not(_ in xers)):
            New_Followers.append(_)
        if(_ in whitelist):
            continue
        if(not(_ in Following)):
            Not_Following.append(_)

    print("\nNumber of New Followers : ",len(New_Followers),"\n \t",New_Followers)
    print("\nNumber of New Following : ",len(New_Following),"\n \t",New_Following)
    print("\nNumber of Unfollowers:",len(Unfollowers),"\n \t",Unfollowers)
    print("\nNumber of Not Following back : ",len(Not_Following_Back),"\n \t",Not_Following_Back)
    print("\nNumber of Not Following : ",len(Not_Following),"\n \t",Not_Following)

print("Logging In..")
L=instaloader.Instaloader()
L.login(username,password)
profile = instaloader.Profile.from_username(L.context,profile_name)
update_data()
read_files()
analysis()
update_files()

junk=input("Enter to close.")
