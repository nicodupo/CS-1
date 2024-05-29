'''
name: Nico
date: 10/27/23
description: this code is a basic while true loop that mimics my morning routine
bugs: I had put the break in the wrong place
challenges: break/while true
'''

description 
while True: #this makes the loop of code repeat
    print ("alarm") #this creates a function for waking up
    snooze = input("snooze?: " ) #takes one of the choices from the library to give you the option to snooze

    if snooze == "yes" : #if the responce to sleep is yes
        print ("Back to sleep")#responce to the command snooze
    elif snooze == "no": #second option from library
        print("Wake up!") #responce to second option 
        break
    else:
        print("Invalid") #if you get any other input but yes or no respond with invalid

while True:
    shower = input ("do you want to shower")#asking me if i want to shower
    if shower == ("yes"): #first input that you can respond with/ option to move on
       print (" you are now clean"
       break
    elif shower == "no": #second asnwer to question rejecting command
        print ( "go to your sink") #responce to rejecting command
        break
    else:
        print("Invalid") #if you get anything that is not the two otions it prints invalid

while True:

    go_to_your_sink = ("brush your teeth") # 3rd command in morning routine
    if go_to_your_sink == "yes": #first responce to command complying to comand
       print ( "your teeth are now clean") #responce to your choice
    elif go_to_your_sink == "no": #second option rejecting command
           print ("your breath smells bad") #responce to rejecting command
           break
    else:
           print ("time to leave")#4th command in morning routine
           time_to_leave = input("get in the car?") #first responce complying to first command
    if time_to_leave == "yes" : #if time to leave is true you leave for school
        print( "your on your way to gcds!")#responce to leaving for school
    elif user_input == "no": #second answers option rejecting command
        print('you are absent') #responce to rejecting question


