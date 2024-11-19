# Import required libraries
import os
import time
import ctypes
import pyttsx3

# Set the repeat interval for the task (in seconds)
REPEAT_INTERVAL = 5  # Repeat frequency in seconds

# Initialize the text-to-speech engine and adjust speaking rate
engine = pyttsx3.init()  
engine.setProperty('rate', 150)  # Adjust speaking rate (speed of speech)

# Infinite loop to repeat the task
while True:
    # Trigger text-to-speech to remind to drink water
    engine.say("Hey, it's time to drink water!")
    engine.runAndWait()  # Wait until the speech is finished before continuing

    # Windows notification using pop up was given by chat GPT
    # Windows notification using ctypes (this is a pop-up message box)
    title = "Reminder"  # Title for the pop-up window
    message = "Hey, it's time to drink water!"  # Message displayed in the pop-up window
    # This function creates a pop-up with the provided title and message
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)

    # Wait for the specified interval before repeating the task
    time.sleep(REPEAT_INTERVAL)

# To run this task automatically on Windows, you can use the "Windows Task Scheduler"
# Research on the topic "Windows Task Scheduler" to learn how to set up this script 
# to run at specific times or on system startup automatically.
