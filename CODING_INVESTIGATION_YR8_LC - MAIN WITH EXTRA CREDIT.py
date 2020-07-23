#######################################################################################################################
# In this code I will be determining the settings required for a camera based on inputted settings from the user in   #
# in order to allow for an effective and high quality photo to be accomplished. This code can determine aperture,     #
# shutterspeed and ISO based off the inputs of the previous three, while maintining a steady baseline. If the lighting#
# condition is brighter, the baseline brightness decreases and vice versa. If a user enters values of which a         #
# brightness baseline cannot be achieved, the program will prompt the user to increase or decrease certain settings to#
# accommodate a brightness baseline which is sought. In addition, this code is formidable against erroneous user      #
# inputs and will not crash at the plight of receiving a false or ill-typed entry. Based on the user's input, the code#
# can recommend 1, 2 or 3 settings, depending on the user's preference. I have also used some object oriented         #
# programming in this code. Selecting the lighting condition is easier as the code allows the user to enter their city#
# or suburb to generate an automatic weather report and status in their area.                                         #
#######################################################################################################################

#BY JOHN PEIRIS

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
#PLAYING CAMERA SOUND FUNCTION
def PlayCameraSound(): #Creates a function to play a camera sound which can be used later
    filename = '/Users/Joel/Downloads/camera-shutter-click-06.wav' #Setting the filename
    wave_obj = sa.WaveObject.from_wave_file(filename) #Converts wave file to audio and processes it
    play_obj = wave_obj.play() #Plays processed file

#######################################################################################################################
#HOW TO SET CAMERA SETTINGS VIDEO FUNCTION
def settingvid():
    showvid = str(input("Would you like to see how to set ISO, shutterspeed and aperture (Y | N)? ")) #Ask the user if they want to see a video to help them
    while showvid not in ["Y", "N"]: #If the user did not enter yes or no, ask again
        print("You did not enter a valid input. Please try again.") #Inform the user of their error
        time.sleep(1)
        showvid = str(input("Would you like to see how to set ISO, shutterspeed and aperture? (Y | N)")) #Ask the user if they want to see a video to help them
    if showvid in "Y": #The user wants to see a video on how to set ISO, shutterspeed and aperture
        import webbrowser #Import the module to open a url
        webbrowser.open('https://www.youtube.com/watch?v=6_B8pVoANyY') #Open a youtube video on how to set shutterspeed, ISO and aperture
        print("Happy photography! :)")
    elif showvid in "N": #The user does not want to see how to set their camera settings
        print("Happy photography! :)")

