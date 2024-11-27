from flask import Flask, render_template, request
from nutritionPlanner import nutrition_health, calculate_macros_based_on_conditions

app = Flask(__name__)

# Define workout plans for various conditions
def heart_disease_workout():
    return {
        "Day 1": "Aerobic Exercise (Walking or Cycling) - 30-40 minutes at moderate pace",
        "Day 2": "Strength Training (Low Resistance) - 3 sets of 12-15 reps, Leg Press, Seated Row, Chest Press",
        "Day 3": "Rest or Active Recovery - Light walking or stretching (15-20 minutes)",
        "Day 4": "Swimming or Water Aerobics - 30 minutes of swimming or water-based exercise",
        "Day 5": "Strength Training - Same as Day 2, adding exercises like tricep extensions and bicep curls",
        "Day 6": "Flexibility and Balance - Gentle yoga, stretches, and balance exercises (10-15 minutes)",
        "Day 7": "Rest or Light Walking"
    }

def diabetes_workout():
    return {
        "Day 1": "Aerobic Exercise (Walking or Stationary Cycling) - 30-40 minutes at moderate intensity",
        "Day 2": "Strength Training (Low Resistance) - 3 sets of 12-15 reps, Bodyweight Exercises, Light Weights",
        "Day 3": "Rest or Active Recovery - 20-30 minutes of light walking",
        "Day 4": "Aerobic Exercise (Swimming or Cycling) - 30 minutes at moderate pace",
        "Day 5": "Strength Training - Add upper body exercises like dumbbell bicep curls",
        "Day 6": "Balance & Flexibility - Yoga or stretching for 20-30 minutes",
        "Day 7": "Rest"
    }

def obesity_workout():
    return {
        "Day 1": "Aerobic Exercise (Walking, Stationary Cycling) - 30-40 minutes at moderate intensity",
        "Day 2": "Strength Training (Low Resistance) - 3 sets of 12-15 reps, Bodyweight Exercises, Light Weights",
        "Day 3": "Rest or Active Recovery - Light walking for 15-20 minutes",
        "Day 4": "Swimming or Water Aerobics - 30 minutes of water exercises",
        "Day 5": "Strength Training - Same as Day 2, adding bicep curls and tricep extensions",
        "Day 6": "Aerobic Exercise (Walking, Cycling) - 30 minutes at moderate pace",
        "Day 7": "Rest"
    }

def cancer_recovery_workout():
    return {
        "Day 1": "Aerobic Exercise (Walking, Stationary Cycling) - 20-30 minutes at light pace",
        "Day 2": "Strength Training (Bodyweight or Light Weights) - 2-3 sets of 8-10 reps",
        "Day 3": "Rest or Active Recovery - Gentle yoga or stretching",
        "Day 4": "Water Aerobics - 20-30 minutes of gentle water exercises",
        "Day 5": "Strength Training - Add upper body exercises like dumbbell rows",
        "Day 6": "Aerobic Exercise (Walking, Cycling) - 20-30 minutes of light walking or cycling",
        "Day 7": "Rest or Gentle Stretching"
    }

def arthritis_workout():
    return {
        "Day 1": "Aerobic Exercise (Walking, Swimming) - 20-30 minutes at moderate pace",
        "Day 2": "Strength Training (Light Resistance) - 2-3 sets of 12-15 reps, Bodyweight Exercises",
        "Day 3": "Rest or Active Recovery - 15-20 minutes of stretching or yoga",
        "Day 4": "Swimming or Water Aerobics - 20-30 minutes of water exercises",
        "Day 5": "Strength Training - Add resistance bands or light weights",
        "Day 6": "Flexibility and Balance - Yoga or Pilates for 20-30 minutes",
        "Day 7": "Rest or Light Walking"
    }

# Combine workout plans for multiple conditions
def get_combined_workout(user_conditions):
    combined_plan = {}

    # Loop through user conditions and add corresponding workouts
    for condition in user_conditions:
        if condition.lower() == 'heart disease':
            workout = heart_disease_workout()
        elif condition.lower() == 'diabetes':
            workout = diabetes_workout()
        elif condition.lower() == 'obesity':
            workout = obesity_workout()
        elif condition.lower() == 'cancer':
            workout = cancer_recovery_workout()
        elif condition.lower() == 'arthritis':
            workout = arthritis_workout()
        else:
            workout = {}

        # Merge workouts for each condition into a combined plan
        for day, activity in workout.items():
            if day not in combined_plan:
                combined_plan[day] = []
            combined_plan[day].append(activity)

    return combined_plan

# Define the macro distributions based on health conditions
def calculate_macros_based_on_conditions(calories, conditions):
    condition_macros = {
        "diabetes": {"protein": 0.30, "carbs": 0.40, "fats": 0.30},
        "obesity": {"protein": 0.40, "carbs": 0.35, "fats": 0.25},
        "heart disease": {"protein": 0.25, "carbs": 0.45, "fats": 0.30},
        "anorexia": {"protein": 0.25, "carbs": 0.50, "fats": 0.25},
        "arthritis": {"protein": 0.30, "carbs": 0.40, "fats": 0.30},
        "cancer": {"protein": 0.35, "carbs": 0.35, "fats": 0.30},
    }

    default_macros = {"protein": 0.30, "carbs": 0.50, "fats": 0.20}
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
        # Get form data from the user
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

        # Get workout plan for the user's conditions
        workout_plan = get_combined_workout(user_conditions)

        # Render the template with the results
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


