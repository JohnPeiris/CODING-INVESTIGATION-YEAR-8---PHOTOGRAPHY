#######################################################################################################################
# In this code I will be determining the settings required for a camera based on inputted settings from the user in   #
# in order to allow for an effective and high quality photo to be accomplished. This code can determine aperture,     #
# shutterspeed and ISO based off the inputs of the previous three, while maintining a steady baseline. If a user      #
# enters values of which a brightness baseline cannot be achieved, the program will prompt the user to increase or    #
# decrease certain settings to accommodate a brightness baseline which is sought. In addition, this code is           #
# formidable against erroneous user inputs and will not crash at the plight of receiving a false or ill-typed entry.  #
#######################################################################################################################
#BY JOHN PEIRIS

#######################################################################################################################
#IMPORTS
import time
import math
from collections import OrderedDict
import time
from PIL import Image
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

#######################################################################################################################
#DICTIONARIES AND LISTS
isosettings = ["6400", "3200","1600","800","400","200","100","50"]

shuuterspeedsettings = ['1/30', '1/60', '1/125', '1/250', '1/500', '1/1000', '1/2000', '1/4000']

Aperturesettings = ["f/2.0","f/2.8","f/4.0", "f/5.6","f/8.0","f/11","f/16","f/22"]

aperturekey = {"1":"f/2.8","2":"f/4.0", "3":"f/5.6","4":"f/8.0","5":"f/11","6":"f/16","7":"f/22"}

lightingconditions = {"1": "Dusk", "2":"Sunset/shade", "3":"Overcast", "4":"Cloudy", "5":"Lightly cloudy", "6":"Sunny", "7":"Snow/sand"}

#######################################################################################################################
#INTRODUCTION AND CODE CHOICE
runagain = "Y"
print("Welcome to this photography settings Python code. Follow the prompts on the screen. Enjoy! :)")
while runagain in "Y":
    lc = input("What is the lighting condition? (A number between 1 and 7)? [1 - Dusk, 2 - Sunset/shade, 3 - Overcast, 4 - Cloudy, 5 - Lightly cloudy, 6 - Sunny, 7 - Snow/sand]: ")
    allowedanswers = {'1', '2', '3', '4', '5', '6', '7'}
    while lc not in allowedanswers:
        print("you did not enter a valid lighting condition. Please try again.")
        time.sleep(1.5)
        lc = input("What is the lighting condition? (A number between 1 and 7)? [1 - Dusk, 2 - Sunset/shade, 3 - Overcast, 4 - Cloudy, 5 - Lightly cloudy, 6 - Sunny, 7 - Snow/sand]: ")
    allowanswers = {'1', '2', '3'}
    setting = input("Which setting do you want the program to recommend (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ")
    while setting not in allowanswers:
        print("You did not enter a valid setting type. Please try again.")
        time.sleep(1.5)
        setting = input("Which setting do you want the program to recommend (A number between 1 and 3)? [1 - ISO, 2 - Shutter speed, 3 - Aperture]: ")

#######################################################################################################################
#FIRST CODE TYPE: DETERMINING ISO BY APERTURE AND SHUTTERSPEED SETTINGS
    if setting in '1':
        verify = 'N'
        while verify in 'N':
            shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
            while shutterspeed not in shuuterspeedsettings:
                print("You did not enter a valid shutterspeed setting. Please try again.")
                time.sleep(1.5)
                shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
            aperture = str(input("Please enter the aperture setting (in the form f/16): "))
            while aperture not in Aperturesettings:
                print("You did not enter a valid aperture setting. Please try again.")
                time.sleep(1.5)
                aperture = str(input("Please enter the aperture setting (in the form f/16): "))
            while (12-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture))) < 0:
                print("The brightness this image will have is too high. It is recommended that you decrease your shutterspeed setting by", abs(0-(12-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture)))), "notche(s).")
                shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
                while shutterspeed not in shuuterspeedsettings:
                    print("You did not enter a valid shutterspeed setting. Please try again.")
                    time.sleep(1.5)
                    shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
            while (12-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture))) > 7:
                print("The brightness this image will have is too low. It is recommended that you increase your shutterspeed by", abs(7-(12-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture)))), "notche(s).")
                shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
                time.sleep(1.5)
                while shutterspeed not in shuuterspeedsettings:
                    print("You did not enter a valid shutterspeed setting. Please try again.")
                    time.sleep(1.5)
                    shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
            print("You entered: Shutterspeed -",shutterspeed, ",", "Aperture -", aperture)
            verify = input("Is this correct? (Y | N) ")
            verify.upper()
        x = 12-int(shuuterspeedsettings.index(shutterspeed))-int(Aperturesettings.index(aperture))
        print("Your ISO setting should be set to", isosettings[x])
        print("Final settings are:")
        time.sleep(1.5)
        print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", shutterspeed, "ISO setting:", isosettings[x])
        class Table: 
      
            def __init__(self,root): 
            
                # code for creating table 
                for i in range(total_rows): 
                        for j in range(total_columns): 
                            
                            self.e = Entry(root, width=20, fg='blue', 
                                        font=('Arial',16,'bold')) 
                            
                            self.e.grid(row=i, column=j) 
                            self.e.insert(END, lst[i][j]) 
            
        # take the data
        lst = [("Lighting condition:",lightingconditions.get(lc)),
            ("Aperture:",aperture),
            ("Shutterspeed:",shutterspeed),
            ("ISO:", isosettings[x])]
        
        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])
        
        # create root window
        root = Tk()
        t = Table(root)
        root.mainloop()