#######################################################################################################################
#GETTING WEATHER DATA
def WeatherGenerator():
    city = str(input("What city/suburb do you live in? This can generate weather reports and help determine settings and the lighting condition. If you do not want to enter this, type N: ")) #Ask the user to enter their city to determine weather. If the user does not want to, they can type N.
    def weather_data(query): #Java code to open a link and open the java code of it.
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
        return res.json();
    def print_weather(result,city): #Java code to access weather data from the Java code of the website
        print("{}'s temperature: {}°C ".format(city,result['main']['temp'])) #Temperature in the city
        time.sleep(0.5)
        print("Description: {}".format(result['weather'][0]['description'])) #Description of the city
        time.sleep(0.5)
        print("Weather: {}".format(result['weather'][0]['main'])) #Weather of the city
    def main():
        if city == 'N' or city == 'n': #The user does not want to disclose their city
            print("Okay. Your privacy is acknowledged.") #Accept their chose
        else: #The user will enter their city
            try: #Try to find the city. If it is not found, an error will not throw
                query='q='+city; #To open link, the city name becomes part of it
                w_data=weather_data(query); #Runs the weather_data(query) (referenced above) to access weather data on the website
                print_weather(w_data, city) #Runs the print_weather function to print the weather attributes in that area which are accessed from the website
            except: #If the city was not found, inform the user.
                print('City name not found...') #Inform the user that the city was not found
    if __name__=='__main__':
        main()

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
#FUNCTION TO ASK FOR A RATING AFTER THE USER USES IT
def ask_for_rating(): #Creates a function
    rating = input("Did you like this code? If so, please rate out of 5 stars. If you do not want to rate, type N: ") #Asks the user to enter a rating
    if rating in "N": #if the user does not want to enter a rating, they can type N.
        print("Thank you :)") #Thanks the user
    else:
        f = open('/Users/Joel/OneDrive - education.wa.edu.au/Ratings.txt') #Opens a rating text file to store ratings by the user
        f.write(rating) #Writes in the text file the rating the user enters
        print("Thank you :)") #Thanks the user

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
    WeatherGenerator() #Generate weather in the user's area. Help for the user to enter lighting condition.
    PlayCameraSound()
    lc = input("What is the lighting condition? (A number between 1 and 7)? [1 - Dusk, 2 - Sunset/shade, 3 - Overcast, 4 - Cloudy, 5 - Lightly cloudy, 6 - Sunny, 7 - Snow/sand]: ") #Ask the user to enter the lighting condition
    PlayCameraSound()
    allowedanswers = {'1', '2', '3', '4', '5', '6', '7'} #List of lighting condition reference numbers which are allowed
    while lc not in allowedanswers: #If the user entered a number that is not a referenced lighting condition, it will ask the user to re-enter the lighting condition. This stops errors.
        print("you did not enter a valid lighting condition. Please try again.") #Inform the user of their error
        time.sleep(1.5)
        lc = input("What is the lighting condition? (A number between 1 and 7)? [1 - Dusk, 2 - Sunset/shade, 3 - Overcast, 4 - Cloudy, 5 - Lightly cloudy, 6 - Sunny, 7 - Snow/sand]: ") #Ask the user a second time
        PlayCameraSound()
    lcr = int(lightresult.get(lc)) #Yields the stop totals to achieve a baseline from the referenced lighting condition
    allowanswers = {'1', '2', '3'} #Create a set of allowed answers for the next input
    preferences = input("Would you like to determine 1, 2 or 3 settings: ") #Ask the user for how many settings they would like the program to determine
    PlayCameraSound()
    while preferences not in allowanswers: #If the user has entered a number not in the allowed list of answers for the input, they will have to keep re-entering their preference. This is a stage of error-handling
        print("You did not enter a valid setting type. Please try again.") #Inform the user of their error
        time.sleep(1.5)
        preferences = input("Would you like to determine 1, 2 or 3 settings: ") #Ask the user a second time
        PlayCameraSound()

#######################################################################################################################

