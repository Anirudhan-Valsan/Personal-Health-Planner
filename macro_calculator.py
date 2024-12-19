import calorie_calculator as cl

def macro_calculator(tdee,weight,goal,weekly_weight):

    calorie_adjustment = (weekly_weight * 7700) / 7
    adjusted_tdee = tdee + calorie_adjustment


    if goal == 'lose fat':

        adjusted_tdee = tdee - calorie_adjustment
        protein = 1.5 * weight
        fat     = 0.25 * adjusted_tdee / 9

    elif goal == 'build muscle':

        protein = 2.0 * weight
        fat     = 0.2 * adjusted_tdee / 9

    else:

        protein = 1.8 * weight
        fat     = 0.25 * adjusted_tdee / 9


    protein_cal = protein * 4
    fat_cal = fat * 9
    carb_cal = adjusted_tdee - (protein_cal + fat_cal)
    carbs = carb_cal / 4

    return {

        "Daily Calories Needed" : round(adjusted_tdee,2),
        "Protein"               : round(protein,2),
        "Fat"                   : round(fat,2),
        "Carbohydrates"         : round(carbs,2)
    }


    
    