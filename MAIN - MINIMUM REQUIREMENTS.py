#YEAR 8 CODING INVESTIGATION MINIMUM REQUIREMENTS
#######################################################################################################################
#IMPORTS AND ERRORS
#IMPORTS
from tkinter import * #Used for table output
import time #Used for timing
import math #Used for math
from collections import OrderedDict #Used for ordering dictionaries
from PIL import Image #Used for image generation
import matplotlib.pyplot as plt; plt.rcdefaults() #Used for table output
import numpy as np #Used for table output
import matplotlib.pyplot as plt #Used for table output
from prettytable import PrettyTable #Used for table output
import requests #Used for weather data
from pprint import pprint #Used for weather data
import os #Used for the code to talk
import sys #Used for the code to talk
import simpleaudio as sa #Used to play camera sound

#ERROR HANDLING
EOFError = False
FutureWarning = False
ArithmeticError = False
AssertionError = False
AttributeError = False
BlockingIOError = False
BrokenPipeError = False
BufferError = False
BytesWarning = False
ChildProcessError = False
ConnectionAbortedError = False
ConnectionError = False
ConnectionRefusedError = False
ConnectionResetError = False
DeprecationWarning = False
IndentationError = False
ImportError = False
IndexError = False
InterruptedError = False
IOError = False
IsADirectoryError = False
KeyError = False
LookupError = False
MemoryError = False
OSError = False
KeyboardInterrupt = False
NameError = False
NotADirectoryError = False
NotImplementedError = False
OverflowError = False
PermissionError = False
ProcessLookupError = False
RecursionError = False
ReferenceError = False
RuntimeError = False
SyntaxError = False
SystemError = False
TabError = False
TimeoutError = False
TypeError = False
UnboundLocalError = False
UnicodeDecodeError = False
UnicodeEncodeError = False
UnicodeError = False
UnicodeTranslateError = False
ValueError = False
FileNotFoundError = False
FileExistsError = False
FloatingPointError = False
WindowsError = False
ZeroDivisionError = False

#######################################################################################################################
#DICTIONARIES AND LISTS
isosettings = ["6400", "3200","1600","800","400","200","100","50"] #List of all ISO settings

shuuterspeedsettings = ['1/30s', '1/60s', '1/125s', '1/250s', '1/500s', '1/1000s', '1/2000s', '1/4000s'] #List of all shutterspeed settings

Aperturesettings = ["f/2.0","f/2.8","f/4.0", "f/5.6","f/8.0","f/11","f/16","f/22"] #List of all aperture settings

lightingconditions = {"1": "Dusk", "2":"Sunset/shade", "3":"Overcast", "4":"Cloudy", "5":"Lightly cloudy", "6":"Sunny", "7":"Snow/sand"} #List of lighting conditions with corresponding reference numbers

lightresult = {"1": "21", "2": "18", "3":"15", "4":"12", "5":"9", "6":"6", "7":"3"} #List of lighting condition reference numbers with assigned stop totals

#######################################################################################################################
#TABLE FUNCTION OF AVAILABLE SETTINGS
def availablesettings(): #Creating a table of available settings. This function can be called upon later.
    x = PrettyTable() #Creates a table

    column_names = ["Stop Number:", "ISO Settings", "Shutterspeed Settings", "Aperture settings"] #Adds setting names to the table

    x.add_column(column_names[0], ["8th", "7th", "6th", "5th", "4th", "3rd", "2nd", "1st"]) #Adds the stop number column to the table
    x.add_column(column_names[1], ["6400", "3200","1600","800","400","200","100","50"]) #Adds the ISO settings column to the table
    x.add_column(column_names[2], ['1/30s', '1/60s', '1/125s', '1/250s', '1/500s', '1/1000s', '1/2000s', '1/4000s']) #Adds the shutterspeed settings column to the table
    x.add_column(column_names[3], ["f/2.0","f/2.8","f/4.0", "f/5.6","f/8.0","f/11","f/16","f/22"]) #Adds the aperture settings column to the table

    print(x) #Prints the table

