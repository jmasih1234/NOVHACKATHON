#cardio
#Bulking Plan:
  #Diet Plan if bulking
#Cutting Plan:
  #Diet Plan if cutting
#Maintain Muscle: 
  #Diet Plan if maintaining
  
# Define the workout plans for each condition
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

    # Loop through user conditions
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
            print(f"Workout plan not available for condition: {condition}")
            continue
        
        # Merge the workout plans
        for day, activity in workout.items():
            if day not in combined_plan:
                combined_plan[day] = []
            combined_plan[day].append(activity)
    
    # Print combined workout plan
    print("\nCombined Workout Plan:")
    for day, activities in combined_plan.items():
        print(f"{day}:")
        for activity in activities:
            print(f"  - {activity}")

# Example usage
user_conditions = ['Heart Disease', 'Diabetes', 'Obesity']  # Example conditions
get_combined_workout(user_conditions)