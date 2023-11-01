#ask the user what their name is
def theuser():
    print ("Hello friend, welcome to Timely.")
    name = input("What's your name: ")
    print ("Greetings, " + name + "!")
    return(name)
    
name = theuser() 

#explain to the user what the program will be doing
print("")
print ("At Timely, it is our goal to create a personalized time chart for our users.")
print("")
print("To begin, lets get to know you a little better.")
print("On a scale from 1 to 10, how well do you manage your time?")
print("1 = extremely poorly")
print("10 = extremely well")

#understand the users current skillset
#ask the user for an integer to describe their current skillset, and give them a custom message based on that input
#if the user does not input an integer, give them a error message
def score():
    functional = True 
    while functional:
        try:
            rating = int(input("Input your rating here: "))
        except Exception as exceptionObject: 
            print( f"Error: {exceptionObject}. Please try again" )
        else:
            functional = False
            if rating < 1:
                print("Your number is real low. You need us bad..")
            if rating == 1:
                print("Thank you for being transparent with us, we are here to help!")
            if rating == 2:
                print("Thank you for being transparent with us, we are here to help!")
            if rating == 3:
                print("Thank you for being transparent with us, we are here to help!")
            if rating == 4:
                print("Thank you for being transparent with us, we are here to help!")
            if rating == 5:
                print("Good progess, we are here to strenghten that skill!")
            if rating == 6:
                print("Good progess, we are here to strenghten that skill!")
            if rating == 7:
                print("Seems like you are able to manage your time well!")
            if rating == 8:
                print("Seems like you are able to manage your time well!")
            elif rating == 9:
                print("WOW!!! Thats great to hear!")
            
            elif rating < 1:
                print("Your number is real high! You must be a champ!")
            elif rating == 10:
                print("WOW!!!! Thats great to hear!")
            elif rating > 10:
                print("Your number is real high! You must be a champ!")

            return rating             

rating = score()

#start message
print("")
print("Lets begin creating your time chart " + name + ".")

#ask user when theyd like to start and end their day
print("")
Rise = input("What time would you like to wake up: ")
Fall = input("What time would you like to fall asleep: ")
print ("")

begin = 0

#ask user for how many activities they will be completing in a given day, and at what time they will be completing those given activities
def sunday():
    print("Its Sunday, lets begin our week!")
    sunact = int(input("how many activites do you have today? "))

    sundayactivities = []
    
    for currentDay in range (sunact):
        sunacti = input (f"please enter your activity {currentDay + 1}: ")
        suntime = input (f"what time will you be completing activity {currentDay + 1}: ")

        sundayactivities.append (suntime)
        sundayactivities.append (sunacti)

    return (sundayactivities)
sundayactivities = sunday()

#ask user for how many activities they will be completing in a given day, and at what time they will be completing those given activities
def monday():
    print("")
    print("Its Monday, lets continue our week!")
    monact = int(input("how many activites do you have today? "))

    mondayactivities = []

    for currentDay in range (monact):
        monacti = input (f"please enter your activity {currentDay + 1}: ")
        montime = input (f"what time will you be completing activity {currentDay + 1}: ")

        mondayactivities.append (montime)
        mondayactivities.append (monacti)

    return (mondayactivities)
mondayactivities = monday()

#ask user for how many activities they will be completing in a given day, and at what time they will be completing those given activities
def tuesday():
    print("")
    print("Its Tuesday, lets continue!")
    tueact = int(input("how many activites do you have today? "))
    
    tuesdayactivities = []

    for currentDay in range (tueact):
        tueacti = input (f"please enter your activity {currentDay + 1}: ")
        tuetime = input (f"what time will you be completing activity {currentDay + 1}: ")

        tuesdayactivities.append (tuetime)
        tuesdayactivities.append (tueacti)

    return (tuesdayactivities)
tuesdayactivities = tuesday()

#ask user for how many activities they will be completing in a given day, and at what time they will be completing those given activities
def wednesday():
    print("")
    print("Its Wednesday now! Half way there!")
    wedact = int(input("how many activites do you have today? "))

    wednesdayactivities = []

    for currentDay in range (wedact):
        wedacti = input (f"please enter your activity {currentDay + 1}: ")
        wedtime = input (f"what time will you be completing activity {currentDay + 1}: ")

        wednesdayactivities.append (wedtime)
        wednesdayactivities.append (wedacti)
        
    return (wednesdayactivities)
wednesdayactivities = wednesday()

#ask user for how many activities they will be completing in a given day, and at what time they will be completing those given activities
def thursday():
    print("")
    print("Its Thursday now, Almost the end!")
    thuract = int(input("how many activites do you have today? "))

    thursdayactivities = []

    for currentDay in range (thuract):
        wedacti = input (f"please enter your activity {currentDay + 1}: ")
        wedtime = input (f"what time will you be completing activity {currentDay + 1}: ")

        thursdayactivities.append (wedtime)
        thursdayactivities.append (wedacti)

    return (thursdayactivities)
thursdayactivities = thursday()

#ask user for how many activities they will be completing in a given day, and at what time they will be completing those given activities
def friday():
    print("")
    print("Whoop Whoop! Its Friday!")
    friacti = int(input("how many activites do you have today? "))

    fridayactivities = []

    for currentDay in range (friacti):
        friacti = input (f"please enter your activity {currentDay + 1}: ")
        fritime = input (f"what time will you be completing activity {currentDay + 1}: ")

        fridayactivities.append (fritime)
        fridayactivities.append (friacti)

    return (fridayactivities)
fridayactivities = friday()

#ask user for how many activities they will be completing in a given day, and at what time they will be completing those given activities
def saturday():
    print("")
    print("Whoop Whoop! Its Saturday!")
    satacti = int(input("how many activites do you have today? "))

    saturdayactivities = []

    for currentDay in range (satacti):
        satacti = input (f"please enter your activity {currentDay + 1}: ")
        sattime = input (f"what time will you be completing activity {currentDay + 1}: ")

        saturdayactivities.append (sattime)
        saturdayactivities.append (satacti)

    return (saturdayactivities)
saturdayactivities = saturday()

#present the user their final schedule based on all the inputs they gave you before hand!
def final():
    print(" ")
    print (name + "'s time chart:")
    print ("")
    
    print ("Sunday:")
    print ("Wake up: " + Rise)
    print (sundayactivities)
    print ("Wake up: " + Fall)
    print ("")
    
    print ("Monday:")
    print ("Wake up: " + Rise)
    print (mondayactivities)
    print ("Wake up: " + Fall)
    print ("")
   
    print ("Tuesday:")
    print ("Wake up: " + Rise)
    print (tuesdayactivities)
    print ("Wake up: " + Fall)
    print ("")

    print ("Wednesday:")
    print ("Wake up: " + Rise)
    print (wednesdayactivities)
    print ("Wake up: " + Fall)
    print ("")
    
    print ("Thursday:")
    print ("Wake up: " + Rise)
    print (thursdayactivities)
    print ("Wake up: " + Fall)
    print ("")
 
    print ("Friday:")
    print ("Wake up: " + Rise)
    print (fridayactivities)
    print ("Wake up: " + Fall)
    print ("")
    
    print ("Saturday:")
    print ("Wake up: " + Rise)
    print (saturdayactivities)
    print ("Wake up: " + Fall)
    print ("")
   
    print("Thank you, " + name + " for using Timely!")
    print("Come again!!")
    
    return(final)

final()



