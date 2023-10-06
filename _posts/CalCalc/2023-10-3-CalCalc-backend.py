# Constants for the Harris-Benedict Equation
BMR_MALE = 88.362
BMR_FEMALE = 447.593
ACTIVITY_MULTIPLIERS = {
    "sedentary": 1.2,
    "lightly active": 1.375,
    "moderately active": 1.55,
    "very active": 1.725,
    "extra active": 1.9,
}

# Function to calculate BMR (Basal Metabolic Rate)
def calculate_bmr(age, gender, weight, height):
    if gender == "male":
        return BMR_MALE + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "female":
        return BMR_FEMALE + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender")

# Function to calculate daily calorie requirements
def calculate_calories(age, gender, weight, height, activity_level):
    bmr = calculate_bmr(age, gender, weight, height)
    activity_multiplier = ACTIVITY_MULTIPLIERS.get(activity_level.lower(), 1.2)
    daily_calories = bmr * activity_multiplier
    return daily_calories

# Input values
age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))
activity_level = input("Enter your activity level (sedentary/lightly active/moderately active/very active/extra active): ")

# Calculate daily calorie requirements
calories = calculate_calories(age, gender, weight, height, activity_level)

# Display the result
print(f"Your daily calorie requirement is approximately {calories:.2f} calories.")

