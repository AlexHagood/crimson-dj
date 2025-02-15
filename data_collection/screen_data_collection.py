# Packages
from PIL import Image, ImageGrab
import pygetwindow as gw

# Screenshotting Entire Screen
fullScreenshot = ImageGrab.grab(bbox = None)

# Get a list of windows with their basic information
allWindows = gw.getAllWindows()

# Prints all windows' information
for window in allWindows:
    print(window)