def bmr_tdee(gender,activity_level,height,weight,age):

    if gender.lower() == "m":

        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.667 * age)

    else:

        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)


    activity_factors = {
    "sedentary": 1.2,
    "lightly active": 1.375,
    "moderately active": 1.55,
    "very active": 1.725
    }

    tdee = bmr * activity_factors[activity_level]

    return [tdee,bmr]