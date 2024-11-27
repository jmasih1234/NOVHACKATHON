def nutrition_health(age, weight, gender, height, activity, conditions, goals):
    # Calculate maintenance calories based on basic formula (can replace with complex logic)
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    # Adjust calories based on activity level
    activity_multiplier = {
        "none": 1.2,
        "little": 1.375,
        "moderate": 1.55,
        "very active": 1.725,
        "extra active": 1.9
    }
    maintenance_calories = bmr * activity_multiplier.get(activity, 1.2)

    # Adjust based on gym goals
    if goals == "bulking":
        intake_calories = maintenance_calories + 500
    elif goals == "cutting":
        intake_calories = maintenance_calories - 500
    else:
        intake_calories = maintenance_calories

    # Modify intake_calories based on health conditions
    if "heart disease" in conditions:
        intake_calories -= 200  # Example adjustment for heart disease
    if "diabetes" in conditions:
        intake_calories -= 150  # Example adjustment for diabetes

    return maintenance_calories, intake_calories



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
