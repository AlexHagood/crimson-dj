# Packages
from PIL import ImageGrab
import pygetwindow as gw
from transformers import pipeline, logging
import numpy as np
import cv2

## Functions ##

def get_image_data():
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

    # Display edge detection result
    cv2.imshow("Edge Detection", edges)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Classify a screenshot (without processing)
def classify_screenshot_no_processing(screenshot):
    # Classify fullScreenshot with text (Google)
    image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224", use_fast=True)
    classification = image_classifier(screenshot)
    print("Image Classification: ", classification)

## Main ##

# Suppress Warnings
logging.set_verbosity_error()

# Run functions
screenshot, allWindows, activeWindow = get_image_data()
procress_screenshot(screenshot)
classify_screenshot_no_processing(screenshot)