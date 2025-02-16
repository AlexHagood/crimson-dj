# Packages
from PIL import ImageGrab
import pygetwindow as gw
from transformers import pipeline, logging
import numpy as np
import cv2

## Functions ##

def get_screen_data():
    # Screenshotting Entire Screen
    # Returns a screenshot of the full screen
    screenshot = ImageGrab.grab(bbox = None)

    # Get a list of all windows with their basic information
    # Returns a list of all windows with their metadata
    allWindows = gw.getAllWindows()

    # Identify active window
    # Returns the active window's metadata
    activeWindow = gw.getActiveWindow()

    return screenshot, allWindows, activeWindow

# Classify a screenshot
def classify_screenshot(screenshot):
    # Classify fullScreenshot with text (Google)
    image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224", processor="google/vit-base-patch16-224", use_fast=True)
    classification = image_classifier(screenshot)
    return classification

# This function is useless now
# Process a screenshot to its edges
def procress_screenshot(screenshot):

    # Convert screenshot to a NumPy array
    screenshotNP = np.array(screenshot)

    # Convert the image to RGB
    screenshotRGB = cv2.cvtColor(screenshotNP, cv2.COLOR_BGR2RGB)

    # Convert the image to grayscale
    screenshotGrayScale = cv2.cvtColor(screenshotRGB, cv2.COLOR_RGB2GRAY)

    # Apply edge detection
    edges = cv2.Canny(screenshotGrayScale, 100, 200)

    return edges

## Main ##

# Suppress warnings in output
logging.set_verbosity_error()

# Run functions
screenshot, allWindows, activeWindow = get_screen_data()
classify_screenshot(screenshot)