 """
Date: 4/19/24
names: Nico DuPont
Description: 7 different functions all carried out differently
challenges: none
sources: W3schools

"""
#def function_name(imputs):
    #action
    #output (print or return)
def chorus(): #creates the function
    print("happy birthday to you, happy birthday to you!")#prints the song
    print("happy birthday,happy birthday happy birthday to you!")#prints more of the song
def sing():#defines the action you are preforming
    chorus()#executes the chorus function
    print("are you one, are you two,are you three!")#prints more of the song
    print("your four!")#prints the end of the song
    chorus()#executes the chorus function
def add(number1,number2): #creates the addition function
    print(number1+number2) #prints the sum of the fuction
def difference (num1, num2): #defines the range between the two number
    print (num2 - num1) #prints it 
def is_positive_number(string): #creates the function that takes in a string
    if string.isnumeric():#checks if th string is numeric
        return True #if it is numberic it will return true
    else: #if it is not numeric
        return False #it will return false
def in_list(my_list,item): #creates the function that takes in a list
    for items in my_list: #checks to make sure the items are in the list
        if items==item: #makes sure items equal the item
            return True #if items line up it will return true
        else:#if it does not line up
    return False #if not it will return false

def list_make (variable):#creates the funtion that takes in a list with variables
    if variable.isnumeric(): #checks if the variable is numeric
        return True #if it it is numeric returns true
    else: #if it is not numeric
        return False #return false
    
def random_number_in_range(): #creates function that takes in random number range
    numba1 = input("enter number 1: ") #creates the first input
    numba2 = input ("enter number 2: ")#creates second input

    while True: #creates while true loop
        if is_int(numba1) and is_int(numba2):#checks if numba 1 one is an interoger and that numba 2 is an interoger aswell
            print (random.randint(int(numba1),int(numba2))) #prints a random interoger between numba 1 and numba 2
        else: #if it is not an interoger
            print ("please enter an int!")#prints the responce if number is not an introger
def main():#main calling function
    
    while True:#creates the while true loop
        action = input("what would you like to do: 1. find a difference or 2. check if string is a psoitive number ")#calls for the question to be asked for the funtion you want to preform

        if action == "1":#asks if number in action is 1 or not
            n1 = int(input("enter number 1: ")) #defines the first input
            n2 = int(input("enter number 2: "))#defines the second input
            difference (n1, n2) #states the difference in the inputs
        elif action == "2": #asks if the action is according to the second action
            string =input ("enter string: ")#sets the string to a an input 
            print (is_positive_number_(string))#prints the number string
        elif action == "3": #calls the 3rd action
            random_number_in_range() #this the what the range the action pulls from
            
main()#calls everything

         
    

                




            

                        
