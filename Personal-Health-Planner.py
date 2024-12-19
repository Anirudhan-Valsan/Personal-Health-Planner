import bmi_calculator 
import calorie_calculator as cl
import macro_calculator as mc

print("\n>>>>>>-> Welcome To BMI Calculator And Personal Health Planner <-<<<<<<<")
print('--------------------------------------------------------------------------\n')

while True:
    try:

        h  = int(input("Please Enter Your Height in centimeters : \t"))

        if h not in range(50,181):
            raise ValueError("\nInvalid Height\n")

        height = h
        break

    except ValueError as e:

        print(e)

while True:
    try:

        w  = int(input("\nPlease Enter Your Weight in Kilo Grams  : \t"))
        
        if w not in range(30,181):
            raise ValueError("\nInvalid weight\n")
        weight = w
        break
    except ValueError as e:
        print(e)

while True:
    try:
        ag = int(input("\nPlease Enter Your Age                   : \t"))

        if ag not in range(1,101):
            raise ValueError("\nInavalid Age\n")
        age = ag
        break

    except ValueError as e:
        print(e)



print(f"\nBased on the details given by you, your BMI is :  {bmi_calculator.calculate_bmi(height,weight)[0]}")

print(f"\nAnd You are classified as {bmi_calculator.calculate_bmi(height,weight)[1]}")

print("------------------------------------------------------------------------------\n")

while True:

    try:
        
        g = int(input("What is your current Goal ?\n\n1) Lose Fat\t2) Maintain\t3) Build Muscle ? (Enter The number)\t"))

        if g not in [1,2,3]:

            raise ValueError("\nInvalid Option\n")

        goal = {1:'lose fat',2:'maintain',3:'build muscle'}[g]

        break

    except ValueError as e:
        print(e)

weekly_weight = 0

if goal == 'build muscle' or goal == 'lose fat':

    while True:

        try:

            w_goal = int(input("\nIf building or losing, how much weight per week? (Options : 1) 0.25 kg, 2) 0.5 kg, 3) 1 kg) (enter the number)\n"))

            if w_goal not in [1,2,3]:

                raise ValueError('\nInvalid Option\n')

            weekly_weight = {1:0.25,2:0.5,3:1}[w_goal]
            break
        except ValueError as e:

            print(e)


gender         = input("\nPlease Enter Your Gender (M/F)          : \t")

while True:

    try:

        activity       = int(input("\nSelect Your Activity Level : \n\n1) sedentary, \n2) lightly active, \n3) moderately active, \n4) very active \n\nEnter the number corresponding to your activity level  : \t"))
        print("--------------------------------------------------------------------------\n")

        if activity not in [1,2,3,4]:

            raise ValueError('\nInvalid choice\n')

        activity_level = {1:'sedentary',2:'lightly active',3:'moderately active',4:'very active'}[activity]
        break
    
    except ValueError as e:
        print(e)



tdee = cl.bmr_tdee(gender,activity_level,height,weight,age)[0]

result = mc.macro_calculator(tdee,weight,goal,weekly_weight)

print(f"To {goal} with weekly weight goal of {weekly_weight}")
print("----------------------------------------------------")
print("Daily Calorie and Macronutrient Breakdown:")
print(f"Calories  : {result['Daily Calories Needed']} kcal")
print(f"Protein   : {result['Protein']} g")
print(f"Fat       : {result['Fat']} g")
print(f"Carbs     : {result['Carbohydrates']} g")
print("\n<----------------------------------------------------->")

input("\nPress Enter To Exit Program")