#######################################################################################################################
#FUNCTION TO GENERATE A TABLE OF RESULTS FOR THE RECOMMENDED SETTINGS
def gentable(): #Creates a function for creating tables which can be used later. This saves many lines of code.
    class Table: #Object code for a table

        def __init__(self,root):

            # code for creating table
            for i in range(total_rows):
                    for j in range(total_columns):

                        self.e = Entry(root, width=20, fg='blue',
                                    font=('Arial',16,'bold'))

                        self.e.grid(row=i, column=j)
                        self.e.insert(END, lst[i][j])

    # take the data
    lst = [("Lighting condition:",answerlist[0]),
        ("Aperture:", answerlist[1]),
        ("Shutterspeed:",answerlist[2]),
        ("ISO:", answerlist[3])]

    # find total number of rows and columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

    # create root window
    root = Tk()
    t = Table(root)
    root.mainloop()
    time.sleep(1)

#######################################################################################################################
#FUNCTION TO ASK ISO
def askiso(): #Creates a function of asking and verifying ISO. This saves many lines of code
    ISO = str(input("Please enter the ISO setting (e.g. 800): ")) #Ask the user to enter the ISO setting
    while ISO not in isosettings: #If the ISO setting entered is not in the allowed ISO setting list, ask the user to re-enter
        print("You did not enter a valid ISO setting. Please try again.") #Inform the user of their error.
        time.sleep(1.5)
        ISO = str(input("Please enter the ISO setting (e.g. 800): ")) #Ask the user to re-enter the ISO setting
    return ISO #Returns the user's ISO

#######################################################################################################################
#FUNCTION TO ASK SHUTTERSPEED
def askshutterspeed(): #Creates a function of asking and verifying shutterspeed. This saves many lines of code
    shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000s): ")) #Ask the user to enter the shutterspeed setting
    while shutterspeed not in shuuterspeedsettings: #If the user entered a setting that is not an EXISTING SETTING, the user will be asked to re-enter.
        print("You did not enter a valid shutterspeed setting. Please try again.") #Inform the user of their error
        time.sleep(1.5)
        shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000s): ")) #Ask the user a second time
    return shutterspeed #Returns the user's shutterspeed

#######################################################################################################################
#FUNCTION TO ASK APERTURE
def askaperture(): #Creates a function of asking and verifying aperture. This saves many lines of code
    aperture = str(input("Please enter the aperture setting (in the form f/16): ")) #Ask the user to enter the aperture setting
    while aperture not in Aperturesettings: #If the user entered a setting that is not an EXISTING SETTING, the user will be asked to re-enter.
        print("You did not enter a valid aperture setting. Please try again.") #Inform the user of their error
        time.sleep(1.5)
        aperture = str(input("Please enter the aperture setting (in the form f/16): ")) #Ask the user a second time
    return aperture #Returns the user's aperture

#######################################################################################################################
#INTRODUCTION AND CODE CHOICE
runagain = "Y" #Assign a runagain variable which can be used to determine if the user wants to run the code again.
print("Welcome to this photography settings Python code. Follow the prompts on the screen. Enjoy! :)") #Introduction to the code
time.sleep(1)
print("Here is a table of all the available settings. This will assist in choosing the correct ISO, shutterspeed and aperture.") #Prove the user with a table of all available settings. The user can refer to this later.
time.sleep(1)
availablesettings() #Runs the available settings function referenced above
time.sleep(1)
while runagain in "Y": #Initially, runagain is true, so the code runs once. If runagain still equals yes, it will "run again".
            
      
    lc = input("What is the lighting condition? (A number between 1 and 7)? [1 - Dusk, 2 - Sunset/shade, 3 - Overcast, 4 - Cloudy, 5 - Lightly cloudy, 6 - Sunny, 7 - Snow/sand]: ") #Ask the user to enter the lighting condition
      
    allowedanswers = {'1', '2', '3', '4', '5', '6', '7'} #List of lighting condition reference numbers which are allowed
    while lc not in allowedanswers: #If the user entered a number that is not a referenced lighting condition, it will ask the user to re-enter the lighting condition. This stops errors.
        print("you did not enter a valid lighting condition. Please try again.") #Inform the user of their error
        time.sleep(1.5)
        lc = input("What is the lighting condition? (A number between 1 and 7)? [1 - Dusk, 2 - Sunset/shade, 3 - Overcast, 4 - Cloudy, 5 - Lightly cloudy, 6 - Sunny, 7 - Snow/sand]: ") #Ask the user a second time
          
    lcr = int(lightresult.get(lc)) #Yields the stop totals to achieve a baseline from the referenced lighting condition
    allowanswers = {'1', '2', '3'} #Create a set of allowed answers for the next input

