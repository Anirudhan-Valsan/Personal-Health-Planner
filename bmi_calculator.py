

def calculate_bmi(height,weight):

    height_in_meters = height / 100

    bmi = round(weight/(height_in_meters**2))

    if bmi < 18.5:

        classification = "Under Weight"

    elif 18.5 <= bmi < 24.9:

        classification = "Normal Weight"

    elif 25 <= bmi < 29.9:
        
        classification = "Over Weight"

    else:

        classification = "Obese"


    return [bmi,classification]
