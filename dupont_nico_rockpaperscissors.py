

import random

rps_options = ["r", "p", "s"]
user_score = 0
bot_score = 0

while True:
    play = str.lower(input("do you want to play rps? "))
    
    if play == ("yes"):
        user_rps = str.lower(input("R, P, S?"))

        if user_rps not in rps_options:
            print("Invalid")
        else:
            bot_rps = random.choice(rps_options)

            if user_rps == bot_rps:
                print("tie")
            elif user_rps == "r" and bot_rps == "s":
                print("user wins!")
                user_score += 1
            elif user_rps == "s" and bot_rps == "p":
                print ("user wins!")
                user_score += 1 
            elif user_rps == "p" and bot_rps == "r":
                print("user wins!")
                user_score +=1 
            elif bot_rps == "r" and user_rps == "s":
                print ("bot wins!")
                bot_score +=1
            elif bot_rps == "s" and user_rps == "p":
                print ("bot wins!")
                bot_score +=1 
            elif bot_rps == "p" and user_rps == "r":
                print ("bot wins!")
                botscore +=1
            print(f"Score is user - {user_score} bot - {bot_score}")
    elif play == "no":
        break
    else:
        print("Invalid")
    
    