#1 SETTING TO BE RECOMMENDED
    if preferences in "1": #One setting is to be recommended. I.e. two camera settings inputted by the user.
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
                PlayCameraSound()
                aperture = askaperture() #Sets aperture as the output of the function referenced above
                PlayCameraSound()
                while (lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture))) < 0: #Calculate if the brightness created will be below baseline
                    print("The brightness this image will have is too low. It is recommended that you increase your shutterspeed and aperture settings by", abs(0-(lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                    PlayCameraSound()
                    aperture = askaperture #Sets aperture as the output of the function referenced above
                    PlayCameraSound()
                while (lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture))) > 7: #Calculate if the brightness created will be above baseline
                    print("The brightness this image will have is too high. It is recommended that you decrease your shutterspeed and aperture settings by", abs(7-(lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                    PlayCameraSound()
                    aperture = askaperture() #Sets aperture as the output of the function referenced above
                    PlayCameraSound()
                print("You entered: Shutterspeed -",shutterspeed, ",", "Aperture -", aperture) #Inform the user what they entered.
                verify = input("Is this correct? (Y | N) ") #Ask the user if the information they entered was correct.
                PlayCameraSound()
                verify.upper() #Format the user input.
            x = lcr-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture)) #Calculate the stops left to achieve a baseline.
            print("Your ISO setting should be set to", isosettings[x]) #Output the desired setting for the user
            PlayCameraSound()
            #Print the final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", shutterspeed, "ISO setting:", isosettings[x])
            answerlist = [lightingconditions.get(lc), aperture, shutterspeed, isosettings[x]] #Create an answers list to be used by the generating answer table function
            PlayCameraSound()
            gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
            PlayCameraSound()
            settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
            PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            PlayCameraSound()

#######################################################################################################################

#SECOND CODE TYPE: DETERMINING SHUTTERSPEED BY APERTURE AND ISO SETTINGS
        elif setting in '2': #Shutterspeed settings to be determined
            verify = 'N' #To be used in the following lines
            #The user will be asked if the information they entered is correct. If it is not, they will re-enter it:
            while verify in 'N':
                ISO = askiso() #Sets ISO as the output of the function referenced above
                PlayCameraSound()
                aperture = askaperture() #Sets aperture as the output of the function referenced above
                PlayCameraSound()
                while (lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture))) < 0: #If the entered settings create a brightness below the baseline, ask the user to re-enter
                    print("The brightness this image will have is too low. It is recommended that you increase your ISO by", abs(0-(lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    ISO = askiso() #Sets ISO as the output of the function referenced above
                    PlayCameraSound()
                    aperture = askaperture() #Sets aperture as the output of the function referenced above
                    PlayCameraSound()
                while (lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture))) > 7: #If the entered settings create a brightness above the baseline, ask the user to re-enter
                    print("The brightness this image will have is too high. It is recommended that you decrease your ISO by", abs(7-(lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    ISO = askiso() #Sets ISO as the output of the function referenced above
                    PlayCameraSound()
                    aperture = askaperture() #Sets aperture as the output of the function referenced above
                    PlayCameraSound()
                print("You entered: ISO -",ISO, ",", "Aperture -", aperture) #Inform the user the settings they entered.
                verify = input("Is this correct? (Y | N) ") #Ask the user if the settings they entered was correct.
                PlayCameraSound()
                verify.upper() #Format the user's input
            x = lcr-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture)) #Calculate the number of stops required to reach the baseline brightness
            print("Your shutterspeed setting should be set to", shuuterspeedsettings[x]) #Print the shutterspeed setting determined
            PlayCameraSound()
            #Output final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", shuuterspeedsettings[x], "ISO setting:", ISO)
            answerlist = [lightingconditions.get(lc), aperture, shuuterspeedsettings[x], ISO] #Create an answers list to be used by the generating answer table function
            PlayCameraSound()
            gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
            PlayCameraSound()
            settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
            PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            PlayCameraSound()

#######################################################################################################################

#THIRD CODE TYPE: DETERMINING APERTURE BY ISO AND SHUTTERSPEED SETTINGS
        elif setting in '3': #Aperture setting to be determined
            verify = 'N' #To be used in following lines
            #The user will be asked if the information they entered is correct. If it is not, they will re-enter it:
            while verify in 'N':
                ISO = askiso() #Sets ISO as the output of the function referenced above
                PlayCameraSound()
                shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                PlayCameraSound()
                while (lcr-int(shuuterspeedsettings.index(shutterspeed))-int(isosettings.index(ISO))) < 0: #If the entered settings create a brightness below the baseline, ask the user to re-enter
                    print("The brightness this image will have is too low. It is recommended that you increase your ISO or shutterspeed by a total of", abs(0-(lcr-int(shuuterspeedsettings.index(shutterspeed))-int(isosettings.index(ISO)))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    ISO = askiso() #Sets ISO as the output of the function referenced above
                    PlayCameraSound()
                    shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                    PlayCameraSound()
                while (lcr-int(isosettings.index(ISO))-int(shuuterspeedsettings.index(shutterspeed))) > 7: #If the entered settings create a brightness above the baseline, ask the user to re-enter
                    print("The brightness this image will have is too high. It is recommended that you decrease your ISO or shutterspeed by a total of", abs((9-(lcr-int(shuuterspeedsettings.index(shutterspeed))-int(isosettings.index(ISO))))), "stop(s).") #Inform the user of the error created
                    time.sleep(1.5)
                    ISO = askiso() #Sets ISO as the output of the function referenced above
                    PlayCameraSound()
                    shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                    PlayCameraSound()
                print("You entered: Shutterspeed -",shutterspeed, ",", "ISO -", ISO) #Inform the user of their entered settings
                verify = input("Is this correct? (Y | N) ") #Ask the user if the information they entered is correct
                PlayCameraSound()
                verify.upper() #Format the verification answer
                x = lcr-int(isosettings.index(ISO))-int(shuuterspeedsettings.index(shutterspeed)) #Calculate the number of stops remaining to achieve a baseline brightness
                apertureanswer = Aperturesettings[x] #Output the desired setting
            #Outputting final answer
            print("Your aperture setting should be set to", apertureanswer)
            PlayCameraSound()
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", apertureanswer, " shutterspeed setting:", shutterspeed, "ISO setting:", ISO)
            answerlist = [lightingconditions.get(lc), apertureanswer, shutterspeed, ISO] #Create an answers list to be used by the generating answer table function
            PlayCameraSound()
            #Generate table of settings for the user
            gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
            PlayCameraSound()
            settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
            PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            PlayCameraSound()

#######################################################################################################################

#2 SETTINGS TO BE RECOMMENDED
    elif preferences in "2": #Two settings to be recommended
        setting = input("Which setting do you want to enter into the program (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ") #Ask the user for the setting they want to enter
        PlayCameraSound()
        while setting not in allowanswers: #If the user did not enter a valid input, ask again
            print("You did not enter a valid setting type. Please try again.")
            time.sleep(1.5)
            setting = input("Which setting do you want to enter into the program (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ")
        PlayCameraSound()
#######################################################################################################################

#ISO INPUTTED
        if setting in '1': #ISO inputted -> Determining shutterspeed and aperture
            ISO = askiso() #Sets ISO as the output of the function referenced above
            while (lcr - (isosettings.index(ISO))) < 0: #If the setting entered creates a brightness below the baseline brightness for the lighting condition, inform the user and ask again
                print("The entered ISO setting is too low. Please increase by", (0-lcr+isosettings.index(ISO)), "stops") #Inform the user of the error created and how they should change their setting
                ISO = askiso() #Sets ISO as the output of the function referenced above
                PlayCameraSound()
            while (lcr - (isosettings.index(ISO))) > 14: #If the setting entered creates a brightness above the baseline brightness for the lighting condition, inform the user and ask again
                print("The entered ISO setting is too high. Please decrease by", abs(14-lcr+isosettings.index(ISO)), "stops") #Inform the user of the error created and how they should adjust their setting
                ISO = askiso() #Sets ISO as the output of the function referenced above
                PlayCameraSound()
            x = int((lcr-isosettings.index(ISO))/2) #Calculate the stops remaining and divide it between the two settings remaining
            y = lcr - isosettings.index(ISO) - x #Calculate the stops remaining and divide it between the two settings remaining
            #Output final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", Aperturesettings[x], " shutterspeed setting:", shuuterspeedsettings[y], "ISO setting:", ISO)
            answerlist = [lightingconditions.get(lc), Aperturesettings[x], shuuterspeedsettings[y], ISO] #Create an answers list to be used by the generating answer table function
            PlayCameraSound()
            #Generate table of settings for the user
            gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
            PlayCameraSound()
            settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
            PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            PlayCameraSound()

#######################################################################################################################

#SHUTTERSPEED INPUTTED
        elif setting in '2': #Shutter speed inputted -> Determining ISO and aperture settings
            shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
            PlayCameraSound()
            while (lcr - (shuuterspeedsettings.index(shutterspeed))) < 0: #If the entered setting creates a brightness below the baseline brightness for that lighting condition, ask again
                print("The entered shutterspeed setting is too high. Please decrease by", (0-lcr+shuuterspeedsettings.index(shutterspeed)), "stops") #Inform the user of the error created and how they should adjust the settings
                shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                PlayCameraSound()
            while (lcr - (shuuterspeedsettings.index(shutterspeed))) > 14: #If the entered setting creates a brightness above the baseline brightness for that lighting condition, ask again
                print("The entered shutterspeed setting is too low. Please increase by", abs(14-lcr+shuuterspeedsettings.index(shutterspeed)), "stops") #Inform the user of the error created and how they should adjust the settings
                shutterspeed = askshutterspeed() #Sets shutterspeed as the output of the function referenced above
                PlayCameraSound()
                x = int((lcr-shuuterspeedsettings.index(shutterspeed))/2) #Calculate the stops remaining and divide it between the two settings remaining
                y = lcr - shuuterspeedsettings.index(shutterspeed) - x #Calculate the stops remaining and divide it between the two settings remaining
            x = int((lcr-shuuterspeedsettings.index(shutterspeed))/2) #Calculate the stops remaining and divide between the 2 remaining settings (ISO and aperture)
            y = lcr - shuuterspeedsettings.index(shutterspeed) - x #Calculate the stops remaining and divide between the 2 remaining settings (ISO and aperture)
            #Output final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", Aperturesettings[x], " shutterspeed setting:", shutterspeed, "ISO setting:", isosettings[y])
            answerlist = [lightingconditions.get(lc), Aperturesettings[x], shutterspeed, isosettings[y]] #Create an answers list to be used by the generating answer table function
            PlayCameraSound()
            #Generate table of settings for the user
            gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
            PlayCameraSound()
            settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
            PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            PlayCameraSound()

#######################################################################################################################

#APERTURE INPUTTED
        elif setting in '3': #Aperture inputted -> Determining shutterspeed and ISO settings
            aperture = askaperture() #Sets aperture as the output of the function referenced above
            PlayCameraSound()
            while (lcr - (Aperturesettings.index(aperture))) < 0: #If the entered setting creates a brightness below the baseline brightness for that lighting condition, ask the user to re-enter
                print("The entered aperture setting is too high. Please decrease by", (0-lcr+Aperturesettings.index(aperture)), "stops") #Inform the user of the error created and how they should adjust their settings
                aperture = askaperture() #Sets aperture as the output of the function referenced above
                PlayCameraSound()
            while (lcr - (Aperturesettings.index(aperture))) > 14: #If the entered setting creates a brightness above the baseline brightness for that lighting condition, ask the user to re-enter
                print("The entered aperture setting is too low. Please increase by", (14-lcr+Aperturesettings.index(aperture)), "stops") #Inform the user of the error created and how they should adjust their settings
                aperture = askaperture() #Sets aperture as the output of the function referenced above
                PlayCameraSound()
            x = int((lcr-Aperturesettings.index(aperture))/2) #Calculate the stops remaining to achieve a baseline brightness and divide it between the 2 remaining settings (ISO and shutterspeed)
            y = lcr - Aperturesettings.index(aperture) - x #Calculate the stops remaining to achieve a baseline brightness and divide it between the 2 remaining settings (ISO and shutterspeed)
            #Output final settings:
            print("Final settings are:")
            time.sleep(1.5)
            print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", shuuterspeedsettings[y], "ISO setting:", isosettings[x])
            answerlist = [lightingconditions.get(lc), aperture, shuuterspeedsettings[y], isosettings[x]] #Create an answers list to be used by the generating answer table function
            PlayCameraSound()
            #Generate table of settings for the user
            gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
            PlayCameraSound()
            settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
            PlayCameraSound()
            runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
            PlayCameraSound()

#######################################################################################################################

#3 SETTINGS TO BE RECOMMENDED
    elif preferences in "3": #Three settings to be recommended based off the lighting condition advised by the user.
        print("ISO:", isosettings[8-int(lc)],  " Shutterspeed:", shuuterspeedsettings[8-int(lc)], " Aperture:", Aperturesettings[8-int(lc)] ) #Calculate the number of stops needed to achieve a stable baseline and print the settings for ISO, shutterspeed and aperture
        answerlist = [lightingconditions.get(lc), Aperturesettings[8-int(lc)], shuuterspeedsettings[8-int(lc)], isosettings[8-int(lc)]] #Create an answers list to be used by the generating answer table function
        PlayCameraSound()
        #Generate table of settings for the user
        gentable() #Calls function to generate a table of answers from the answerlist. Function referenced above.
        PlayCameraSound()
        settingvid() #Calls function to ask if the user wants to see how to set their camera settings. Function referenced above
        PlayCameraSound()
        runagain = input("Would you like to run this code again? (Y | N) ") #Ask the user if they want to run again.
        PlayCameraSound()

#######################################################################################################################

#ENDING OF CODE
ask_for_rating() #Asks the user to enter a rating.
print("Thank you for using this code. If you liked it, please rate 100%", "on rubric and Google reviews. Thank you for your compliance. Goodbye!") #Flatter the user
PlayCameraSound()
PlayCameraSound()

#######################################################################################################################
####THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END####