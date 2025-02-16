# Packages
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from PIL import ImageGrab
import pygetwindow as gw
from transformers import pipeline, logging
import numpy as np
import cv2
import llmCaller as llm
## Functions ##

def get_screen_data():
    # Screenshotting Entire Screen
    # Returns a screenshot of the full screen
    screenshot = ImageGrab.grab(bbox = None)
    print("Got Screenshot")

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
    return classification[0]['label'].split(", ")[0]

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

def getPromptForImageClassification():

    return "You are a audio mixer. You love to hear about items around the world that might be seen on a computer screen. You then return a list in the format [\"theme\"], where \"theme\" is a list of no more than 5 spotify themes. What you see is: "

def cleanThemes(themesString):

    splitString = themesString.replace("\"", "").split("[")
    print("Length of Split String: " + str(len(splitString)))
    if len(splitString) > 2:

        print("Something Terrible Has Occured, Pray and Return")
        return splitString[-1].replace("]", "")
    
    elif len(splitString) == 2:

        return splitString[-1].replace("]", "")

    else:

        #Did not follow the format so we are just praying that it fits
        return splitString[0]

def dataMain(apiKey):

    logging.set_verbosity_error()
    screenshot, allWindows, activeWindow = get_screen_data()
    classification = classify_screenshot(screenshot)

    if "web" in classification or "screen" in classification or "monitor" in classification or "notebook" in classification:

        activeWindow.title
        print("Type:" + activeWindow.title)
        themes = llm.llmCaller(api_key=apiKey).getResponse(prompt=getPromptForImageClassification() + activeWindow.title)['choices'][0]['message']['content']
    
    else:

        print("PreCLassifcation Classification: " + classification)
        themes = llm.llmCaller(api_key=apiKey).getResponse(prompt=getPromptForImageClassification() + classification)['choices'][0]['message']['content']

    return cleanThemes(themes)