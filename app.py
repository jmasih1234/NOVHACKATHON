from flask import Flask, render_template, request
from nutritionPlanner import nutrition_health

app = Flask(__name__)

# Define workout plans
def heart_disease_workout():
    return {
        "Day 1": "Aerobic Exercise (Walking or Cycling) - 30-40 minutes at moderate pace",
        "Day 2": "Strength Training (Low Resistance) - 3 sets of 12-15 reps",
        "Day 3": "Rest or Light Walking",
        "Day 4": "Swimming or Water Aerobics - 30 minutes",
        "Day 5": "Strength Training (Low Resistance) - 3 sets of 12-15 reps",
        "Day 6": "Yoga and Stretching - 20-30 minutes",
        "Day 7": "Rest"
    }

def diabetes_workout():
    return {
        "Day 1": "Aerobic Exercise (Walking or Stationary Cycling) - 30-40 minutes",
        "Day 2": "Strength Training (Low Resistance) - 3 sets of 12-15 reps",
        "Day 3": "Rest or Active Recovery",
        "Day 4": "Aerobic Exercise (Swimming or Cycling) - 30 minutes",
        "Day 5": "Strength Training - Add upper body exercises",
        "Day 6": "Balance & Flexibility - Yoga for 20-30 minutes",
        "Day 7": "Rest"
    }

def get_combined_workout(user_conditions):
    combined_plan = {}

    condition_workouts = {
        'heart disease': heart_disease_workout,
        'diabetes': diabetes_workout,
        # Add other conditions here
    }

    for condition in user_conditions:
        workout_func = condition_workouts.get(condition.lower())
        if workout_func:
            workout = workout_func()
            for day, activity in workout.items():
                if day not in combined_plan:
                    combined_plan[day] = []
                combined_plan[day].append(activity)

    return combined_plan

def calculate_macros_based_on_conditions(calories, conditions):
    # Define macro distributions for each condition
    condition_macros = {
        "diabetes": {"protein": 0.30, "carbs": 0.40, "fats": 0.30},
        "obesity": {"protein": 0.40, "carbs": 0.35, "fats": 0.25},
        "heart disease": {"protein": 0.25, "carbs": 0.45, "fats": 0.30},
        "anorexia": {"protein": 0.25, "carbs": 0.50, "fats": 0.25},
        "arthritis": {"protein": 0.30, "carbs": 0.40, "fats": 0.30},
        "cancer": {"protein": 0.35, "carbs": 0.35, "fats": 0.30},
    }

    # Default macros if no conditions match
    default_macros = {"protein": 0.30, "carbs": 0.50, "fats": 0.20}

    # Aggregate macro percentages for user's conditions
    total_macros = {"protein": 0, "carbs": 0, "fats": 0}
    count = 0

    for condition in conditions:
        condition = condition.lower()
        if condition in condition_macros:
            macros = condition_macros[condition]
            total_macros["protein"] += macros["protein"]
            total_macros["carbs"] += macros["carbs"]
            total_macros["fats"] += macros["fats"]
            count += 1

    # Calculate mean percentages if any conditions are matched
    if count > 0:
        mean_macros = {
            "protein": total_macros["protein"] / count,
            "carbs": total_macros["carbs"] / count,
            "fats": total_macros["fats"] / count,
        }
    else:
        mean_macros = default_macros  # Use default if no conditions are matched

    # Calculate grams of macros based on calorie intake
    protein_grams = (calories * mean_macros["protein"]) / 4  # 4 calories per gram of protein
    carbs_grams = (calories * mean_macros["carbs"]) / 4  # 4 calories per gram of carbs
    fats_grams = (calories * mean_macros["fats"]) / 9  # 9 calories per gram of fats

    return round(protein_grams, 2), round(carbs_grams, 2), round(fats_grams, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        weight = int(request.form['weight'])
        gender = request.form['gender']
        height = float(request.form['height'])
        activity = request.form['activity']
        user_conditions = request.form.getlist('conditions')
        gym_goals = request.form['goals']

        # Calculate nutrition details
        maintenance_cal, intake_cal = nutrition_health(age, weight, gender, height, activity, user_conditions, gym_goals)
        protein, carbs, fats = calculate_macros_based_on_conditions(intake_cal, user_conditions)

        # Get workout plan
        workout_plan = get_combined_workout(user_conditions)

        # Render results
        return render_template(
            'index.html',
            maintenance_cal=maintenance_cal,
            intake_cal=intake_cal,
            protein=protein,
            carbs=carbs,
            fats=fats,
            workout_plan=workout_plan
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
