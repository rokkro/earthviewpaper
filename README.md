# Earthviewpaper
Earthviewpaper grabs a random image from [Google's Earthview]( https://earthview.withgoogle.com ) site and sets it as your wallpaper.

<p align="center">
  <img src="https://cdn3.iconfinder.com/data/icons/faticons/32/globe-01-128.png"/>
</p>

##Linux:
* See your distribution's software repository if Python 3 isn't already installed.
* Earthviewpaper supports Unity 7, GNOME 3, Zorin 2.0 (Zorin OS 12), MATE (1.14), and Budgie.
* Cinnamon and Pantheon should work, but are untested.
* In a terminal: ```python3 /path/to/earthviewpaper.py```
* XFCE and LXQT will be supported sometime in the future.
* MATE 1.16 support will be added soon.
* There are multiple ways to add to your distribution's startup such as: through a GUI, adding it to your crontab, adding it as a systemd service, and more.

####Unsupported Desktop Enironments/WM's:
#####The script can still download and save the wallpaper, despite not being able to change the wallpaper on its own.
* [KDE Plasma](https://www.reddit.com/r/linux/comments/4k1wht/i_made_a_script_that_changes_your_wallpaper_based/d3cvat2), LXDE, PIXEL, Enlightenment, Deepin, Unity 8.
* Older GTK2 based DE's.
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
2. ChromeOS (need to learn JS).
3. Look into multi monitor configurations.
4. Look into timed wallpaper changing.
5. Look into adding more wallpaper sources.

##Unlikely:
1. BSD
2. MacOS (no ability to test)