#######################################################################################################################
#FIRST CODE TYPE: DETERMINING ISO BY APERTURE AND SHUTTERSPEED SETTINGS
    elif setting in '2':
        verify = 'N'
        while verify in 'N':
            ISO = str(input("Please enter the ISO setting (e.g. 800): "))
            while ISO not in isosettings:
                print("You did not enter a valid ISO setting. Please try again.")
                time.sleep(1.5)
                ISO = str(input("Please enter the ISO setting (e.g. 800): "))
            aperture = str(input("Please enter the aperture setting (in the form f/16): "))
            while aperture not in Aperturesettings:
                print("You did not enter a valid aperture setting. Please try again.")
                time.sleep(1.5)
                aperture = str(input("Please enter the aperture setting (in the form f/16): "))
            while (12-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture))) < 0:
                print("The brightness this image will have is too low. It is recommended that you increase your ISO by", abs(0-(12-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture)))), "notche(s).")
                time.sleep(1.5)
                ISO = str(input("Please enter the ISO setting (e.g. 800): "))
                while ISO not in isosettings:
                    print("You did not enter a valid ISO setting. Please try again.")
                    time.sleep(1.5)
                    ISO = str(input("Please enter the ISO setting (e.g. 800): "))
            while (12-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture))) > 7:
                print("The brightness this image will have is too high. It is recommended that you decrease your ISO by", abs(7-(12-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture)))), "notche(s).")
                time.sleep(1.5)
                ISO = str(input("Please enter the ISO setting (e.g. 800): "))
                while ISO not in isosettings:
                    print("You did not enter a valid ISO setting. Please try again.")
                    time.sleep(1.5)
                    ISO = str(input("Please enter the ISO setting (e.g. 800): "))
            print("You entered: ISO -",ISO, ",", "Aperture -", aperture)
            verify = input("Is this correct? (Y | N) ")
            verify.upper()
        x = 12-int(isosettings.index(ISO))-int(Aperturesettings.index(aperture))
        print("Your shutterspeed setting should be set to", shuuterspeedsettings[x])
        print("Final settings are:")
        time.sleep(1.5)
        print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", aperture, " shutterspeed setting:", shuuterspeedsettings[x], "ISO setting:", ISO)

#######################################################################################################################
#FIRST CODE TYPE: DETERMINING ISO BY APERTURE AND SHUTTERSPEED SETTINGS
    elif setting in '3':
        verify = 'N'
        while verify in 'N':
            ISO = str(input("Please enter the ISO setting (e.g. 800): "))
            while ISO not in isosettings:
                print("You did not enter a valid ISO setting. Please try again.")
                time.sleep(1.5)
                ISO = str(input("Please enter the ISO setting (e.g. 800): "))
            shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
            while shutterspeed not in shuuterspeedsettings:
                print("You did not enter a valid shutterspeed setting. Please try again.")
                time.sleep(1.5)
                shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
            while (12-int(shuuterspeedsettings.index(shutterspeed))-int(isosettings.index(ISO))) < 0:
                print("The brightness this image will have is too low. It is recommended that you increase your ISO or shutterspeed by a total of", abs(0-(12-int(shuuterspeedsettings.index(shutterspeed))-int(isosettings.index(ISO)))), "notche(s).")
                time.sleep(1.5)
                ISO = str(input("Please enter the ISO setting (e.g. 800): "))
                while ISO not in isosettings:
                    print("You did not enter a valid ISO setting. Please try again.")
                    time.sleep(1.5)
                    ISO = str(input("Please enter the ISO setting (e.g. 800): "))
                shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
                while shutterspeed not in shuuterspeedsettings:
                    print("You did not enter a valid shutterspeed setting. Please try again.")
                    time.sleep(1.5)
                    shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
            while (12-int(isosettings.index(ISO))-int(shuuterspeedsettings.index(shutterspeed))) > 7:
                print("The brightness this image will have is too high. It is recommended that you decrease your ISO or shutterspeed by a total of", abs(0-(7-int(shuuterspeedsettings.index(shutterspeed))-int(isosettings.index(ISO)))), "notche(s).")
                time.sleep(1.5)
                ISO = str(input("Please enter the ISO setting (e.g. 800): "))
                while ISO not in isosettings:
                    print("You did not enter a valid ISO setting. Please try again.")
                    time.sleep(1.5)
                    ISO = str(input("Please enter the ISO setting (e.g. 800): "))
                shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
                while shutterspeed not in shuuterspeedsettings:
                    print("You did not enter a valid shutterspeed setting. Please try again.")
                    time.sleep(1.5)
                    shutterspeed = str(input("Please enter the shutterspeed setting (in the form 1/1000): "))
            print("You entered: Shutterspeed -",shutterspeed, ",", "ISO -", ISO)
            verify = input("Is this correct? (Y | N) ")
            verify.upper()
            x = 12-int(isosettings.index(ISO))-int(shuuterspeedsettings.index(shutterspeed))
            apertureanswer = Aperturesettings[x]
        print("Your aperture setting should be set to", apertureanswer)
        print("Final settings are:")
        time.sleep(1.5)
        print("Lighting condition:", lightingconditions.get(lc), " aperture setting:", apertureanswer, " shutterspeed setting:", shutterspeed, "ISO setting:", ISO)

    runagain = input("Would you like to run this code again? (Y | N) ")

#######################################################################################################################
#ENDING OF CODE
print("Thank you for using this code. If you liked it, please rate 100%", "on rubric and Google reviews. Thank you for your compliance. Goodbye!")

#######################################################################################################################
####THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END#THE#END####