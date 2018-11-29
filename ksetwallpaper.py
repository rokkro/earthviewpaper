#!/usr/bin/env python3

# ORIGINAL PROJECT SOURCE: https://github.com/pashazz/ksetwallpaper

import dbus


def change_wallpaper_plasma(image_path):

    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
        d.writeConfig("Image", "file://%s")
    }
    """

    # Attach to dbus
    bus = dbus.SessionBus()

    # Get plasmashell interface
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')

    # Run javascript to update wallpaper on all plasma desktops
    plasma.evaluateScript(jscript % image_path)
