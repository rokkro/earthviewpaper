# Earthviewpaper
Earthviewpaper grabs a random image from [Google's Earthview]( https://earthview.withgoogle.com ) site and sets it as your wallpaper.

<p align="center">
  <img src="https://cdn3.iconfinder.com/data/icons/faticons/32/globe-01-128.png"/>
</p>

##Linux:
* See your distribution's software repository if Python 3 isn't already installed.
* Earthviewpaper supports Unity 7 and GNOME 3. Cinnamon, Pantheon, and MATE should work, but are untested.
* KDE Plasma wallpaper-changning support doesnt seem possible/reliable (see [this](https://www.reddit.com/r/linux/comments/4k1wht/i_made_a_script_that_changes_your_wallpaper_based/d3cvat2)). The script can still download and save the wallpaper, however.
* In a terminal: ```python3 /path/to/earthviewpaper.py```

##Windows:
* You'll probably need to [install Python 3](https://www.python.org/downloads/windows/).
* Earthviewpaper should work on Windows Vista and newer.
* Double click to run, or in cmd: ```python C:\path\to\earthviewpaper.py```

####Adding to Windows Startup:
* Place a shortcut to the script in your startup folder (enter ```shell:startup``` in Run to access).

##Todo:
1. Look into adding support for XFCE, LXQT, and Deepin.
2. MacOS support, Maybe BSD support?
3. Test stuff.
