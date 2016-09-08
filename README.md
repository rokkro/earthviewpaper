# Earthviewpaper
Earthviewpaper grabs a random image from [Google's Earthview]( https://earthview.withgoogle.com ) site and sets it as your wallpaper.

<p align="center">
  <img src="https://cdn3.iconfinder.com/data/icons/faticons/32/globe-01-128.png"/>
</p>

##Linux:
* See your distribution's software repository if Python 3 isn't already installed.
* Earthviewpaper supports Unity 7, GNOME 3, and MATE (1.14).
* Cinnamon, Pantheon, and mayyybe Budgie should work, but are untested.
* In a terminal: ```python3 /path/to/earthviewpaper.py```
* XFCE and LXQT will be supported soon.

####Unsupported Desktop Enironments/WM's:
#####The script can still download and save the wallpaper, despite not being able to change the wallpaper on its own.
* GTK2 based DE's, excluding XFCE and MATE while they transition to GTK3.
* [KDE Plasma](https://www.reddit.com/r/linux/comments/4k1wht/i_made_a_script_that_changes_your_wallpaper_based/d3cvat2)
* LXDE
* Deepin 
* i3, Openbox, awesomeWM, etc.

##Windows:
* You'll probably need to [install Python 3](https://www.python.org/downloads/windows/).
* Earthviewpaper should work on Windows Vista and newer.
* Double click to run, or in cmd: ```python C:\path\to\earthviewpaper.py```

####Adding to Windows Startup:
1. Rename the script's file extension to end in .pyw instead of .py. This prevents a Python console from showing whenever the script is run.
2. Place a shortcut to the script in your startup folder (enter ```shell:startup``` in Run to access).

##Todo:
1. XFCE and LXQT.
2. MacOS support, BSD?
3. Test stuff.
