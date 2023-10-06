from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route('/calculate-calories', methods=['POST'])
def calculate_calories_api():
    data = request.get_json()
    age = data.get('age')
    gender = data.get('gender')
    weight = data.get('weight')
    height = data.get('height')
    activity_level = data.get('activity')

    try:
        calories = calculate_calories(age, gender, weight, height, activity_level)
        return jsonify({'calories': calories})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
