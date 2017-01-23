import platform, os, random, ctypes
from urllib.request import urlretrieve

def linuxde(wallid):
    dir = os.path.expanduser("~") + "/Pictures/earthview/"
    currentd = os.getcwd() + "/" + wallid + ".jpg"
    if not os.path.exists(dir): #checks if earthview directory exists
        print("*You can find downloaded images in your ~/Pictures/earthview/ directory.")
        os.makedirs(dir)
    os.rename(currentd, dir + wallid + ".jpg") #moves the file to the earthview directory
    de = os.environ.get("DESKTOP_SESSION")
    
    if de in['ubuntu', 'gnome', 'cinnamon', 'pantheon', 'gnome-classic', 'budgie-desktop', 'default', 'mate']:  #GTK3 based DE's. 'default' refers to Zorin.
        os.system("gsettings set org.gnome.desktop.background picture-uri file://" + dir + wallid + ".jpg")
    else:
        print("*Your desktop environment is not supported.\n*You can manually change your wallpaper to " + wallid + ".jpg in your ~/Pictures/earthview/ directory.")

def win(wallid):
    dir = os.path.expanduser("~") + "\Pictures\earthview\\"
    currentd = os.getcwd() + "\\" + wallid + ".jpg" #location of dl'd image in current dir
    if not os.path.exists(dir): #checks if earthview directory exists
        print("You can find downloaded images in your Pictures\earthview folder.")
        os.makedirs(dir)
    os.rename(currentd, dir + wallid + ".jpg") #moves the file to the earthview directory
    return dir

def detectOS():
    if(platform.system()=='Windows'):
        if(platform.architecture()[0]=='64bit'):
            directory = win(wallid)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, directory + wallid + ".jpg", 3) #changes wallpaper on 64bit systems
        else: #32 bit
            directory = win(wallid)
            ctypes.windll.user32.SystemParametersInfoA(20, 0, directory + wallid + ".jpg", 3)
    elif(platform.system()=='Linux'):
        linuxde(wallid)
    else:
        print("Your system isn't compatible.")
        quit()

def connectdl(): #attempts to retrieve wallids, splits into a list, randomly picks one, and downloads the image
    for i in range(0,250000):
        try:
            urlretrieve("http://pastebin.com/raw/n9hAzgBQ", "temp.txt")
            urlid = open("temp.txt").read().split(' ')
            os.remove("temp.txt")
            wallid = urlid[random.randrange(0, len(urlid)-1)]
            urlretrieve("https://earthview.withgoogle.com/download/" + wallid + ".jpg", wallid + ".jpg")
        except: #will keep attempting to connect until the loop ends (30 seconds?)
           continue
        else:
          return wallid
    return

wallid = connectdl()
if(wallid != None):
    detectOS()