#######################################################################################################################

#1 SETTING TO BE RECOMMENDED
    if int(lcr) > -1: #Lcr must be positive
        setting = input("Which setting do you want the program to recommend (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ") #Ask the user which camera setting they want the program to recommend.
        while setting not in allowanswers: #Allowed answers are 1, 2 and 3. If the user does not enter one of these numbers, they will have to keep re-entering until they do. This stops errors.
            print("You did not enter a valid setting type. Please try again.") #Inform the user of their error.
            time.sleep(1.5)
            setting = input("Which setting do you want the program to recommend (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ") #Ask the user a second time

#######################################################################################################################

#FIRST CODE TYPE: DETERMINING ISO BY APERTURE AND SHUTTERSPEED SETTINGS
        if setting in '1': #ISO to be recommended
            verify = 'N' #To be used in next lines
            #The user will be asked if the information they entered is correct. If it is not, they will re-enter it:
            while verify in 'N':
                shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                  
                aperture = askaperture() #Sets aperture as the output of the function referenced above
                  
                while (lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture))) < 0: #Calculate if the brightness created will be below baseline
                    print("The brightness this image will have is too low. It is recommended that you increase your shutterspeed and aperture settings by", abs(0-(lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                      
                    aperture = askaperture() #Sets aperture as the output of the function referenced above
                      
                while (lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture))) > 7: #Calculate if the brightness created will be above baseline
                    print("The brightness this image will have is too high. It is recommended that you decrease your shutterspeed and aperture settings by", abs(7-(lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                      
                    aperture = askaperture() #Sets aperture as the output of the function referenced above
                      
                print("You entered: Shutterspeed -",shutterspeed, ",", "Aperture -", aperture) #Inform the user what they entered.
                verify = input("Is this correct? (Y | N) ") #Ask the user if the information they entered was correct.
                  
                verify.upper() #Format the user input.
            x = lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture)) #Calculate the stops left to achieve a baseline.
            print("Your ISO setting should be set to", isosettings[x]) #Output the desired setting for the user
              
            #Print the final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", shutterspeed, "ISO setting:", isosettings[x])
            answerlist = [lightingconditions.get(lc), aperture, shutterspeed, isosettings[x]] #Create an answers list to be used by the generating answer table function
              
            gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
              
                  #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
              
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
              

#######################################################################################################################

#SECOND CODE TYPE: DETERMINING SHUTTERSPEED BY APERTURE AND ISO SETTINGS
        elif setting in '2': #Shutterspeed settings to be determined
            verify = 'N' #To be used in the following lines
            #The user will be asked if the information they entered is correct. If it is not, they will re-enter it:
            while verify in 'N':
                ISO = askiso() #Sets ISO as the output of the function referenced above
                  
                aperture = askaperture() #Sets aperture as the output of the function referenced above
                  
                while (lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture))) < 0: #If the entered settings create a brightness below the baseline, ask the user to re-enter
                    print("The brightness this image will have is too low. It is recommended that you increase your ISO by", abs(0-(lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    ISO = askiso() #Sets ISO as the output of the function referenced above
                      
                    aperture = askaperture() #Sets aperture as the output of the function referenced above
                      
                while (lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture))) > 7: #If the entered settings create a brightness above the baseline, ask the user to re-enter
                    print("The brightness this image will have is too high. It is recommended that you decrease your ISO by", abs(7-(lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    ISO = askiso() #Sets ISO as the output of the function referenced above
                      
                    aperture = askaperture() #Sets aperture as the output of the function referenced above
                      
                print("You entered: ISO -",ISO, ",", "Aperture -", aperture) #Inform the user the settings they entered.
                verify = input("Is this correct? (Y | N) ") #Ask the user if the settings they entered was correct.
                  
                verify.upper() #Format the user's input
            x = lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture)) #Calculate the number of stops required to reach the baseline brightness
            print("Your shutterspeed setting should be set to", shuuterspeedsettings[x]) #Print the shutterspeed setting determined
              
            #Output final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", shuuterspeedsettings[x], "ISO setting:", ISO)
            answerlist = [lightingconditions.get(lc), aperture, shuuterspeedsettings[x], ISO] #Create an answers list to be used by the generating answer table function
              
            gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
              
                  #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
              
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
              

#######################################################################################################################

#THIRD CODE TYPE: DETERMINING APERTURE BY ISO AND SHUTTERSPEED SETTINGS
        elif setting in '3': #Aperture setting to be determined
            verify = 'N' #To be used in following lines
            #The user will be asked if the information they entered is correct. If it is not, they will re-enter it:
            while verify in 'N':
                ISO = askiso() #Sets ISO as the output of the function referenced above
                  
                shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                  
                while (lcr-int(shuuterspeedsettings.index(shutterspeed))-int(isosettings.index(ISO))) < 0: #If the entered settings create a brightness below the baseline, ask the user to re-enter
                    print("The brightness this image will have is too low. It is recommended that you increase your ISO or shutterspeed by a total of", abs(0-(lcr-int(shuuterspeedsettings.index(shutterspeed))-int(isosettings.index(ISO)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    ISO = askiso() #Sets ISO as the output of the function referenced above
                      
                    shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                      
                while (lcr-int(isosettings.index(ISO))-int(shuuterspeedsettings.index(shutterspeed))) > 7: #If the entered settings create a brightness above the baseline, ask the user to re-enter
                    print("The brightness this image will have is too high. It is recommended that you decrease your ISO or shutterspeed by a total of", abs((9-(lcr-int(shuuterspeedsettings.index(shutterspeed))-int(isosettings.index(ISO))))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    ISO = askiso() #Sets ISO as the output of the function referenced above
                      
                    shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                      
                print("You entered: Shutterspeed -",shutterspeed, ",", "ISO -", ISO) #Inform the user of their entered settings
                verify = input("Is this correct? (Y | N) ") #Ask the user if the information they entered is correct
                  
                verify.upper() #Format the verification answer
                x = lcr-int(isosettings.index(ISO))-int(shuuterspeedsettings.index(shutterspeed)) #Calculate the number of stops remaining to achieve a baseline brightness
                apertureanswer = Aperturesettings[x] #Output the desired setting
            #Outputting final answer
            print("Your aperture setting should be set to", apertureanswer)
              
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", apertureanswer, " shutterspeed setting:", shutterspeed, "ISO setting:", ISO)
            answerlist = [lightingconditions.get(lc), apertureanswer, shutterspeed, ISO] #Create an answers list to be used by the generating answer table function
              
            #Generate table of settings for the user
            gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
              
                  #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
              
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
              

#######################################################################################################################

#ENDING OF CODE
print("Thank you for using this code. If you liked it, please rate 100%", "on rubric and Google reviews. Thank you for your compliance. Goodbye!") #Flatter the user

#######################################################################################################################
####THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END####