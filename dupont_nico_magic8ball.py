'''
Author: Nico Dupont
Date: 11/13/23
Description: this is an loop models an 8 ball that when it shakes you get a randomized answer
bugs: I had an issue at the begining with the syntac of my list.
Challenges: while true, delay
Sources: w3 schools, Ms. Marciano
'''

import random #brings in random library for use of random functions
import time # brings in  time from time library

question_words = ["is", "does", "will", "am", "are"]

while True: #loops the action
    shake = input("ask the ball a question") #tells program to ask the question
    time.sleep(1)   # brings in 1 second delay from time library
    
    if shake == "stop": #this breaks the loop from repeating
        print("bye") # reaction to stop
        break # breaks the while true
    elif "?" in shake or any(word in shake for word in question_words): #it takes words from list library and options from random choice
        print(random.choice(["dog","log","frog","rock"])) # my list of random variables.
    else:
        print("Not a question!")#responce to invalid responce not in question word library
