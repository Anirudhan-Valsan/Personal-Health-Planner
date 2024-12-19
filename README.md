This is a python mini project done as a part of my DataScience and Machine Learning Internship at Luminar TechnoLab, Kochi

# BMI Calculator and Personal Health Planner

## Project Overview
The **BMI Calculator and Personal Health Planner** is a comprehensive tool designed to help users manage their health by providing personalized insights and recommendations. 
This project showcases practical applications of Python programming, data analysis, and health-related calculations.

## Key Features
- **BMI Calculation**: Computes Body Mass Index (BMI) and provides health classifications (Underweight, Normal Weight, Overweight, Obese).
- **BMR and TDEE Estimation**: Calculates Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE) based on user-specific data.
- **Macronutrient Breakdown**: Offers personalized daily macronutrient recommendations (Protein, Fat, Carbohydrates) based on user goals (Lose Fat, Maintain, Build Muscle).

## Project Objectives
- Develop a user-friendly health management tool using Python.
- Implement modular programming principles for clean, reusable code.
- Strengthen problem-solving skills through real-world health and fitness applications.

## Technologies Used
- **Programming Language**: Python
- **Integrated Development Environment (IDE)**: Visual Studio Code

## Future Enhancements
- Integration of additional health metrics for comprehensive analysis.
- Development of a user-friendly graphical interface (GUI) for improved user experience.

## How to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/bmi-health-planner.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd bmi-health-planner
   ```
3. **Install Required Dependencies**:
   Ensure you have Python installed on your machine. You may also need to install any required libraries using `pip`.
4. **Run the Main Script**:
   ```bash
   Personal-Health-Planner.py
   ```

## Project Structure
- **Personal-Health-Planner**: The main script that integrates all functionalities and handles user interaction.
- **bmi_calculator.py**: Contains functions for BMI calculation.
- **calorie_calculator.py**: Contains functions for BMR and TDEE estimation.
- **macro_calculator.py**: Contains functions for calculating daily macronutrient needs.

## Example Code Snippet
```python
import bmi_calculator
import calorie_calculator as cl
import macro_calculator as mc

print("\n>>>>>>-> Welcome To BMI Calculator And Personal Health Planner <-<<<<<<<")
print('--------------------------------------------------------------------------\n')

# User inputs and validation...
# BMI calculation and display...
# User goals and activity level...
# TDEE and macronutrient calculation...

print(f"To {goal} with weekly weight goal of {weekly_weight}")
print("----------------------------------------------------")
print("Daily Calorie and Macronutrient Breakdown:")
print(f"Calories  : {result['Daily Calories Needed']} kcal")
print(f"Protein   : {result['Protein']} g")
print(f"Fat       : {result['Fat']} g")
print(f"Carbs     : {result['Carbohydrates']} g")
```
