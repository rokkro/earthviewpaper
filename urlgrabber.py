'''
Url grabber: Checks whether Google has added more URLs/images.
If a url doesnt return a 404, then it is appended to a list + file.
Used to create the Pastebin link in the main earthview script.
Will take a while to check all of the links specified in the loop range.
'''

from urllib.request import *

urls = []
for i in range(1000,7500):
    try:
        urlretrieve('https://www.gstatic.com/prettyearth/assets/full/' + str(i) + ".jpg")
    except:
        continue
    else:
        urls.append(i)
        with open("Output.txt","a") as text_file:
            text_file.write(str(i) + " ")

print("\nDONE. See Output.txt for the usable url ids.\nUse https://www.gstatic.com/prettyearth/assets/full/ URL-ID .jpg")

