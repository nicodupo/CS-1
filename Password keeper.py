def add_entry(websites, usernames, passwords):#creates function
    '''
    description: funtion that holds all the variables in the f string


    Args:
        websites (list): websites entered by the user
        username (list): websites entered by the user
        passwords (list): passwords entered  by user
    Print:
        adds user reply to your lists
    
'''
    websites.append(input("what website would you like to use? "))#asks the user what website they would like to use
    usernames.append(input("what is your user name? ")) #asks user for their user name
    passwords.append(input ("what is your password? "))#add password to passwords list
def print_entry(websites, usernames, passwords, i): #prints funtion that has usernames,passwords,and websites
    '''
description: takes your function and prints it

    args:
        websites (list): websites entered by the user
        username (list): websites entered by the user
        passwords (list): passwords entered  by user
        i : tells you witch website with what username and password
        
    print: what username, with what username, with what password.
    '''
    print(f'''website: {websites[i]}
    username ={usernames[i]}
    password = {passwords[i]}''')
def main(): #main function that starts the exectution of the code
    websites = [] #gives empty list for websites to be stored
    usernames = [] #gives empty list for usernames to be stored
    passwords = [] #gives empty list for passwords to be stored
    
    while True : #creates a loops for code to continue over and over
        add_entry(websites, usernames, passwords) #gives you the 3 different topics things are stored in
        ask_user = input( "would you like to stop entering websites ") #asks user if they want to stop entering websites

        if ask_user ==("stop "): #if the user wants to end the program
            break #ends it and the while true loop 
    while True: #new loops for the code
        mode = input ("which would you like: 1. Add entry 2. print all, 3. print specific 4. Change 5. end") #defines the 5 different options with the passwords, usernames and passwords. 

        if mode == "5": #if the user chooses the 5th mode
            break #end program and break the while true loop
        elif mode == "1": #if user chooses the 1st mode
            add_entry(websites, usernames, passwords) #add answer to list of websites, usernames, and passwords
        elif mode == "2": #if user selects mode 2
            for i in range(len(websites)): #print all websites
              print_entry(websites, usernames, passwords, i)#prints all websites,usernames, and passwords
        elif mode == "3": #if user selects mode 3
            name = input("Enter website: ") #asls user to enter website of their choice
        
            if name in websites:   #if the name of the website is in website list
                print_entry(websites, usernames, passwords, websites.index(name))#print websites usernames, passwords and the whole website index. 
        elif mode == "4": #if user selects mode 4
            ask_website = input("would you like to change ?") #asks user if they want to switch their password

            if ask_website in websites: #checks if ask website exists in websites
                i = websites.index(ask_website) #sets I equal to your website index that you are checking for ask website
                usernames[i] = input ("enter new username: ") #asks the user to enter new username
                passwords[i] = input ("enter new password: ") #asks the user to enter new username
            
                
                
main()

