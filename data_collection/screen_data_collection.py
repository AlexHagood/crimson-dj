# Packages
from PIL import ImageGrab
import pygetwindow as gw

# Screenshotting Entire Screen
# Returns a screenshot of the full screen
fullScreenshot = ImageGrab.grab(bbox = None)

# Get a list of all windows with their basic information
# Returns a list of all windows with their metadata
allWindows = gw.getAllWindows()

# Identify active window
# Returns the active window's metadata
activeWindow = gw.getActiveWindow()