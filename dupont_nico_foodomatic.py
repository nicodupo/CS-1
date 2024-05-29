import random
fav_foods = ["pizza", "chicken", "wings", "icecream", "rice","burrito","dumplings","tacos","steak","sushi"]
fav_food_comments = ["delicious!","breath taking","tasty","mouth watering","hunger inducing","amazing","life changing","delectable","good", "favorable"]
least_fav_foods = ["artichoke", "ham", "pepper jack" "balogni" "salmon", "dark chocolate", "almonds","caviar","mayo","milk","stew","red apples"]
least_fav_food_comments = ["disgusting!", "vommit inducing", "off putting", "not good", "sickening","gross","sub par","below average","bad", "repulsive"]

print(len(fav_foods),len(fav_food_comments), len(least_fav_foods), len(least_fav_food_comments))
while True:
    try:
        number_of_items = int(input("how many items would you like? "))
        break
    except ValueError:
        print("Please enter an integer!")

for i in range(number_of_items):
    fav_food = random.choice(fav_foods)
    least_fav_food = random.choice(least_fav_foods)
    print(f"fave:{fav_food}, least fave:{least_fav_food}")
    print(f"{fav_food} is {fav_food_comments[fav_foods.index(fav_food)]}, but {least_fav_food} is {least_fav_food_comments[least_fav_foods.index(least_fav_food)]}")
          
        
 
